证明 首先注意，满足初始条件 $\varphi(t_0) = x_0$ 的微分方程 (2.2.19) 的解是积分方程 (2.2.21) 的连续解，而积分方程 (2.2.21) 的连续解 $\varphi(t)$ 也是微分方程 (2.2.19) 的以 $\varphi(t_0) = x_0$ 为初始条件的解.

其次，由于点 $(t_0, x_0) \in \Omega_{n+1}$ ，所以存在正数 $\alpha, \beta$ ，使闭区域 $\pi(\alpha, \beta)$ 完全包含在 $\Omega_{n+1}$ 内。因此存在正数 $M$ ，使得

$$| f (t, x) | < M, \quad \forall (t, x) \in \pi (\alpha , \beta). \tag {2.2.23}$$

令 $r = \min \{\alpha, \beta / M\}$ , 显然, $\pi(r, \beta)$ 包含在 $\pi(\alpha, \beta)$ 内部.

构造向量值函数序列 $\{\varphi_m(t)\}_{m=0}^{\infty}$ (称为 Picard 序列)

$$
\left\{ \begin{array}{l} \varphi_ {0} (t) = x _ {0}, \\ \varphi_ {m + 1} (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, \varphi_ {m} (s)) \mathrm{d} s, \quad m = 0, 1, 2 \dots . \end{array} \right. \tag {2.2.24}
$$

容易用数学归纳法证明诸 $\varphi_{m}(t)$ 定义在 $[t_0 - r, t_0 + r]$ 上且连续。下面用归纳法证明不等式

$$\left| \varphi_ {m + 1} (t) - \varphi_ {m} (t) \right| \leqslant \frac {M}{L} \frac {(L | t - t _ {0} |) ^ {m + 1}}{(m + 1) !}. \tag {2.2.25}$$

当 $m = 0$ 时，式(2.2.25)显然成立．设 $m = k$ 时，式(2.2.25)成立．由Lipschitz条件(2.2.22)和归纳假设，有

$$
\begin{array}{l} \left| \varphi_ {k + 2} (t) - \varphi_ {k + 1} (t) \right| \leqslant \int_ {t _ {0}} ^ {t} | f (\tau , \varphi_ {k + 1} (\tau)) - f (\tau , \varphi_ {k} (\tau)) | d \tau \\ \leqslant \int_ {t _ {0}} ^ {t} L | \varphi_ {k + 1} (\tau) - \varphi_ {k} (\tau) | d \tau \\ \leqslant \int_ {t _ {0}} ^ {t} M \frac {(L | t - t _ {0} |) ^ {k + 1}}{(k + 1) !} d \tau \\ \leqslant \frac {M}{L} \frac {(L | t - t _ {0} |) ^ {k + 2}}{(k + 2) !}, \\ \end{array}
$$

由此式 (2.2.25) 得证. 容易看到式 (2.2.25) 蕴含着 $\{\varphi_m(t)\}_{m=0}^{\infty}$ 在区间 $[t_0 - r, t_0 + r]$ 上一致收敛. 设

$$\lim _ {m \rightarrow \infty} \varphi_ {m} (t) = \varphi (t).$$

在式 (2.2.24) 中，令 $m \to \infty$ 得

$$\varphi (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, \varphi (s)) \mathrm{d} s, \quad \forall t \in [ t _ {0} - r, t _ {0} + r ],$$

即结论 (1) 成立. 现证明定理结论 (2).

令 $\varphi(t), \psi(t)$ 是微分方程 (2.2.19) 的满足相同初始条件 $\varphi(t_0) = \psi(t_0) = x_0$ 的两个解，并设 $(r_1, r_2)$ 是 $\varphi(t), \psi(t)$ 的共同存在区间。显然有 $r_1 < t_0 < r_2$ 。于是

$$
\begin{array}{l} | \varphi (t) - \psi (t) | \leqslant \int_ {t _ {0}} ^ {t} | f (\tau , \varphi (\tau) - \psi (\tau)) | d \tau \tag {2.2.26} \\ \leqslant L \int_ {t _ {0}} ^ {t} | \varphi (\tau) - \psi (\tau) | d \tau , \quad \forall t \in (r _ {1}, r _ {2}). \\ \end{array}
$$

由此从 Gronwall 不等式得到 $\varphi(t) = \psi(t), \forall t \in (r_1, r_2)$ . 于是定理得证.

定理 2.2.8(Kamke 普遍唯一性定理) $^{[6]}$ 假设
