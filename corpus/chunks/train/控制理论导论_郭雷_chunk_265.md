只要积分对一个小方块定义好了，它对任何区域也就定义好了，因为区域可分解成小方块.

显然流形上的积分依赖于体积元的选择。幸运的是，下面的定理保证唯一的约定积分在Riemann流形上的存在。（证明见文献[2])

定理 3.11.1 设 M 为一个可定向 Riemann 流形，Riemann 距离为 $\Phi$ . 那么存在 M 上唯一的定向张量 $\omega \in \Omega^{n}(M)$ 使对任何直交基 $e_{1}, \cdots, e_{n}$ ，有 $\omega(e_{1}, \cdots, e_{n}) = 1$ . 此外，设 $M_{\Phi}(x)$ 为 $\Phi$ 在给定局部坐标 x 下的矩阵形式，那么 $\omega$ 可表示成

$$\omega = \sqrt {g} \mathrm{d} x ^ {1} \wedge \dots \wedge \mathrm{d} x ^ {n}, \tag {3.11.5}$$

这里 $g = \operatorname{det}(M_{\phi})$

这个 $\omega$ 称为自然体积元. 在定向Riemann流形上的约定积分就是对这个 $\omega$ 的积分.

例3.11.2 在 $\mathbb{R}^3$ 上设曲面 $S$ 由 $z = F(x, y)$ 定义。在 $S$ 上的距离为 $\mathbb{R}^3$ 上的导出距离。考虑在区域 $\tilde{D}$ 上的积分，这里

$$\widetilde {D} = \{(x, y), F (x, y) \mid (x, y) \in D \}.$$

设 $T^{*}(S)$ 的基为 $\{E_1,E_2\}$ . 那么

$$
\boldsymbol {E} _ {1} = \phi^ {- 1} \left(\frac {\partial}{\partial x}\right) = J _ {\phi^ {- 1}} \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ \frac {\partial F}{\partial x} & \frac {\partial F}{\partial y} \end{array} \right] \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] = \left[ \begin{array}{c} 1 \\ 0 \\ \frac {\partial F}{\partial x} \end{array} \right].
$$

同理，

$$
\boldsymbol {E} _ {2} = \left[ \begin{array}{c} 1 \\ 0 \\ \frac {\partial F}{\partial y} \end{array} \right].
$$

现在自然体积元的矩阵为

$$
\boldsymbol {M} _ {\phi} = \left[ \begin{array}{l l} \langle E _ {1}, E _ {1} \rangle & \langle E _ {1}, E _ {2} \rangle \\ \langle E _ {2}, E _ {1} \rangle & \langle E _ {2}, E _ {2} \rangle \end{array} \right] = \left[ \begin{array}{c c} 1 + \left(\frac {\partial F}{\partial x}\right) ^ {2} & \frac {\partial F}{\partial x} \frac {\partial F}{\partial y} \\ \frac {\partial F}{\partial y} \frac {\partial F}{\partial x} & 1 + \left(\frac {\partial F}{\partial y}\right) ^ {2} \end{array} \right].
$$

因此

$$\sqrt {g} = \sqrt {1 + \left(\frac {\partial F}{\partial x}\right) ^ {2} + \left(\frac {\partial F}{\partial y}\right) ^ {2}}.$$

设 $h(x,y)$ 为 $S$ 上的一个函数，它在 $\tilde{D}$ 上的积分为

$$\int_ {D} h (x, y) \sqrt {1 + \left(\frac {\partial F}{\partial x}\right) ^ {2} + \left(\frac {\partial F}{\partial y}\right) ^ {2}} \mathrm{d} x \wedge \mathrm{d} y.$$

下面考虑 Riemann 流形上的微分．联络在几何和物理中均很重要 [4]．利用半张量积我们将联络的一些基本公式表示为矩阵形式.

定义3.11.3 设 $f, g \in V(M)$ 为两向量场. 如果一个映射 $\nabla: V(M) \times V(M) \to V(M)$ 满足

(1)

$$\nabla_ {r f} s g = r s \nabla_ {f} g, \quad r, s \in \mathbb {R}; \tag {3.11.6}$$

(2)
