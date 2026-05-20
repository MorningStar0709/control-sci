其中 $f_{a}(0)=0,f(0)=0,h(0)=0$ ，函数 $f_{a},F,f$ 和G是局部利普希茨函数，h是连续函数。把整个系统看成驱动系统（14.78）～（14.79）和被驱动系统（14.77）的级联 $^{①}$ 。假设表达式（14.77）～（14.79）全局成立，驱动系统是无源系统，具有径向无界的正定存储函数 $V(x)$ ，此外 $\dot{z}=f_{a}(z)$ 的原点是稳定的，并且已知对于 $\dot{z}=f_{a}(z)$ ，存在一个径向无界的李雅普诺夫函数 $W(z)$ ，满足

$$\frac {\partial W}{\partial z} f _ {a} (z) \leqslant 0, \quad \forall z$$

用 $U(z,x) = W(z) + V(x)$ 作为整个系统(14.77)\~(14.79)的备选存储函数，可得

$$\dot {U} = \frac {\partial W}{\partial z} f _ {a} (z) + \frac {\partial W}{\partial z} F (z, y) y + \frac {\partial V}{\partial x} f (x) + \frac {\partial V}{\partial x} G (x) u\leqslant \frac {\partial W}{\partial z} F (z, y) y + y ^ {T} u = y ^ {T} \left[ u + \left(\frac {\partial W}{\partial z} F (z, y)\right) ^ {T} \right]$$

反馈控制为 $u = -\left(\frac{\partial W}{\partial z} F(z,y)\right)^{\mathrm{T}} + v$

可得 $\dot{U} \leqslant y^{\mathrm{T}}v$

因此,系统 $\dot{z} = f_{a}(z) + F(z,y)y$ (14.80)

$$\dot {x} = f (x) - G (x) \left(\frac {\partial W}{\partial z} F (z, y)\right) ^ {\mathrm{T}} + G (x) v \tag {14.81}y = h (x) \tag {14.82}$$

是无源系统,其输入为 v, 输出为 y, 存储函数为 U。如果系统(14.80)\~(14.82)是零状态可观测的,那么可应用定理 14.4 使原点达到全局稳定。

例 14.17 受三个独立标量控制力矩的刚体旋转运动可采用下面的模型①

$$\dot {\rho} = \frac {1}{2} \left[ I _ {3} + S (\rho) + \rho \rho^ {\mathrm{T}} \right] \omegaM \dot {\omega} = - S (\omega) M \omega + u$$

其中 $\omega\in R^{3}$ 是速度向量, $\rho\in R^{3}$ 是待选的运动参数,由此可得出旋转体的三维表示。矩阵 $S(x)$ 是斜对称矩阵,定义为

$$
S (x) = \left[ \begin{array}{c c c} {0} & {- x _ {3}} & {x _ {2}} \\ {x _ {3}} & {0} & {- x _ {1}} \\ {- x _ {2}} & {x _ {1}} & {0} \end{array} \right]
$$

M 是正定对称惯量矩阵, $I_{3}$ 是 $3 \times 3$ 单位阵。取 $y = \omega$ , 可看出系统取级联系统方程(14.77)至方程(14.79)的形式, 其中驱动系统为

$$M \dot {\omega} = - S (\omega) M \omega + u, \quad y = \omega$$

被驱动系统为

$$\dot {\rho} = \frac {1}{2} [ I _ {3} + S (\rho) + \rho \rho^ {\mathrm{T}} ] \omega$$

取 $V(\omega) = (1 / 2)\omega^{\mathrm{T}}M\omega$ ，可看出

$$\dot {V} = \omega^ {\mathrm{T}} M \dot {\omega} = - \omega^ {\mathrm{T}} S (\omega) M \omega + \omega^ {\mathrm{T}} u = y ^ {\mathrm{T}} u$$

其中用到性质 $\omega^{T}S(\omega)=0$ 。因此，驱动系统是无源的。无激励驱动系统 $\rho=0$ 在 $\rho=0$ 处具有稳定的平衡点，并且任何径向无界的正定连续可微函数 $W(\rho)$ 都可作为李雅普诺夫函数。这样，所有假设都得到满足，且控制律

$$u = - \left\{\frac {\partial W}{\partial \rho} \frac {1}{2} [ I _ {3} + S (\rho) + \rho \rho^ {\mathrm{T}} ] \right\} ^ {\mathrm{T}} + v$$

使系统成为无源系统。取 $W(\rho) = k\ln (1 + \rho^{\mathrm{T}}\rho), k > 0$ ，可得
