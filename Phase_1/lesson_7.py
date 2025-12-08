def calculate_distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

print(calculate_distance(0, 0, 3, 4))
print(calculate_distance(1, 2, 4, 6))