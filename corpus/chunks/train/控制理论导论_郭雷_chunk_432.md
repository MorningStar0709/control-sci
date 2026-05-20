$$
\bar {A} = \left[ \begin{array}{c c} A + B B ^ {\mathrm{T}} X & B B ^ {\mathrm{T}} \\ 0 & - (A + B B ^ {\mathrm{T}} X) ^ {\mathrm{T}} \end{array} \right], \quad \ddot {B} = \left[ \begin{array}{c} B \\ - X B \end{array} \right], \quad \bar {C} = [ B ^ {\mathrm{T}} X \setminus B ^ {\mathrm{T}} ].
$$

所以有

$$
\begin{array}{l} T (s) = \left(I - G ^ {T} (- s) G (s)\right) ^ {- 1} \\ = I + \bar {C} (s I - \bar {A}) ^ {- 1} \bar {B} \\ = I + B ^ {T} X \left(s I - A _ {X}\right) ^ {- 1} B + B ^ {T} \left(- s I - A _ {X}\right) ^ {- 1} X B \\ + B ^ {T} X (s I - A _ {X}) ^ {- 1} B B ^ {T} (- s I - A _ {X}) ^ {- 1} X B \\ = N (s) N (- s), \\ \end{array}
$$

其中 $N(s) = I + B^{\mathrm{T}}X(sI - A_X)^{-1}B, A_X = A + BB^{\mathrm{T}}X.$ 因此

$$T (\mathrm{j} \omega) \geqslant 0, \quad \forall \omega \in \mathbb {R}.$$

又因为 $A_{X} = A + BB^{\mathrm{T}}X$ 是稳定阵，所以 $(XB,A^{\mathrm{T}})$ 是可检测的。另一方面，式(6.2.1)又可以表示成Lyapunov方程形式

$$A ^ {\mathsf {T}} X + X A = - R R ^ {\mathsf {T}}, \quad R = [ X B C ^ {\mathsf {T}} ]. \tag {6.2.10}$$

由于 $(R, A^{\mathrm{T}})$ 是可检测的且 $X \geqslant 0$ , 所以根据 Lyapunov 稳定性定理, $A$ 是稳定阵. 此外, 由

$$
\begin{array}{l} \left| N (s) \right| = \left| I + B ^ {\mathrm{T}} X \left(s I - A _ {X}\right) ^ {- 1} B \right| \\ = | I + (s I - A _ {X}) ^ {- 1} B B ^ {\mathrm{T}} X | = | s I - A | \cdot | s I - A _ {X} | \\ \end{array}
$$

可得

$$T (\mathrm{j} \omega) \neq 0, \quad \forall \omega \in \mathbb {R}.$$

因此

$$T (\mathrm{j} \omega) = (I - G ^ {T} (- \mathrm{j} \omega) G (\mathrm{j} \omega)) ^ {- 1} > 0, \quad \forall \omega \in \mathbb {R}, \tag {6.2.11}$$

即

$$\| G (s) \| _ {\infty} = \sup _ {\omega} \dot {\sigma} \{G (\mathrm{j} \omega) \} < 1.$$

注6.2.1 在闭右半平面解析且 $H_{\infty}$ 范数小于1的有理函数阵 $G(s) \in RH_{\infty}^{n \times m}$ 称为是有界实的(Bounded Real). 上述定理表明, 一个传递函数阵是有界实的等价条件是Riccati方程(6.2.1)有半正定的稳定解, 或者Hamilton矩阵 $H$ 在虚轴上无特征值. 上述命题(1)和(2)的等价性称为有界实引理[5].

注6.2.2 依据定理6.2.1还可以近似计算有理函数阵 $G(s)$ 的 $H_{\infty}$ 范数。注意对于有理函数阵 $G(s) = C(sI - A)^{-1}B$ 。 $\| G(\cdot)\|_{\infty} < \gamma$ 等价于 $\|\gamma^{-1}G(\cdot)\|_{\infty} < 1$ ，而后者根据定理6.2.1又等价于如下定义的Hamilton矩阵 $H_r$ 在虚轴上无特征值：

$$
H _ {\gamma} = \left[ \begin{array}{c c} A & \gamma^ {- 2} B B ^ {\mathrm{T}} \\ - C ^ {\mathrm{T}} C & - A ^ {\mathrm{T}} \end{array} \right].
$$

因此，对于给定的 $\gamma > 0$ ，如果 $H_{\gamma}$ 在虚轴上无特征值，则 $\|G(\cdot)\|_{\infty} < \gamma$ ，否则 $\|G(\cdot)\|_{\infty} \geqslant \gamma$ 。于是我们可以找到充分大的 $\gamma_{M} > 0$ 和充分小的 $\gamma_{m} > 0$ 使得

$$\gamma_ {m} \leqslant \| G (s) \| _ {\infty} < \gamma_ {M}.$$
