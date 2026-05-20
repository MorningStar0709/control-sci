$$\Gamma (\mathrm{j} \omega) = I - G ^ {\mathrm{T}} (- \mathrm{j} \omega) G (\mathrm{j} \omega) > 0, \quad \forall \omega \in \mathbb {R},$$

故， $\| G(\cdot)\|_{\infty} < 1$ 成立.

(1) $\Longrightarrow$ (4). 设 $\| G(s)\|_{\infty} = \gamma < 1$ , 且 $\| (sI - A)^{-1}B\|_{\infty} = \rho$ , 则存在充分小正数 $\varepsilon_1 > 0$ 使得

$$(1 - \varepsilon_ {1}) I > \gamma^ {2} I \geqslant G ^ {\mathrm{T}} (- \mathrm{j} \omega) G (\mathrm{j} \omega), \quad \forall \omega \in \mathbb {R}. \tag {6.2.15}$$

再令 $\varepsilon > 0$ 为小于 $\varepsilon_1 / \rho^2$ 的充分小正数，则

$$\varepsilon_ {1} I \geqslant \varepsilon \rho^ {2} I \geqslant \varepsilon B ^ {\mathrm{T}} (- \mathrm{j} \omega I - A ^ {\mathrm{T}}) ^ {- 1} (\mathrm{j} \omega I - A) ^ {- 1} B, \quad \forall \omega \in \mathbb {R}. \tag {6.2.16}$$

所以由式 (6.2.15) 得

$$I > \varepsilon_ {1} I + G ^ {\mathbf {T}} (- \mathrm{j} \omega) G (\mathrm{j} \omega), \quad \forall \omega \in \mathbb {R},$$

并且由式 (6.2.16) 进一步得

$$I > B ^ {\mathrm{T}} (- \mathrm{j} \omega - A ^ {\mathrm{T}}) ^ {- 1} C _ {e} ^ {\mathrm{T}} C _ {e} (\mathrm{j} \omega - A) ^ {- 1} B, \quad \forall \omega \in \mathbb {R},$$

其中 $C_e^{\mathrm{T}} = [C^\mathrm{T}\sqrt{\varepsilon} I]$ . 上式表明

$$\left\| C _ {e} (s I - A) ^ {- 1} B \right\| _ {\infty} < 1.$$

因此根据定理6.2.1可知Riccati方程

$$A ^ {T} Z + Z A + Z B B ^ {T} Z + C ^ {T} C + \varepsilon I = 0$$

有半正定解 $Z \geqslant 0$ . 令 $S = ZBB^{\mathrm{T}}Z + C^{\mathrm{T}}C + \varepsilon I > 0$ , 则上式可以表示为

$$A ^ {T} Z + Z A = - S.$$

于是根据 $A$ 的稳定性以及 Lyapunov 稳定性理论可知 $Z$ 是正定阵.

(4) $\Longrightarrow$ (2). 令 $X = Z > 0$ , 则命题显然成立.

(2) $\Longleftrightarrow$ (3). 定义分块矩阵 $S$ 如下:

$$
S = \left[ \begin{array}{l l} S _ {1 1} & S _ {1 2} \\ S _ {1 2} ^ {\mathrm{T}} & S _ {2 2} \end{array} \right].
$$

熟知， $S > 0$ 当且仅当

$$S _ {2 2} > 0, \quad S _ {1 1} - S _ {1 2} S _ {2 2} ^ {- 1} S _ {1 2} ^ {\mathrm{T}} > 0.$$

因此矩阵不等式 (6.2.13) 成立当且仅当

$$A Y + Y A ^ {\mathrm{T}} + B B ^ {\mathrm{T}} + Y C ^ {\mathrm{T}} C Y < 0. \tag {6.2.17}$$

令 $X = Y^{-1} > 0$ , 则 Riccati 不等式 (6.2.17) 与不等式 (6.2.12) 等价。从而命题 (2) 和 (3) 的等价性得证。

上述讨论的结果都是针对严格真有理函数阵的，即 $G(s)$ 的状态空间实现的 $D$ 阵为零．如果

$$G (s) = D + C (s I - A) ^ {- 1} B, \qquad D \neq 0, \tag {6.2.18}$$

显然 $\| G(\cdot)\|_{\infty} < 1$ 的一个必要条件是 $R^2 = I - D^{\mathrm{T}}D > 0$ 。实际上，可以证明 $\| G(\cdot)\|_{\infty} < 1$ 等价于

$$\left\| C _ {d} (s I - A _ {d}) ^ {- 1} B _ {d} \right\| _ {\infty} < 1,$$

其中 $A_{d} = A + BR^{-2}D^{\mathrm{T}}C, B_{d} = BR^{-1}, C_{d} = (I + DR^{-2}D^{\mathrm{T}})C$ 。因此，定理6.2.1以及定理6.2.2的结果均可以推广到 $D \neq 0$ 的情况。有关详细结果读者可参阅文献[7], [15].
