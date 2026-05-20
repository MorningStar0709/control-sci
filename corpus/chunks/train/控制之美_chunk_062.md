我们之前已经计算过了矩阵 $\mathbf{A}$ 的特征值(参考式(3.2.9))及特征向量(参考式(3.2.11)和式(3.2.13)),代入式(3.2.25)可得

$$
\left\{ \begin{array}{l} \overline {{z}} _ {1} (t) = C _ {1} \mathrm{e} ^ {2 t} \\ \overline {{z}} _ {2} (t) = C _ {2} \mathrm{e} ^ {- 3 t} \end{array} \right. \tag {3.2.26}
$$

此时,根据式(3.2.20),可以得到系统的原状态变量 $z(t)$ 的表达式,即

$$
\boldsymbol {z} (t) = \boldsymbol {P} \overline {{\boldsymbol {z}}} (t) = \left[ \begin{array}{l l} v _ {1 1} & v _ {2 1} \\ v _ {1 2} & v _ {2 2} \end{array} \right] \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {2 t} \\ C _ {2} \mathrm{e} ^ {- 3 t} \end{array} \right] = \left[ \begin{array}{l l} 1 & 0. 5 \\ 1 & - 2 \end{array} \right] \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {2 t} \\ C _ {2} \mathrm{e} ^ {- 3 t} \end{array} \right] = \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {2 t} + 0. 5 C _ {2} \mathrm{e} ^ {- 3 t} \\ C _ {1} \mathrm{e} ^ {2 t} - 2 C _ {2} \mathrm{e} ^ {- 3 t} \end{array} \right] \tag {3.2.27}
$$

请读者观察式(3.2.27)，会发现状态矩阵A的特征值 $\lambda_{1}=2$ 和 $\lambda_{2}=-3$ 出现在指数的部分。它们将决定 $z(t)$ 随时间的变化趋势。例如， $z_{1}(t)=C_{1}e^{2t}+0.5C_{2}e^{-3t}$ 的第一项 $C_{1}e^{2t}$ 会随着时间的增加趋于无穷大，而第二项 $0.5C_{2}e^{-3t}$ 则会随着时间的增加趋于零。因此，这两项相加的结果也会随着时间的增加趋于无穷大。 $z_{2}(t)$ 也有同样的表现。综上所述，随着时间的增加，系统的状态变量 $z(t)$ 会趋于无穷。以上解耦的方法也可以推广到更高阶的矩阵当中，这部分推导留给读者自行分析。

讨论过数学基础之后,我们将正式进入相平面与相轨迹的分析中。
