class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t in operators:
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                print(num1, t, num2)
                print("---")
                if t == "+":
                    nums.append(num2 + num1)
                elif t == "-":
                    nums.append(num2 - num1)
                elif t == "*":
                    nums.append(num2 * num1)
                elif t == "/":
                    nums.append(num2 / num1)
            else:
                nums.append(t)
        
        return int(nums[0])