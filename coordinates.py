from random import random


class Point:
    """
    Your class definition below! Remember to get rid of the pass keyword.
    """
    pass


def main():
    # Generating random coordinates and creating our first Point object.
    x_coord1 = round(random() * 100)
    y_coord1 = round(random() * 100)
    point_1 = Point(x_coord1, y_coord1)

    # Generating random coordinates and creating our second Point object.
    x_coord2 = round(random() * 100)
    y_coord2 = round(random() * 100)
    point_2 = Point(x_coord2, y_coord2)

    print("Point 1 coordinates: ({}, {})".format(point_1.x_coord, point_1.y_coord))
    print("Point 2 coordinates: ({}, {})".format(point_2.x_coord, point_2.y_coord))

    """
    MAKE SURE THE THE CODE ABOVE WORKS BEFORE MOVING ON! Then you can uncomment the next section below.
    """

    # # Calculating the distance between them according to their respective coordinates
    # # You could have also called the get_distance() method of point_2. Both ways yield the same answer
    # distance = point_1.get_distance(point_2)
    #
    # # Printing our rounded result
    # print("The distance between these two points is ~{}".format(round(distance, 3)))
    #
    # some_point = Point(4, 5.6)
    # other_point = Point(10, 29.3)
    #
    # distance = some_point.get_distance(other_point)
    # print(distance)

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
