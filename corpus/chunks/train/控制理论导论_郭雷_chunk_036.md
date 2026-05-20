$$
\left\{ \begin{array}{l} X (s) = (s I _ {n} - A) ^ {- 1} x _ {0} + (s I _ {n} - A) ^ {- 1} B U (s), \\ Y (s) = C (s I _ {n} - A) ^ {- 1} x _ {0} + C (s I _ {n} - A) ^ {- 1} B U (s) + D U (s), \end{array} \right.
$$

式中 $X(s), U(s)$ 和 $Y(s)$ 分别为 $x(t), u(t)$ 和 $y(t)$ 的 Laplace 变换式， $x_0$ 为状态方程 (1.2.6) 的初始状态。当 $x_0 = 0$ 时，有

$$Y (s) = \left[ C (s I _ {n} - A) ^ {- 1} B + D \right] U (s).$$

当

$$\boldsymbol {W} (s) = \boldsymbol {C} (s \boldsymbol {I} _ {n} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} + \boldsymbol {D}$$

为真有理分式矩阵时， $W(s)$ 叫做系统(1.2.6)的传递函数矩阵．而 $(sI_{n} - A)^{-1}$ 称为系统矩阵 $\pmb{A}$ 的预解矩阵.

根据 $(sI_{n} - A)^{-1}$ 的定义和1.1节中的矩阵函数理论，可知

$$(s I _ {n} - A) ^ {- 1} = \sum_ {k = 0} ^ {\infty} \frac {1}{s ^ {k + 1}} A ^ {k}.$$

对上式两边作 Laplace 反变换可得

$$\mathcal {L} ^ {- 1} \left(\left(s I _ {n} - A\right) ^ {- 1}\right) = \sum_ {k = 0} ^ {\infty} \frac {t ^ {k}}{k !} A ^ {k}.$$

再由 $\mathbf{e}^{\pmb{A}t}$ 的定义可知

$$\mathcal {L} ^ {- 1} \left((s I _ {n} - A) ^ {- 1}\right) = \mathrm{e} ^ {\boldsymbol {A t}}.$$

这里 $\mathcal{L}^{-1}$ 表示 Laplace 反变换.

设系统矩阵 $\pmb{A}$ 的特征多项式为

$$\Delta (s) = \det (s I _ {n} - A) = s ^ {n} + \alpha_ {n - 1} s ^ {n - 1} + \dots + \alpha_ {1} s + \alpha_ {0}. \tag {1.2.7}$$

并记

$$
\left\{ \begin{array}{l} p _ {n - 1} (s) = 1, \\ p _ {n - 2} (s) = s + \alpha_ {n - 1}, \\ p _ {n - 3} (s) = s ^ {2} + \alpha_ {n - 1} s + \alpha_ {n - 2}, \\ \vdots \\ p _ {0} (s) = s ^ {n - 1} + \alpha_ {n - 1} s ^ {n - 2} + \dots + \alpha_ {2} s + \alpha_ {1}, \end{array} \right. \tag {1.2.8}
$$

可以验证

$$(s \boldsymbol {I} - A) ^ {- 1} = \frac {1}{\Delta (s)} \left[ p _ {0} (s) \boldsymbol {I} _ {n} + p _ {1} (s) \boldsymbol {A} + \dots + p _ {n - 1} (s) \boldsymbol {A} ^ {n - 1} \right]. \tag {1.2.9}$$

由式 (1.2.8), 式 (1.2.9) 及 Laplace 反变换可得:

命题 1.2.1 对任给的 n 阶方阵 A, 存在 n 个实值连续可微标量函数 $\beta_{k}(t)$ $(k=0,1,\cdots,n-1)$ 使得

$$\mathrm{e} ^ {\boldsymbol {A} t} = \sum_ {k = 0} ^ {n - 1} \beta_ {k} (t) \boldsymbol {A} ^ {k}.$$

与系统的传递函数描述一样，对系统 (1.2.6) 的状态空间方法描述也有特征多项式等概念.

定义1.2.1 对线性系统(1.2.6), $\operatorname{det}(sI_n - A)$ 称为系统的特征多项式；代数方程

$$\det (s I _ {n} - A) = 0$$

称为系统的特征方程；特征方程的根叫做系统的极点； $W(s)$ 各元素的最小公分母的零点叫做传递函数矩阵的极点.

对于多输入、多输出定常系统 (1.2.6)，系统的零点是一个复杂的概念。这里不准备详细去讨论它。下面只就一些常用的零点的概念简单地叙述一下它们的定义。

定义1.2.2 已知定常线性系统(1.2.6). 定义满足

$$\operatorname{rank} \left[ s I _ {n} - A, B \right] < n$$

的 $s$ 为系统的输入解耦零点；满足

$$
\operatorname{rank} \left[ \begin{array}{c} s I _ {n} - A \\ C \end{array} \right] <   n
$$

的 $s$ 为系统的输出解耦零点；满足

$$
\operatorname{rank} \left[ \begin{array}{c c} s I _ {n} - A & - B \\ C & D \end{array} \right] <   \min (r, m) + n
$$

的 s 为系统的传输零点.
