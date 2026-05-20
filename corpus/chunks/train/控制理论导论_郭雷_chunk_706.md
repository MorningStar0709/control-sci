$$
\operatorname{sgn} (x) = \left\{ \begin{array}{l l} 1, & x \geqslant 0, \\ - 1, & x <   0. \end{array} \right.
$$

如上定义的 $\hat{b}_{1n}$ 有下列良好的性质：

$$\left| \hat {b} _ {1 n} \right| \geqslant \frac {1}{\sqrt {\log r _ {n - 1}}}, \quad \forall n \geqslant 1, \tag {9.5.44}$$

且

$$\left| \hat {b} _ {1 n} - b _ {1 n} \right| \leqslant \frac {1}{\sqrt {\log r _ {n - 1}}}, \quad \forall n \geqslant 1. \tag {9.5.45}$$

为了将对 $b_{1n}$ 的修正与不修正两种情形作统一处理，考虑如下一般的STR:

$$y _ {n + 1} ^ {*} = \theta_ {n} ^ {\mathrm{T}} \varphi_ {n} + (\Delta \hat {b} _ {1 n}) u _ {n}, \tag {9.5.46}$$

其中 $\{\theta_n\}$ 由LS算法(9.5.11)\~(9.5.13)给出， $\{\Delta \hat{b}_{1n}\}$ 是任意适应于 $\{\mathcal{F}_n\}$ 的序列，满足

$$\Delta \hat {b} _ {1 n} \equiv 0 \quad \text {或} \quad \Delta \hat {b} _ {1 n} \longrightarrow 0.$$

注意，若 $\Delta \hat{b}_{1n} \equiv 0$ ，则式(9.5.46)就是标准的LS-STR(9.5.14)；若 $\Delta \hat{b}_{1n} = \hat{b}_{1n} - b_{1n}$ ，则式(9.5.46)就是由式(9.5.43)所定义的STR.

为了分析方便，我们暂时假定由STR式(9.5.46)所定义的输入序列满足增长速度

$$u _ {n} ^ {2} = O \left(\log^ {2} r _ {n - 1} \left[ \sum_ {i = 0} ^ {p - 1} y _ {n - i} ^ {2} + \sum_ {i = 1} ^ {q - 1} u _ {n - i} ^ {2} \right] + \log r _ {n - 1}\right). \tag {9.5.47}$$

注意到由推论9.2.1知 $a_{in}, b_{jn}$ 的增长速度不超过 $O\left(\sqrt{\log r_{n-1}}\right)$ ，因此利用式(9.5.44)知由式(9.5.43)所定义的控制律 $u_n$ 确实满足式(9.5.47);另一方面，当 $b_{1n}$ 本身满足下列条件时：

$$\liminf _ {n \to \infty} \sqrt {\log r _ {n - 1}} | b _ {1 n} | \neq 0, \tag {9.5.48}$$

则 LS-STR 控制律 (9.5.15) 也满足式 (9.5.47). (本节习题中给出了另外两种保证此性质满足的方法.)

类似于引理9.5.1，我们有

引理 9.5.3 对系统 (9.5.42) 设条件 (A1)\~(A3) 成立且控制律满足关系式 (9.5.46) 与 (9.5.47), 那么存在正随机序列 $\{L_k\}$ 使

$$y _ {k} ^ {2} \leqslant L _ {k}, \quad \forall k$$

且 $\{L_k\}$ 满足关系式

$$L _ {k + 1} \leqslant (\lambda + C f _ {k}) L _ {k} + \xi_ {k},$$

其中常数 $\lambda \in (0,1), C > 0$ ，而

$$z f _ {k} = \left(\alpha_ {k} \delta_ {k} \log r _ {k - 1}\right) ^ {2} + \alpha_ {k} \delta_ {k} + \left(\Delta \hat {b} _ {1 k}\right) ^ {2},\xi_ {k} = O \left(d _ {k} \log^ {4} r _ {k}\right).$$

证明 由式 (9.5.4) 及式 (9.5.46) 知

$$y _ {k + 1} = \varphi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} - (\Delta \hat {b} _ {1 k}) u _ {k} + y _ {k + 1} ^ {*} + w _ {k + 1}, \tag {9.5.49}$$

于是利用式 (9.5.24) 与式 (9.5.25), 知
