(1) $H_{n}$ 的第一列的元依次是 $a_{1}, a_{3}, a_{5}, \cdots$ , 不足部分用零补上:  
(2) $H_{n}$ 的第二列的第一元为 1, 然后依次是 $a_{2}, a_{4}, a_{6}, \cdots$ . 不足部分用零补上,  
(3) $H_{n}$ 的第三列的第一元为0, 然后仿第一列组成方式:  
(4) 第四列的第一个元是 0, 往下与第二列的组成方式相同:

如此重复前面的手续，直到第 $n$ 列为止.

例如，多项式 $\varphi_5(\lambda) = \lambda^5 + a_1\lambda^4 + a_2\lambda^3 + a_3\lambda^2 + a_4\lambda + a_5$ 的矩阵 $H_5$ 为

$$
H _ {5} = \left[ \begin{array}{c c c c c} a _ {1} & 1 & 0 & 0 & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 & 0 \\ a _ {5} & a _ {4} & a _ {3} & a _ {2} & a _ {1} \\ 0 & 0 & a _ {5} & a _ {4} & a _ {3} \\ 0 & 0 & 0 & 0 & a _ {5} \end{array} \right].
$$

矩阵 $H_{n}$ 称为多项式 $\varphi_{n}(\lambda)$ 的 Hurwitz 矩阵，它的主对角线上的元是多项式 $\varphi_{n}(\lambda)$ 的系数。Hurwitz 矩阵的主对角线上的诸子阵的行列式分别记为 $\Delta_{1}, \Delta_{2}, \cdots, \Delta_{n}$ ，即

$$
\begin{array}{l} \Delta_ {1} = a _ {1}, \quad \Delta_ {2} = \left| \begin{array}{l l} a _ {1} & 1 \\ a _ {3} & a _ {2} \end{array} \right|, \quad \Delta_ {3} = \left| \begin{array}{l l l} a _ {1} & 1 & 0 \\ a _ {3} & a _ {2} & a _ {1} \\ a _ {5} & a _ {4} & a _ {3} \end{array} \right|. \\ \dots , \quad \Delta_ {n} = \left[ \begin{array}{c c c c c c} a _ {1} & 1 & 0 & 0 & \dots & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 & \dots & 0 \\ a _ {5} & a _ {4} & a _ {3} & a _ {2} & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & 0 & \dots & a _ {n} \end{array} \right] = a _ {n} \Delta_ {n - 1} = \det H _ {n}. \\ \end{array}
$$

$\Delta_{1},\Delta_{2},\cdots,\Delta_{n}$ 皆称为Hurwitz行列式.

定理 2.4.3(Routh-Hurwitz 定理) $^{[12]}$ 为了 $\varphi_{n}(\lambda)$ 是稳定多项式，必须且只需其 Hurwitz 行列式皆为正，即 $\Delta_{k}>0, k=1,\cdots,n.$

研究稳定多项式的另一个方便的工具是 Routh 矩阵，定义如下：

定义2.4.8 实系数多项式

$$g (\lambda) = q _ {n} \lambda^ {n} + q _ {n - 1} \lambda^ {n - 1} + \dots + q _ {1} \lambda + q _ {0} \tag {2.4.10}$$

的Routh矩阵 $\pmb{R}$ 定义为

$$
\boldsymbol {R} = \left[ \begin{array}{c c c c} q _ {n} & q _ {n - 2} & q _ {n - 4} & \dots \\ q _ {n - 1} & q _ {n - 3} & q _ {n - 5} & \dots \\ a _ {1 1} & a _ {1 2} & a _ {1 3} & \dots \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & \dots \\ \vdots & \vdots & \vdots \\ a _ {(n - 1) 1} & a _ {(n - 1) 2} & a _ {(n - 1) 3} & \dots \end{array} \right],
$$

这里

$$
\begin{array}{l} a _ {1 1} = \frac {q _ {n - 1} q _ {n - 2} - q _ {n} q _ {n - 3}}{q _ {n - 1}}, \\ a _ {1 2} = \frac {q _ {n - 1} q _ {n - 4} - q _ {n} q _ {n - 3}}{q _ {n - 1}}, \\ a _ {2 1} = \frac {a _ {1 1} q _ {n - 3} - a _ {1 2} q _ {n - 1}}{a _ {1 1}}, \\ a _ {2 2} = \frac {a _ {1 1} q _ {n - 5} - a _ {1 3} q _ {n - 1}}{a _ {1 1}}, \\ a _ {(n - 1) 1} = \frac {a _ {(n - 2) 1} a _ {(n - 3) 1} - a _ {(n - 2) 2} a _ {(n - 3) 2}}{a _ {(n - 2) 1}}. \\ \end{array}
$$

...

定理 2.4.4 $^{[14]}$ $y(\lambda)$ 为稳定多项式的充要条件是矩阵 R 的第一列元素非零同号.
