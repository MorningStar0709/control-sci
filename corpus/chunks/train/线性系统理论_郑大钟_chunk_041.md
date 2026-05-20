$$
\dot {x} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ 0 & & & 1 & \\ - a _ {0} & - a _ {1} & \dots & - a _ {n - 1} \end{array} \right] x + \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] u
y = \left[ b _ {0}, \dots , b _ {m}, 0, \dots , 0 \right] x \tag {1.35}
$$

例 给定系统的输入-输出描述为:

$$y ^ {(3)} + 1 6 y ^ {(2)} + 1 9 4 y ^ {(1)} + 6 4 0 y = 1 6 0 u ^ {(1)} + 7 2 0 u$$

则利用（1.35）即可定出相应的一个状态空间描述为：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 4 0 & - 1 9 4 & - 1 6 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u

y = [ 7 2 0 \quad 1 6 0 \quad 0 ] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

(2) 当 $m = n$ 时: 先将 (1.29) 中的有理分式进行严格真化, 可导出:

$$y = \left[ b _ {n} + \frac {\left(b _ {n - 1} - b _ {n} a _ {n - 1}\right) p ^ {n - 1} + \cdots + \left(b _ {0} - b _ {s} a _ {0}\right)}{p ^ {n} + a _ {n - 1} p ^ {n - 1} + \cdots + a _ {1} p + a _ {0}} \right] u \tag {1.36}$$

并由此可进而表为：

$$
\left\{ \begin{array}{l} \tilde {y} ^ {(n)} + a _ {n - 1} \tilde {y} ^ {(n - 1)} + \dots + a _ {1} \tilde {y} ^ {(1)} + a _ {0} \tilde {y} = u \\ y = (b _ {n - 1} - b _ {n} a _ {n - 1}) \tilde {y} ^ {(n - 1)} + \dots + (b _ {0} - b _ {n} a _ {0}) \tilde {y} + b _ {n} u \end{array} \right. \tag {1.37}
$$

注意到（1.37）的第一个方程等同于（1.31）的第一个方程，所以在按（1.32）的状态变量组的选取下，可知其状态方程同于 $m < n$ 的情况。而由（1.37）的第二个方程，则可进而得到：

$$y = \left(b _ {0} - b _ {n} a _ {0}\right) x _ {1} + \dots + \left(b _ {n - 1} - b _ {n} a _ {n - 1}\right) x _ {n} + b _ {n} u \tag {1.38}$$

由此即可导出此种情况下对应于输入-输出描述（1.27）的状态空间描述为：

$$
\dot {x} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ \vdots & & & \ddots & \\ 0 & & & & 1 \\ \hline - a _ {0} & - a _ {1} & \dots & - a _ {n - 1} \end{array} \right] x + \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ 1 \end{array} \right] u
y = \left[ \left(b _ {0} - b _ {n} a _ {0}\right), \dots , \left(b _ {n - 1} - b _ {n} a _ {n - 1}\right) \right] x + b _ {n} u \tag {1.39}
$$

例 给定系统的输入-输出描述为:

$$y ^ {(3)} + 1 6 y ^ {(2)} + 1 9 4 y ^ {(1)} + 6 4 0 y = 4 u ^ {(3)} + 1 6 0 u ^ {(1)} + 7 2 0 u$$

则利用（1.39）即可定出其相应的一个状态空间描述为：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 4 0 & - 1 9 4 & - 1 6 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] u
