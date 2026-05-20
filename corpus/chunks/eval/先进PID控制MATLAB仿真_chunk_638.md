# 17.3.1 系统描述

针对倒立摆模型式（17.7）和式（17.8），取控制指标为4个，即单级倒立摆的摆角 $\theta$ 、摆速 $\dot{\theta}$ 、小车位置x和小车速度 $\dot{x}$ 。

将倒立摆运动方程转化为状态方程的形式。令 $x(1)=\theta$ ， $x(2)=\dot{\theta}$ ， $x(3)=x$ ， $x(4)=\dot{x}$ ，则式（17.7）和式（17.8）可表示为状态方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} \tag {17.9}$$

式中， $A = \begin{pmatrix} 0 & 1 & 0 & 0\\ t_1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\\ t_2 & 0 & 0 & 0 \end{pmatrix};\quad B = \begin{pmatrix} 0\\ t_3\\ 0\\ t_4 \end{pmatrix};\quad t_1 = \frac{m(m + M)gl}{(M + m)I + Mml^2};\quad t_2 = -\frac{m^2gl^2}{(M + m)I + Mml^2};$

$$t _ {3} = - \frac {m l}{(M + m) I + M m l ^ {2}}; t _ {4} = \frac {I + m l ^ {2}}{(M + m) I + M m l ^ {2}}.$$

控制的目标是通过给小车底座施加一个力 u （控制量），使小车停留在零位置，并使摆杆不倒下，即 $\theta \rightarrow 0$ 、 $\dot{\theta} \rightarrow 0$ 、 $x \rightarrow 0$ 和 $\dot{x} \rightarrow 0$ 。

![](image/7c3ff8d9a567cb6edc1f4c07258195d21724a68e71b45955b2a5cc24a8dc0d04.jpg)
