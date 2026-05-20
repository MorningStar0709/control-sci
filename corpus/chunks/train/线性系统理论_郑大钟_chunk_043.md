$$\left\{x _ {n + 1} + a _ {n - 1} x _ {n} + \dots + a _ {1} x _ {2} + a _ {0} x _ {1} \right\} + \left\{\beta_ {0} u ^ {(m)} + \left(\beta_ {1} + a _ {n - 1} \beta_ {0}\right) \right.\cdot u ^ {(n - 1)} + \dots + \left(\beta_ {n - 1} + a _ {n - 1} \beta_ {n - 2} + \dots + a _ {2} \beta_ {1} + a _ {1} \beta_ {0}\right) u ^ {(1)}+ \left(\beta_ {n} + a _ {n - 1} \beta_ {n - 1} + \dots + a _ {1} \beta_ {1} + a _ {0} \beta_ {0}\right) u \}= b _ {n} u ^ {(n)} + \dots + b _ {1} u ^ {(1)} + b _ {0} u \tag {1.48}$$

比较上式中 $u^{(i)}\left(i=0,1,\cdots,n\right)$ 的系数，于是可导出：

$$
\left\{ \begin{array}{l} \beta_ {0} = b _ {n} \\ \beta_ {1} = b _ {n - 1} - a _ {n - 1} \beta_ {0} \\ \beta_ {2} = b _ {n - 2} - a _ {n - 1} \beta_ {1} - a _ {n - 2} \beta_ {0} \\ \dots \dots \\ \beta_ {n} = b _ {0} - a _ {n - 1} \beta_ {n - 1} - a _ {n - 2} \beta_ {n - 2} - \dots - a _ {1} \beta_ {1} - a _ {0} \beta_ {0} \end{array} \right. \tag {1.49}
$$

进而，由（1.46）、（1.45）和（1.48），又可得到：

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = y ^ {(1)} - \beta_ {0} u ^ {(1)} = x _ {2} + \beta_ {1} u \\ \dot {x} _ {2} = y ^ {(2)} - \beta_ {0} u ^ {(2)} - \beta_ {1} u ^ {(1)} = x _ {3} + \beta_ {2} u \\ \dots \dots \\ \dot {x} _ {n - 1} = y ^ {(n - 1)} - \beta_ {0} u ^ {(n - 1)} - \dots - \beta_ {n - 2} u ^ {(1)} = x _ {n} + \beta_ {n - 1} u \end{array} \right. \tag {1.50}

\left\{ \begin{array}{l} \dot {x} _ {n} = y ^ {(n)} - \beta_ {0} u ^ {(n)} - \beta_ {1} u ^ {(n - 1)} - \dots - \beta_ {n - 1} u ^ {(1)} = x _ {n + 1} + \beta_ {n} u \\ = - a _ {0} x _ {1} - a _ {1} x _ {2} - \dots - a _ {n - 1} x _ {n} + \beta_ {n} u \end{array} \right.
$$

和

$$y = x _ {1} + \beta_ {0} u \tag {1.51}$$

表 $x = [x_{1}, \cdots, x_{n}]^{T}$ ，并注意到 $\beta_{0} = b_{n}$ ，所以将（1.50）和（1.51）表示为向量方程的形式就可得到此种情况下的状态空间描述为：

$$
\dot {x} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ \vdots & & & \ddots & \\ 0 & & & & 1 \\ \hline - a _ {0} & - a _ {1} & \dots & - a _ {n - 1} \end{array} \right] x + \left[ \begin{array}{c} \beta_ {1} \\ \vdots \\ \beta_ {n} \end{array} \right] u
y = [ 1 0 \dots 0 ] x + b _ {n} u \tag {1.52}
$$

例 给定系统的输入-输出描述为：

$$y ^ {(3)} + 1 6 y ^ {(2)} + 1 9 4 y ^ {(1)} + 6 4 0 y = 4 u ^ {(3)} + 1 6 0 u ^ {(1)} + 7 2 0 u$$

先利用(1.49)定出:

$$b _ {n}\beta_ {0} = b _ {3} = 4\beta_ {1} = b _ {2} - a _ {2} \beta_ {0} = - 6 4\beta_ {2} = b _ {1} - a _ {2} \beta_ {1} - a _ {1} \beta_ {0} = 4 0 8\beta_ {3} = b _ {0} - a _ {2} \beta_ {2} - a _ {1} \beta_ {1} - a _ {0} \beta_ {0} = 4 0 4 8$$

从而，由（1.52）即可导出相应的一个状态空间描述为：

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 4 0 & - 1 9 4 & - 1 6 \end{array} \right] x + \left[ \begin{array}{l} - 6 4 \\ 4 0 8 \\ 4 0 4 8 \end{array} \right] u

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] x + 4 u
$$
