'''lc 166 medium'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, d = numerator, denominator
        if n % d == 0:
            return str(n // d)
        res = []
        if (n > 0) ^ (d > 0):
            res.append("-")
        n, d = abs(n), abs(d)
        res.append(str(n//d))
        n %= d
        res.append(".")
        i = len(res)
        n_ind = dict()
        while n:
            n_ind[n] = i
            n *= 10
            res.append(str(n//d))
            n %= d
            i += 1
            if n in n_ind:
                t = res[:n_ind[n]]
                t.append("(")
                t += res[n_ind[n]:]
                t.append(")")
                res = t
                break
        return ''.join(res)
