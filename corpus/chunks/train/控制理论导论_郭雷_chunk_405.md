$$
\begin{array}{l} \operatorname{Re} \left\langle - A T (s) x, x ^ {*} \right\rangle = \lim _ {t \rightarrow s ^ {-}} \operatorname{Re} \left\langle \frac {T (2 s - t) x - T ^ {\prime} (s) x}{s - t}, x ^ {*} \right\rangle \\ = \lim _ {t \rightarrow s ^ {-}} \operatorname{Re} \frac {1}{s - t} \left[ \langle T (2 s - t) x, x ^ {*} \rangle - \| T (s) x \| ^ {2} \right] \\ \leqslant \lim _ {t \rightarrow s ^ {-}} \operatorname{Re} \frac {1}{s - t} \left[ \| T (2 s - t) x \| \| T (s) x \| - \| T (s) x \| ^ {2} \right] = 0, \\ \end{array}
$$

即 $\operatorname{Re}\langle AT(s)x, x^*\rangle \geqslant 0, \forall x^* \in F(T(s)x)$ . 对于任意 $s > 0$ , 取 $x_s^* \in F(T(s)x)$ , 我们有 $\operatorname{Re}\langle AT(s)x, x_s^*\rangle \geqslant 0$ . 但是 $\|x_s^*\| = \|T(s)x\| = \|x\|$ , 故存在正数列 $\{s_n\}$ 和元 $x_0^* \in X^*$ 使得 $s_n \to 0$ , 并且当 $n \to \infty$ 时 $x_{s_n}^* \rightharpoonup x_0^*$ . 然后在 $\operatorname{Re}\langle AT(s_n)x, x_{s_n}^*\rangle$ 中让 $n \to \infty$ 取极限, 得到 $\operatorname{Re}\langle Ax, x_0^*\rangle \geqslant 0$ . 容易验证 $x_0^* \in F(x)$ . 这表明 $\operatorname{Re}\langle Ax, x_0^*\rangle = 0$ , 从而 $A$ 是守恒的.

充分性. 假定 $A$ 是守恒的并且 $\mathcal{R}(I - A) = X$ . 根据定理5.3.7, $A$ 生成某个 $C_0$ 压缩半群 $T(t)$ . 于是当 $x \in \mathcal{D}(A)$ 时, $T(t)x$ 对于 $t \geqslant 0$ 是可微的. 根据定理5.3.1, 容易验证 $\|T(t)x\|$ 是绝对连续的, 从而 $\|T(t)x\|$ 对于几乎所有的 $t > 0$ 是可微的. 因此从引理5.3.12和 $A$ 的守恒性可知, 对于几乎所有的 $t > 0$ 和任意 $x^* \in F(T(t)x$ , 有

$$
\begin{array}{l} \| T (t) x \| \frac {\mathrm{d}}{\mathrm{d} t} \| T (t) x \| = \operatorname{Re} \langle A T (t) x, x ^ {*} \rangle \\ = \sup \left\{\operatorname{Re} \langle A T (t) x, y ^ {*} \rangle \mid y ^ {*} \in F (T ^ {\prime} (t) x) \right\} = 0. \\ \end{array}
$$

这表明对于任意 $x \in \mathcal{D}(A)$ , $\|T(t)x\|$ 与 $t \geqslant 0$ 无关, 从而 $\|T(t)x\| = \|x\|$ , $\forall x \in \mathcal{D}(A)$ , $\forall t \geqslant 0$ . 但是 $\mathcal{D}(A)$ 在 $X$ 中稠, 故 $\|T(t)x\| = \|x\|$ , $\forall x \in X$ , $\forall t \geqslant 0$ , 即 $T(t)$ 是等距的. 证毕.

定理5.3.25 设 $A$ 是 $X$ 中闭稠定线性算子，那么为了 $A$ 是一 $C_0$ 等距群 $T(t)$ 的生成算子，必须且只须 $A$ 是强守恒的，并且 $\mathcal{R}(I \pm A) = X$ .

证明 必要性. 如果 $T(t)$ 是 $C_0$ 等距群, 那么 $T(t)$ 和 $T(-t)$ 都是 $C_0$ 等距半群, 从而必要性从定理5.3.24得出.

充分性. 如果 $A$ 是强守恒的, 并且 $\mathcal{R}(I \pm A) = X$ , 则再次根据定理 5.3.24, $A$ 和 $-A$ 分别生成 $C_0$ 等距半群 $T(t)$ 和 $S(t)$ . 显然 $T(t)^{-1} = S(t)$ , $\forall t \geqslant 0$ , 从而若我们定义 $T(-t) = S(t)$ , $\forall t \geqslant 0$ , 则 $T(t)$ 对于所有 $t \in \mathbb{R}$ 是等距的. 证毕.
