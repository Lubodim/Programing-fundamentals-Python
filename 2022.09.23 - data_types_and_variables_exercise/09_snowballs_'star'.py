number_of_snowballs = int(input())
snowball_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_quality_dict = {}
for snowballs in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    best_snowball = int(snowball_weight / snowball_time) ** snowball_quality
    if best_snowball > snowball_value:
        snowball_value = best_snowball
        snowball_quality_dict = {"snowball_weight": snowball_weight, "snowball_time": snowball_time,
                                 "snowball_value": snowball_value, "snowball_quality": snowball_quality}
print(snowball_quality_dict["snowball_weight"], end=" : ")
print(snowball_quality_dict["snowball_time"], end=" = ")
print(snowball_quality_dict["snowball_value"], end=" (")
print(snowball_quality_dict["snowball_quality"], end=")")


