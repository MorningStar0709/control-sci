下面三个例子将说明定理13.2的应用和偏微分方程(13.34)的解。各例均假设当 $u = 0$ 时，系统(13.27)有一个平衡点 $x^{*}$ 。选择 $h(x)$ ，使 $h(x^{*}) = 0$ ，因而变量代换 $z = T(x)$ 将平衡点 $x = x^{*}$ 映射到原点 $z = 0$ 。

例13.13 重新考虑13.1节中的系统

$$
\dot {x} = \left[ \begin{array}{c} a \sin x _ {2} \\ - x _ {1} ^ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \stackrel {\text { def }} {=} f (x) + g u
$$

有 $ad_{f}g=[f,g]=-\frac{\partial f}{\partial x}g=\left[\begin{array}{c}-a\cos x_{2}\\0\end{array}\right]$

对于所有 $x$ ，矩阵 $\mathcal{G} = [g, ad_{f}g] = \left[ \begin{array}{cc}0 & -a\cos x_{2}\\ 1 & 0 \end{array} \right]$

的秩为2,故 $\cos x_{2} \neq 0$ 。分布 $\mathcal{D} = \operatorname{span}\{g\}$ 是对合的。因此，定理13.2的条件在定义域 $D_0 = \{x \in R^2 | \cos x_2 \neq 0\}$ 上成立。为了找到使系统转换为方程(13.6)的变量代换，需要求 $h(x)$ ，使之满足

$$\frac {\partial h}{\partial x} g = 0; \quad \frac {\partial (L _ {f} h)}{\partial x} g \neq 0, \quad h (0) = 0$$

根据条件 $[\partial h / \partial x]g = 0$ ，有 $\frac{\partial h}{\partial x} g = \frac{\partial h}{\partial x_2} = 0$

这样 $h$ 一定与 $x_{2}$ 无关，因此 $L_{f}h(x) = \frac{\partial h}{\partial x_{1}} a\sin x_{2}$

选择任意满足 $(\partial h/\partial x_{1})\neq0$ 的h,条件

$$\frac {\partial (L _ {f} h)}{\partial x} g = \frac {\partial (L _ {f} h)}{\partial x _ {2}} = \frac {\partial h}{\partial x _ {1}} a \cos x _ {2} \neq 0$$

在定义域 $D_{0}$ 上都成立。取 $h(x) = x_{1}$ 即可得到前面用到的变换。也可以选择其他 $h$ ，例如取 $h(x) = x_{1} + x_{1}^{3}$ ，则给出另一个变量代换，也能使系统转换为方程(13.6)的形式。 $\triangle$ 例13.14 一个带有柔性接头的单连杆操纵器，阻尼忽略不计，可用形如

$$\dot {x} = f (x) + g u$$

的四阶模型表示(见习题1.5),其中

$$
f (x) = \left[ \begin{array}{c} {x _ {2}} \\ {- a \sin x _ {1} - b (x _ {1} - x _ {3})} \\ {x _ {4}} \\ {c (x _ {1} - x _ {3})} \end{array} \right], g = \left[ \begin{array}{l} {0} \\ {0} \\ {0} \\ {d} \end{array} \right]
$$

a,b,c 和 d 是正常数。该无激励系统平衡点为 x=0，故有

$$
a d _ {f} g = [ f, g ] = - \frac {\partial f}{\partial x} g = \left[ \begin{array}{c} 0 \\ 0 \\ - d \\ 0 \end{array} \right]

a d _ {f} ^ {2} g = [ f, a d _ {f} g ] = - \frac {\partial f}{\partial x} a d _ {f} g = \left[ \begin{array}{c} 0 \\ b d \\ 0 \\ - c d \end{array} \right]

a d _ {f} ^ {3} g = [ f, a d _ {f} ^ {2} g ] = - \frac {\partial f}{\partial x} a d _ {f} ^ {2} g = \left[ \begin{array}{c} - b d \\ 0 \\ c d \\ 0 \end{array} \right]
$$

对于所有 $x \in R^4$ ，矩阵

$$
\mathcal {G} = [ g, a d _ {f} g, a d _ {f} ^ {2} g, a d _ {f} ^ {3} g ] = \left[ \begin{array}{c c c c} 0 & 0 & 0 & - b d \\ 0 & 0 & b d & 0 \\ 0 & - d & 0 & c d \\ \dot {d} & 0 & - c d & 0 \end{array} \right]
$$
