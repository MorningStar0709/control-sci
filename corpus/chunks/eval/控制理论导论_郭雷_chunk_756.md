$$B ^ {*} R (\overline {{{\lambda}}}; A ^ {*}) x ^ {*} = 0, \quad \forall \lambda \in \rho (A).$$

于是从假设式 (10.2.30) 得出 $x^{*} = 0$ ，即式 (10.2.33) 成立。反过来，设式 (10.2.33) 成立，并且 $B^{*}R(\overline{\lambda}; A^{*})x^{*} = 0, \forall \lambda \in \rho(A)$ ，则从式 (10.2.31) 我们有

$$B ^ {*} P _ {k} ^ {*} x ^ {*} = 0, \quad \forall k \geqslant 1,$$

因此从假设式 (10.2.33) 得到 $x^{*} = 0$ ，即式 (10.2.30) 成立。证毕。

例10.2.4 设 $X$ 是一自反Banach空间， $A$ 是 $X$ 上 $C_0$ 半群 $T(t)$ 的生成算子。假定 $A$ 是标量型离散谱算子， $\sigma(A) = \{\lambda_k | k \geqslant 1\}$ ， $P_k$ 是对应于本征值 $\lambda_k$ 的投影算子，并且 $\dim \mathcal{R}(P_k) = r_k, \forall k \geqslant 1$ 。设 $\varphi_{nk}$ 是 $A$ 的对应于 $\lambda_n$ 的本征元

$$A \varphi_ {n k} = \lambda_ {n} \varphi_ {n k}, \quad 1 \leqslant k \leqslant r _ {n},$$

并设 $\psi_{nk}$ 是 $A^{*}$ 的对应于本征值 $\overline{\lambda}_n$ 的本征元。由此不失一般性，我们可以假定 $\{\varphi_{nk} \mid 1 \leqslant k \leqslant r_n, n \geqslant 1\}$ 和 $\{\psi_{nk} \mid 1 \leqslant k \leqslant r_n, n \geqslant 1\}$ 构成 $X$ 和 $X^{*}$ 的一双直交基

$$\left\langle \varphi_ {n k}, \psi_ {m j} \right\rangle = \delta_ {m n} \delta_ {j k}, 1 \leqslant k \leqslant r _ {n}, 1 \leqslant j \leqslant r _ {m}, n, m \geqslant 1.$$

于是

$$P _ {n} x = \sum_ {j = 1} ^ {r _ {n}} \langle x, \psi_ {n j} \rangle \varphi_ {n j}, \quad x \in X,P _ {n} ^ {*} x ^ {*} = \sum_ {j = 1} ^ {r _ {n}} \left\langle x ^ {*}, \varphi_ {n j} \right\rangle \psi_ {n j}, \quad x ^ {*} \in X ^ {*},$$

从而

$$B ^ {*} P _ {n} ^ {*} x ^ {*} = \sum_ {j = 1} ^ {r _ {n}} \left\langle x ^ {*}, \varphi_ {n j} \right\rangle B ^ {*} \psi_ {n j}, \quad x ^ {*} \in X ^ {*}, n \geqslant 1. \tag {10.2.36}$$

由此可见 $(A, B)$ 完全近似能控当且仅当对于所有 $n \geqslant 1$ , $\{B^{*}\psi_{nj} \mid 1 \leqslant j \leqslant r_{n}\}$ 是 $U^{*}$ 中的线性无关序列.

特别当对于 $n \geqslant 1, r_n = 1$ 时， $(A, B)$ 完全近似能控当且仅当 $B^* \psi_n \neq 0, \forall n \geqslant 1$ .

现在我们考虑控制输入是有穷维的情形，即

$$B u = \sum_ {j = 1} ^ {m} u _ {j} b _ {j}, \quad \forall [ u _ {1}, \dots , u _ {m} ] ^ {\mathrm{T}} \in \mathbb {R} ^ {m},$$

其中 $b_{1},\cdots,b_{m}$ 是 X 中给定元. 于是

$$B ^ {*} x ^ {*} = \left[ \langle x ^ {*}, b _ {1} \rangle , \dots , \langle x ^ {*}, b _ {m} \rangle \right] ^ {\mathbf {T}}, \quad \forall x ^ {*} \in X ^ {*},B ^ {*} \psi_ {n j} = [ \langle \psi_ {n j}, b _ {1} \rangle , \dots , \langle \psi_ {n j}, b _ {m} \rangle ] ^ {\mathrm{T}}.$$

容易验证 $B^{*}\psi_{n1},\cdots,B^{*}\psi_{nr_{n}}$ 线性无关当且仅当
