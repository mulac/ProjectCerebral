import math
import sys
import os


def dist_from_pivot(x, y):
    square = (21-x)**2 + (21-y)**2
    return math.sqrt(square)


def upper(d):
    return d / 3


def lower(d):
    theta = math.acos(d/60)
    return math.sqrt(153 + 67.88225099 * math.cos(theta+40/75))


def base(x, y):
    angle = math.atan2((210-x), (210-y)) - math.pi / 4
    motor_conversion = 1100 / 0.726
    return angle * motor_conversion


def move_arm(x, y):
    d = dist_from_pivot(x, y)

    u = upper(d)
    l = lower(d)
    b = base(x, y)

    return u, l, b


def make_tictactoe_move(move, counters):
    # for now we just want to see if the arm can move to the right place on the board
    u1, l1, b1 = 0, 0, 0
    # Move arm to next available counter
    # free_counter = counters['spare'][0]
    # u1, l1, b1 = move_arm(*free_counter.translate_from_origin())

    # Finds the position of empty move space
    x, y = counters[move].translate_from_origin()
    #u2, l2, b2 = move_arm(x, y)
    b2 = base(x, y)

    os.system("ssh ev3 ./ev3control.py {} {} {} {} {} {}".format(u1, l1, b1, 0, 0, b2))


if __name__ == '__main__':
    assert len(sys.argv) == 3

    print(move_arm(int(sys.argv[1]), int(sys.argv[2])))

