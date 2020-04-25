import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_c = collections.Counter(secret)

        guess_c = collections.Counter(guess)

        B = sum((secret_c & guess_c).values())
        A = 0
        for s, b in zip(secret, guess):
            if s == b:
                A += 1
                B -= 1
            elif secret_c[b] > 0:
                secret_c[b] -= 1

        return str(A) + "A" + str(B) + "B"