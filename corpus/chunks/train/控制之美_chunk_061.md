$$
\boldsymbol {A} \boldsymbol {P} = \left[ \lambda_ {1} \left[ \begin{array}{l} v _ {1 1} \\ v _ {1 2} \end{array} \right] \lambda_ {2} \left[ \begin{array}{l} v _ {2 1} \\ v _ {2 2} \end{array} \right] \right] = \left[ \begin{array}{l l} \lambda_ {1} v _ {1 1} & \lambda_ {2} v _ {2 1} \\ \lambda_ {1} v _ {1 2} & \lambda_ {2} v _ {2 2} \end{array} \right] = \left[ \begin{array}{l l} v _ {1 1} & v _ {2 1} \\ v _ {1 2} & v _ {2 2} \end{array} \right] \left[ \begin{array}{c c} \lambda_ {1} & 0 \\ 0 & \lambda_ {2} \end{array} \right] = \boldsymbol {P D} \tag {3.2.18}
$$

其中， $D=\begin{bmatrix}\lambda_{1}&0\\0&\lambda_{2}\end{bmatrix}$ 是一个特征值位于对角线上的对角矩阵。现在对式(3.2.18)等号两边同时左乘以 $P^{-1}$ ，可得

$$\boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \boldsymbol {P} ^ {- 1} \boldsymbol {P} \boldsymbol {D}\Rightarrow \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} = \boldsymbol {D} \tag {3.2.19}$$

式(3.2.19)通过过渡矩阵 P 将原矩阵 A 对角化。

下面定义一组新的状态变量 $\overline{z}(t)$ ，令

$$\mathbf {z} (t) = \mathbf {P} \overline {{{\mathbf {z}}}} (t) \tag {3.2.20}$$

将式(3.2.20)代入式(3.2.15)，可得

$$\boldsymbol {P} \frac {\mathrm{d} \overline {{\boldsymbol {z}}} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {P} \overline {{\boldsymbol {z}}} (t) \tag {3.2.21}$$

式(3.2.21)等号两边同时左乘以 $P^{-1}$ ，得到

$$\boldsymbol {P} ^ {- 1} \boldsymbol {P} \frac {\mathrm{d} \overline {{\boldsymbol {z}}} (t)}{\mathrm{d} t} = \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} \overline {{\boldsymbol {z}}} (t) \tag {3.2.22}$$

其中， $P^{-1}P = I$ 是单位矩阵。根据式(3.2.19)， $P^{-1}AP = D$ 。可得

$$
\frac {\mathrm{d} \overline {{z}} (t)}{\mathrm{d} t} = D \overline {{z}} (t) = \left[ \begin{array}{c c} \lambda_ {1} & 0 \\ 0 & \lambda_ {2} \end{array} \right] \overline {{z}} (t) \tag {3.2.23}
$$

即

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} \overline {{z}} _ {1} (t)}{\mathrm{d} t} = \lambda_ {1} \overline {{z}} _ {1} (t) \\ \frac {\mathrm{d} \overline {{z}} _ {2} (t)}{\mathrm{d} t} = \lambda_ {2} \overline {{z}} _ {2} (t) \end{array} \right. \tag {3.2.24}
$$

式(3.2.24)说明新的状态变量 $\bar{z}_{1}(t)$ 和 $\bar{z}_{2}(t)$ 的变化率只和自身相关, 因此通过这样的一个变换之后, 原来系统中的耦合关系就不再存在。而求解式(3.2.24)则非常容易, 根据微分方程的求解公式可得

$$
\left\{ \begin{array}{l} \overline {{z}} _ {1} (t) = C _ {1} \mathrm{e} ^ {\lambda_ {1} t} \\ \overline {{z}} _ {2} (t) = C _ {2} \mathrm{e} ^ {\lambda_ {2} t} \end{array} \right. \tag {3.2.25}
$$

其中， $C_1$ 和 $C_2$ 是常数，与初始条件有关。
