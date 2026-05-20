$$\sum_ {n = N _ {\mathrm{I}} + 1} ^ {\infty} \left\| \varphi_ {n} - \psi_ {n} \right\| ^ {2} < \infty ,$$

那么 $A$ 的广义本征元全体构成 $H$ 的一Riesz基.

证明 设 $\mathfrak{sp}(A)$ 表示 $A$ 的所有广义本征元张成的闭线性子空间，叫做 $A$ 的根子空间。当 $\mathfrak{sp}(A) = H$ 时，称 $A$ 的根子空间是完备的。对于 $\lambda \in \sigma(A)$ ，设 $P_{\lambda}$ 为对应于 $A$ 的本征值 $\lambda$ 的广义本征子空间的投影算子。于是我们有

$$\operatorname{sp} (A) = \overline {{\operatorname{span}}} \left\{\mathcal {R} \left(P _ {\lambda}\right) \mid \lambda \in \sigma (A) \right\}.$$

由于 $A$ 的伴随 $A^{*}$ 仍然是离散的，故 $\operatorname{sp}(A)$ 的直交补是

$$\sigma_ {\infty} (A ^ {*}) = \left\{x \in H \mid P _ {\lambda} x = 0, \forall \lambda \in \sigma (A ^ {*}) \right\}.$$

(1) 我们先证明对于一个闭稠定的离散线性算子 $A, \operatorname{sp}(A) = H$ 当且仅当 $\operatorname{sp}(A)$ 在 $H$ 中的余维数 $\operatorname{codim} \operatorname{sp}(A)$ 是有穷的。事实上，从上面的分析可知有如下直交分解：

$$H = \sigma_ {\infty} (A ^ {*}) \oplus \operatorname{sp} (A).$$

于是 $\operatorname{sp}(A) = H$ 当且仅当 $\sigma_{\infty}(A^{*}) = \{0\}$ . 但从文献 [13] 第 2295 页得知 $\sigma_{\infty}(A^{*})$ 只可能是零空间 $\{0\}$ 或无穷维子空间. 因此, 为了 $\operatorname{codim} \operatorname{sp}(A) < \infty$ , 必须且只须 $\sigma_{\infty}(A^{*}) = \{0\}$ , 即 $\operatorname{sp}(A) = H$ ;

(2) 从引理 10.4.3 可知存在 $N \geqslant N_1$ 使得 $\{\varphi_n \mid 1 \leqslant n \leqslant N\} \cup \{\psi_n \mid n > N\}$ 构成 $H$ 的 Riesz 基. 由此可见 $\{\psi_n \mid n > N\}$ 是 $\overline{\operatorname{span}}\{\psi_n \mid n > N\}$ 的 Riesz 基. 于是

$$H = \operatorname{span} \left\{\varphi_ {1}, \dots , \varphi_ {N} \right\} + \overline {{\operatorname{span}}} \left\{\psi_ {n} \mid n > N \right\},$$

其中 $\dot{+}$ 表示直和。从上式可见 $\overline{\operatorname{span}}\{\psi_n | n > N\}$ 的余维数是 $N$ 。但 $\overline{\operatorname{span}}\{\psi_n | n > N\} \subset \operatorname{sp}(A)$ ，故 $\operatorname{sp}(A)$ 的余维数不超过 $N$ 。从上面已经证明的 (1) 的结论可知 $\operatorname{sp}(A) = H$ ，即 $A$ 的根子空间是完备的；

(3) 由于 $\{\varphi_1, \cdots, \varphi_N\} \cup \{\psi_n | n > N\}$ 是 $H$ 的 Riesz 基，显然 $\{\psi_n | n > N\}$ 是 $\overline{\operatorname{span}}\{\psi_n | n > N\}$ 的 Riesz 基。现在设 $A$ 的除 $\{\psi_n | n > N\}$ 之外的所有广义本征元张成的线性子空间记作 $V$ 。我们有

$$\overline {{\operatorname{span}}} \left\{\psi_ {n} \mid n > N \right\} + V \subset H = \overline {{\operatorname{span}}} \left\{\psi_ {n} \mid n > N \right\} + \operatorname{span} \left\{\varphi_ {1}, \dots , \varphi_ {N} \right\}.$$
