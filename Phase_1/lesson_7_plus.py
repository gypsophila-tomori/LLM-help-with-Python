import math 

def calculate_center_distance(box1, box2):
    cx1 = (box1[0] + box1[2]) / 2
    cx2 = (box2[0] + box2[2]) / 2

    cy1 = (box1[1] + box1[3]) / 2
    cy2 = (box2[1] + box2[3]) / 2
    distance = math.sqrt((cx1 - cx2)**2 + (cy1 - cy2)**2)
    return distance


def main():
    box_a = [10, 20, 100, 200]
    box_b = [50, 60, 150, 250]
    result = calculate_center_distance(box_a, box_b)
    print(f"The distance between centers is: {result}")

if __name__ == "__main__":
    main()