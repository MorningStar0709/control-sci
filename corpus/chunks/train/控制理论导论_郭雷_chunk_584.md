证明 因为 $\operatorname{rank}(\mathcal{F}_{x_0}) = n$ , 故存在 $x_0$ 的一个邻域 $U$ 使得 $\operatorname{rank}(\mathcal{F}_x) = n, x \in U$ . 现在如果 $f(x_0) = 0, \forall f(x) \in F$ , 则显然 $\operatorname{rank}(\mathcal{F}_x) = 0$ . 因此, 存在一个 $f_1 \in F$ 使得 $f_1(x) \neq 0, x \in U_1 \subset U$ . 因此存在一条积分曲线, $\phi_{t_1}^{f_1}(x_0), -\varepsilon_1 < t_1 < \varepsilon_1$ , 它是一个一维子流形, 记作 $L_1$ . 然后我们证明存在 $-\varepsilon_1 < t_1^0 < \varepsilon_1$ , 使得 $f_2 \in F$ , 且在 $t_1^0, f_2(x_1) \notin T_{x_1}(L_1)$ , 这里 $x_1 = \phi_{t_1^0}^{f_1}(x_0)$ . 否则 $\operatorname{rank}(\mathcal{F}(x)) = 1, x \in L_1$ . (读者可自行检验这一点.) 现在考虑映射

$$\pi_ {2} (t _ {2}, t _ {1}) := \phi_ {t _ {2}} ^ {f _ {2}} \phi_ {t _ {1}} ^ {f _ {1}} (x _ {0}).$$

因为Jacobi矩阵

$$J _ {\pi_ {2}} (0, t _ {1} ^ {0}) = \left(f _ {2} (x _ {1}), f _ {1} (x _ {1})\right)$$

是非奇异的，局部看这是从 $|t_2| < \varepsilon_2, |t_1 - t_1^0| < e_1$ 到 $\pi_2$ 的像的微分同胚，其像为二维流形，记作 $L_2$ 。如果 $F$ 中每个向量场 $f$ 在 $L_2$ 的每一点 $x$ 均在其切方向上，即 $f(x) \in T_x(L_2)$ ，则 $\operatorname{rank}(\mathcal{F}(x)) = 2, \forall x \in L_2$ ，故存在 $|t_2^0| < \varepsilon_2$ 及 $|t_1^0 - t_1^0| < e_1$ ，及一向量场 $f_3 \in F$ ，使得 $f_3(x_2) \notin T_{x_2}(L_2)$ ，这里 $x_2 = \phi_{t_2^0}^{f_2} \phi_{t_1^0}^{f_1}(x_0)$ 。为记号简单，我们仍用 $t_1^0$ 代表 $\tilde{t}_1^0$ 。定义

$$\pi_ {3} (t _ {3}, t _ {2}, t _ {1}) := \phi_ {t _ {3}} ^ {f _ {3}} \phi_ {t _ {2}} ^ {f _ {2}} \phi_ {t _ {1}} ^ {f _ {1}} (x _ {0}),$$

即得一三维子流形 $L_{3}$ . 继续这一过程，可得到 $f_{1}, \cdots, f_{n} \in F$ 并构造局部微分同胚

$$\pi_ {n} (t _ {n}, \dots , t _ {2}, t _ {1}) := \phi_ {t _ {n}} ^ {f _ {n}} \dots \phi_ {t _ {2}} ^ {f _ {2}} \phi_ {t _ {1}} ^ {f _ {1}} (x _ {0}), \tag {8.1.4}$$

它将 $(0,t_{n-1}^{0},\cdots,t_{1}^{0})\in\mathbb{R}^{n}$ 的一个邻域 $V_{n}$ 映射到 $\phi_{0}^{f_{n}}\cdots\phi_{t_{2}^{0}}^{f_{2}}\phi_{t_{1}^{0}}^{f_{1}}(x_{0})$ 的一个邻域 $U_{n}$ . 再构造一个微分同胚 $G(x)=\phi_{-t_{1}^{0}}^{f_{1}}\phi_{-t_{2}^{0}}^{f_{2}}\cdots\phi_{-t_{n-1}^{0}}^{f_{n-1}}(x),\quad x\in U_{n}$ , 它将 $U_{n}$ 映回 $x_{0}$ 的一个邻域. 最后, 定义 $\pi:=G\circ\pi_{n}(t),\quad t\in V_{n}$ , 它是从 $V_{n}$ 到 $x_{0}$ 的一个邻域的一个微分同胚. 由定义 $\pi(V_{n})\subset WR_{U}(x_{0})$ . 即系统在 $x_{0}$ 局部弱能控.

反之，如果系统是局部弱能控或弱能控，我们希望知道是否能控性秩条件满足？

命题8.1.4 假定系统(8.1.1)局部弱能控，则存在一个开稠集 $D \subset M$ 使能控性秩条件在 $D$ 上满足，即

$$\operatorname{rank} (\mathcal {F} (x)) = n, \quad x \in D.$$
