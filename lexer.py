import re

from jam_funcs import (
    lex_divide,
    lex_multiply,
    lex_add,
    lex_subtract,
    lex_exponent,
    exprs,
)

pointers = [lex_exponent, lex_divide, lex_multiply, lex_add, lex_subtract]

paren_expr = r"(?<=\()[\s\S]+(?=\))"


def lex(arg):
    parensp = re.search(paren_expr, arg)
    if bool(parensp):
        in_parens = parensp.group()
        solution = lex(in_parens)
        allparens = "(" + in_parens + ")"
        arg2 = arg.replace(allparens, solution)
        return lex(arg2)

    for point, expr in zip(pointers, exprs):
        expressionp = re.search(expr, arg)
        if bool(expressionp):
            arg2 = point(arg)
            return lex(arg2)
    return arg


# Maybe we could make this more efficient with a meta-circular evaluator?
