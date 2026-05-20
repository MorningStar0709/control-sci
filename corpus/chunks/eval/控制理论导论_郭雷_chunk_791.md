# 频域乘子法

时域乘子法也可适用于非线性系统，包括非线性控制。对于定常线性系统，则也可以在频率域中采用乘子法，而且有时会更简单。我们知道，为了Hilbert空间 $\mathcal{H}$ 中由线性算子 $\mathcal{A}$ 生成的一致有界 $C_0$ 半群指数稳定，必须且只须 $\mathrm{i}\mathbb{R} \subset \rho(\mathcal{A})$ ，并且

$$\sup \left\{\| R (\mathcal {A}; \mathrm{i} \omega) \| \mid \omega \in \mathbb {R} \right\} < \infty . \tag {10.4.25}$$

在一些情形下，可以直接计算出豫解式 $R(\mathcal{A};\mathrm{i}\omega)$ ，进而进行估计。但在许多情形下，这并不是一件容易的事情。相反，如果用反证法，则事情可能会相对容易些。假设条件(10.4.25)不成立，则存在序列 $\{\omega_n\} \subset \mathbb{R}$ 和 $\{Y_n\} \subset \mathcal{D}(\mathcal{A})$ ，满足

$$
\left\{\begin{array}{l}\| Y _ {n} \| = 1, \quad \lim _ {n \rightarrow \infty} | \omega_ {n} | = \infty ,\\\lim _ {n \rightarrow \infty} \| (\mathrm{i} \omega_ {n} - \mathcal {A}) Y _ {n} \| = 0.\end{array}\right. \tag {10.4.26}
$$

频域乘子法就是通过选择适当的乘子，从 (10.4.26) 导出矛盾，从而证明系统指数稳定。参见文献 [28], [29]。下面我们举例说明之。

例10.4.5 (Timoshenko 梁的局部分布反馈镇定) 考虑具有局部分布反馈的 Timoshenko 梁方程

$$
\left\{ \begin{array}{l l} \rho \ddot {w} + (K (\varphi - w ^ {\prime})) ^ {\prime} + \rho b _ {1} (x) \dot {w} = 0, & 0 <   x <   \ell , \\ I _ {\rho} \ddot {\varphi} - (E I \varphi^ {\prime}) ^ {\prime} + K (\varphi - w ^ {\prime}) + I _ {\rho} b _ {2} (x) \dot {\varphi} = 0, & 0 <   x <   \ell , \\ w (0, t) = \varphi (0, t) = 0, \\ \varphi (\ell , t) = w ^ {\prime} (\ell , t), \quad \varphi^ {\prime} (\ell , t) = 0, \end{array} \right. \tag {10.4.27}
$$

其中 $\varphi(x, t)$ 为梁的转角， $I_{\rho}$ 和 $K$ 分别为梁的质量惯量矩和剪切模量，其余变量同前。关于函数 $\rho, I_{\rho}, EI, K, b_{1}(x)$ 和 $b_{2}(x)$ ，我们作如下假设：

$$
\left\{ \begin{array}{l} b _ {j} (x) = 0, \quad x \notin [ a, b ]; \quad b _ {j} (x) \geqslant 0, \quad x \in [ a, b ]; \\ b _ {j} (x) \geqslant \gamma_ {0} > 0, \quad x \in [ c, d ] \subset [ a, b ]; \quad b _ {j} \in L ^ {\infty} (0, \ell); \\ \rho , K, E I, I _ {\rho} \in C ^ {1} ([ 0, \ell ]); \\ \rho (x), K (x), E I (x), I _ {\rho} (x) \geqslant \gamma_ {1} > 0, \quad x \in [ 0, \ell ]. \end{array} \right. \tag {10.4.28}
$$

现在我们在假设 (10.4.28) 下，利用频域乘子法证明系统 (10.4.27) 是指数稳定的。

取状态空间为乘积 Hilbert 空间 $\mathcal{H} = V_0^1 \times L_\rho^2(0, \ell) \times V_0^1 \times L_{I_\rho}^2(0, \ell)$ , 其中 $V_0^k = \{\varphi \in H^k(0, \ell) \mid \varphi(0) = 0\}$ . 对于 $Y_k = [\varphi_k, z_k, \varphi_k, \psi_k]^{\mathrm{T}} \in \mathcal{H}, k = 1, 2$ , 定义 $\mathcal{H}$ 中内积为
