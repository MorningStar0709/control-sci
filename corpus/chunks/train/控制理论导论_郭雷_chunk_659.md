$$c _ {i j} ^ {k} = \frac {\partial^ {2} q _ {k}}{\partial z _ {i} \partial x _ {j}} (0), \quad k = 1, 2, \quad i = 1, 2, \quad j = 1, 3;d _ {i j} ^ {k} = \frac {\partial^ {3} q _ {k}}{i ! j ! \partial (z _ {1}) ^ {i} \partial (z _ {2}) ^ {j}} (0), \quad k = 1, 2, \quad i + j = 3;\psi_ {1} = a z _ {1} ^ {2} + b z _ {1} z _ {2} + c z _ {2} ^ {2}, \quad \psi_ {2} = d z _ {1} ^ {2} + e z _ {1} z _ {2} + f z _ {2} ^ {2}.$$

于是式 (8.6.42) 变为

$$
\dot {z} = \left[ \begin{array}{l l} c _ {1 1} ^ {1} z _ {1} + c _ {2 1} ^ {1} z _ {2} & c _ {1 3} ^ {1} z _ {1} + c _ {2 3} ^ {1} z _ {2} \\ c _ {1 1} ^ {2} z _ {1} + c _ {2 1} ^ {2} z _ {2} & c _ {1 3} ^ {2} z _ {1} + c _ {2 3} ^ {2} z _ {2} \end{array} \right] \left[ \begin{array}{l} \psi_ {1} (z) \\ \psi_ {2} (z) \end{array} \right] + \left[ \begin{array}{l} \sum_ {t = 0} ^ {3} d _ {t 3 - t} ^ {1} z _ {1} ^ {t} z _ {2} ^ {3 - t} \\ \sum_ {t = 0} ^ {3} d _ {t 3 - t} ^ {2} z _ {1} ^ {t} z _ {2} ^ {3 - t} \end{array} \right]. \tag {8.6.44}
$$

这样前面那些充分条件就可用来判定它的稳定性. 为使以上例子更具体化, 我们考虑下面这个系统 (8.6.43) 的特殊形式

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2}, \\ \dot {x} _ {2} = f _ {1} (x, z) + g _ {1} (x, z) u _ {1}, \\ \dot {x} _ {3} = f _ {2} (x, z) + g _ {2} (x, z) u _ {2}, \\ \dot {z} _ {1} = \sin (x _ {1} z _ {1} - z _ {1} ^ {2} z _ {2}) - 3 \tan (z _ {1} ^ {2} z _ {2}), \\ \dot {z} _ {2} = z _ {1} - z _ {2} + z _ {2} ^ {3} - z _ {1} \mathrm{e} ^ {x _ {1}} + z _ {2} \mathrm{e} ^ {x _ {3}}. \end{array} \right. \tag {8.6.45}
$$

于是有关系数可计算如下：

$$
\begin{array}{l} c _ {1 1} ^ {1} = 1, \quad c _ {1 3} ^ {1} = 0, \quad c _ {2 1} ^ {1} = 0, \quad c _ {2 3} ^ {1} = 0, \\ c _ {1 1} ^ {2} = - 1, \quad c _ {1 3} ^ {2} = 0, \quad c _ {2 1} ^ {2} = 0, \quad c _ {2 3} ^ {2} = 1, \\ d _ {3 0} ^ {1} = 0, \quad d _ {2 1} ^ {1} = - 4, \quad d _ {1 2} ^ {1} = 0, \quad d _ {0 3} ^ {1} = 0, \\ d _ {3 0} ^ {2} = 0, \quad d _ {2 1} ^ {2} = 0, \quad d _ {1 2} ^ {2} = 0, \quad d _ {0 3} ^ {2} = 1. \\ \end{array}
$$

式 (8.6.44) 变为

$$
\begin{array}{l} \left[ \begin{array}{c c} z _ {1} & 0 \\ - z _ {1} & z _ {2} \end{array} \right] \left[ \begin{array}{c} \psi_ {1} (z) \\ \psi_ {2} (z) \end{array} \right] + \left[ \begin{array}{c} - 4 z _ {1} ^ {2} z _ {2} \\ z _ {2} ^ {3} \end{array} \right] \\ = \left[ \begin{array}{c} a z _ {1} ^ {3} + b z _ {1} ^ {2} z _ {2} + c z _ {1} z _ {2} ^ {2} - 4 z _ {1} ^ {2} z _ {2} \\ - a z _ {1} ^ {3} + (d - b) z _ {1} ^ {2} z _ {2} + (e - c) z _ {1} z _ {2} ^ {2} + (f + 1) z _ {2} ^ {3} \end{array} \right]. \tag {8.6.46} \\ \end{array}
$$

利用 CRDDP 且令 m = 2, 则得
