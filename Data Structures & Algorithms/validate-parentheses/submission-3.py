class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stck.append(i)
                continue
            elif i == "]":
                if len(stck) > 0 and stck[-1] == "[":
                    stck.pop(-1)
                else:
                    return False
            elif i == ")":
                if len(stck) > 0 and  stck[-1] == "(":
                    stck.pop(-1)
                else:
                    return False
            elif i == "}":
                if len(stck) > 0 and  stck[-1] == "{":
                    stck.pop(-1)
                else:
                    return False
        if len(stck) == 0:
            return True
        else:
            return False