def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_areas(radius):
    circle_areas = radius * radius * 3.14
    return circle_areas

prompt = "넓이를 구하고자 하는 원의 반지름은?"
radius = get_radius(prompt)
result = get_circle_areas(radius)
print("반지름", radius, end = "")
print("인 원의 넓이 =", radius, "X", radius, "X 3.14 =", result)
