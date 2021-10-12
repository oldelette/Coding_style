"""function"""


def cau(typee, num1, num2):
    """calculate"""
    if typee == 1:
        temp = num1 + num2
    elif typee == 2:
        temp = num1 - num2
    else:
        temp = num1 * num2
    return temp
