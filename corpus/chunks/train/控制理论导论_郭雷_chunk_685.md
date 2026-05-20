$$I _ {\Omega_ {k} ^ {c}} E [ \alpha_ {k + 1} | \mathcal {F} _ {k h} ] \geqslant I _ {\Omega_ {k} ^ {c}} \left\{1 - \left(1 - \frac {\lambda_ {k}}{2 (1 + h)}\right) \right\} = \frac {\lambda_ {k}}{2 (1 + h)} I _ {\Omega_ {k} ^ {c}}.$$

从而式 (9.3.22) 在 $\Omega_k^c$ 上也成立，证毕.

定理9.3.5 设 $\{F_k, \mathcal{F}_k\}$ 是适应矩阵列， $0 \leqslant F_k \leqslant I$ 。若存在 $h > 0$ 使得由式(9.3.15)所定义的 $\lambda_k$ 满足 $\{\lambda_k\} \in S^0$ 则对任何 $p \geqslant 1$ 。

$$\{F _ {k} \} \in S _ {p}.$$

证明 由于 $0 \leqslant F_{k} \leqslant I$ ，我们只需考虑 $p = 2$ 的情形。对任何 $n > m + h$ ，定义

$$k _ {0} = \min \{k: m \leqslant k h + 1 \leqslant n \}, \quad k _ {1} = \max \{k: m \leqslant k h + 1 \leqslant n \}.$$

易见

$$(k _ {1} + 1) h + 1 > n, \quad (k _ {0} - 1) h + 1 < m,$$

且

$$E \| \Phi (n, m) \| ^ {2} \leqslant E \| \Phi (k _ {1} h + 1, k _ {0} h + 1) \| ^ {2},$$

其中 $\Phi(n, m)$ 如引理 9.3.1 所定义。因此为证 $\{F_i\} \in S_2$ ，只需证明存在不依赖于 $k_0$ 及 $k_1$ 的常数 $C$ 及 $\lambda \in (0, 1)$ 使 $\forall k_1 > k_0$ 有

$$E \| \Phi (k _ {1} h + 1, k _ {0} h + 1) \| ^ {2} \leqslant C \lambda^ {2 \alpha h (k _ {1} - k _ {0} + 1)}. \tag {9.3.23}$$

下面考虑方程 (9.3.20), 易见

$$x _ {k _ {1}} = \Phi (k _ {1} h + 1, k _ {0} h + 1) x _ {k _ {0}}.$$

因此，为证式(9.3.22)只需证明对任何满足 $\| x_{k_0}\| = 1$ 确定性向量 $x_{p_0}$ 有

$$E \| x _ {k _ {1}} \| ^ {2} \leqslant C \lambda^ {2 \alpha h (k _ {1} - k _ {0})}, \tag {9.3.24}$$

其中常数 $C$ 不依赖于 $k_{0}$ 及 $k_{1}$ .

由于 $\lambda_{k} \in \left[0, \frac{h}{1 + h}\right]$ 且 $\lambda_{k} \in S^{0}$ , 利用命题9.3.2知

$$\left\{\frac {\lambda_ {k}}{2 (1 + h)} \right\} \in S ^ {0}.$$

据此利用引理9.3.2, 类似于命题9.3.1的证明知

$$E \prod_ {k = k _ {0} + 1} ^ {k _ {1}} (1 - \alpha_ {k}) \leqslant C \lambda^ {2 \alpha h (k _ {1} - k _ {0})},$$

其中 $C$ 是不依赖于 $k_{0}, k_{1}$ 及 $x_{k_{0}}$ 的常数。由此利用式 (9.3.21) 易见式 (9.3.24) 成立。从而定理证毕。

定理9.3.6 设 $\{F_i, \mathcal{F}_i\}$ 是适应矩阵序列， $0 \leqslant F_i \leqslant I$ ，若 $\{F_i\} \in S_1$ ，则存在整数 $h > 0$ 使

$$\inf _ {m} \lambda_ {\min} \left\{\sum_ {i = m h + 1} ^ {(m + 1) h} E F _ {i} \right\} > 0.$$

证明 根据假设，存在常数 $M > 0, \lambda \in (0,1)$ 及适当大的整数 $h > 0$ 使

$$E \left\| \prod_ {i = m h + 1} ^ {(m + 1) h} (I - F _ {i}) \right\| \leqslant M \lambda^ {h} < \frac {1}{2}, \quad \forall m \geqslant 0. \tag {9.3.25}$$

设 $\rho_{m}$ 是矩阵 $E\left[\sum_{i - mh + 1}^{(m + 1)h}F_{i}\right]$ 的最小特征值，且 $x_{m}$ 是相应的单位特征向量。于是我们有

$$\rho_ {m} = E \left[ \sum_ {i = m h + 1} ^ {(m + 1) h} x _ {m} ^ {\mathrm{T}} F _ {i} x _ {m} \right].$$

因此对任何整数 $i_{j} \in [mh + 1, (m + 1)h]$ , $j = 1, \cdots, k$ , $k \leqslant h$ .
