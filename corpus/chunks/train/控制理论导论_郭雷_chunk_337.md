$$
\begin{array}{l} E \left(\mathrm{e} ^ {\mathrm{i} \lambda^ {T} x} | y\right) = \exp \left\{\mathrm{i} \lambda^ {T} E (x | y) \right\} E \left[ \exp \left\{\mathrm{i} \lambda^ {T} (x - E (x | y)) \right\} | y \right] \\ = \exp \left\{\mathrm{i} \lambda^ {T} E (x | y) \right\} E \exp \left\{\mathrm{i} \lambda^ {T} (x - E (x | y)) \right\} \\ = \exp \left\{\mathrm{i} \lambda^ {\mathrm{T}} E (x | y) - \frac {1}{2} \lambda^ {\mathrm{T}} R _ {x} ^ {y} \lambda \right\}; \\ \end{array}
$$

ii) 和 (4.4.5) 类似，仍有

$$R _ {x z} ^ {y} (R _ {z} ^ {y}) ^ {+} R _ {z} ^ {y} = R _ {x z} ^ {y}, \tag {4.4.29}$$

并且可取 $(R_z^y)^+$ 为对 $y$ 可测的.

只要把取期望 $E(\cdot)$ 换成取条件期望 $E(\cdot |y)$ , 其余的证明完全和 i) 类似. 例如, 我们来证 (4.4.27). 由式 (4.4.29) 知

$$E \{[ x - E (x | y)) - R _ {x z} ^ {y} (R _ {z} ^ {y}) ^ {+} (z - E (z | y)) ] (z - E (z | y)) ^ {\mathrm{T}} | y \} = 0,$$

因此在 $y$ 条件下， $x - E(x|y) - R_{xz}^{y}(R_{z}^{y})^{+}(z - E(z|y))$ 和 $z$ 条件独立。因此

$$
\begin{array}{l} E \left\{\left[ x - E (x | y) - R _ {x z} ^ {y} \left(R _ {z} ^ {y}\right) ^ {+} (z - E (z | y)) \right] \mid y, z \right\} \\ = E \left\{\left[ x - E (x | y) - R _ {x z} ^ {y} \left(R _ {z} ^ {y}\right) ^ {+} (z - E (z | y)) \right] \mid y \right\} = 0 \\ \end{array}
$$

由此便得式 (4.4.27). 其他也类似地证明.

注4.4.1 定理4.4.1给出了系统(4.4.1)\~(4.4.2)的线性无偏最小方差的递推滤波公式．假设 $\{w_{k}\}$ 为相互独立的正态向量， $w_{k}\in \mathcal{N}(0,I)$ ，那么 $x_{k},y_{k}k = 0,1,2\dots$ 为联合正态．而对正态向量最小方差估计和线性无偏最小方差估计相同，所以这时式(4.4.15)\~(4.4.19)也是最小方差滤波的递推公式.

现考察系统

$$x _ {k + 1} = \Phi_ {k + 1, k} x _ {k} + B _ {k} u _ {k} + D _ {k + 1} w _ {k + 1}, \tag {4.4.30}y _ {k} = C _ {k} x _ {k} + H _ {k} v _ {k - 1} + F _ {k} w _ {k}, \text {初值} x _ {0}, y _ {0}. \tag {4.4.31}$$

系统 (4.4.1) 及 (4.4.2) 中的系数 $\Phi_{k+1,k}, B_k, b_k, D_{k+1}, C_k, H_k$ 和 $F_k$ 都是确定性的。现在来考虑它们可能非线性地依赖过去的量测量的情况。确切地说，允许 $\Phi_{k+1,k}, B_k u_k, D_{k+1}$ 可以非线性地依赖 $[y_0, y_1, \cdots, y_k]$ ，而 $C_k, H_k v_{k-1}$ 及 $F_k$ 可非线性地依赖 $[y_0, y_1, \cdots, y_{k-1}]$ 。具体要求如下：

A1. $\Phi_{k+1,k}, B_k, u_k, D_{k+1}$ 对 $y^k \stackrel{\operatorname{def}}{=} [y_0^T, y_1^T, \cdots, y_k^T]^T$ 可测，并且 $\Phi_{k+1,k}, B_k$ 对 $\omega$ 一致有界， $E\|u_k\|^2 < \infty, E\|D_k\|^2 < \infty.$

A2. $C_k, F_k, H_k, v_{k-1}$ 对 $y^{k-1}$ 可测， $\| C_k\|$ 对 $\omega$ 一致有界，

$$E \| H _ {k} v _ {k - 1} \| ^ {2} < \infty , \quad E \| F _ {k} \| ^ {2} < \infty , \quad \forall k.$$

A3. $E(\| x_0\|^2 + \| y_0\|^2) < \infty$ ，在 $y_0$ 条件下， $x_0$ 是期望为 $E(x_0|y_0)$ ，协方差为 $R_{x_0}^{y_0}$ 的条件正态向量。
