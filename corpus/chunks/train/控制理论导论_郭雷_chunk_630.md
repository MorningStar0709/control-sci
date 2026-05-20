$\mathcal{F}_0$ 与 $I_{i}$ 的结构可描述如下：

引理8.4.8 $\mathcal{F}_0$ 和 $I_{i}$ 可表示为

$$\mathcal {F} _ {0} = \operatorname{span} \left\{\mathrm{ad} _ {f _ {1}} \dots \mathrm{ad} _ {f _ {s}} X \mid s \geqslant 0, f _ {i} \in F, X \in F _ {0} \right\}, \tag {8.4.46}I _ {i} = \operatorname{span} \left\{\mathrm{ad} _ {f _ {1}} \dots \mathrm{ad} _ {f _ {s}} X \mid s \geqslant 0, f _ {i} \in F, X \in F _ {i} \right\}, \quad i = 1, \dots , k. \tag {8.4.47}$$

证明 首先我们证明 $\mathcal{F}'$ 有结构

$$\mathcal {F} ^ {\prime} = \operatorname{span} \left\{\mathrm{ad} _ {f _ {1}} \dots \mathrm{ad} _ {f _ {s}} f _ {s + 1} \mid s \geqslant 1, f _ {i} \in F \right\}. \tag {8.4.48}$$

显然式 (8.4.48) 的右边包含于式 (8.4.48) 的左边。另外，式 (8.4.48) 的右边是包含 $\{[X,Y] \mid X, Y \in F\}$ 的 Lie 代数，故它包含由 $\{[X,Y] \mid X, Y \in F\}$ 生成的 Lie 代数，这就是式 (8.4.48) 的右边。

现在我们只要证明式 (8.4.46) 即可．记式 (8.4.46) 的右边为 $\mathcal{F}_1$

由于 $\mathcal{F}_0$ 是一个理想，且 $\mathcal{F}_0 \supset F_0$ ，故显然 $\mathcal{F}_1 \subset \mathcal{F}_0$ 。现在任选一个 $X \in \mathcal{F}_0$ ，它能表示为

$$X = \sum_ {i = 1} ^ {p} \lambda_ {i} X _ {i} + Y, \quad X _ {i} \in \mathcal {F}, Y \in \mathcal {F} ^ {\prime}.$$

由于 $\sum_{i=1}^{p} \lambda_i = 0$ , 故

$$\sum_ {i = 1} ^ {p} \lambda_ {i} X _ {i} = \sum_ {i = 1} ^ {p - 1} \lambda_ {i} (X _ {i} - X _ {p}) \in \mathcal {F} _ {1}.$$

于是只要证 $Y \in \mathcal{F}_1$ . 利用式 (8.4.48), 不失一般性可假设

$$Y = \mathrm{ad} _ {f _ {1}} \dots \mathrm{ad} _ {f _ {s}} f _ {s + 1}, \quad s \geqslant 1.$$

因此， $Y = \mathrm{ad}_{f_1}\dots \mathrm{ad}_{f_s}(f_{s + 1} - f_s)\in \mathcal{F}_1.$

引理 8.4.9 设 $F_{0}$ 在 $x_{0}$ 非奇异，且 $I_{1}, \cdots, I_{k}$ 作为在 $x_{0}$ 的邻域的分布是线性无关的，则诸 $I_{i}$ 在 $x_{0}$ 同时可积.

证明 首先证明 $I_{i}$ 在 $x_0$ 非奇异.

显然 $F_{0}$ 的一个向量场可表示为 $F_{1}, \cdots, F_{k}$ 的线性组合. 事实上

$$
\begin{array}{l} f (x, u _ {1}) - f (x, u _ {2}) = \left(f (x, u _ {1} ^ {1}, \dots , u _ {1} ^ {k}) - f (x, u _ {2} ^ {1}, u _ {1} ^ {2}, \dots , u _ {1} ^ {k})\right) \\ + \left(f (x, u _ {2} ^ {1}, u _ {1} ^ {2}, \dots , u _ {1} ^ {k}) - f (x, u _ {2} ^ {1}, u _ {2} ^ {2}, \dots , u _ {1} ^ {k})\right) \\ + \dots \\ + \left(f (x, u _ {2} ^ {1}, u _ {2} ^ {2}, \dots , u _ {2} ^ {k - 1}, u _ {1} ^ {k}) - f (x, u _ {2} ^ {1}, u _ {2} ^ {2}, \dots , u _ {2} ^ {k})\right). \\ \end{array}
$$

根据式 (8.4.46) 及式 (8.4.47) 有

$$\mathcal {F} _ {0} \subset I _ {1} + \dots + I _ {k}.$$

再由式 (8.4.45), 我们有

$$\mathcal {F} _ {0} = I _ {1} + \dots + I _ {k}. \tag {8.4.49}$$

设 $\mathrm{rank}(\mathcal{F}_{0}(x_{0})) = s$ 和 $\mathrm{rank}(I_{i}) = s_{i}, i = 1, \cdots, k.$ 利用式 (8.4.49) 和诸 $I_{i}$ 线性无关这一事实，可得

$$\sum_ {i = 1} ^ {k} s _ {i} = s.$$
