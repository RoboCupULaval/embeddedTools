import numpy as np
from random import shuffle
import matplotlib.pyplot as plt

from sklearn import svm

data = [
    [1186,	546  , 1],
    [1448,	582  , 1],
    [1264,	640  , 1],
    [758	,780 , 1],
    [472	,1376, 1],
    [433	,1360, 1],
    [410	,1344, 1],
    [410	,1000, 1],
    [400	,1060, 1],
    [407	,1730, 1],
    [440	,1453, 1],
    [598	,1040, 1],
    [1055,	686  , 1],
    [1440,	610  , 1],
    [1736,	636  , 1],
    [614,	462, -1] ,
    [728,	473, -1] ,
    [532,	504, -1] ,
    [434,	558, -1] ,
    [406,	652, -1] ,
    [404,	506, -1] ,
    [400,	420, -1] ,
    [473,	440, -1] ,
    [400,	416, -1] ,
    [403,	419, -1],
    [660,	680, -1],
    [620,	640, -1],
    [504,	518, -1],
    [440,	442, -1],
    [468,	520, -1],
    [430,	480, -1],
    [580,	655, -1]
]

data = np.array(data)
X = data[:, 0:2]
y = data[:, 2]

clf = svm.LinearSVC(max_iter=100000, dual=False)
clf.fit(X, y)
clf.densify()

w =[clf.coef_[0][0], clf.coef_[0][1], clf.intercept_[0]]
print("Score:", clf.score(X, y))
print("Best weight [w0, w1, w2]:", w)
print("Limit define by plane {:.4f}x + {:.4f}y + {:.4f} > 0".format(*w))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

good = X[y ==  1, :]
bad = X[y == -1, :]

ax.scatter(good[:, 0], good[:, 1])
ax.scatter(bad[:, 0], bad[:, 1])

# w0*x + w1*y + w2 = 0
ax.plot([0, -w[2]/w[0]], [-w[2]/w[1], 0], '-')


plt.show()