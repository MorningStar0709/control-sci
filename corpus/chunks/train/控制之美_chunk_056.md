# 3.1.2 状态空间方程与传递函数的关系

如 3.1.1 节所分析的,一个单输入单输出系统可以写成式(3.1.2)的传递函数形式和式(3.1.8a)、式(3.1.8b)的状态空间方程表达式,下面我们来讨论这两种形式之间的联系。

对式(3.1.8a)、式(3.1.8b)的等式两边进行拉普拉斯变换,得到

$$\mathcal {L} \left[ \frac {\mathrm{d} z (t)}{\mathrm{d} t} \right] = \mathcal {L} [ A z (t) + B u (t) ] \tag {3.1.14a}\mathcal {L} [ \mathbf {y} (t) ] = \mathcal {L} [ \mathbf {C z} (t) + \mathbf {D u} (t) ] \tag {3.1.14b}$$

考虑零初始状态， $z_{1}(0)=z_{2}(0)=0$ ，式(3.1.14a)、式(3.1.14b)可以整理为

$$s \mathbf {Z} (s) = \mathbf {A Z} (s) + \mathbf {B U} (s) \tag {3.1.15a}\mathbf {Y} (s) = \mathbf {C Z} (s) + \mathbf {D U} (s) \tag {3.1.15b}$$

其中， $Z(s) = \mathcal{L}[z(t)],Y(s) = \mathcal{L}[y(t)],U(s) = \mathcal{L}[u(t)]$ 。式(3.1.15a)调整后可得

$$\mathbf {Z} (s) = (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B U} (s) \tag {3.1.16}$$

其中， $(sI - A)^{-1}$ 是 $(sI - A)$ 的逆矩阵； $I$ 是 $n \times n$ 单位矩阵， $I_{n \times n} = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 1 \end{bmatrix}$ 。

将式(3.1.16)代入式(3.1.15b)中并调整,可得

$$\mathbf {Y} (s) = (\mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D}) \mathbf {U} (s) \tag {3.1.17}$$

因此，系统的传递函数可以表达为

$$G (s) = \frac {\mathbf {Y} (s)}{\mathbf {U} (s)} = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D} \tag {3.1.18}$$

考虑图 3.1.1 的弹簧质量阻尼系统, 其中 D = 0, 根据矩阵求逆公式 $(sI - A)^{-1} = \frac{(sI - A)^{*}}{|sI - A|}$ , 代入式 (3.1.18) 可得

$$G (s) = \frac {\mathbf {Y} (s)}{\mathbf {U} (s)} = \frac {\mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {*} \mathbf {B}}{| s \mathbf {I} - \mathbf {A} |} \tag {3.1.19}$$

其中， $(sI-A)^{*}$ 是 $(sI-A)$ 的伴随矩阵， $|sI-A|$ 是 $(sI-A)$ 的行列式。

观察式(3.1.19)，如果令 $G(s)$ 的分母部分为零，即 $|sI - A| = 0$ ，得出的 $s$ 值有两个含义：第一，从传递函数的角度考虑，它是传递函数的极点；第二，从状态矩阵的角度考虑，它是矩阵 $\mathbf{A}$ 的特征值（令 $|sI - A| = 0$ 是求矩阵 $\mathbf{A}$ 特征值的公式，见3.2.1节）。在2.3节中曾经介绍过，通过分析传递函数极点可以判断系统的表现。而当把系统写成状态空间方程之后，状态矩阵 $\mathbf{A}$ 的特征值即为其相对应的传递函数 $G(s)$ 的极点。因此，通过分析矩阵 $\mathbf{A}$ 的特征值也可以判断系统的表现。

状态空间方程系统建模内容请扫描此二维码观看。
