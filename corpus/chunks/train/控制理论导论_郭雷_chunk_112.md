# 1. 由状态反馈加全状态观测器构成的动态补偿器

假设系统 (1.6.1) 是完全能控和完全能观测的，即 $(A, B)$ 能控， $(A, C)$ 能观测，那么依极点配置定理 1.6.1，存在状态反馈控制规律

$$u (t) = K x (t) \tag {1.8.10}$$

使得矩阵 $A + BK$ 是稳定的，其中 K 是 $r \times n$ 常值控制增益矩阵.

但是，由于状态反馈控制规律（1.8.10）在物理上不能实现，因此需要重构状态 $x(t)$ 。由于 $(A, C)$ 能观测，那么存在 $n \times m$ 常值观测器增益矩阵 $G$ ，使得 $A - GC$ 是稳定的。由观测器的结构性质可以看出，系统（1.6.1）的状态观测器为

$$\dot {x} _ {e} (t) = (\boldsymbol {A} - \boldsymbol {G C}) x _ {e} (t) + \boldsymbol {B u} (t) + \boldsymbol {G y} (t).$$

于是，取系统(1.6.1)的动态补偿器为

$$
\left\{ \begin{array}{l} \dot {x} _ {e} (t) = (\boldsymbol {A} - \boldsymbol {G C}) x _ {e} (t) + \boldsymbol {B u} (t) + \boldsymbol {G y} (t), \\ u (t) = \boldsymbol {K x} _ {e} (t). \end{array} \right.
$$

这是一个物理上能实现的动态输出反馈控制规律。若将 $u(t) = Kx_{e}(t)$ 代到观测器方程中，得出所要求的动态补偿器为

$$
\left\{ \begin{array}{l} \dot {x} _ {e} (t) = (\boldsymbol {A} - \boldsymbol {G C} + \boldsymbol {B K}) x _ {e} (t) + \boldsymbol {G y} (t), \\ u (t) = \boldsymbol {K} x _ {e} (t). \end{array} \right. \tag {1.8.11}
$$

现说明动态补偿器 (1.8.11) 的确是系统 (1.6.1) 的一个无静差补偿器.

事实上，如果将动态补偿器用于系统(1.6.1)，那么可以得到闭环系统

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} (t) \\ \dot {x} _ {e} (t) \end{array} \right] = \left[ \begin{array}{c c} A & B K \\ G C & A - G C + B K \end{array} \right] \left[ \begin{array}{c} x (t) \\ x _ {e} (t) \end{array} \right],} \\ y (t) = [ C 0 ] \left[ \begin{array}{c} x (t) \\ x _ {e} (t) \end{array} \right]. \end{array} \right. \tag {1.8.12}
$$

令

$$e (t) = x _ {e} (t) - x (t),$$

可得

$$
\left[ \begin{array}{l} x (t) \\ e (t) \end{array} \right] = \left[ \begin{array}{c c} I _ {n} & 0 \\ - I _ {n} & I _ {n} \end{array} \right] \left[ \begin{array}{l} x (t) \\ x _ {e} (t) \end{array} \right].
$$

在这个坐标变换下，系统(1.8.12)变成代数等价系统

$$
\left\{ \begin{array}{l} {\left[ \begin{array}{c} \dot {x} (t) \\ \dot {e} (t) \end{array} \right] = \left[ \begin{array}{c c} A + B K & B K \\ 0 & A - G C \end{array} \right] \left[ \begin{array}{c} x (t) \\ e (t) \end{array} \right],} \\ y (t) = [ C \quad 0 ] \left[ \begin{array}{c} x (t) \\ e (t) \end{array} \right]. \end{array} \right.
$$

由于矩阵 $\mathbf{A} + \mathbf{B}\mathbf{K}$ 和 $\mathbf{A} - \mathbf{G}\mathbf{C}$ 都是稳定的，因此矩阵

$$
\left[ \begin{array}{c c} \boldsymbol {A} + \boldsymbol {B K} & \boldsymbol {B K} \\ 0 & \boldsymbol {A} - \boldsymbol {G C} \end{array} \right]
$$

也是稳定的，从而必有

$$\lim _ {t \rightarrow \infty} x (t) = \lim _ {t \rightarrow \infty} e (t) = 0.$$

于是有 $\lim_{t\to \infty}y(t) = 0$ 。这说明动态补偿器(1.8.11)是系统(1.6.1)的一个无静差补偿器。其实，这个动态补偿器不仅使调节输出是无静差的，而且使状态变量也是无静差的，它是一个性能相当强的动态补偿器。
