于是若 $t_0 \leqslant t \leqslant t' < t_1$ ，则 $P(t) \geqslant P(t')$ 。这样我们证明了 (1).

为证 (2), 注意到 $P(t)$ 的有界对称性, 我们有 $\| P(t) \| = \sup \{(P(t)x, x) | \| x \| = 1\}$ . 于是根据引理 10.6.1,

$$(P (t) x, x) \leqslant \frac {\mu_ {4} \mu_ {1} ^ {2} (\mathrm{e} ^ {2 \omega t _ {1}} - \mathrm{e} ^ {2 \omega t _ {0}})}{2 \omega} \| x \| ^ {2} + \| G \| \mu_ {1} ^ {2} \mathrm{e} ^ {2 \omega (t _ {1} - t _ {0})} \| x \| ^ {2}, \quad \forall x \in H,$$

由此 $\| P(t)\| \leqslant \mu_4\mu_1^2 (\mathrm{e}^{2\omega t_1} - \mathrm{e}^{2\omega t_0}) / 2\omega +\| G\| \mu_1^2 \mathrm{e}^{2\omega (t_1 - t_0)},\forall t\in [t_0,t_1).$

现在我们证明 (3). 首先假定数列 $\{s_n\} \subset (t, t_1)$ 使得当 $n \to \infty$ 时 $s_n \downarrow t$ . 于是根据已经证明了的 (1), 我们有

$$m (s _ {n}, t _ {1}, x) = (P (s _ {n}) x, x) \leqslant (P (t) x, x) = m (t, t _ {1}, x).$$

设 $u_{n}^{0}(s)$ 和 $x_{n}^{0}(s)$ 是关于性能指标 $J(\cdot ;s_n,t_1,x)$ 的最优控制和最优轨线．根据引理10.6.1， $m(s_n,t_1,x)$ 是 $n$ 的增函数，从而序列 $\{u_n^0\}$ 在 $L^2 (t,t_1;U)$ 中是有界的，其中 $u_{n}^{0}$ 在区间 $(t,t_1)$ 之外规定为零．于是存在 $\{u_n^0\}$ 的子序列，为简单起见仍记作 $\{u_n^0\}$ ，它在 $L^2 (t,t_1;U)$ 中弱收敛于 $u^{0}$ ．显然对于任意 $s\in (t,t_1)$ ，序列 $\{x_{n}^{0}(s)\}$ 在 $H$ 中也弱收敛于 $x^{0}(s)$ ，其中

$$x ^ {0} (s) = T (s - t) x + \int_ {t} ^ {s} T (s - \tau) B u ^ {0} (\tau) \mathrm{d} \tau .$$

注意到

$$\left(R u ^ {0}, u ^ {0}\right) _ {L ^ {2} \left(t, t _ {1}; U\right)} \leqslant \lim _ {n \rightarrow \infty} \left(R u _ {n} ^ {0}, u _ {n} ^ {0}\right) _ {L ^ {2} \left(t, t _ {1}; U\right)},\left(Q x ^ {0} (s), x ^ {0} (s)\right) \leqslant \lim _ {\overline {{n \rightarrow \infty}}} \left(Q x _ {0} ^ {n} (s), x _ {n} ^ {0} (s)\right), \quad \forall s \in (t, t _ {1}),\left(G x ^ {0} \left(t _ {1}\right), x ^ {0} \left(t _ {1}\right)\right) \leqslant \lim _ {n \rightarrow \infty} \left(G x _ {0} ^ {n} \left(t _ {1}\right), x _ {n} ^ {0} \left(t _ {1}\right)\right),$$

我们有

$$J (u ^ {0}; t, t _ {1}, x) \leqslant \lim _ {n \rightarrow \infty} J (u _ {n} ^ {0}; s _ {n}, t _ {1}, x) \leqslant m (t, t _ {1}, x).$$

这表明 $u^0$ 和 $x^0$ 分别是关于性能指标 $J(\cdot ;t,t_1,x)$ 的最优控制和最优轨线．由此可见

$$\lim _ {n \rightarrow \infty} J (u _ {n} ^ {0}; s _ {n}, t _ {1}, x) = J (u ^ {0}; t, t _ {1}, x),$$

即当 $n \to \infty$ 时 $m(s_n, t_1, x) \to m(t, t_1, x)$ .

现在我们假定 $\{s_n\} \subset [t_0, t)$ , 并且当 $n \to \infty$ 时 $s_n \uparrow t$ . 根据引理10.6.1, 我们有 $m(s_n, t_1, x) \geqslant m(t, t_1, x), \forall n$ . 令 $\tau_n = t_1 + t - s_n$ . 并再次使用引理10.6.1, 我们得到 $m(t, \tau_n, x) = m(s_n, t_1, x), \forall n$ . 设 $u^0$ 是关于性能指标 $J(\cdot; t, t_1, x)$ 的最优控制, 而 $x^0$ 是相应的最优轨线. 我们定义
