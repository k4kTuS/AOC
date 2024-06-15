def p1(lines):
    numbers = []
    for line in lines:
        left = None
        right = None

        for char in line:
            if char.isdigit():
                left = char
                break
        for char in reversed(line):
            if char.isdigit():
                right = char
                break
        if left and right:
            numbers.append(int(left + right))
    print(sum(numbers))

def p2(lines):
    numbers = []
    for line in lines:
        digits = []

        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d+1))

        if len(digits) > 0:
            numbers.append(int(digits[0] + digits[-1]))
    print(sum(numbers))


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        p1(lines)
        p2(lines)