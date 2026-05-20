图 9-10 例 9-3 可观测标准型状态变量图

2) $\frac{N(s)}{D(s)}$ 只含单实极点时的情况。当 $\frac{N(s)}{D(s)}$ 只含单实极点时，除了可化为上述可控标准型或可观测标准型动态方程以外，还可化为对角型动态方程，其 $\mathbf{A}$ 阵是一个对角阵。

设 $D(s)$ 可分解为

$$D (s) = (s - \lambda_ {1}) (s - \lambda_ {2}) \dots (s - \lambda_ {n})$$

式中， $\lambda_{1},\cdots,\lambda_{n}$ 为系统的单实极点，则传递函数可展成部分分式之和

$$\frac {Y (s)}{U (s)} = \frac {N (s)}{D (s)} = \sum_ {i = 1} ^ {n} \frac {c _ {i}}{s - \lambda_ {i}}$$

而 $c_{i} = \left[\frac{N(s)}{D(s)} (s - \lambda_{i})\right]\Bigg|_{s = \lambda_{i}}$ ，为 $\frac{N(s)}{D(s)}$ 在极点 $\lambda_{i}$ 处的留数，且有

$$Y (s) = \sum_ {i = 1} ^ {n} \frac {c _ {i}}{s - \lambda_ {i}} U (s)$$

若令状态变量

$$X _ {i} (s) = \frac {1}{s - \lambda_ {i}} U (s); \quad i = 1, 2, \dots , n$$

其反变换结果为

$$\dot {x} _ {i} (t) = \lambda_ {i} x _ {i} (t) + u (t)y (t) = \sum_ {i = 1} ^ {n} c _ {i} x _ {i} (t)$$

展开得 $\dot{x}_1 = \lambda_1x_1 + u$

$$\dot {x} _ {2} = \lambda_ {2} x _ {2} + u$$

:

$$\dot {x} _ {n} = \lambda_ {n} x _ {n} + uy = c _ {1} x _ {1} + c _ {2} x _ {2} + \dots + c _ {n} x _ {n}$$

其向量-矩阵形式为

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \vdots \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{l l l l} \lambda_ {1} & & & 0 \\ & \lambda_ {2} & & \\ 0 & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \\ \vdots \\ 1 \end{array} \right] u, \quad y = \left[ \begin{array}{l l l l} c _ {1} & c _ {2} & \dots & c _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right] \tag {9-18}
$$

其状态变量图如图 9-11(a) 所示。

若令状态变量

$$X _ {i} (s) = \frac {c _ {i}}{s - \lambda_ {i}} U (s); \quad i = 1, 2, \dots , n$$

则 $Y(s) = \sum_{i=1}^{n} X_i(s)$

进行反变换并展开有

$$\dot {x} _ {1} = \lambda_ {1} x _ {1} + c _ {1} u\dot {x} _ {2} = \lambda_ {2} x _ {2} + c _ {2} u$$

:

$$\dot {x} _ {n} = \lambda_ {n} x _ {n} + c _ {n} uy = x _ {1} + x _ {2} + \dots + x _ {n}$$

其向量-矩阵形式为

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \vdots \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{l l l l} \lambda_ {1} & & & 0 \\ & \lambda_ {2} & & \\ 0 & & \ddots & \\ & & & \lambda_ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} c _ {1} \\ c _ {2} \\ \vdots \\ c _ {n} \end{array} \right] u, \quad y = [ 1, 1, \dots , 1 ] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right] \tag {9-19}
$$

其状态变量图如图 9-11(b) 所示。显见式(9-19)与式(9-18)存在对偶关系。
