import numpy as np
from random import shuffle
import matplotlib.pyplot as plt

import argparse

from sklearn import svm


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

    clf = svm.LinearSVC(penalty='l1', class_weight={-1: 0.1, 1: 1.0}, tol=1e-8, max_iter=1000000, dual=False) 
    clf.fit(X, y)
    clf.densify()

    w =[clf.coef_[0][0], clf.coef_[0][1], clf.intercept_[0]]
    print("Score:", clf.score(X, y))
    print("Best weight [w0, w1, w2]:", w)
    print("Limit define by plane {:.4f}x + {:.4f}y + {:.4f} > 0".format(*w))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    print("data", y)
    good = X[y == +1, :]
    bad = X[y == -1, :]

    ax.scatter(good[:, 0], good[:, 1])
    ax.scatter(bad[:, 0], bad[:, 1])

    # w0*x + w1*y + w2 = 0
    ax.plot([0, -w[2]/w[0]], [-w[2]/w[1], 0], '-')

    plt.show()
