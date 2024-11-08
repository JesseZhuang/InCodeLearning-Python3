"""leet code 68, hard"""


class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, n_letter = [], [], 0
        for w in words:
            if n_letter + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - n_letter):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, n_letter = [], 0
            cur += [w]
            n_letter += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
