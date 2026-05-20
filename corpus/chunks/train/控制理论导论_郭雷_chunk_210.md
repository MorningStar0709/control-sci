(1) $x \in \overline{A}$ , 当且仅当, 对 $x$ 的任何邻域 $N_x, N_x \cap A \neq \varnothing$ ;  
(2) $x \in \operatorname{int}(A)$ , 当且仅当, 存在一个 $x$ 的开邻域 $N_x, N_x \subset A$ ;  
(3) $x \in \operatorname{bd}(A)$ , 当且仅当, $x$ 的任何邻域 $N_x, N_x \cap A \neq \varnothing$ 且 $N_x \cap A^c \neq \varnothing$ .

证明 (1) 设 $x \in \overline{A}$ . 如果存在 $x$ 的一个邻域 $U$ 使得 $U \cap A = \varnothing$ , 不失一般性, 设 $U$ 是开集, 那么 $A \subset U^c$ . 但 $U^c$ 是闭集, 于是 $\overline{A} \subset U^c$ . 因此 $x \in U^c$ , 这与 $x \in U$ 矛盾.

反之，设 $x \notin \overline{A}$ ，那么 $x \in (\operatorname{cl}(A))^c$ ，因此后者是 $x$ 的一个开邻域。但显然， $(\operatorname{cl}(A))^c \cap \operatorname{cl}(A) = \varnothing$ 。

(2) 和 (3) 的证明类似，我们留给读者.

定义 3.3.8 设 M 为一个拓扑空间.

(1) $M$ 称为可分的，如果存在一个可数集 $A$ ，它在 $M$ 中稠；  
(2) $M$ 称为是第一纲的，如果它能表示成可数个无处稠的集合的并．否则，它称为是第二纲的.

定理 3.3.1(Baire 纲定理) 如果一个距离空间 $X \neq \varnothing$ 是完备的，则它是第二纲的.

证明 设

$$X = \bigcup_ {k = 1} ^ {\infty} M _ {k}.$$

我们只需证明至少有一个 $M_{k}$ 不是无处稠的即可．设所有的 $M_{k}$ 均无处稠．选

$$B _ {1} = B _ {\epsilon_ {1}} (p _ {1}) \subset \overline {{{M}}} _ {1} ^ {c},$$

这里 $\varepsilon_1 < 1$ . 构造 $C_1 = B_{\varepsilon_1 / 2}(p_1)$ . 因为 $M_2$ 是无处稠, $\overline{M}_2$ 不包含 $C_1$ , 我们可以定义一开球

$$B _ {2} = B _ {\varepsilon_ {2}} (p _ {2}) \subset \overline {{{M}}} _ {2} ^ {c} \cap C _ {1},$$

这里 $\varepsilon_2 < 2^{-1}\varepsilon_1$ 。再构造 $C_2 = B_{\varepsilon_2 / 2}(p_2)$

一般地说，因为 $M_{k + 1}$ 是无处稠的， $\overline{M}_{k + 1}$ 不包含 $C_k$ ，我们可以找到一个开球

$$B _ {k + 1} = B _ {\epsilon_ {k + 1}} (p _ {k + 1}) \subset (\overline {{{M}}} _ {k + 1}) ^ {c} \cap C _ {k},$$

这里 $\varepsilon_{k + 1} < 2^{-1}\varepsilon_k$ 构造 $C_{k + 1} = B_{\varepsilon_{k + 1} / 2}(p_{k + 1})$ 于是有

$$B _ {k + 1} \subset C _ {k} \subset B _ {k}.$$

因此

$$B _ {k + t} \subset C _ {k}, \quad t > 0,$$

并且对 $m > k$ 均有

$$d (p _ {k}, p _ {m}) < 2 ^ {- 1} \varepsilon_ {k},$$

这表明 $\{p_k\}$ 是一个Cauchy列．因为 $X$ 是完备的， $p_k \to p \in X (k \to \infty)$ . 因为

$$d (p _ {k}, p) \leqslant d (p _ {k}, p _ {m}) + d (p _ {m}, p) < 2 ^ {- 1} \varepsilon_ {k} + d (p _ {m}, p) < \varepsilon_ {k},$$

所以

$$p \in B _ {k} \subset (\overline {{{M}}} _ {k}) ^ {c}.$$

这说明 $p \notin M_k$ . 于是

$$p \not \in \bigcup_ {k = 1} ^ {\infty} M _ {k} = X,$$

显然这是一个矛盾.

定义3.3.9 (1) 一个拓扑空间 $(X, T)$ 称为 $T_0$ 空间，如果对任何两个点 $x, y \in X$ ，或者存在一个 $U_x \in T$ 使得 $x \in U_x$ 且 $y \notin U_x$ ，或者存在一个 $U_y \in T$ 使得 $y \in U_y$ 且 $x \notin U_y$ ;

(2) 一个拓扑空间 $(X, \mathcal{T})$ 称为 $T_{1}$ 空间，如果对任何两个点 $x, y \in X$ 存在两个开集 $U_{x} \in \mathcal{T}$ 及 $U_{y} \in \mathcal{T}$ ，使得 $x \in U_{x}$ 及 $y \notin U_{x}$ 并且 $y \in U_{y}$ 及 $x \notin U_{y}$ ;
