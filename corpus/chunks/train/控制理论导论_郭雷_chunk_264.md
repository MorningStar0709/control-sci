# 3.11 Riemann 几何

直观地说，Riemann流形是对一个微分流形定义一个一般性的距离。它在非线性系统的优化控制，分布参数系统控制等中有许多重要作用。

当 $r = 2$ 时，张量场 $\phi(x) \in T^2(M)$ 是一个二次型。在局部坐标下它可表示为

$$\phi (X, Y) = X ^ {\mathrm{T}} (x) M _ {\phi} (x) Y (x), \quad X (x), Y (x) \in V (M),$$

这里 $M_{\phi}(x)$ 是 $\phi$ 的矩阵表示，它的元素为

$$\boldsymbol {M} _ {\phi} ^ {i, j} (\boldsymbol {x}) = \phi (\boldsymbol {x}) \left(\frac {\partial}{\partial x _ {i}}, \frac {\partial}{\partial x _ {j}}\right).$$

张量场 $\phi(x)$ 是对称的 (反对称的), 当且仅当 $M_{\phi}(x)$ 是对称 (反对称) 矩阵. 如果

$$\phi (x) (X, X) \geqslant 0, \quad \text {且} \phi (X (x), X (x)) = 0 \text {当且仅当} X (x) = 0, \quad \forall x \in M,$$

则 $\phi(x)$ 称为正定的。显然 $\phi(x)$ 是正定的，当且仅当 $M_{\phi}(x)$ 是正定矩阵。

定义3.11.1 一个流形 $M$ 连同一个对称张量 $\phi \in T^2(M)$ 称为一个伪Riemann流形．如果 $\phi$ 还是正定的，则 $(M,\phi)$ 称为一个Riemann流形.

设 $M$ 为一个Riemann流形. $M$ 上的一条光滑曲线 $L$ 定义为映射 $L:[a,b]\to M$ . $L$ 的长度定义为

$$| L | = \int_ {a} ^ {b} \sqrt {\phi \left(\frac {\mathrm{d} L}{\mathrm{d} t} , \frac {\mathrm{d} L}{\mathrm{d} t}\right)} \mathrm{d} t. \tag {3.11.1}$$

两点 $A = L(a)$ 及 $B = L(b)$ 的Riemann距离定义为

$$d (A, B) = \inf \left\{\left| L \right| \mid L (a) = A, L (b) = B \right\}. \tag {3.11.2}$$

可以证明这是一个距离 $^{[2]}$ ，因此 Riemann 流形是一个距离空间.

例3.11.1 (1) 在 $\mathbb{R}^n$ 中设 $\phi$ 由 $M_{\phi} = I_n$ 给出。那么显然它是一个Riemann流形。事实上由这个二次型 $\phi$ 定义的距离是 $\mathbb{R}^n$ 上的距离(参见例3.3.1);

(2) 在 $\mathbb{R}^4$ 中设 $\phi$ 由下式给出 (其中 $c$ 为光速):

$$
\boldsymbol {M} _ {\phi} = \left[ \begin{array}{c c c c} c & 0 & 0 & 0 \\ 0 & - 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & - 1 \end{array} \right].
$$

那么 $\mathbb{R}^4$ 带上这个 $\phi$ 是一个伪Riemann流形，它是相对论的几何框架[6].

下面考虑 Riemann 流形上的积分. 先考虑一般流形上的积分. 设 $M$ 为一可定向流形. $\omega \in \Omega^n(M)$ 是处处不为零的 $n$ -形式. 它给 $M$ 定向. $\omega$ 称为一个体积元.

定义 3.11.2 设 $(U,x)$ 为一坐标卡，即 $\phi(U)\subset\mathbb{R}^{n}$ ，在这个坐标卡下 $\phi$ 表示为 $\phi(x)=g(x)\mathrm{d}x^{1}\wedge\cdots\wedge\mathrm{d}x^{n}$ . $C\subset\phi(U)$ 是一个立方体。那么 $\omega$ 在 $\phi^{-1}(C)$ 上的积分定义为

$$\int_ {\phi^ {- 1} (C)} \omega = \int_ {C} g (x) \mathrm{d} v. \tag {3.11.3}$$

设 $f(x)$ 为一有界分段连续函数. 那么 $f$ 在 $\phi^{-1}(C)$ 上的积分定义为

$$\int_ {\phi^ {- 1} (C)} f \omega = \int_ {C} f (x) g (x) \mathrm{d} v. \tag {3.11.4}$$

要说明积分是定义好的，我们必须指出它与局部坐标无关。设 $y = y(x)$ 为另一坐标。由微积分可知式(3.11.3)的右边为

$$\int_ {C ^ {\prime}} g (x (y)) \det (J _ {x} (y)) \mathrm{d} v ^ {\prime}.$$

而 $\omega$ 在 $y$ 坐标下可表示为

$$\omega = \det (J _ {x} (y)) \mathrm{d} y ^ {1} \wedge \dots \wedge \mathrm{d} y ^ {n}.$$

因此式 (3.11.3) 仍然成立.
