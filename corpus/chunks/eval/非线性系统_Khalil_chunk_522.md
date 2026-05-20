# C. 15 证明定理 8.1 和定理 8.3

证明这两个定理主要是以压缩映射理论为依据,该理论几乎贯穿于两个定理的证明中。为避免重复,我们先给出并证明一个引理,它是所用压缩映射理论的核心,然后用此引理证明这两个定理。引理的叙述似乎与定理8.1非常相似,但它有一个定理8.3需要的附加要求。

引理 C.6 考虑设系统为

$$\dot {y} = A y + f (y, z) \tag {C.54}\dot {z} = B z + g (y, z) \tag {C.55}$$

其中 $y \in R^{k}, z \in R^{m}, A$ 的特征值实部为零, B 的特征值实部为负, f 和 g 是二次连续可微函数, 与其一阶导数在原点均为零。则存在 $\delta > 0$ , 并对于所有 $\|y\| < \delta$ , 定义连续可微函数 $\eta(y)$ , 使得 $z = \eta(y)$ 为系统 (C.54) \~ (C.55) 的一个中心流形, 而且如果对于所有 $\|y\| \leqslant r$ , 有 $\|g(y,0)\| \leqslant k \|y\|^{p}$ , 其中 p > 1, r > 0, 则存在 c > 0, 使得 $\|\eta(y)\| \leqslant c \|y\|^{p}$ 。

证明: 当对于所有 $t \in R$ ，流形内的解都有定义时，证明存在中心流形更为方便。一般来说，系统(C.54)～(C.55)的中心流形可能仅是局部的，即流形内的解可能只在区间 $[0, t_{1}) \subset R$ 上有定义。因此,证明中用到下面的思想:考虑在原点的一个邻域内对方程(C.54)\~(C.55)相同的一个修正方程,但它具有某些理想的全局性质,即保证中心流形内的解对于所有t有定义。我们证明修正方程存在一个中心流形。由于两个方程在原点的邻域内相同,这样就证明了原方程存在一个(局部)中心流形。

设 $\psi: R^k \to [0,1]$ 是光滑（无穷多次连续可微）函数①，当 $\|y\| \leqslant 1$ 时， $\psi(y) = 1$ ，当 $\|y\| \geqslant 2$ 时， $\psi(y) = 0$ 。对于 $\varepsilon > 0$ ，定义 $F$ 和 $G$ 为

$$F (y, z) = f \left(y \psi \left(\frac {y}{\varepsilon}\right), z\right); G (y, z) = g \left(y \psi \left(\frac {y}{\varepsilon}\right), z\right)$$

函数 $F$ 和 $G$ 是二次连续可微的，连同其一阶偏导数都对 $y$ 全局有界，即只要 $\| z\| \leqslant k_1$ ，函数对于所有 $y\in R^k$ 都是有界的。考虑修正系统

$$\dot {y} = A y + F (y, z) \tag {C.56}\dot {z} = B z + G (y, z) \tag {C.57}$$

我们证明系统(C.56)\~(C.57)存在一个中心流形。设 $X$ 表示所有全局有界连续函数 $\eta: R^k \to R^m$ 的集合，以 $\sup_{y \in R^k} \| \eta(y) \|$ 为范数，则 $X$ 为 Banach 空间。当 $c_1 > 0, c_2 > 0, c_3 > 0$ 时，设 $S \subset X$ 是全体连续可微函数 $\eta: R^k \to R^m$ 的集合，对于所有 $x, y \in R^k$ 满足

$$\eta (0) = 0, \frac {\partial \eta}{\partial y} (0) = 0, \| \eta (y) \| \leqslant c _ {1}, \left\| \frac {\partial \eta}{\partial y} (y) \right\| \leqslant c _ {2}, \left\| \frac {\partial \eta}{\partial y} (y) - \frac {\partial \eta}{\partial y} (x) \right\| \leqslant c _ {3} \| y - x \|$$

为证明 S 是闭集, 设 $\eta_{i}(y)$ 是 S 内的收敛序列, 并证明 $\eta(y)=\lim_{i\to\infty}\eta_{i}(y)$ 属于 S, 其中的关键步骤是证明 $\eta(y)$ 连续可微, 其余可由反证法证明。由于连续可微可由分量方式证明, 因此我们只对标量 $\eta$ 证明。设 v 是 $R^{k}$ 内的任意向量, $\|v\|=1,\mu$ 是正常数。根据均值定理, 有

$$\eta_ {i} (y + \mu v) - \eta_ {i} (y) = \frac {\partial \eta_ {i}}{\partial y} (y + \alpha_ {i} \mu v) \mu v\eta_ {j} (y + \mu v) - \eta_ {j} (y) = \frac {\partial \eta_ {j}}{\partial y} (y + \alpha_ {j} \mu v) \mu v$$

其中 $0 < \alpha_{i} < 1, 0 < \alpha_{j} < 1$ 。通过加减项，可写出以下方程：
