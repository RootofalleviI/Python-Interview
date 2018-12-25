def evaluate(RPN_expression):
    """ Write a program that takes an arithmetic expression in RPN and returns the number 
    that the expression evaluates to.

    An RPN expression can be evaluated uniquely to an integer, which is determined recursively:
    - It is a single digit of sequence of digits, prefixed with an option - (negative).
    - It is of the form "A, B, o", where o is +, -, *, l and A, B are RPN expressions.

    We scan from left to right. When we encounter an operand, we append it to intermediate_results.
    When we encounter an operator, we pop two off of intermediate results, compute the result, and 
        append it back to the list. Finally, we return intermediate_results[-1]
    """
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y)
    }

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(
                    OPERATORS[token](
                        intermediate_results.pop(), 
                        intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))

    return intermediate_results[-1]
