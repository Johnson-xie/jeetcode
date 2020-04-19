class Solution:
    def convertToBase7(self, num: int) -> str:

        ret = []
        flag = False
        if num < 0:
            flag = True
            num = -num

        while num:
            num, cur = divmod(num, 7)
            ret.append(str(cur))

        return "-" + "".join(reversed(ret)) if flag else "".join(reversed(ret))

    def convertToBase72(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        elif num < 7:
            return str(num)
        else:
            return self.convertToBase7(num//7) + str(num % 7)
