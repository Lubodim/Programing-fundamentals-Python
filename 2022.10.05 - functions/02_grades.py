grade = float(input())

def Grade(x):
    if 2 <= x < 3:
        return "Fail"
    elif 3 <= x < 3.5:
        return "Poor"
    elif 3.5 <= x < 4.5:
        return "Good"
    elif 4.5 <= x < 5.5:
        return "Very Good"
    elif 5.5 <= x < 6:
        return "Excellent"

print(Grade(grade))