$$(P (t _ {f}) z) (t) = C S (t) z, \quad 0 \leqslant t \leqslant t _ {f}, z \in Z. \tag {10.2.10}$$

定义10.2.5 我们说系统(10.2.9)在 $[0, t_f]$ 上是初态能观测的，或简称 $(F, C)$ 在 $[0, t_f]$ 上是初态能观测的，是指算子 $P(t_f)$ 可逆，即

$$z \in Z, \quad C S (t) z = 0, \quad \forall 0 \leqslant t \leqslant t _ {f} \Longrightarrow z = 0.$$

定义10.2.6 我们说 $(F, C)$ 在 $[0, t_f]$ 上连续初态能观测，是指算子 $P(t_f)$ 具有有界逆，即存在 $\gamma > 0$ 使得

$$\gamma \| P (t _ {f}) z \| _ {L ^ {q} (0, t _ {f}; Y)} \geqslant \| z \|, \quad \forall z \in Z.$$

定义 10.2.7 我们说 $(F,C)$ 在 $[0,t_{f}]$ 上是末态能观测的，是指 $\mathcal{N}(P(t_{f}))\subset\mathcal{N}(S(t_{f}))$ ，即

$$z \in Z, \quad C S (t) z = 0, \quad \forall 0 \leqslant t \leqslant t _ {f} \Longrightarrow S (t _ {f}) z = 0.$$

定义10.2.8 我们说 $(F, C)$ 在 $[0, t_f]$ 上是连续末态能观测的，是指存在一常数 $\gamma > 0$ 使得

$$\gamma \| P (t _ {f}) z \| _ {L ^ {q} (0, t _ {f}; Y)} \geqslant \| S (t _ {f}) z \|, \quad \forall z \in Z.$$

一个系统在 $[0, t_f]$ 上的初态或末态能观测性意味着有可能利用 $[0, t_f]$ 上的观测数据重构系统的初始或末时刻状态。在大多数情形下，为了设计控制器，必须知道整个系统的状态。但显然，如果我们可以知道系统的初始状态，则我们就能够找到系统在任意时刻 $t \geqslant 0$ 的状态。能观测性的重要性正在于此。

为了讨论能控性和能观测性之间对偶关系，设

$$U = Y ^ {*}, \quad X = Z ^ {*}, \quad A = F ^ {*}, \quad B = C ^ {*},T (t) = S (t) ^ {*}, \quad \frac {1}{p} + \frac {1}{q} = 1,$$

并假定 $Z, Y$ 是两个自反的 Banach 空间，而且 $p > 1$ .

定理10.2.4 基于上述记号和假设，我们有

(1) $(F, C)$ 在 $[0, t_f]$ 上初态能观测，当且仅当 $(A, B)$ 在 $[0, t_f]$ 上近似能控；

(2) $(F, C)$ 在 $[0, t_f]$ 上连续初态能观测，当且仅当 $(A, B)$ 在 $[0, t_f]$ 上精确能控；

(3) $(F, C)$ 在 $[0, t_f]$ 上末态能观测，当且仅当 $(A, B)$ 在 $[0, t_f]$ 上近似零能控；

(4) $(F, C)$ 在 $[0, t_f]$ 上连续末态能观测，当且仅当 $(A, B)$ 在 $[0, t_f]$ 上精确零能控.

证明 这是定理 10.2.1, 10.2.2 和定理 10.2.3 的直接结果.

当 $H = X$ 和 $U$ 是 Hilbert 空间时，为了讨论一个系统的能控性，我们可以引进所谓能控性算子 $W(t_{f}) \stackrel{\mathrm{def}}{=} G(t_{f}) G(t_{f})^{*}$ ，

$$W (t _ {f}) x = \int_ {0} ^ {t _ {f}} T (s) B B ^ {*} T ^ {*} (s) x \mathrm{d} s, \qquad x \in H. \tag {10.2.11}$$

定理10.2.5 设 $H$ 和 $U$ 是Hilbert空间，算子 $W(t_{f})$ 由式(10.2.11)给出，那么

(1) $(A, B)$ 在 $[0, t_f]$ 上近似能控，当且仅当 $W(t_f)$ 是 $H$ 中一正自伴算子，即

$$(W (t _ {f}) x, x) _ {H} > 0, \quad \forall x \in H, x \neq 0;$$

(2) $(A, B)$ 在 $[0, t_f]$ 上精确能控，当且仅当 $W(t_f)$ 是 $H$ 中一正定自伴算子，即存在一常数 $\gamma > 0$ 使得

$$(W (t _ {f}) x, x) _ {H} \geqslant \gamma \| x \| _ {H} ^ {2}, \quad \forall x \in H.$$

证明 依据定理 10.2.3, (A, B) 在 $[0, t_f]$ 上近似能控，当且仅当 $\mathcal{N}(G(t_f)^*) = \{0\}$ . 显然， $W(t_f) = G(t_f)G(t_f)^*$ 是 $H$ 中自伴算子。注意

$$\| G (t _ {f}) ^ {*} x \| _ {L ^ {2} (0, t _ {f}; U)} ^ {2} = \left(W ^ {\prime} (t _ {f}) x, x\right) _ {H}, \quad \forall x \in H,$$
