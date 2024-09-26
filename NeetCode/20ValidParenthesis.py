



def validParenthesis(s):

    char = {'(':')', '{':'}', '[':']'}

    stack = []

    for ch in s:
        if ch in char:
            stack.append(ch)
        elif len(stack) == 0 or char[stack.pop()] != ch:
            return False

    return len(stack) == 0

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
print(validParenthesis(s1))
print(validParenthesis(s2))
print(validParenthesis(s3))