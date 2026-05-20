$$\bigcap^ {n} B _ {\varepsilon} (x _ {i}) \supset M.$$

这样一个结构称为 M 的一个 $\varepsilon-$ 网. $^{1}$

证明 任取 $x_{1}$ . 如果 $B_{\varepsilon}(x_{1}) \supset M$ , 获证. 否则, 选 $x_{2} \in (B_{\varepsilon}(x_{1}))^{c}$ , 构造 $B_{\varepsilon}(x_{2})$ . 依此类推, 在第 $i$ 步选 $x_{i} \in \left(\bigcup_{k=1}^{i-1} B_{\varepsilon}(x_{k})\right)^{c}$ . 如果在第 $i$ 步我们找不到这样的 $x_{i}$ 则结论获证. 否则, 我们可找到一个序列 $\{x_{i}\}$ , 有 $d(x_{i}, x_{j}) \geqslant \varepsilon$ . 这个序列不存在收敛子列, 导致矛盾.

引理3.3.2 设 $M$ 为一列紧距离空间，且 $\{U_{\lambda} \mid \lambda \in \Lambda\}$ 为一开覆盖。那么就存在一个数 $\mu > 0$ ，称为Lebesgue数，使得对任意 $x \in M$ ，存在 $U_{\lambda}$ ，使得 $B_{\mu}(x) \in U_{\lambda}$ 。

证明 对每个 $x \in M$ 选择最大的 $\mu_x > 0$ , 使得 $B_{\mu_x}(x) \subset U_{\lambda_x}$ . 只要能证明

$$\inf _ {x \in M} \mu_ {x} \stackrel {\text { def }} {=} \mu > 0,$$

就够了. 设 $x_{n}$ 为一序列使 $\mu_{x_n} \to \mu$ . 由列紧性, 存在子列 $x_{n_i} \to x_0$ . 那么对这个 $x_0$ 存在 $\mu_0$ 及 $U_{\lambda_0}$ , 使得 $B_{\mu_0}(x_0) \in U_{\lambda_0}$ . 回忆列紧性, 则存在 $N > 0$ 使得 $i > N$ 时, $x_{n_i} \in B_{\mu_0/2}(x_0)$ . 那么 $B_{\mu_0/2}(x_{n_i}) \subset U_{\lambda_0}$ , 这就意味着 $\mu_{n_i} \geqslant \mu_0/2$ . 但是 $\mu_{n_i} \to \mu$ . 因此 $\mu \geqslant \mu_0/2 > 0$ .

定理3.3.4 设 $M$ 为一列紧距离空间，那么 $M$ 是紧空间.

证明 设 $\{U_{\lambda} \mid \lambda \in A\}$ 为一开覆盖. 引理 3.3.2 说存在一个 $\mu$ 使得 $B_{\mu}(x) \subset U_{\lambda_x}$ . 显见 $\{B_{\mu}(x) \mid x \in M\}$ 是 M 的一个开覆盖. 由引理 3.3.1, 存在 $x_1, \cdots, x_n$ 使得 $\bigcup_{i=1}^{n} B_{\mu}(x_i) \supset M$ . 于是可得到 M 的一个有限子覆盖

$$\{U _ {\lambda_ {x _ {i}}} \mid i = 1, 2, \dots , n \}.$$

下面这个命题虽简单却有用。它说一个紧集的连续象也是紧的。准确地说，

命题3.3.4 设 $f: M \to N$ 为一连续映射，且 $V \subset M$ 为一紧集。则 $f(V)$ 也是一个紧集。

证明 设 $\{U_{\lambda} \mid \lambda \in \Lambda\}$ 为 $f(V)$ 的一个开覆盖. 那么 $\{f^{-1}(U_{\lambda}) \mid \lambda \in \Lambda\}$ 是 $V$ 的一个开覆盖. 因为 $V$ 是紧的, 则有一 $V$ 的子覆盖 $\{f^{-1}(U_{\lambda_i}), i = 1, \cdots, k\}$ . 于是有

$$\bigcup_ {i = 1} ^ {k} U _ {\lambda_ {i}} \supset V.$$

我们知道对一连续映射，一个开集（或闭集）的逆象也是开的（闭的）。但一个紧集的逆象却未必是紧的。例如， $f(x)=\sin(x)$ 是 $R\to R$ 是连续的。 $I=[-1,1]$ 是紧的，但 $f^{-1}(I)=R$ 却不紧。

定义3.3.19 设 $f: M \to N$ 为一连续映射。如果对每一个紧集 $V \subset M$ ，其逆象 $f^{-1}(V)$ 也是紧的，则 $f$ 称为一个恰当映射。

最后我们考虑商空间.

定义3.3.20 设 $S$ 为一集合， $\sim$ 为 $S$ 上两个元之间的一个关系。 $\sim$ 称为一个等价关系，如果

ER1: $x \sim x$ ;

ER2: 如果 $x \sim y$ , 则 $y \sim x$ ;

ER3: 如果 $x \sim y$ 且 $y \sim z$ , 则 $x \sim z$ .

定义3.3.21 设 $M$ 为一拓扑空间， $\sim$ 为 $M$ 上的一个等价关系.

(1) 对任一 $x \in M$ ，一个等价类，记作 $[x]$ ，定义为

$$[ x ] = \{y \in M \mid y \sim x \};$$

(2) 等价类集合记作 $M / \sim$ , 映射 $\pi: x \to [x]$ 称为自然投影;
