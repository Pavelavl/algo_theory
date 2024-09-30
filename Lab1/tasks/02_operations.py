#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"
result = (1 + 2) * 3
print(result)

def find_expression(numbers, target):
    operators = ['+', '-', '*', '']
    
    def evaluate_expression(expr):
        try:
            return eval(expr)
        except Exception:
            return None

    def generate_expressions(numbers):
        for ops in itertools.product(operators, repeat=len(numbers)-1):
            expr = ""
            for i, num in enumerate(numbers):
                expr += str(num)
                if i < len(ops):
                    expr += ops[i]
            yield expr
    
    for expression in generate_expressions(numbers):
        evaluated = evaluate_expression(expression)
        if evaluated == target:
            return expression

    return None

numbers = [1, 2, 3, 4, 5]
target = 25
result = find_expression(numbers, target)

if result:
    print(f"expression found: {result} = {target}")
else:
    print(f"no expression for target = {target}")
