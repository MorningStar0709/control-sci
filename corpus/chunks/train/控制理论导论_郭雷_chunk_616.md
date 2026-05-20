首先假定 $\Delta\cap G=\{0\}$ . 那么可以证明，如果式 (8.4.5) 的第二个方程成立，则式 (8.4.4) 的第二个方程等价于存在一个 $m\times(n-k)$ 矩阵 K，它与 $x_{1},\cdots,x_{k}$ 无关，使得 $Kg^{2}$ 是非奇异的.

设式 (8.4.4) 的第二个方程成立. 令 $K = \beta^{\mathrm{T}}(g^{2})^{\mathrm{T}}$ , 它与 $x_{i}$ 无关. 因为 $\Delta \cap G = \{0\}$ , $\operatorname{rank}(g^{2}) = k$ , 表明 $(g^{2})^{\mathrm{T}}g^{2} > 0$ 即为正定的. 因此 $Kg^{2} = \beta^{\mathrm{T}}(g^{2})^{\mathrm{T}}g^{2}$ 是非奇异的.

反之，从式(8.4.5)的第二个方程可知

$$\frac {\partial g ^ {2}}{\partial x _ {i}} = g ^ {2} \Gamma_ {i}, \quad i = 1, \dots , k,$$

这里 $\Gamma_{i}$ 是某个 $m \times n$ 函数矩阵. 选择

$$\beta = (K g ^ {2}) ^ {- 1},$$

这里 $K$ 与 $x_{i}$ 无关，则有

$$
\begin{array}{l} \frac {\partial}{\partial x _ {i}} \left(g ^ {2} \beta\right) = \frac {\partial}{\partial x _ {i}} g ^ {2} \left(K g ^ {2}\right) ^ {- 1} \\ = \frac {\partial}{\partial x _ {i}} (g ^ {2}) (K g ^ {2}) ^ {- 1} - g ^ {2} (K g ^ {2}) ^ {- 1} \frac {\partial}{\partial x _ {i}} (K g ^ {2}) (K g ^ {2}) ^ {- 1} \\ = g ^ {2} \Gamma_ {i} (K g ^ {2}) ^ {- 1} - g ^ {2} (K g ^ {2}) ^ {- 1} K g ^ {2} \Gamma_ {i} (K g ^ {2}) ^ {- 1} \\ = 0. \\ \end{array}
$$

现在证明式 (8.4.5) 的第二个方程蕴涵式 (8.4.4) 的第二个方程，为此只要证明这样的 $K$ 存在即可。事实上，我们可取

$$K = (g ^ {2} (x _ {0} ^ {1}, x ^ {2})) ^ {\mathrm{T}},$$

这里 $x^{1}$ 是 x 的前 k 个坐标，且 $x_{0}^{1}$ 是 $x_{0}$ 的前 k 个坐标，它们是固定的，于是 K 与 $x_{i}, i=1,\cdots,k,$ 无关。要证明 $Kg^{2}$ 非奇异，因为它在 $x_{0}$ 点非奇异，故在 $x_{0}$ 的一个邻域上非奇异。

其次假定 $\operatorname{rank}(\Delta \bigcup G) = k + s < k + m$ ，那么我们能找到 $g^2$ 的 $s$ 个线性无关的列，如 $(b_1(x), \dots, b_s(x))$ ，使得

$$g ^ {2} = b (x) E (x), \tag {8.4.6}$$

这里 $E(x)$ 是一个 $s \times m$ 矩阵. 由于 $\operatorname{rank}(E(x)) = s$ , 故容易将 $E(x)$ 用 $b(x)$ 表示, 或反过来将 $b(x)$ 用 $E(x)$ 表示, 即

$$E (x) = \left(b ^ {\mathrm{T}} (x) b (x)\right) ^ {- 1} b ^ {\mathrm{T}} (x) g ^ {2} (x), \tag {8.4.7}$$

和

$$b (x) = g ^ {2} (x) E ^ {\mathrm{T}} (x) \left(E (x) E ^ {\mathrm{T}} (x)\right) ^ {- 1}. \tag {8.4.8}$$

因此 $E(x)$ 是光滑的，而且由于 $\operatorname{rank}(E(x)) = s$ ，我们可选择一个 $m \times (m - s)$ 光滑函数矩阵 $Q(x)$ ，使得

$$\operatorname{rank} \left[ Q (x), E ^ {T} (x) (E (x) E ^ {T} (x)) ^ {- 1} \right] = m.$$

定义

$$
\left\{ \begin{array}{l} W (x) = Q (x) - E ^ {\mathrm{T}} (x) \left(E (x) E ^ {\mathrm{T}} (x)\right) ^ {- 1} E (x) Q (x), \\ L (x) = E ^ {\mathrm{T}} (x) \left(E (x) E ^ {\mathrm{T}} (x)\right) ^ {- 1}, \\ \beta_ {0} (x) = [ W (x) L (x) ]. \end{array} \right. \tag {8.4.9}
$$

则可证明

$$
\beta_ {0} (x) = \left[ Q (x), E ^ {\mathrm{T}} (x) (E (x) E ^ {\mathrm{T}} (x)) ^ {- 1} \right] \left[ \begin{array}{c c} I _ {m - s} & 0 \\ - E (x) Q (x) & I _ {s} \end{array} \right],
$$
