input_string = input()
count_number = int(input())

repeat_string = lambda string, number: string * number

result = repeat_string(input_string, count_number)

print(result)
