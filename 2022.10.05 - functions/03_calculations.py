def calculations(first: int, second: int, to_do: str):
    result = None
    if to_do == "multiply":
        result = first * second
    elif to_do == "divide":
        result = int(first / second)
    elif to_do == "add":
        result = first + second
    elif to_do == "subtract":
        result = first - second
    return result



operator = input()
first_num = int(input())
second_num = int(input())

print(calculations(first_num, second_num, operator))
