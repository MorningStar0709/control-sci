# 10.3.1 极点配置

回到本章开始的指尖平衡的例子,本节将设计控制器稳定其位置,并以此为例讲解控制

![](image/600321047c1dc2057b00659d523077402d7ca8679f04b2d02a611e14805891da.jpg)

器的设计流程,此例子的状态空间方程在10.1.3节中已经得到,即

$$
\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t), \quad \text {其中,} \boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right], \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {10.3.1a}
$$

$$
\mathbf {y} (t) = \mathbf {C} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \mathbf {D u} (t), \quad \text {其中,} \mathbf {C} = [ 1 0 ], \mathbf {D} = [ 0 ] \tag {10.3.1b}
$$

首先分析无输入的系统, 即 $\boldsymbol{u}(t)=0$ 的情况。此时 $\frac{\mathrm{d}\boldsymbol{z}(t)}{\mathrm{d}t}=\boldsymbol{A}\boldsymbol{z}(t)$ , 求它的平衡点, 令 $\frac{\mathrm{d}\boldsymbol{z}(t)}{\mathrm{d}t}=0$ , 可得

$$
\left\{ \begin{array}{l} 0 = z _ {2 \mathrm{f}} \\ 0 = \frac {g}{d} z _ {1 \mathrm{f}} \end{array} \Rightarrow \left\{ \begin{array}{l} z _ {1 \mathrm{f}} = 0 \\ z _ {2 \mathrm{f}} = 0 \end{array} \right. \right. \tag {10.3.2}
$$

根据 3.3 节所介绍的相平面和相轨迹的分析方法, 可以根据状态矩阵 A 的特征值判断平衡点的类型。求矩阵 A 的特征值, 令 $\left|A - \lambda I\right| = 0$ , 得到

$$
\left| \begin{array}{c c} - \lambda & 1 \\ \frac {g}{d} & - \lambda \end{array} \right| = 0 \tag {10.3.3}
$$

即

$$
\lambda^ {2} - \frac {g}{d} = 0 \tag {10.3.4}
$$

计算出矩阵 A 的两个特征值为

$$
\left\{ \begin{array}{l} \lambda_ {1} = - \sqrt {\frac {g}{d}} <   0 \\ \lambda_ {2} = \sqrt {\frac {g}{d}} > 0 \end{array} \right. \tag {10.3.5}
$$

式(10.3.5)说明状态矩阵的特征值一正一负,根据表3.3.1可以判断系统的平衡点 $z_{f}(t)=[0,0]^{T}$ 是一个鞍点, $\frac{g}{d}$ 的值仅仅会改变相轨迹的形状,但不会影响平衡点的性质。它的相轨迹如图10.3.1所示(图中选取 $\frac{g}{d}=10$ )。这意味着系统的状态变量一旦偏离平衡点,在没有外力输入的情况下,将无法回到平衡点,所以这是一个不稳定的系统。这个结果并不意外,本例中的倒立摆在没有外力介入的情况下,当连杆小球偏离直立位置后,当然无法回来。若要改变平衡点的性质,则需要设计合适的输入 $u(t)$ ,在设计之前,首先要判断系统的能控性,根据式(10.2.3), $C_{o}=[B\quad AB]=\begin{bmatrix}0&1\\ 1&0\end{bmatrix}$ , $\mathrm{Rank}(C_{o})=2$ ,所以系统能控。

思考：仅仅通过位置输出的比例反馈 $u(t) = -ky(t)$ 是否可以稳定系统？

将 $u(t)=-ky(t)$ 代入式(10.3.1a)，可得
