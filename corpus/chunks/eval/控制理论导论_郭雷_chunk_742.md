其中 $x$ 为取自 $[x]$ 中的任意元. 容易看出对于任意 $[x] \neq 0$ , 有 $\| [x] \| > 0$ . 因此 $\| \cdot \|_2$ 是 $X_1$ 上的一个范数, 并且 $\| [x] \|_2 \leqslant \| [x] \|_1, \forall [x] \in X_1$ . 容易验证 $T_1(t)$ 在 $X_1$ 中相对于范数 $\| \cdot \|_2$ 是等距的, 即 $\| T_1(t)[x] \|_2 = \| [x] \|_2, \forall [x] \in X_1$ . 我们用 $X_2$ 表示 $X_1$ 相对于范数 $\| \cdot \|_2$ 的完备化空间, 并用 $T_2(t)$ 表示 $T_1(t)$ 在 $X_2$ 上的等距延拓. 设 $A_2$ 是 $T_2(t)$ 的生成算子.

引理10.1.5 采用上述记号，则 $T_{2}(t)$ 的生成算子 $A_{2}$ 是 $A_{1}$ 的闭延拓，即 $A_{2}$ 的定义域 $\mathcal{D}(A_2)$ 为

$$\mathcal {D} (A _ {2}) = \big \{\widetilde {x} \big | \exists [ x _ {n} ] \in \mathcal {D} (A _ {1}), \| [ x _ {n} ] - \widetilde {x} \| _ {2} \to 0, \{A _ {1} [ x _ {n} ] \} \text {在} X _ {2} \text {中收敛} \big \},$$

并且对于 $\widetilde{x} \in \mathcal{D}(A_2)$ , 在 $X_2$ 中有 $A_2\widetilde{x} = \lim_{n \to \infty} A_1[x_n]$ , 其中 $[x_n] \in \mathcal{D}(A_1)$ 使得 $\| [x_n] - \widetilde{x}\|_2 \to 0$ , 并且 $\{A_1[x_n]\}$ 是 $X_2$ 中的 Cauchy 列.

证明是直接的，留作练习.

现在我们能够证明有关 $C_0$ 半群强稳定性的主要结果了。在下面的推导中，为简单起见， $X_1$ 中的元仍写作 $x, y$ 等。

定理 10.1.11 设 $T(t)$ 是 Banach 空间 X 上一致有界 $C_{0}$ 半群，其生成算子为 A。如果 $\operatorname{Re}\lambda < 0, \forall\lambda \in \sigma(A)$ ，则 $T(t)$ 是强稳定的。

证明 根据 $X_0$ 的定义, 我们只需证明 $X_1 = \{0\}$ . 事实上, 若不然, 则 $X_2$ 是一个非平凡的 Banach 空间, 并且 $T_2(t)$ 是 $X_2$ 上的等距 $C_0$ 半群. 于是根据定理 5.3.28, 我们有 $\sigma(A_2) \cap \mathrm{iR} \neq \emptyset$ . 今取 $\mathrm{i}\omega \in \sigma(A_2) \cap \mathrm{iR}$ , 我们要证 $\mathrm{i}\omega \in \sigma(A)$ . 如果 $\mathrm{i}\omega \in \rho(A)$ , 则依据引理 10.1.4, $\mathrm{i}\omega \in \rho(A_1)$ . 对于任意 $\widetilde{x} \in X_2$ , 存在一序列 $\{[x_n]\} \subset X_1$ 使得当 $n \to \infty$ 时有 $\| [x_n] - \widetilde{x} \|_2 \to 0$ . 显然, $\{R(\mathrm{i}\omega; A_1)[x_n]\}$ 是 $X_1$ 中一 Cauchy 列, 故存在 $\widetilde{y} \in X_2$ 使得当 $n \to \infty$ 时, 在 $X_2$ 中有 $[y_n] = R(\mathrm{i}\omega; A_1)[x_n] \to \widetilde{y}$ . 注意 $\{A_1[y_n]\}$ 也是 $X_2$ 中的 Cauchy 列并且利用引理 10.1.4, 我们得到

$$A _ {2} \widetilde {y} = \lim _ {n \rightarrow \infty} A _ {1} [ y _ {n} ] = - \widetilde {x} + \mathrm{i} \omega \widetilde {y},$$

即 $(\mathrm{i}\omega - A_2)\widetilde{y} = \widetilde{x}$ , 从而 $\mathcal{R}(\mathrm{i}\omega I - A_2) = X_2$ . 再次利用引理10.1.4, 我们有
