# rev a sentence using stack
# sentence = "hi this is me"
# print(n[::-1])
# like this : em si siht ih
from  collections import deque
def rev(sentence):
    stack = deque()
    for i in sentence:
        stack.appendleft(i)
    print(''.join(stack))
rev("hi this is me")

# valid parenthesis
def valid_pair(sentence):
    stack = deque()
    dict = {"(" : ")","{":"}","[":"]" }
    for i in sentence:
        if i in dict.keys():
            stack.append(i)
            print(stack)
        if i in dict.values():
            if not stack:
                return False
            n = stack.pop()

            if dict[n]!=i:
                return False
    if stack:
        return False
    else:
        return True
print(valid_pair("(a[b{ef}d]h)k"))
print(valid_pair("(a*b)+{this}+[1,2,3]"))
