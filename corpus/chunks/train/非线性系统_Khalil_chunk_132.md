例 4.21 证明了 $V(t,x)=x^{\mathrm{T}}P(t)x$ 是李雅普诺夫函数。

□

当线性系统(4.29)是时不变系统,即 A 为常数时,则可选择定理 4.12 中的李雅普诺夫函数 $V(t,x)$ 与 t 无关。回顾线性时不变系统

$$\Phi (\tau , t) = \exp [ (\tau - t) A ]$$

当 $A$ 是赫尔维茨矩阵时，满足式(4.30)。选择 $Q$ 为正定对称(常数)矩阵，则矩阵 $P(t)$ 为

$$P = \int_ {t} ^ {\infty} \exp [ (\tau - t) A ^ {\mathrm{T}} ] Q \exp [ (\tau - t) A ] d \tau = \int_ {0} ^ {\infty} \exp [ A ^ {\mathrm{T}} s ] Q \exp [ A s ] d s$$

上式与 $t$ 有关。与式(4.13)比较，说明 $P$ 是李雅普诺夫方程(4.12)的唯一解。这样，定理4.12中的李雅普诺夫函数简化为4.3节中用到的李雅普诺夫函数。

现在用定理 4.12 对于线性系统存在李雅普诺夫函数的证明扩展到定理 4.7 中非自治系统的线性化。考虑非线性非自治系统

$$\dot {x} = f (t, x) \tag {4.31}$$

其中 $f: [0, \infty) \times D \to R^n$ 连续可微，且 $D = \{x \in R^n \mid \| x \|_2 < r\}$ 。假设原点 $x = 0$ 是系统在 $t = 0$ 时的平衡点，即对于所有 $t \geqslant 0$ ，有 $f(t, 0) = 0$ 。进一步假设雅可比矩阵 $[\partial f / \partial x]$ 有界，且在 $D$ 上是利普希茨的，对 $t$ 一致。因此，对于所有 $1 \leqslant i \leqslant n$ ，有

$$\left\| \frac {\partial f _ {i}}{\partial x} (t, x _ {1}) - \frac {\partial f _ {i}}{\partial x} (t, x _ {2}) \right\| _ {2} \leqslant L _ {1} \| x _ {1} - x _ {2} \| _ {2}, \forall x _ {1}, x _ {2} \in D, \forall t \geqslant 0$$

由均值定理得

$$f _ {i} (t, x) = f _ {i} (t, 0) + \frac {\partial f _ {i}}{\partial x} (t, z _ {i}) x$$

其中 $z_{i}$ 是由 $\pmb{x}$ 到原点的线段上的一点。由于 $f(t,0) = 0$ ，则 $f_{i}(t,x)$ 可以写成

$$f _ {i} (t, x) = \frac {\partial f _ {i}}{\partial x} (t, z _ {i}) x = \frac {\partial f _ {i}}{\partial x} (t, 0) x + \left[ \frac {\partial f _ {i}}{\partial x} (t, z _ {i}) - \frac {\partial f _ {i}}{\partial x} (t, 0) \right] x$$

因此 $f(t,x) = A(t)x + g(t,x)$

其中 $A(t) = \frac{\partial f}{\partial x} (t,0),\qquad g_i(t,x) = \left[\frac{\partial f_i}{\partial x} (t,z_i) - \frac{\partial f_i}{\partial x} (t,0)\right]x$

函数 $g(t,x)$ 满足

$$\| g (t, x) \| _ {2} \leqslant \left(\sum_ {i = 1} ^ {n} \left\| \frac {\partial f _ {i}}{\partial x} (t, z _ {i}) - \frac {\partial f _ {i}}{\partial x} (t, 0) \right\| _ {2} ^ {2}\right) ^ {1 / 2} \| x \| _ {2} \leqslant L \| x \| _ {2} ^ {2}$$

其中 $L = \sqrt{n} L_{1}$ 。因此，在原点的一个小邻域内，可通过对非线性系统(4.31)在原点的线性化逼近该系统。下一个定理将表述李雅普诺夫间接法，用以说明非自治系统中原点的指数稳定性。

定理4.13 设 $x = 0$ 是非线性系统

$$\dot {x} = f (t, x)$$

的一个平衡点,其中 $f:[0,\infty)\times D\to R^{n}$ 连续可微, $D=\{x\in R^{n}\mid\|x\|_{2}<r\}$ ,雅可比矩阵 $\left[\partial f/\partial x\right]$ 有界,且在D上是利普希茨的,对t一致。设

$$A (t) = \left. \frac {\partial f}{\partial x} (t, x) \right| _ {x = 0}$$

如果原点是线性系统

$$\dot {x} = A (t) x$$

的指数稳定平衡点,则它对非线性系统也是指数稳定平衡点。

![](image/d646231a8a359c8b59739a18041be985c6d5dededc8f8e03362b9d01e24128bd.jpg)
