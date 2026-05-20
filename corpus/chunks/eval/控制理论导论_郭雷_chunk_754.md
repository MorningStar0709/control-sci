这证明了式 (10.2.18) 也是系统 (10.2.16) 近似能控的充分必要条件.

对于某些系统来说，有穷时间区间上的近似能控性概念仍太严格。为此我们引入另一种更弱的能控性概念——完全近似能控性。

设 $t > 0, G(t)$ 由式 (10.2.3) 给出. 定义

$$C (A, B) = \overline {{{{\bigcup_ {t \geqslant 0} \mathcal {R} (G (t))}}}},$$

$C(A,B)$ 叫做系统(10.2.2)或 $(A,B)$ 的能控性子空间. 当一集合 $M$ 包含在 $C(A,B)$ 中时， $M$ 就叫做近似能控集.

定义10.2.9 系统(10.2.2)或 $(A,B)$ 叫做完全近似能控的，是指 $C(A,B) = X$ ，即 $\forall x\in X$ 和 $\forall \varepsilon >0,$ 必存在 $t > 0$ 和 $u\in L^{p}(0,t;U),p\geqslant 1$ 使得

$$\left\| x - \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s \right\| < \varepsilon .$$

定理10.2.7 设 $X$ 和 $U$ 为自反Banach空间，那么 $(A, B)$ 完全近似能控当且仅当

$$x ^ {*} \in X ^ {*}, B ^ {*} T ^ {*} (t) x ^ {*} = 0, \forall t \geqslant 0 \Longrightarrow x ^ {*} = 0. \tag {10.2.23}$$

证明 取 $p > 1$ 并设 $\frac{1}{p} + \frac{1}{q} = 1$ , 那么 $L^p(0, t; U)$ 也是自反的, 并且 $L^p(0, t; U)^* = L^q(0, t; U^*)$ . 根据完全近似能控性的定义和 $X$ 的自反性, $(A, B)$ 完全近似能控当且

仅当

$$x ^ {*} \in X ^ {*}, \quad \langle G (t) u, x ^ {*} \rangle = 0, \forall t \geqslant 0, \forall u \in L ^ {p} (0, t; U) \Longrightarrow x ^ {*} = 0. \tag {10.2.24}$$

但

$$\langle G (t) u, x ^ {*} \rangle = 0, \forall u \in L ^ {p} (0, t; U) \Longleftrightarrow G ^ {*} (t) x ^ {*} = 0,$$

因此式 (10.2.24) 等价于

$$x ^ {*} \in X ^ {*}, G ^ {*} (t) x ^ {*} = 0, \forall t \geqslant 0 \Longrightarrow x ^ {*} = 0. \tag {10.2.25}$$

注意 $G^{*}(t)x^{*}$ 作为 $L^q (0,t;U^*)$ 中的元表示成

$$G ^ {*} (t) x ^ {*} = B ^ {*} T ^ {*} (t - s) x ^ {*}, \quad 0 \leqslant s \leqslant t.$$

于是式 (10.2.25) 正是式 (10.2.23). 证毕.

对于有穷维系统，近似能控性和精确能控性是等价的，并且可以通过矩阵 $A$ 和 $B$ 的秩条件来检验： $(A, B)$ 完全能控当且仅当

$$\operatorname{rank} [ B, A B, \dots , A ^ {n - 1} B ] = n, \tag {10.2.26}$$

其中 $n$ 是 $X$ 的维数。对于很多无穷维系统，一般来说我们仅知道系统算子 $A$ 而不是由其生成的 $C_0$ 半群。因此给出直接由 $A$ 和 $B$ 表达的能控性判据会更有实际意义。

定理10.2.8 设 $X$ 和 $U$ 是两个自反的Banach空间，那么 $(A,B)$ 完全近似能控当且仅当

$$x ^ {*} \in X ^ {*}, B ^ {*} R (\lambda ; A) ^ {*} x ^ {*} = 0, \forall \operatorname{Re} \lambda > \omega \Longrightarrow x ^ {*} = 0, \tag {10.2.27}$$

其中 $\omega$ 是一常数满足 $\omega > \omega(A)$ .

证明 依据定理 10.2.7, 我们只需证明式 (10.2.23) 和式 (10.2.27) 之间的等价性. 首先假定式 (10.2.27) 成立. 注意

$$R (\lambda ; A) ^ {*} x ^ {*} = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T ^ {*} (t) x ^ {*} \mathrm{d} t, \quad \forall x ^ {*} \in X ^ {*}, \forall \operatorname{Re} \lambda > \omega , \tag {10.2.28}$$

于是当 $B^{*}T^{*}(t)x^{*} = 0,\forall t\geqslant 0$ 时，从式(10.2.28)得出

$$B ^ {*} R (\lambda ; A) ^ {*} x ^ {*} = 0 \quad \forall \operatorname{Re} \lambda > \omega ,$$

从而 $x^{*} = 0$ ，即式(10.2.23)成立.

现在设式 (10.2.23) 成立. 从式 (10.2.28) 我们有
