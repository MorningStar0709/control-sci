的向量微分方程称为标准一阶微分方程组，其中 $x^{T}=[x_{1},x_{2},\cdots,x_{n}]\in\mathbb{R}^{n},f^{T}(t,x)=[f_{1}(t,x),f_{2}(t,x),\cdots,f_{n}(t,x)]$ 是定义在 $R^{n+1}$ 中某开域 $\Omega_{n+1}$ 内的 n 维向量值函数.

所谓微分方程 (2.2.19) 的解是指定义在某区间 $(t_1, t_2)$ 内的连续可微分向量值函数 $\varphi(t)$ , 它满足

$$(t, \varphi (t)) \in \Omega_ {n + 1}, \quad \forall t \in (t _ {1}, t _ {2}),\frac {\mathrm{d} \varphi (t)}{\mathrm{d} t} = f (t, \varphi (t)), \quad \forall t \in (t _ {1}, t _ {2}).$$

微分方程 (2.2.19) 的解 $\varphi(t)$ . 称为它的积分曲线. 给定 $(t_0, x_0) \in \Omega_{n+1}$ , 当微分方程 (2.2.19) 的解 $\varphi(t)$ 满足

$$x _ {0} = \varphi (t _ {0}), \quad t _ {0} \in (t _ {1}, t _ {2}) \tag {2.2.20}$$

时，我们说 $\varphi(t)$ 是方程 (2.2.19) 的满足初始条件 (2.2.20) 的解，或者说微分方程 (2.2.19) 的积分曲线通过点 $(t_0, x_0)$ .

考虑微分方程 (2.2.19) 的同时也研究相应的积分方程

$$x (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, x (s)) \mathrm{d} s, \tag {2.2.21}$$

其中点 $(t_0, x_0) \in \Omega_{n+1}$ .

所谓积分方程 (2.2.21) 的解指的是在含 $t_0$ 的某区间 $(t_1, t_2)$ 上定义的向量值函数 $\varphi(t)$ , 满足

$$\varphi (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, \varphi (s)) \mathrm{d} s, \quad \forall t \in (t _ {1}, t _ {2}).$$

定理 2.2.6(Peano) $^{[6]}$ 设 $f(t,x)$ 在区域 $\pi(a,b)=\{(t,x)\mid|t-t_{0}|\leqslant a,|x-x_{0}|\leqslant b\}$ 上连续，则方程 (2.2.19) 至少存在一个满足初始条件 $x(t_{0})=x_{0}$ 并定义在区间 $[t_{0}-h,t_{0}+h]$ 上的解 $x=x(t)$ ，这里 $h=\min(a,b/M),M=\max_{(t,x)\in\pi(a,b)}|f(t,x)|$ ，并且对于 $y\in\mathbb{R}^{m},|y|$ 表示 y 的欧氏模，而对 m 不加区别。

设向量值函数 $f(t,x)$ 在区域 $\Omega_{n + 1}\subset \mathbb{R}^{n + 1}$ 内有定义．如果存在 $L > 0$ ，使得

$$\left| f \left(t, x _ {1}\right) - f \left(t, x _ {2}\right) \right| \leqslant L \left| x _ {1} - x _ {2} \right|, \quad \forall (t, x _ {1}), (t, x _ {2}) \in \Omega_ {n + 1}, \tag {2.2.22}$$

则称在 $f(t,x)$ 在 $\Omega_{n + 1}$ 内满足对 $x$ 的Lipschitz条件.

定理2.2.7(Lipschitz) 设 $f(t, x)$ 在 $\Omega_{n+1}$ 内连续，且满足对 $x$ 的Lipschitz条件(2.2.22)，则有

(1) 对于任意 $(t_0, x_0) \in \Omega_{n+1}$ , 存在包含 $t_0$ 的一个区间 $(t_1, t_2)$ 及定义在 $(t_1, t_2)$ 的向量值函数 $\varphi(t)$ , 满足

$$
\left\{ \begin{array}{l l} \varphi (t _ {0}) = x _ {0}, \\ (t, \varphi (t)) \in \Omega_ {n + 1}, & \forall t \in (t _ {1}, t _ {2}), \\ \frac {\mathrm{d} \varphi (t)}{\mathrm{d} t} = f (t, \varphi (t)), & \forall t \in (t _ {1}, t _ {2}); \end{array} \right.
$$

(2) 如果还有另一个向量值函数 $\psi(t)$ 定义在包含 $t_0$ 的某区间内满足上述性质，则在 $\varphi(t)$ 和 $\psi(t)$ 定义区间的交集上必定成立

$$\varphi (t) \equiv \psi (t).$$
