import numpy as np
from random import shuffle
import matplotlib.pyplot as plt

import argparse

def load_file(file_path):
    with open(file_path) as file:
        raw_data = []
        for line in file.readlines():
            # Remove useless log header, ex: "INFO|294301|R4|B15.5|"
            _, pipe, sample_str = line.rpartition("|")
            assert pipe == "|"
            sample_str = sample_str.strip()

            # Checking for the header
            if sample_str == "id,left,right,good":
                continue
            line_data = [int(value) for value in sample_str.split(",")]
            raw_data.append(line_data)
        return raw_data

point = [None, None]
point_nb = 0

def onclick(event):
    global point_nb
    global point
    global line
    global good, bad
    x, y = event.xdata, event.ydata
    point[point_nb] = (x, y)
    point_nb += 1

    if point_nb >= 2:
        point_nb = 0
        # ax + by = c,
        # [x1, y1][a] = [0]
        # [x2, y2][b]   [0]
        m = (point[1][1] - point[0][1]) / (point[1][0] - point[0][0])
        b = y - m * x
        # cy = mx +b
        w = [-m, 1, -b]
        print("Best weight [w0, w1, w2]:", w)
        print("Limit define by plane {:.4f}x + {:.4f}y + {:.4f} > 0".format(*w))
        line.set_data([0, -w[2]/w[0]], [-w[2]/w[1], 0])
        line.figure.canvas.draw()

        error = 0
        print("[test good points]")
        for i in range(0, good.shape[0]):
            res = w[0]*good[i, 0] + w[1]*good[i, 1] + w[2]
            if res <= 0:
                print("error", good[i, :], res > 0, " != true")
                error += 1
        print("[test bad points]")
        for i in range(0, bad.shape[0]):
            res = w[0]*bad[i, 0] + w[1]*bad[i, 1] + w[2]
            if res > 0:
                print("error", bad[i, :], res > 0, " != false")
                error += 1

        print(f"Error {error}/{good.shape[0] + bad.shape[0]}")

        # ax.plot([0, -w[2]/w[0]], [-w[2]/w[1], 0], '-')


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(prog='IR calibration for ULTRON\'s robots.')

    arg_parser.add_argument('calib_file',
                            action='store',
                            help='Sample points from the bluetooth calibration-tool')

    args = arg_parser.parse_args()

    data = load_file(args.calib_file)

    data = np.array(data)
    # data[0, :] => (id, left, right, class)
    X = data[:, 1:3]
    y = data[:, 3]

    fig = plt.figure()
    fig.canvas.mpl_connect('button_press_event', onclick)
    ax = fig.add_subplot(1, 1, 1)

    print("data", y)
    good = X[y == +1, :]
    bad = X[y == -1, :]

    ax.scatter(good[:, 0], good[:, 1])
    ax.scatter(bad[:, 0], bad[:, 1])

    # w0*x + w1*y + w2 = 0
    # ax.plot([0, -w[2]/w[0]], [-w[2]/w[1], 0], '-')
    line, = ax.plot([0], [0])

    plt.show()
