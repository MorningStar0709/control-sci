# C. 4 证明引理 4.3

定义 $\psi (s)$ 为

$$\psi (s) = \inf _ {s \leqslant \| x \| \leqslant r} V (x), \quad 0 \leqslant s \leqslant r$$

函数 $\psi (\cdot)$ 是连续正定递增的，且当 $0\leqslant \| x\| \leqslant r$ 时，有 $V(x)\geqslant \psi (\| x\|)$ ，但 $\psi (\cdot)$ 不必严格递增。设 $\alpha_{1}(s)$ 是 $\mathcal{K}$ 类函数，满足 $\alpha_{1}(s)\leqslant k\psi (s),0 < k < 1$ ，则

$$V (x) \geqslant \psi (\| x \|) \geqslant \alpha_ {1} (\| x \|), \quad \| x \| \leqslant r$$

另一方面,定义 $\phi(s)$ 为

$$\phi (s) = \sup _ {\| x \| \leqslant s} V (x), \qquad 0 \leqslant s \leqslant r$$

函数 $\phi (\cdot)$ 是连续正定递增的（不必严格递增），且当 $V(x)\geqslant \phi (\| x\|)$ 时，有 $\| x\| \leqslant r$ 。设 $\alpha_{2}(s)$ 是K类函数，满足 $\alpha_{2}(s)\geqslant k\phi (s),k > 1$ ，则

$$V (x) \leqslant \phi (\| x \|) \leqslant \alpha_ {2} (\| x \|), \quad \| x \| \leqslant r$$

如果 $D = R^n$ 并且 $V(x)$ 是径向无界的，则 $\psi (s)$ 和 $\phi (s)$ 的定义变为

$$\psi (s) = \inf _ {\| x \| \geqslant s} V (x), \quad \phi (s) = \sup _ {\| x \| \leqslant s} V (x), \qquad s \geqslant 0$$

函数 $\psi$ 和 $\phi$ 都是连续正定递增的,且

$$\psi (\| x \|) \leqslant V (x) \leqslant \phi (\| x \|), \forall x \in R ^ {n}$$

函数 $\alpha_{1}$ 和 $\alpha_{2}$ 的选取同前，由于 $V(x)$ 是径向无界的，当 $s$ 趋于无穷时， $\psi(s)$ 和 $\phi(s)$ 趋于无穷，因此可选取 $\alpha_{1}$ 和 $\alpha_{2}$ 为 $\mathcal{K}_{\infty}$ 类函数。
