# 16.1.1 系统描述

为了使倒立摆线性化，必须满足倒立摆的各级摆杆的转角是小角度，此时 $\sin\theta\approx\theta$ ， $\cos\theta\approx1$ 。线性化后的单级倒立摆方程为

$$\ddot {\theta} = \frac {m (m + M) g l}{(M + m) I + M m l ^ {2}} \theta - \frac {m l}{(M + m) I + M m l ^ {2}} u \tag {16.1}\ddot {x} = - \frac {m ^ {2} g l ^ {2}}{(M + m) I + M m l ^ {2}} \theta + \frac {I + m l ^ {2}}{(M + m) I + M m l ^ {2}} u \tag {16.2}$$

式中， $I=\frac{1}{12}mL^{2}$ ; $l=\frac{1}{2}L$ 。

控制的目标是通过给小车底座施加一个力 u （控制量），使小车停留在预定的位置，并使杆不倒下，即不超过一预先定义好的垂直偏离角度范围。

如将倒立摆方程转化为状态方程的形式，令 $x(1)=\theta$ ， $x(2)=x$ ， $x(3)=\dot{\theta}$ ， $x(4)=\dot{x}$ ，考虑控制输入干扰 w，则式（16.1）和式（16.2）可表示为状态方程

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} _ {1} w + \boldsymbol {B} _ {2} u \tag {16.3}$$

式中， $A = \begin{pmatrix} 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\ t_1 & 0 & 0 & 0\\ t_2 & 0 & 0 & 0 \end{pmatrix}$ ； $B_{1} = \begin{pmatrix} 0\\ 0\\ 1\\ 1 \end{pmatrix}$ ； $B_{2} = \begin{pmatrix} 0\\ 0\\ t_3\\ t_4 \end{pmatrix}$ ； $t_1 = \frac{m(m + M)gl}{(M + m)I + Mml^2}$ ； $t_2 =$

$$- \frac {m ^ {2} g l ^ {2}}{(M + m) I + M m l ^ {2}}; t _ {3} = - \frac {m l}{(M + m) I + M m l ^ {2}}; t _ {4} = \frac {I + m l ^ {2}}{(M + m) I + M m l ^ {2}}.$$

![](image/3ac71bc0016cc3f299fa4d44a85bfe68556f31a38a8ba4d7867b1361dfdb9e8e.jpg)
