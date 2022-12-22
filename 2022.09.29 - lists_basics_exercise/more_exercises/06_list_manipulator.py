import sys

integers = input().split(" ")

for i, number in enumerate(integers):
    integers[i] = int(number)

command = input()
while command != "end":
    if "exchange" in command:
        command = command.split(" ")
        index = int(command[1])
        if 0 <= index < len(integers):
            first_part = []
            second_part = []
            for i in range(len(integers)):
                if i > index:
                    first_part.append(integers[i])
                else:
                    second_part.append(integers[i])
            integers = first_part + second_part
        else:
            print("Invalid index")
    elif "max" in command:
        if "odd" in command:
            found_odd = False
            max_odd = -sys.maxsize
            index_max_odd = 0
            for i in range(len(integers)):
                if integers[i] % 2 != 0 and integers[i] >= max_odd:
                    max_odd = integers[i]
                    index_max_odd = i
                    found_odd = True

            if not found_odd:
                print("No matches")
            else:
                print(index_max_odd)
        elif "even" in command:
            found_even = False
            max_even = -sys.maxsize
            index_max_even = 0
            for i in range(len(integers)):
                if integers[i] % 2 == 0 and integers[i] >= max_even:
                    max_even = integers[i]
                    index_max_even = i
                    found_even = True

            if not found_even:
                print("No matches")
            else:
                print(index_max_even)
    elif "min" in command:
        if "odd" in command:
            found_odd = False
            min_odd = sys.maxsize
            index_min_odd = 0
            for i in range(len(integers)):
                if integers[i] % 2 != 0 and integers[i] <= min_odd:
                    min_odd = integers[i]
                    index_min_odd = i
                    found_odd = True

            if not found_odd:
                print("No matches")
            else:
                print(index_min_odd)
        elif "even" in command:
            found_even = False
            min_even = sys.maxsize
            index_min_even = 0
            for i in range(len(integers)):
                if integers[i] % 2 == 0 and integers[i] <= min_even:
                    min_even = integers[i]
                    index_min_even = i
                    found_even = True

            if not found_even:
                print("No matches")
            else:
                print(index_min_even)
    elif "first" in command:
        command = command.split(" ")
        count = int(command[1])
        if 1 <= count <= len(integers):
            if "odd" in command:
                odd_counter = 0
                odd_numbers = []
                for i in range(len(integers)):
                    if integers[i] % 2 != 0:
                        odd_counter += 1
                        odd_numbers.append(integers[i])
                        if odd_counter == count:
                            break
                print(odd_numbers)
            elif "even" in command:
                even_counter = 0
                even_numbers = []
                for i in range(len(integers)):
                    if integers[i] % 2 == 0:
                        even_counter += 1
                        even_numbers.append(integers[i])
                        if even_counter == count:
                            break
                print(even_numbers)
        else:
            print("Invalid count")
    elif "last" in command:
        command = command.split(" ")
        count = int(command[1])
        if 1 <= count <= len(integers):
            numbers = []
            if "odd" in command:
                odd_counter = 0
                for i in range(len(integers) - 1, -1, -1):
                    if integers[i] % 2 != 0:
                        odd_counter += 1
                        numbers.append(integers[i])
                        if odd_counter == count:
                            break
            elif "even" in command:
                even_counter = 0
                for i in range(len(integers) - 1, -1, -1):
                    if integers[i] % 2 == 0:
                        even_counter += 1
                        numbers.append(integers[i])
                        if even_counter == count:
                            break
            reverse_numbers = []
            for i in range(len(numbers) - 1, -1, -1):
                reverse_numbers.append(numbers[i])
            numbers = reverse_numbers

            print(numbers)

        else:
            print("Invalid count")

    command = input()

print(integers)
