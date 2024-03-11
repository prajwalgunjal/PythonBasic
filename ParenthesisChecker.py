stack = []

def CheckParenthesis(stringData):
    for i in stringData:
        if isopening(i):
            stack.append(i)
        else:
            if not stack:  # Check if stack is empty
                return False
            elif not isClosing(stack.pop(), i):
                return False

    return not stack  # Check if the stack is empty after processing all characters

def isopening(word):
    return word == "(" or word == "{" or word == "["

def isClosing(opening, closing):
    return (opening == "(" and closing == ")") or \
           (opening == "{" and closing == "}") or \
           (opening == "[" and closing == "]")

if __name__ == '__main__':
    stringData = input("Enter String: ")
    if CheckParenthesis(stringData):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")


#https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Strings&sortBy=submissions