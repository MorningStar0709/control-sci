矩阵在虚轴上有一个特征值,因此不能用线性化确定原点的稳定性。这是因为原点可能是渐近稳定的、稳定的或非稳定的,这取决于参数 a 的取值。如果 a<0,原点是渐近稳定的,因为由李雅普诺夫函数 $V(x)=x^{4}$ , 当 $x\neq0$ 时其导数 $\dot{V}(x)=4ax^{6}<0$ 。如果 a=0,则系统是线性的,且根据定理 4.5 可得原点是稳定的。根据定理 4.3 以及函数 $V(x)=x^{4}$ 在 $x\neq0$ 时其导数 $\dot{V}(x)=4ax^{6}>0$ , 如果 a>0,则原点是非稳定的。

例4.15 单摆方程

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - a \sin x _ {1} - b x _ {2}$$

有两个平衡点 $(x_{1}=0,x_{2}=0)$ 和 $(x_{1}=\pi,x_{2}=0)$ 。我们用线性化研究这两个点的稳定性。
雅可比矩阵为

$$
\frac {\partial f}{\partial x} = \left[ \begin{array}{c c} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {1}}{\partial x _ {2}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {2}} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - a \cos x _ {1} & - b \end{array} \right]
$$

为了确定原点的稳定性,计算x=0时的雅可比矩阵,有

$$
A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0} = \left[ \begin{array}{c c} 0 & 1 \\ - a & - b \end{array} \right]
$$

则 $A$ 的特征值为

$$\lambda_ {1, 2} = - \frac {1}{2} b \pm \frac {1}{2} \sqrt {b ^ {2} - 4 a}$$

当所有 $a, b > 0$ 时，特征值满足 $\operatorname{Re} \lambda_i < 0$ 。因此，原点处的平衡点是渐近稳定的。在不计摩擦力的情况下 $(b = 0)$ ，两个特征值都在虚轴上，因此不能确定线性化后原点的稳定性。在例4.3中看到，这种情况下原点是否为稳定平衡点，是由能量李雅普诺夫函数决定的。为了确定平衡点 $(x_1 = \pi, x_2 = 0)$ 的稳定性，先计算该点的雅可比矩阵。这等价于进行变量代换 $z_1 = x_1 - \pi, z_2 = x_2$ ，把平衡点平移到原点，并计算 $z = 0$ 时的雅可比矩阵 $[\partial f / \partial z]$ ，

$$
\tilde {A} = \left. \frac {\partial f}{\partial x} \right| _ {x _ {1} = \pi , x _ {2} = 0} = \left[ \begin{array}{c c} 0 & 1 \\ a & - b \end{array} \right]
$$

$\tilde{A}$ 的特征值为

$$\lambda_ {1, 2} = - \frac {1}{2} b \pm \frac {1}{2} \sqrt {b ^ {2} + 4 a}$$

当所有 a > 0 且 $b \geqslant 0$ 时，在右半开平面内有一个特征值。因而，平衡点 $(x_{1} = \pi, x_{2} = 0)$ 是非稳定的。
