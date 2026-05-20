$$
\begin{array}{l} \dot {x} _ {2 e} (t) = \left(A _ {2 2} - G _ {2} A _ {1 2}\right) x _ {2 e} (t) + \left(A _ {2 1} - G _ {2} A _ {1 1}\right) y (t) \\ + \left(\boldsymbol {B} _ {2} - \boldsymbol {G} _ {2} \boldsymbol {B} _ {1}\right) u (t) + \boldsymbol {G} _ {2} \dot {y} (t). \tag {1.7.18} \\ \end{array}
$$

然而，由于在观测器方程(1.7.18)中，输入数据包含着量测数据的导数 $\dot{y}(t)$ ，因此，在物理上不可实现。为此，令

$$z _ {c} (t) = x _ {2 e} (t) - G _ {2} y (t),$$

于是有

$$
\begin{array}{l} \dot {z} _ {c} (t) = \left(A _ {2 2} - G _ {2} A _ {1 2}\right) z _ {c} (t) + \left(B _ {2} - G _ {2} B _ {1}\right) u (t) \\ + \left[ \left(\boldsymbol {A} _ {2 1} - \boldsymbol {G} _ {2} \boldsymbol {A} _ {1 1}\right) + \left(\boldsymbol {A} _ {2 2} - \boldsymbol {G} _ {2} \boldsymbol {A} _ {1 2}\right) \boldsymbol {G} _ {2} \right] y (t). \\ \end{array}
$$

这时

$$x _ {2 e} (t) = z _ {c} (t) + G _ {2} y (t).$$

综合所述，有如下定理：

定理 1.7.3 已知定常线性系统 (1.6.1). 假设它是完全能观测的, 并且 $C = [I_m 0]$ , 那么存在一个极小阶观测器

$$
x _ {2 e} (t) = z _ {c} (t) + \mathbf {G} _ {2} y (t), \tag {1.7.19}
\begin{array}{l} \dot {z} _ {c} (t) = \left(A _ {2 2} - G _ {2} A _ {1 2}\right) z _ {c} (t) + \left(B _ {2} - G _ {2} B _ {1}\right) u (t) \\ + \left[ \left(A _ {2 1} - G _ {2} A _ {1 1}\right) + \left(A _ {2 2} - G _ {2} A _ {1 2}\right) G _ {2} \right] y (t), \tag {1.7.20} \\ \end{array}
$$

其中 $G_{2}$ 为极小阶观测器的增益常数矩阵，它使得 $A_{22} - G_2A_{12}$ 是稳定的.

例1.7.3 找出例1.7.2中定常线性系统的一个极小阶观测器.

解 首先写出系统的状态空间表达式，为此令

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c c} 0 & \mu & 0 \\ - \mu & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], \quad \boldsymbol {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \end{array} \right], \\ x (t) = \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \\ x _ {3} (t) \end{array} \right], \quad u (t) = \left[ \begin{array}{l} u _ {1} (t) \\ u _ {2} (t) \\ u _ {3} (t) \end{array} \right], \quad y (t) = \left[ \begin{array}{l} y _ {1} (t) \\ y _ {2} (t) \end{array} \right]. \\ \end{array}
$$

于是有

$$
\left\{ \begin{array}{l} \dot {x} (t) = A x (t) + u (t), \\ y (t) = C x (t), \end{array} \right.
$$

这里 $\pmb{C} = [\pmb{C}_1\pmb{C}_2]$ ，而且

$$
\boldsymbol {C} _ {1} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right], \quad \boldsymbol {C} _ {2} = \left[ \begin{array}{l} 0 \\ - 1 \end{array} \right].
$$

取

$$
\boldsymbol {P} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & - 1 \\ 0 & 0 & 1 \end{array} \right],
$$

那么

$$
\boldsymbol {P} ^ {- 1} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{array} \right].
$$

做坐标变换 $\overline{x} = Px$ ，得代数等价系统
