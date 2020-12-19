import re
file = open('day18input.txt',mode='r')
equations = [e for e in file.read().split("\n")]

def solve(line):
    def doInner(inner):
        while '+' in inner or '*' in inner:
            inner = re.sub('^(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), inner)
            inner = re.sub('^(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), inner)
        # while '+' in inner:
            # inner = re.sub('(\d+)\s*\+\s*(\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), inner)
        # while '*' in inner:
            # inner = re.sub('(\d+)\s*\*\s*(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), inner)
        return inner
    while '(' in line:
        def doExpr(match):
            inner = match.group(1)
            return doInner(inner)
        line = re.sub(r'\(([^()]+)\)', doExpr, line)
    return doInner(line)

def calc(s):
    s = re.sub("(\(|\))", "", s)
    while "*" in s or "+" in s:
        s_replace = re.findall("\d*", s)[0] + re.findall("(\+|\*)",s)[0] + re.findall("\d*", s)[2]
        if re.findall("(\+|\*)",s)[0] == "*":
            s_math = int(re.findall("\d*", s)[0]) * int(re.findall("\d*", s)[2])
        if re.findall("(\+|\*)",s)[0] == "+":
            s_math = int(re.findall("\d*", s)[0]) + int(re.findall("\d*", s)[2])
        s = s.replace(s_replace, str(s_math), 1)
    return s

def advanced(s):
    s = re.sub("(\(|\))", "", s)
    while "*" in s:
        s_replace = re.findall("\d*", s)[0] + re.findall("(\+|\*)",s)[0] + re.findall("\d*", s)[2]
        s_math = int(re.findall("\d*", s)[0]) * int(re.findall("\d*", s)[2])
    while "+" in s:    
        s_replace = re.findall("\d*", s)[0] + re.findall("(\+|\*)",s)[0] + re.findall("\d*", s)[2]
        if re.findall("(\+|\*)",s)[0] == "+":
            s_math = int(re.findall("\d*", s)[0]) + int(re.findall("\d*", s)[2])
        s = s.replace(s_replace, str(s_math), 1)
    return s

result = 0
for equation in equations:
    equation = equation.replace(" ", "")
    while "(" in equation:
        for replace_s in re.findall("\([\d|+|*]*\)", equation):
            equation = equation.replace( replace_s, calc(replace_s) )
    equation = calc(equation)
    result += int(equation)

print(f"Part One: {result}")

#print(total)
