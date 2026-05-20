$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - l _ {1} e _ {1} \\ \dot {z} _ {2} = \left(a _ {1} z _ {1} + a _ {2} z _ {2}\right) - l _ {2} e _ {1} + b u \end{array} \right. \tag {4.1.7}
$$

其中，参数 $l_{1}, l_{2}$ 就是在式(4.1.4)中要选取的 $\pmb{L} = \begin{bmatrix} l_{1} \\ l_{2} \end{bmatrix}$ . 这个系统与原系统的误差方程为

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - x _ {1}, e _ {2} = z _ {2} - x _ {2} \\ \dot {e} _ {1} = - l _ {1} e _ {1} + e _ {2} \\ \dot {e} _ {2} = (- l _ {2} + a _ {1}) e _ {1} + a _ {2} e _ {2} + b u \end{array} \right.
$$

因此只要选取参数 $l_{1}, l_{2}$ , 使得矩阵

$$
\left[ \begin{array}{c c} - l _ {1} & 1 \\ - l _ {2} + a _ {1} & a _ {2} \end{array} \right]
$$

稳定,那么系统(4.1.7)将成为系统(4.1.6)的状态观测器.

对非线性系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}) + b u \\ y = x _ {1} \end{array} \right. \tag {4.1.8}
$$

当函数 $f(x_{1},x_{2})$ 和 $b$ 已知时，也可以建立如下状态观测器

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - l _ {1} e _ {1} \\ \dot {z} _ {2} = f (z _ {1}, z _ {2}) - l _ {2} e _ {1} + b u \end{array} \right. \tag {4.1.9}
$$

这时，系统(4.1.8)和系统(4.1.9)的误差方程为

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - x _ {1}, e _ {2} = z _ {2} - x _ {2} \\ \dot {e} _ {1} = e _ {2} - l _ {1} e _ {1} \\ \dot {e} _ {2} = f (x _ {1} + e _ {1}, x _ {2} + e _ {2}) - f (x _ {1}, x _ {2}) - l _ {2} e _ {1} \end{array} \right.
$$

假定函数 $f(x_{1},x_{2})$ 连续可微，那么按泰勒展开线性近似成

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1} - x _ {1}, e _ {2} = z _ {2} - x _ {2} \\ \dot {e} _ {1} = e _ {2} - l _ {1} e _ {1} \\ \dot {e} _ {2} = \frac {\partial f (x _ {1} , x _ {2})}{\partial x _ {1}} e _ {1} + \frac {\partial f (x _ {1} , x _ {2})}{\partial x _ {2}} e _ {2} - l _ {2} e _ {1} \end{array} \right. \tag {4.1.10}
$$

这里，只要 $\frac{\partial f(x_1,x_2)}{\partial x_1},\frac{\partial f(x_1,x_2)}{\partial x_2}$ 有界，总可以选 $l_{1},l_{2}$ ，使误差系统(4.1.10）稳定，于是系统(4.1.9）将成为系统(4.1.8）的状态观测器

下面要讨论的问题是,原系统(4.1.5)和(4.1.7)中的参数 $a_{1},a_{2}$ 或函数 $f(x_{1},x_{2})$ 未知时,我们能否构造出估计状态变量 $x_{1}$ 和 $x_{2}$ 的状态观测器?暂时先假定参数b已知.

已知线性系统

$$
\left\{ \begin{array}{l} \dot {X} = A X + B U \\ Y = C X + D U \end{array} \right. \tag {4.1.11}
$$

(这里 U, X, Y 是列向量) 的对偶系统为

$$
\left\{ \begin{array}{l} \dot {\psi} = - \psi A + \eta C \\ \varphi = \psi B - \eta D \end{array} \right. \tag {4.1.12}
$$

式中： $\psi$ 为对偶系统的状态向量； $\eta$ 为对偶系统的输入向量，即对偶系统的控制向量； $\varphi$ 为对偶系统的输出向量。 $\psi$ 、 $\eta$ 、 $\varphi$ 都是横向量。现在对对偶系统(4.1.12)取状态反馈

$$\boldsymbol {\eta} = \psi L \tag {4.1.13}$$

那么对偶的闭环系统变成

$$\dot {\psi} = - \psi A + \psi L B = - \psi (A - L C) \tag {4.1.14}$$
