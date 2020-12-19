import re
file = open('day18input.txt',mode='r')
equations = [e for e in file.read().split("\n")]

def calc(s):
    s = re.sub("(\(|\))", "", s)
    while "*" in s or "+" in s:
        s_replace = re.findall("\d+", s)[0] + re.findall("(\+|\*)",s)[0] + re.findall("\d+", s)[1]
        if re.findall("(\+|\*)",s)[0] == "*":
            s_math = int(re.findall("\d+", s)[0]) * int(re.findall("\d+", s)[1])
        if re.findall("(\+|\*)",s)[0] == "+":
            s_math = int(re.findall("\d+", s)[0]) + int(re.findall("\d+", s)[1])
        s = s.replace(s_replace, str(s_math), 1)
    return s

def advanced(s):
    s = re.sub("(\(|\))", "", s)
    while "+" in s:
        for sub_equation in re.findall("\d+\+\d+", s):
            s_math = int(re.findall("\d+", sub_equation)[0]) + int(re.findall("\d+", sub_equation)[1])
            s = s.replace(sub_equation, str(s_math), 1)
    while "*" in s:
        for sub_equation in re.findall("\d+\*\d+", s):
            s_math = int(re.findall("\d+", sub_equation)[0]) * int(re.findall("\d+", sub_equation)[1])
            s = re.sub(r"\b%s\b" % re.escape(sub_equation), str(s_math), s)
    return s

result = 0
advanced_result = 0
for equation in equations:
    equation = equation.replace(" ", "")
    advanced_equation = equation
    # Part One
    while "(" in equation:
        for replace_s in re.findall("\([\d|+|*]*\)", equation):
            equation = equation.replace( replace_s, calc(replace_s) )
    equation = calc(equation)
    result += int(equation)

    # Part Two
    while "(" in advanced_equation:
        for replace_s in re.findall("\([\d|+|*]*\)", advanced_equation):
            advanced_equation = advanced_equation.replace( replace_s, advanced(replace_s), 1)
    advanced_equation = advanced(advanced_equation)
    advanced_result += int(advanced_equation)


print(f"Part One: {result}")
print(f"Part Two: {advanced_result}")
