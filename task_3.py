def bracket_checker(expression: str) -> bool:
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    length = len(open_brackets)

    # when length is 0 - nothing to check
    if len(expression) == 0:
        return True

    # Stack to remember the currently open delimiter characters.
    stack = []
    for char in expression:
        for index in range(length):

            # compare opened brackets
            if char == open_brackets[index]:

                # add the bracket to the stack
                stack.append(char)
                break

            # compare closed brackets
            elif char == close_brackets[index]:

                # if the char is some of the closed brackets - compare the last in stack bracket with current closed char
                # as a closed char choose a bracket on a related position in the open_brackets list
                if stack.pop() != open_brackets[index]:
                    return False

    # True when stack is empty
    return len(stack) == 0


def main():
    check_list = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",  # True
        "( 23 ( 2 - 3);",  # False
        "( 11 }",  # False
    ]

    print("Is the expression valid?")
    for expression in check_list:
        result = str(bracket_checker(expression))
        print("{:>25} | {:<10} ".format(expression, result))


if __name__ == "__main__":
    main()
