a = int(input())
b = int(input())
save_num = a
print(f"Before: \na = {a} \nb = {b}")
is_printed = True
if is_printed:
    a = b
    b = save_num
print(f"After: \na = {a} \nb = {b}")