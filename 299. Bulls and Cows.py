import collections
import operator


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

    def getHint2(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, both - bulls)

    def getHint3(self, secret, guess):
        A = sum(a == b for a, b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)