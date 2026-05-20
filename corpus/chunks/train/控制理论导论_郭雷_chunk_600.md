$$\mathcal {H} ^ {\perp} = \operatorname{span} \{X \mid \langle \omega , X \rangle = 0, \forall \omega \in \mathcal {H} \}. \tag {8.2.14}$$

引理8.2.3 分布 $\mathcal{H}^{\perp}$ 是对合且对 $F$ 不变.

证明 设 $X, Y \in \mathcal{H}^{\perp}$ , 且 $\omega \in \mathcal{H}$ , 则

$$\langle \omega , \mathrm{ad} _ {X} Y \rangle = L _ {X} (\omega , Y) - \langle L _ {X} \omega , Y \rangle = 0.$$

因此， $[X,Y]\in \mathcal{H}^{\perp}$ ，这表明 $\mathcal{H}^{\perp}$ 是对合的.

设 $X \in F$ 且 $Y \in \mathcal{H}^{\perp}$ , 要证明 $\mathcal{H}^{\perp}$ 是 $F$ 不变的, 我们只要证明 $\operatorname{ad}_X Y \in \mathcal{H}^{\perp}$ . 设 $\omega \in \mathcal{H}$ , 那么 $\langle \omega, Y \rangle = 0$ , 于是有

$$\langle \omega , \mathrm{ad} _ {X} Y \rangle = L _ {X} \langle \omega , Y \rangle - \langle L _ {X} \omega , Y \rangle = 0,$$

从而第二项也是零. 因 $X \in F$ 且 $\omega \in \mathcal{H}$ , 故 $L_{X} \omega \in \mathcal{H}$ .

定理8.2.4 设 $x_0$ 为能观测对偶分布 $\mathcal{H}$ 的一个正则点，则存在 $x_0$ 的一个局部坐标卡 $(V, z)$ ，使系统(8.1.1)可局部地表示为

$$
\left\{ \begin{array}{l} z ^ {1} = f ^ {1} (z, u), \\ z ^ {2} = f ^ {2} (z ^ {2}. u), \quad z \in V, \\ y = h (z ^ {2}), \end{array} \right. \tag {8.2.15}
$$

这里分布 $H^{\perp} = \operatorname{span}\left\{\frac{\partial}{\partial z_{1}^{1}}, \frac{\partial}{\partial z_{2}^{1}}, \cdots, \frac{\partial}{\partial z_{k}^{1}}\right\}.$

证明 选局部平整坐标卡 $z$ 使得

$$\mathcal {H} ^ {\perp} = \operatorname{span} \left\{\frac {\partial}{\partial z _ {1} ^ {1}}, \dots , \frac {\partial}{\partial z _ {k} ^ {1}} \right\}.$$

在这个坐标下，由于 $\mathrm{d}h\in \mathcal{H},\left\langle \mathrm{d}h,\frac{\partial}{\partial z_i^1}\right\rangle = 0,$ 故 $h(z) = h(z^2)$ .因为 $\mathcal{H}^{\perp}$ 是 $F$ 不变的，所以

$$\frac {\partial f ^ {2} (z)}{\partial z _ {i} ^ {1}} = 0, \quad i = 1, \dots , k.$$

式 (8.2.15) 显见.

推论8.2.2 对仿射非线性系统(8.1.2)，设 $x_0$ 为能观测余分布 $\mathcal{H}$ 的一个正则点，则存在 $x_0$ 的一个局部坐标卡 $(V,z)$ ，使得系统(8.1.2)可局部表示为

$$
\left\{ \begin{array}{l} z ^ {1} = f ^ {1} (z) + \sum_ {i = 1} ^ {m} g _ {i} (z) u _ {i}, \\ z ^ {2} = f ^ {2} (z ^ {2}) + \sum_ {i = 1} ^ {m} g _ {i} (z ^ {2}) u _ {i}, \quad z \in V, \\ y = h (z ^ {2}), \end{array} \right. \tag {8.2.16}
$$

这里分布 $H^{\perp} = \operatorname{span}\left\{\frac{\partial}{\partial z_{1}^{1}}, \frac{\partial}{\partial z_{2}^{1}}, \cdots, \frac{\partial}{\partial z_{k}^{1}}\right\}.$

为得到非线性系统的 Kalman 分布，我们给出以下引理：

引理8.2.4 分布 $\mathcal{F}_0\cap \mathcal{H}^\perp$ 和 $\mathcal{F}_0\bigcup \mathcal{H}^\perp$ 均为对合分布.
