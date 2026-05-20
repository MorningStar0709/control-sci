# 2.3.1 考察 $n$ 次线性齐次方程

$$\frac {\mathrm{d} ^ {n} x}{\mathrm{d} t ^ {n}} = a _ {n - 1} (t) \frac {\mathrm{d} ^ {n - 1} x}{\mathrm{d} t ^ {n - 1}} + \dots + a _ {1} (t) \frac {\mathrm{d} x}{\mathrm{d} t} + a _ {0} (t) x.$$

假定对 $i = 0,1,\dots ,n - 1,a_{i}(t)$ 为区间 $[\alpha ,\beta ]$ 上的连续函数．设 $\alpha <  \alpha_{1} <   \beta_{1} <   \beta .$ 如果方程的解 $x(t)$ 在区间 $[\alpha_1,\beta_1]$ 上有无穷多个零点，则 $x(t) = 0,\forall t\in [\alpha_1,\beta_1].$

2.3.2 令 $\Phi(t, t_0)$ 为方程 (2.4.2) 的状态转移矩阵。设 $P(t)$ 为可微非奇异矩阵，试证明

$$\boldsymbol {\Phi} (t, t _ {0}) = \boldsymbol {P} ^ {- 1} (t) \boldsymbol {\Psi} (t, t _ {0}) \boldsymbol {P} (t _ {0}),$$

其中 $\Psi(t, t_0)$ 为方程 $z = B(t)z$ 的状态转移矩阵，这里 $B(t) = (P(t)A(t) + \dot{P}(t))P^{-1}(t)$ .

2.3.3 试证明齐次线性方程 (2.4.2) 的 $n$ 个解组构成基本解组的充要条件是其 Wronsky 行列式在某 $\bar{t}$ 处不等于零.
