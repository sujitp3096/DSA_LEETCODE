class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            carry = 0

            for j in range(n - 1, -1, -1):
                total = int(num1[i]) * int(num2[j]) + res[i + j + 1] + carry

                res[i + j + 1] = total % 10
                carry = total // 10

            res[i] += carry

        return ''.join(map(str, res)).lstrip('0') or '0'