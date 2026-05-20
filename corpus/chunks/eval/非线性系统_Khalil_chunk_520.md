# C. 14 证明定理 7.4

如果在引理7.1的证明中定义了 $P_{1} = 0, P_{h} = I$ ，那么如果 $\omega \in \tilde{\Omega}$ ，映射 $T$ 就是压缩映射。因此， $y = y_{h} = 0$ 是 $y_{h} = Ty_{h}$ 的唯一解，这就证明了不存在基频为 $\omega \in \tilde{\Omega}$ 的半波对称周期解。条件

$$\left| \frac {1}{G (j \omega)} + \Psi (a) \right| \leqslant \sigma (\omega)$$

的必要性说明,若相应的误差圆与 $-\Psi(a)$ 的轨线不相交,就不存在基频为 $\omega \in \Omega'$ 的半波对称周期解。因此只剩定理的第三部分,需证明对每个定义 $\Gamma$ 的完全交叉,存在一个半波对称周期解, $(\omega, a) \in \bar{\Gamma}$ 。该证明用到由阶次理论(degree theory)得到的一个结果。首先解释该结果。

假设给定一个连续可微函数 $\phi: D \to R^n$ ，其中 $D \subset R^n$ 是有界的开区域，设 $p \in R^n$ 是对于 $D$ 内的某个 $x$ 满足 $\phi(x) = p$ 的点，但在 $D$ 的边界 $\partial D$ 上，即 $\phi(x) \neq p$ 。我们只想证明 $\tilde{\phi}(x) = p$ 在 $D$ 内有一个解，其中 $\tilde{\phi}(x)$ 是 $\phi(x)$ 的扰动。阶次理论通过保证当 $\phi$ 被扰动到 $\tilde{\phi}$ 时，没有解留在 $D$ 内，从而证明了这一点，这就是为什么不允许有解在边界 $\partial D$ 上。假设对于 $\phi(x) = p$ 的每个解 $x_i \in D$ ，雅可比矩阵 $[\partial \phi / \partial x]$ 是非奇异的，定义 $\phi$ 在 $p$ 点相对于 $D$ 的阶次为

$$d (\phi , D, p) = \sum_ {x _ {i} = \phi^ {- 1} (p)} \operatorname{sgn} \left\{\det \left[ \frac {\partial \phi}{\partial x} \left(x _ {i}\right) \right] \right\}$$

注意如果 $\phi (x)\neq p,\forall x\in D$ ，则阶次为零。阶次的两个基本性质如下①：

\- 如果 $d(\phi, D, p) \neq 0$ ，则 $\phi(x) = p$ 在 $D$ 内至少有一个解。

\- 如果 $\eta: \bar{D} \times [0,1] \to R^n$ 连续，且对于所有 $x \in \partial D$ 和 $\mu \in [0,1]$ ，有 $\eta(x, \mu) \neq 0$ ，则 $d[\eta(\cdot, \mu), D, p]$ 对于所有 $\mu \in [0,1]$ 都是相同的（具有与之相同的特性）。

第二个性质也称为 d 的同伦不变性。

现在回到我们要解决的问题上,在 $\Gamma$ 上定义

$$\phi (\omega , a) = \Psi (a) + \frac {1}{G (j \omega)}$$

其中 $\phi$ 是复变量。取 $\phi$ 的实部和虚部作为二阶向量的分量，这样 $\phi$ 就可以看成 $\Gamma$ 到 $R^2$ 的映射。根据假设，方程 $\phi(w, a) = 0$ 在 $\Gamma$ 内有唯一解 $(\omega_s, a_s)$ ，在 $(\omega_s, a_s)$ 点 $\phi$ 对于 $(\omega, a)$ 的雅可比矩阵为

$$
\left[ \begin{array}{c c} \left. \frac {d}{d a} \Psi (a) \right| _ {a = a _ {s}} & - \Psi^ {2} (a _ {s}) \left\{\frac {d}{d \omega} \mathrm{Re} [ G (j \omega) ] \right\} _ {\omega = \omega_ {s}} \\ 0 & - \Psi^ {2} (a _ {s}) \left\{\frac {d}{d \omega} \mathrm{Im} [ G (j \omega) ] \right\} _ {\omega = \omega_ {s}} \end{array} \right]
$$

假设

$$\left. \frac {d}{d a} \Psi (a) \right| _ {a = a _ {s}} \neq 0; \quad \left. \frac {d}{d \omega} \mathrm{Im} [ G (j \omega) ] \right| _ {\omega = \omega_ {s}} \neq 0$$

保证了雅可比矩阵是非奇异的。这样

$$d (\phi , \Gamma , 0) = \pm 1$$

我们想要证明 $\tilde{\phi} (\omega ,a)\stackrel {\mathrm{def}}{=}\frac{1}{G(j\omega)} +\Psi (a) - \delta \Psi (\omega ,a) = 0$ (C.52)

在 $\bar{\Gamma}$ 内有一个解，只需证明 $d(\tilde{\phi},\Gamma ,0)\neq 0$
