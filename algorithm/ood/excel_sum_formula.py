"""LeetCode 631, hard: design excel sum formula."""

from collections import Counter, defaultdict, deque

type Cell = tuple[int, int]


class _ExcelBase:
    def __init__(self, height: int, width: str):
        """Store sheet dimensions in row count and parsed column count."""
        self.rows = height
        self.cols = self._parse_column(width)

    @staticmethod
    def _parse_column(column: str) -> int:
        """Convert an Excel-style column label to a 1-based index."""
        value = 0
        for char in column:
            value = value * 26 + ord(char) - ord("A") + 1
        return value

    def _cell(self, row: int, column: str) -> Cell:
        """Convert public row/column input to a 0-based cell tuple."""
        return row - 1, self._parse_column(column) - 1

    def _parse_ref(self, ref: str) -> Cell:
        """Parse a cell reference like A1 into 0-based coordinates."""
        idx = 0
        while idx < len(ref) and ref[idx].isalpha():
            idx += 1
        return int(ref[idx:]) - 1, self._parse_column(ref[:idx]) - 1

    def _parse_formula(self, numbers: list[str]) -> Counter[Cell]:
        """Expand refs and ranges into a weighted cell counter."""
        refs: Counter[Cell] = Counter()
        for token in numbers:
            if ":" not in token:
                refs[self._parse_ref(token)] += 1
                continue

            start_ref, end_ref = token.split(":")
            start_row, start_col = self._parse_ref(start_ref)
            end_row, end_col = self._parse_ref(end_ref)
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col + 1):
                    refs[(row, col)] += 1
        return refs


class Excel(_ExcelBase):
    """Main solution: cached values plus a weighted dependency graph.

    A 2D BIT or segment tree helps rectangle-sum queries, but the hard part
    here is maintaining formula dependencies after cells are overwritten.
    We therefore keep reverse edges for propagation and cache each cell's
    displayed value so repeated get() calls are O(1).
    """

    def __init__(self, height: int, width: str):
        """Initialize cached values, formulas, and reverse dependency edges."""
        super().__init__(height, width)
        self.values = [[0] * self.cols for _ in range(self.rows)]
        self.formulas: dict[Cell, Counter[Cell]] = {}
        self.dependents: defaultdict[Cell, Counter[Cell]] = defaultdict(Counter)

    def set(self, row: int, column: str, val: int) -> None:
        """Assign a raw value and propagate its delta downstream."""
        target = self._cell(row, column)
        old_value = self.values[target[0]][target[1]]
        self._clear_formula(target)
        self.values[target[0]][target[1]] = val
        self._propagate(target, val - old_value)

    def get(self, row: int, column: str) -> int:
        """Return the cached displayed value of a cell."""
        target = self._cell(row, column)
        return self.values[target[0]][target[1]]

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        """Replace the cell with a formula and return its current value."""
        target = self._cell(row, column)
        old_value = self.values[target[0]][target[1]]
        self._clear_formula(target)

        refs = self._parse_formula(numbers)
        self.formulas[target] = refs
        for src, weight in refs.items():
            self.dependents[src][target] += weight

        new_value = sum(self.values[src[0]][src[1]] * weight for src, weight in refs.items())
        self.values[target[0]][target[1]] = new_value
        self._propagate(target, new_value - old_value)
        return new_value

    def _clear_formula(self, target: Cell) -> None:
        """Remove a cell's old formula edges before overwriting it."""
        refs = self.formulas.pop(target, None)
        if not refs:
            return

        for src, weight in refs.items():
            self.dependents[src][target] -= weight
            if self.dependents[src][target] == 0:
                del self.dependents[src][target]
            if not self.dependents[src]:
                del self.dependents[src]

    def _collect_affected(self, start: Cell) -> set[Cell]:
        """BFS over reverse edges to find all downstream dependents."""
        affected: set[Cell] = set()
        queue = deque([start])
        while queue:
            src = queue.popleft()
            for dst in self.dependents.get(src, {}):
                if dst in affected:
                    continue
                affected.add(dst)
                queue.append(dst)
        return affected

    def _propagate(self, start: Cell, delta: int) -> None:
        """Push one cell's delta through the dependency DAG in topo order."""
        if delta == 0 or start not in self.dependents:
            return

        affected = self._collect_affected(start)
        if not affected:
            return

        indegree = {cell: 0 for cell in affected}
        for src in [start, *affected]:
            for dst in self.dependents.get(src, {}):
                if dst in indegree:
                    indegree[dst] += 1

        accumulated = defaultdict(int)
        accumulated[start] = delta
        queue = deque([start])
        while queue:
            src = queue.popleft()
            for dst, weight in self.dependents.get(src, {}).items():
                if dst not in indegree:
                    continue
                accumulated[dst] += accumulated[src] * weight
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    self.values[dst[0]][dst[1]] += accumulated[dst]
                    queue.append(dst)


class Excel2(_ExcelBase):
    """Alternative solution: store formulas and evaluate lazily on get()."""

    def __init__(self, height: int, width: str):
        """Initialize raw values and stored formulas for lazy evaluation."""
        super().__init__(height, width)
        self.values = [[0] * self.cols for _ in range(self.rows)]
        self.formulas: dict[Cell, Counter[Cell]] = {}

    def set(self, row: int, column: str, val: int) -> None:
        """Assign a raw value and discard any previous formula."""
        target = self._cell(row, column)
        self.formulas.pop(target, None)
        self.values[target[0]][target[1]] = val

    def get(self, row: int, column: str) -> int:
        """Recompute the cell value on demand from its formula graph."""
        return self._evaluate(self._cell(row, column), {})

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        """Store a formula on the cell and evaluate it immediately."""
        target = self._cell(row, column)
        self.formulas[target] = self._parse_formula(numbers)
        return self.get(row, column)

    def _evaluate(self, cell: Cell, memo: dict[Cell, int]) -> int:
        """DFS a formula cell, memoizing results within one get() call."""
        if cell in memo:
            return memo[cell]
        if cell not in self.formulas:
            return self.values[cell[0]][cell[1]]

        total = 0
        for src, weight in self.formulas[cell].items():
            total += self._evaluate(src, memo) * weight
        memo[cell] = total
        return total
