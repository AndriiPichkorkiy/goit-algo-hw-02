from collections import deque
import re


def palindrome_checker(text: str) -> bool:
    # remove extra symbols
    text = re.sub(pattern="[ |,|!|?]", repl="", string=text)

    # normilize text
    text_list = list(text.upper())

    # create queue
    queue = deque(text_list)

    # work with both an even and an odd number of characters
    while len(queue) > 1:
        # compare left and right chars
        if queue.popleft() != queue.pop():
            return False

    # True when left 1 or 0 symbol
    return True


def main():
    print("Is the word palindrome?")
    for word in ["kayak", "deified", "rotator", "repaper", "deed", "peep", "wow", "civic", "racecar", "level", "mom", "bird rib", "taco cat", "UFO tofu", "Borrow or rob?", "Yo, Banana Boy!", "I am not a Palindrome"]:
        result = str(palindrome_checker(word))
        print("{:>25} | {:<10} ".format(word, result))


if __name__ == "__main__":
    main()
