推论 4.2.4 设 $\{x_{k}\}$ 为相互独立随机变量序列， $F_{k}=\sigma\{x_{1},\cdots,x_{k}\}$ . 若对于某个常数 c>0，下列三级数收敛， $\sum_{k=1}^{\infty}P(|x_{k}|>c)<\infty,\sum_{k=1}^{\infty}Ex_{k}I_{||x_{k}|\leqslant c]}<\infty,$

$$\sum_ {k = 1} ^ {\infty} \left\{E x _ {k} ^ {2} I _ {[ | x _ {k} | \leqslant c ]} - (E x _ {k} I _ {\{| x _ {k} | \leqslant c \}}) ^ {2} \right\} < \infty ,$$

则 $\xi_{n} \stackrel{\mathrm{def}}{=} \sum_{k=1}^{n} x_{k}$ a.s. 收敛.

这是定理4.2.10的直接推论。反之，可以证明，如果 $\xi_{n}$ a.s. 收敛，那么推论中所列的三个级数对任意 $c > 0$ 都收敛。换句话说，上述三个级数对某个 $c > 0$ 收敛是使 $\xi_{n}$ a.s. 收敛的充分必要条件。这是著名的Kolmogorov三级数准则。

定理4.2.11(周元燮）设 $\{x_{k},\mathcal{F}_{k}\}$ 为鞅差列，记

$$A = \left\{\sum_ {k = 1} ^ {\infty} E [ | x _ {k} | ^ {p} | \mathcal {F} _ {k - 1} ] < \infty \right\}, \quad p \in (0, 2 ].$$

鞅 $\xi_{n} \stackrel{\mathrm{def}}{=} \sum_{k=1}^{n} x_{k}$ 在 $A$ 上收敛.

证明 i) 先设 $p \in [1,2]$ . 利用三级数准则，只要证明 $A$ 包含在由定理 4.2.10 中定义的 $S$ 中，也就是要证在 $A$ 上，定理 4.2.10 中的三个级数收敛.

注意到

$$
\begin{array}{l} P \left(\left| x _ {k} \right| \geqslant c \mid \mathcal {F} _ {k - 1}\right) = E \left(I _ {\{| x _ {k} | \geqslant c \}} \mid \mathcal {F} _ {k - 1}\right) \\ \leqslant \frac {1}{c ^ {p}} E \left[ \left| x _ {k} \right| ^ {p} I _ {\{| x _ {k} | \geqslant c \}} \mid \mathcal {F} _ {k - 1} \right] \\ \leqslant \frac {1}{c ^ {p}} E [ | x _ {k} | ^ {p} | \mathcal {F} _ {k - 1} ], \\ \end{array}
$$

所以三级数中的第一个级数在 $A$ 上收敛.

注意到 $E(x_{k}|\mathcal{F}_{k - 1}) = 0$ ，就有

$$
\begin{array}{l} \frac {1}{c} \sum_ {k = 1} ^ {\infty} \left| E \left[ x _ {k} I _ {\{| x _ {k} | \leqslant c \}} \mid \mathcal {F} _ {k - 1} \right] \right| = \frac {1}{c} \sum_ {k = 1} ^ {\infty} \left| E \left[ x _ {k} I _ {\{| x _ {k} | > c \}} \mid \mathcal {F} _ {k - 1} \right] \right| \\ \leqslant \sum_ {k = 1} ^ {\infty} \left[ E \left[ \frac {| x _ {k} |}{c} I _ {\{| x _ {k} | > c \}} \mid \mathcal {F} _ {k - 1} \right] \right. \\ \leqslant \frac {1}{c ^ {p}} \sum_ {k = 1} ^ {\infty} E [ | x _ {k} | ^ {p} | \mathcal {F} _ {k - 1} ], \\ \end{array}
$$

所以三级数中的第二个级数在 $A$ 上也收敛.

最后，由于

$$\frac {1}{c ^ {2}} \sum_ {k = 1} ^ {\infty} E \left[ x _ {k} ^ {2} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1} \right] \leqslant \frac {1}{c ^ {p}} \sum_ {k = 1} ^ {\infty} E [ x _ {k} ^ {2} I _ {\{| x _ {k} | \geqslant c \}} | \mathcal {F} _ {k - 1} ],$$

同时用 Lyapunov 不等式

$$\left(E [ x _ {k} I _ {\{| | x _ {k} | \leqslant c ] \}} | \mathcal {F} _ {k - 1}\right) ^ {2} \leqslant E [ x _ {k} ^ {2} I _ {\{| | x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1} ],$$

所以三级数中的最后一个级数在 $A$ 上收敛．因此对 $p \in [1,2]$ ， $\xi_n$ 在 $A$ 上收敛；
