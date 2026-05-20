# 3.3.3 二维相平面与相轨迹——一般形式

掌握了简化形式的二维系统相轨迹后,可以推广到一般形式。首先将式(3.3.5)解耦(对角化),定义一个新的状态变量 $\overline{z}(t)$ , 令 $z(t)=P\overline{z}(t)$ 。P 是过渡矩阵 $P=\left[v_{1},v_{2}\right]$ , 其中 $v_{1}$ 和 $v_{2}$ 是矩阵 A 的特征向量。根据 3.3.2 节中的介绍, 可得

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} \overline {{z}} _ {1} (t) \\ \overline {{z}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} \lambda_ {1} & 0 \\ 0 & \lambda_ {2} \end{array} \right] \overline {{z}} (t) \tag {3.3.9}
$$

其中， $\lambda_{1}$ 和 $\lambda_{2}$ 是矩阵 $\mathbf{A}$ 的特征值。式(3.3.9)是一个对角矩阵，分析它的相轨迹可以使用3.3.2节的结论。下面通过几个例子深入地讨论一般形式矩阵的相轨迹。

例 3.3.2 分析二阶系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t}=Az$ 的相轨迹, 其中 $A=\begin{bmatrix}-3&4\\-2&3\end{bmatrix}$ 。

解：首先求矩阵 A 的特征值，令 $\left|A-\lambda I\right|=0$ ，可得 $\left\{\begin{aligned}\lambda_{1}&=-1\\ \lambda_{2}&=1\end{aligned}\right.$ ，与其相对应的特征向量分别为 $v_{1}=[2,1]^{T},v_{2}=[1,1]^{T}$ 。令 $z(t)=P\bar{z}(t)$ ，其中 $P=\left[v_{1},v_{2}\right]=\left[\begin{matrix}2&1\\ 1&1\end{matrix}\right]$ ，根据式(3.3.9)，得到

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} \overline {{z}} _ {1} (t) \\ \overline {{z}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l l} - 1 & 0 \\ 0 & 1 \end{array} \right] \overline {{z}} (t) \tag {3.3.10}
$$

式(3.3.10)所示矩阵 $\mathbf{A}$ 的特征值都是实数且符号相反, 这种情况和 3.3.2 节中讨论的类(2)是一样的, 如前面所分析的, 平衡点 $\overline{z}_{\mathrm{f}} = [0,0]^{\mathrm{T}}$ 是一个鞍点。它的相轨迹如图 3.3.8(a) 所示, $\overline{z}_{1}(t)$ 随着时间增加而靠近平衡点, $\overline{z}_{2}(t)$ 随着时间增加而远离平衡点。式(3.3.10)中 $\overline{z}(t)$ 的解为

$$
\overline {{{z}}} (t) = \left[ \begin{array}{l} \overline {{{z}}} _ {1} (t) \\ \overline {{{z}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {- t} \\ C _ {2} \mathrm{e} ^ {t} \end{array} \right] \tag {3.3.11}
$$

其中， $C_{1}$ 、 $C_{2}$ 为两个常数，和初始条件 $\bar{z}(t_{0})$ 相关。

此时原始状态变量 $z(t)$ 为
