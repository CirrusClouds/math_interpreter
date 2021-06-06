import re

expr = r"\[[\s\S]*\]"
exprs = [
    r"\d{1,}(\.\d{1,})*\ *\^\ *\d{1,}(\.\d{1,})*",
    r"\d{1,}(\.\d{1,})*\ *\/\ *\d{1,}(\.\d{1,})*",
    r"\d{1,}(\.\d{1,})*\ *\*\ *\d{1,}(\.\d{1,})*",
    r"\d{1,}(\.\d{1,})*\ *\+\ *\d{1,}(\.\d{1,})*",
    r"\d{1,}(\.\d{1,})*\ *\-\ *\d{1,}(\.\d{1,})*",
]


def lex_exponent(arg):
    indexp = re.search(exprs[0], arg)
    indexp = indexp.group()
    nums = re.split(r"\ *\^\ *", indexp)
    nums = [float(num) for num in nums]
    num_3 = nums[0] ** nums[1]
    arg2 = arg.replace(indexp, str(num_3))
    return arg2


def lex_divide(arg):
    dividep = re.search(exprs[1], arg)
    dividep = dividep.group()
    nums = re.split(r"\ *\/\ *", dividep)
    nums = [float(num) for num in nums]
    num_3 = nums[0] / nums[1]
    arg2 = arg.replace(dividep, str(num_3))
    return arg2


def lex_multiply(arg):
    multiplyp = re.search(exprs[2], arg)
    multiplyp = multiplyp.group()
    nums = re.split(r"\ *\*\ *", multiplyp)
    nums = [float(num) for num in nums]
    num_3 = nums[0] * nums[1]
    arg2 = arg.replace(multiplyp, str(num_3))
    return arg2


def lex_add(arg):
    addp = re.search(exprs[3], arg)
    addp = addp.group()
    nums = re.split(r"\ *\+\ *", addp)
    nums = [float(num) for num in nums]
    num_3 = nums[0] + nums[1]
    arg2 = arg.replace(addp, str(num_3))
    return arg2


def lex_subtract(arg):
    subtractp = re.search(exprs[4], arg)
    subtractp = subtractp.group()
    nums = re.split(r"\ *\-\ *", subtractp)
    nums = [float(num) for num in nums]
    num_3 = nums[0] - nums[1]
    arg2 = arg.replace(subtractp, str(num_3))
    return arg2


# If only I had macros for this... it would make things a looooot easier
