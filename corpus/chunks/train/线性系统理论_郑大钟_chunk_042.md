y = \left[ - 1 8 4 0 - 6 1 6 - 6 4 \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + 4 u
$$

算法之二 为易于理解,不妨区分为 m=0 和 m=n 的两种情况来进行讨论。实质上, m=n 的情况代表了一般的情况。当 m 为小于 n 的任意正整数时, 即等价于所讨论的情况中, 系数 $b_{k}=0$ , k=n, $n-1,\cdots,m+1$ 。

(1) 当 m = 0 时：此时，输入-输出描述 (1.27) 可写成为：

$$y ^ {(n)} + a _ {s - 1} y ^ {(n - 1)} + \dots + a _ {1} y ^ {(1)} + a _ {0} y = b _ {0} u \tag {1.40}$$

再取状态变量组为：

$$x _ {1} = y, x _ {2} = y ^ {(1)}, \dots , x _ {n} = y ^ {(n - 1)} \tag {1.41}$$

那么，由此就可导出

$$y = x _ {1} \tag {1.42}$$

和

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = y ^ {(1)} - x _ {2} \\ \dot {x} _ {2} = y ^ {(2)} - x _ {3} \\ \dots \dots \\ \dot {x} _ {n - 1} = y ^ {(n - 1)} = x _ {n} \\ \dot {x} _ {n} = - a _ {0} x _ {1} - a _ {1} x _ {2} - \dots - a _ {n - 1} x _ {n} + b _ {0} u \end{array} \right. \tag {1.43}
$$

令状态向量 $x = [x_{1}, \cdots, x_{n}]^{T}$ ，并将上述方程表为向量方程的形式，即得到此种情况下的状态空间描述为：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c c c} 0 & 1 & & & \\ \vdots & & \ddots & & \\ 0 & & & 1 & \\ - a _ {0} & - a _ {1} & \dots & - a _ {n - 1} \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \\ b _ {0} \end{array} \right] u
y = [ 1 0 \dots 0 ] x \tag {1.44}
$$

(2) 当 m = n 时：此时，输入-输出描述具有如下的形式：

$$y ^ {(m)} + a _ {n - 1} y ^ {(m - 1)} + \dots + a _ {1} y ^ {(1)} + a _ {0} y= b _ {n} u ^ {(n)} + \dots + b _ {1} u ^ {(1)} + b _ {0} u \tag {1.45}$$

并把状态变量组取为 y 和 u 及它们的各阶导数的适当组合：

$$
\left\{ \begin{array}{l} x _ {1} = y - \beta_ {0} u \\ x _ {2} = y ^ {(1)} - \beta_ {0} u ^ {(1)} - \beta_ {1} u \\ x _ {3} = y ^ {(2)} - \beta_ {0} u ^ {(2)} - \beta_ {1} u ^ {(1)} - \beta_ {2} u \\ \dots \dots \\ x _ {n} = y ^ {(n - 1)} - \beta_ {0} u ^ {(n - 1)} - \beta_ {1} u ^ {(n - 2)} - \dots - \beta_ {n - 2} u ^ {(1)} - \beta_ {n - 1} u \end{array} \right. \tag {1.46}
$$

式中，待定常数 $\beta_{0}, \beta_{1}, \cdots, \beta_{n-1}$ 的计算式可这样地来导出：先由（1.46）可得

$$
\left\{ \begin{array}{l} a _ {0} y = a _ {0} x _ {1} + a _ {0} \beta_ {0} u \\ a _ {1} y ^ {(1)} = a _ {1} x _ {2} + a _ {1} \beta_ {0} u ^ {(1)} + a _ {1} \beta_ {1} u \\ a _ {2} y ^ {(2)} = a _ {2} x _ {3} + a _ {2} \beta_ {0} u ^ {(2)} + a _ {2} \beta_ {1} u ^ {(1)} + a _ {2} \beta_ {2} u \\ \dots \dots \\ a _ {n - 1} y ^ {(n - 1)} = a _ {n - 1} x _ {n} + a _ {n - 1} \beta_ {0} u ^ {(n - 1)} + \dots + a _ {n - 1} \beta_ {n - 1} u \\ y ^ {(n)} = x _ {n + 1} + \beta_ {0} u ^ {(n)} + \beta_ {1} u ^ {(n - 1)} + \dots + \beta_ {n - 1} u ^ {(1)} + \beta_ {n} u \end{array} \right. \tag {1.47}
$$

容易看出，(1.47)各式的等式左边相加的结果即等于式(1.45)的等式左边的表达式，因此(1.47)各式的等式右边相加的结果必等于式(1.45)的等式右边的表达式，从而有
