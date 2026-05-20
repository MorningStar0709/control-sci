$$
\boldsymbol {x} _ {0} = \left[ \begin{array}{c} \boldsymbol {c} \\ \boldsymbol {c} G \\ \vdots \\ \boldsymbol {c} G ^ {n - 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} y (0) \\ y (1) \\ \vdots \\ y (n - 1) \end{array} \right] \tag {3.135}
$$

连续系统时间离散化后保持能控和能观测的条件 限于讨论定常的情况，设连续时间系统为

$$\Sigma : \quad \dot {x} = A x + B u, \quad t \geqslant 0 \tag {3.136}y = C x$$

而以 $T$ 为采样周期的时间离散化系统为

$$
\begin{array}{l l} \Sigma_ {T}: & x (k + 1) = G x (k) + H u (k), \quad k = 0, 1, 2, \dots \\ & v (k) = G v (k) \end{array} \tag {3.137}
\mathbf {y} (k) = C \mathbf {x} (k)
$$

其中， $G = e^{AT}$ 和 $H = \int_0^T e^{At}dtB$ 。于是，我们有如下的一个基本结论。

结论 令 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{\mu}$ 为 $A$ 的全部特征值，且当 $i \neq j$ 时有 $\lambda_{i} \neq \lambda_{j}$ 。则时间离散化系统 $\Sigma_{T}$ 保持能控(能观测)的一个充分条件是采样周期 $T$ 的数值，对一切满足

$$\operatorname{Re} \left[ \lambda_ {i} - \lambda_ {j} \right] = 0, \quad i, j = 1, 2, \dots , \mu \tag {3.138}$$

的特征值,应成立

$$T \neq \frac {2 l x}{\operatorname{Im} \left(\lambda_ {i} - \lambda_ {j}\right)}, \quad l = \pm 1, \pm 2, \dots \tag {3.139}$$

证 首先来证明：在条件(3.138)和(3.139)下， $\Sigma_{T}$ 能控归结为 $e^{AkT}B$ 行线性无关。

利用约当规范形，有

$$
Q A Q ^ {- 1} = \left[ \begin{array}{c c c} J _ {1} & & \\ & J _ {2} & \\ & & \ddots \\ & & J _ {\mu} \end{array} \right], \quad J _ {i} = \left[ \begin{array}{c c c} J _ {i 1} & & \\ & J _ {i 2} & \\ & & \ddots \\ & & J _ {i a _ {i}} \end{array} \right]

J _ {i k} = \left[ \begin{array}{c c c c} \lambda_ {i} & 1 & & \\ & \lambda_ {i} & \ddots & \\ & & \ddots & 1 \\ & & & \lambda_ {i} \end{array} \right] \tag {3.140}
$$

从而，即得

$$
\begin{array}{l} \det \left[ \int_ {0} ^ {T} e ^ {A t} d t \right] = \det \left[ \int_ {0} ^ {T} e ^ {(Q A Q ^ {- 1}) t} d t \right] \\ = \prod_ {i = 1} ^ {\mu} \det \left[ \int_ {0} ^ {T} e ^ {J _ {i} t} d t \right] \tag {3.141} \\ \end{array}
$$

进而，又有

$$
\begin{array}{l} \int_ {0} ^ {T} e ^ {J _ {i} t} d t = I T + \frac {1}{2 !} J _ {i} T ^ {2} + \frac {1}{3 !} J _ {i} ^ {2} T ^ {3} + \dots \\ = \left(I + J _ {i} T + \frac {1}{2 !} J _ {i} ^ {2} T ^ {2} + \dots\right) J _ {i} ^ {- 1} - J _ {i} ^ {- 1} \\ = \left(e ^ {J _ {i} T} - I\right) J _ {i} ^ {- 1} \tag {3.142} \\ \end{array}
$$

将(3.142)代入(3.141)可得

$$
\begin{array}{l} \det \left[ \int_ {0} ^ {T} e ^ {A t} d t \right] = \prod_ {i = 1} ^ {n} \det (e ^ {J _ {i} T} - I) (\det J _ {i}) ^ {- 1} \\ = \prod_ {i = 1} ^ {\mu} \left(e ^ {\lambda_ {i} T} - 1\right) ^ {\sigma_ {i}} (\det J _ {i}) ^ {- 1} \tag {3.143} \\ \end{array}
$$

其中 $\sigma_{i}$ 为特征值 $\lambda_{i}$ 的重数。再注意到满足(3.138)的特征值只可能是复数或虚数，从而此时必有 $\det J_{i} \neq 0$ 。而考虑到条件(3.139)成立时，有
