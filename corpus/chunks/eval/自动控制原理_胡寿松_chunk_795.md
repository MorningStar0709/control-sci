$$\dot {\lambda} (t) = - \frac {\partial H}{\partial x} = - (1 + \lambda)$$

其解为 $\lambda(t)=ce^{-t}-1$ ，其中常数 c 待定。

由横截条件

$$\lambda (1) = c \mathrm{e} ^ {- 1} - 1 = 0$$

求出 $c = \mathrm{e}$ 。于是

$$\lambda (t) = \mathrm{e} ^ {1 - t} - 1$$

显然，当 $\lambda(t_s)=1$ 时， $u^*(t)$ 产生切换，其中 $t_s$ 为切换时间。令 $\lambda(t_s)=\mathrm{e}^{1-t_s}-1=1$ ，得 $t_s=0.307$ ，故最优控制

$$
u ^ {*} (t) = \left\{ \begin{array}{l l} 1, & 0 \leqslant t <   0. 3 0 7 \\ 0. 5, & 0. 3 0 7 \leqslant t \leqslant 1 \end{array} \right.
$$

将 $u^{*}(t)$ 代入状态方程，有

$$
\dot {x} (t) = \left\{ \begin{array}{l l} x (t) - 1, & 0 \leqslant t <   0. 3 0 7 \\ x (t) - 0. 5, & 0. 3 0 7 \leqslant t \leqslant 1 \end{array} \right.
$$

解得

$$
x (t) = \left\{ \begin{array}{l l} c _ {1} \mathrm{e} ^ {t} + 1, & 0 \leqslant t <   0. 3 0 7 \\ c _ {2} \mathrm{e} ^ {t} + 0. 5, & 0. 3 0 7 \leqslant t \leqslant 1 \end{array} \right.
$$

代入 $x(0) = 5$ ，求出 $c_{1} = 4$ ，因而

$$x ^ {*} (t) = 4 \mathrm{e} ^ {t} + 1, \quad 0 \leqslant t < 0. 3 0 7$$

在上式中，令 $t = 0.307$ ，可以求出 $0.307 \leqslant t \leqslant 1$ 时 $x(t)$ 的初态 $x(0.307) = 6.44$ ，从而求得 $c_{2} = 4.37$ 。于是，最优轨线为

$$
x ^ {*} (t) = \left\{ \begin{array}{l l} 4 \mathrm{e} ^ {t} + 1, & 0 \leqslant t <   0. 3 0 7 \\ 4. 3 7 \mathrm{e} ^ {t} + 0. 5, & 0. 3 0 7 \leqslant t \leqslant 1 \end{array} \right.
$$

本例最优解曲线如图 10-4 所示。
