式中， $x \in R^{n}$ 为状态向量；u 为标量输入；y 为标量输出；A, b, c 维数适当。设参考输入 $r(t) = \sin(t)$ ，定义跟踪误差 $e(t) = r(t) - y(t)$ 。试论证系统能以零稳态误差跟踪正弦参考输入信号。

9-45 设带有扰动 $n(t)$ 的单输入-单输出系统的状态空间表达式为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {b} \boldsymbol {u} (t)y (t) = \mathbf {c x} (t) + n (t)$$

式中， $x \in R^{n}$ 为状态向量；u 为标量输入；y 为标量输出；A, b, c 维数适当。设参考输入 $r(t) = t$ ，扰动信号 $n(t) = 1(t)$ ，为阶跃扰动。试论证可设计扰动内模控制器，使系统输出能以零稳态误差渐近跟踪斜坡输入 t，且不受阶跃扰动 $n(t)$ 的影响。

9-46 设有系统

$$
\dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 2 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{l} 1 \\ 2 \end{array} \right] u (t)
y (t) = [ 1 \quad 0 ] x (t) + n (t)
$$

式中， $n(t)=3t^{2}$ 为输出端扰动信号。要求系统输出能以零稳态误差跟踪斜坡参考输入信号，并克服输出端加速度扰动对跟踪性能的影响。
