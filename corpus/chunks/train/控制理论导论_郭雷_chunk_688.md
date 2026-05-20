# 习题 9.3

9.3.1 利用定理 9.3.1 证明定理 9.3.2.

9.3.2 考虑方程 (9.3.1), 其中 $x_0 = 0$ . 设 $\{A_k, k \geqslant 0\}$ 是独立的随机矩阵序列且有 $\operatorname{det}[E(A_k A_k^{\mathsf{T}})] \neq 0$ . 定义集合

$$\mathcal {B} \stackrel {\mathrm{def}} {=} \{\xi : \xi = \{\xi_ {k} \} \text {是} L _ {2} \text {稳定且与} \{A _ {k} \} \text {独立} \}$$

证明：对任何 $\{\xi_k\} \in B, \{x_k\}$ 都是 $L_2$ 稳定的充分必要条件是 $\{I - A_k\} \in S_2$ ，其中 $S_2$ 由定义9.3.3给出.

9.3.3 考虑 Lyapunov 方程 (9.3.5). 假设

(i) 存在常数 $M > 0, c_{2} \geqslant c_{1} > 0$ 使

$$\| F _ {k} \| \leqslant M, \quad c _ {1} I < Q _ {k} \leqslant c _ {2} I, \forall k;$$

(ii) 存在常数 $h \geqslant 1$ 使对任何 $k$ , 都有

$$\left\| \prod_ {k + 1} ^ {k + h} \left(\prod_ {k + 1} ^ {k + h}\right) ^ {\mathbf {T}} \right\| \leqslant 1 - f _ {k + 1},$$

其中 $\prod_{k+1}^{k+h} \stackrel{\mathrm{def}}{=} (I - F_{k+h}) \cdots (I - F_{k+1}), 0 \leqslant f_{k+1} \leqslant f < 1.$

证明： $\{E[f_{k + 1}|\mathcal{F}_k]\} \in S^0\Rightarrow \{F_k\} \in S_p,$ 其中 $\mathcal{F}_k\stackrel {\mathrm{def}}{=} \sigma \{F_i,i\leqslant k\}$

9.3.4 设 $\{a_k, \mathcal{F}_k\}$ 是适应序列， $a_k \geqslant 1, \forall k \geqslant 0, Ea_0 < \infty$ 且

$$E \left[ a _ {k} \mid \mathcal {F} _ {k - 1} \right] \leqslant \alpha a _ {k - 1} + \beta , \quad \forall k \geqslant 1, \alpha \in (0, 1), \beta \in (0, \infty),$$

证明 $\left\{\frac{1}{a_k}\right\} \in S^0$ （提示：可参考文献[12].）

9.3.5 对怎样的随机序列 $\{F_i\}$ , 它是属于集合 $M_p$ 的？试举出至少三个不同的例子并加以证明.

9.3.6 证明定理 9.3.8 中的条件 1) 可换成下列条件：存在正常数 $\varepsilon, \delta, M$ 和 $K$ 使对任何 $n \geqslant i > 0$ 都有

$$E \exp \left\{\epsilon \sum_ {j = i + 1} ^ {n} \| F _ {j} \| ^ {1 + \delta} \right\} \leqslant M \exp \{K (n - i) \}.$$

9.3.7 设 $F_{k} = \phi_{k}\phi_{k}^{\mathrm{T}}$ 而 $\{\phi_k\}$ 有下列表达式：

$$\phi_ {k} = \sum_ {j = - \infty} ^ {\infty} A _ {j} \epsilon_ {k - j} + \xi_ {k}, \quad \sum_ {j = - \infty} ^ {\infty} \| A _ {j} \| < \infty ,$$

其中 $\{\xi_k\}$ 是有界确定性信号，而 $\{\varepsilon_k\}$ 是独立序列且存在 $\alpha > 0$ 使

$$\sup _ {k} E \left[ \exp \left(\alpha \| \epsilon_ {k} \| ^ {2}\right) \right] < \infty .$$

证明定理9.3.8的条件1)和2)都成立.

9.3.8 在题 9.3.7 中若假定 $\{\varepsilon_k\}$ 是 $\phi-$ 混合序列，且满足 $\sup_k E \| \varepsilon_k\|^4 < \infty$ 。在其他条件不变的情况下，证明 $\{F_k\} \in M_2$ 。
