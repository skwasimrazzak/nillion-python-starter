# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     party4 = Party(name="Party4")

#     # Define secret inputs
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))
#     c = SecretInteger(Input(name="C", party=party3))

#     # Determine the greatest number
#     max_ab = If(a > b, a, b)
#     max_abc = If(max_ab > c, max_ab, c)

#     # Output the result
#     return [Output(max_abc, "greatest_number", party4)]

# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     party4 = Party(name="Party4")

#     # Define secret inputs
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))
#     c = SecretInteger(Input(name="C", party=party3))

#     # Determine the greatest number using conditional assignments
#     max_ab = a * (a > b) + b * (b >= a)
#     max_abc = max_ab * (max_ab > c) + c * (c >= max_ab)

#     # Output the result
#     return [Output(max_abc, "greatest_number", party4)]

# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     party4 = Party(name="Party4")

#     # Define secret inputs
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))
#     c = SecretInteger(Input(name="C", party=party3))

#     # Determine the greatest number using conditional operations
#     max_ab = Conditional(a > b, a, b)
#     max_abc = Conditional(max_ab > c, max_ab, c)

#     # Output the result
#     return [Output(max_abc, "greatest_number", party4)]

# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     party4 = Party(name="Party4")

#     # Define secret inputs
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))
#     c = SecretInteger(Input(name="C", party=party3))

#     # Determine the greatest number using the max method
#     max_ab = a.max(b)
#     max_abc = max_ab.max(c)

#     # Output the result
#     return [Output(max_abc, "greatest_number", party4)]

# from nada_dsl import *
# import nada_ops as ops

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     party4 = Party(name="Party4")

#     # Define secret inputs
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))
#     c = SecretInteger(Input(name="C", party=party3))

#     # Determine the greatest number using conditional selections
#     max_ab = ops.if_else(a > b, a, b)
#     max_abc = ops.if_else(max_ab > c, max_ab, c)

#     # Output the result
#     return [Output(max_abc, "greatest_number", party4)]
from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    # party2 = Party(name="Party2")
    # party3 = Party(name="Party3")
    # party4 = Party(name="Party4")

    # Define secret inputs
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))

    # Determine the greatest number using conditional operations
    # max_ab = a * (a >= b) + b * (b > a)
    # max_abc = max_ab * (max_ab >= c) + c * (c > max_ab)

    max_abc = a + b + c

    # Output the result
    return [Output(max_abc, "Output", party1)]



