# (1) 根据系统机理建立状态空间表达式

下面通过例题来介绍根据系统机理建立线性定常连续系统状态空间表达式的方法。

例 9-1 试列写如图 9-4 所示 RLC 网络的电路方程,选择几组状态变量并建立相应的状态空间表达式,就所选状态变量间的关系进行讨论。

解 根据电路定律可列写如下方程：

$$R i + L \frac {\mathrm{d} i}{\mathrm{d} t} + \frac {1}{C} \int i \mathrm{d} t = e$$

电路输出量为

$$y = e _ {c} = \frac {1}{C} \int i \mathrm{d} t$$

![](image/11219dc2f6d7d12b9a475421fe92dbe668defe5a3dadfbcb51303105ae242d04.jpg)

<details>
<summary>text_image</summary>

R
L
e
i
C
e_c
</details>

图 9-4 RLC 网络

1) 设状态变量 $x_{1} = i, x_{2} = \frac{1}{C} \int i \mathrm{d}t$ ，则状态方程为

$$\dot {x} _ {1} = - \frac {R}{L} x _ {1} - \frac {1}{L} x _ {2} + \frac {1}{L} e\dot {x} _ {2} = \frac {1}{C} x _ {1}$$

输出方程为

$$y = x _ {2}$$

其向量-矩阵形式为

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - \frac {R}{L} & - \frac {1}{L} \\ \frac {1}{C} & 0 \end{array} \right], \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} \frac {1}{L} \\ 0 \end{array} \right] e

y = \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

简记为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b e}y = c x$$

式中

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right], \boldsymbol {x} = \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right], \boldsymbol {A} = \left[ \begin{array}{c c} - \frac {R}{L} & - \frac {1}{L} \\ \frac {1}{C} & 0 \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{l} \frac {1}{L} \\ 0 \end{array} \right], \boldsymbol {c} = [ 0 1 ]
$$

2）设状态变量 $x_{1} = i, x_{2} = \int i\mathrm{d}t$ ，则有

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - \frac {R}{L} & - \frac {1}{L C} \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \frac {1}{L} \\ 0 \end{array} \right] e, \quad y = \left[ \begin{array}{c c} 0 & \frac {1}{C} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

3）设状态变量 $x_{1} = \frac{1}{C}\int i\mathrm{d}t + Ri,x_{2} = \frac{1}{C}\int i\mathrm{d}t$ ，则

$$x _ {1} = x _ {2} + R i, \quad L \frac {\mathrm{d} i}{\mathrm{d} t} = - x _ {1} + e$$

故
