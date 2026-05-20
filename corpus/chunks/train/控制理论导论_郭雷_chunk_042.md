定理1.3.1 系统 $(A(t), B(t))$ 在 $t_0$ 时刻能控的充要条件是，存在某有限时刻 $t_1 > t_0$ ，使得矩阵

$$\boldsymbol {W} (t _ {1}, t _ {0}) = \int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {\Phi} (t _ {1}, \tau) \boldsymbol {B} (\tau) \boldsymbol {B} ^ {\mathrm{T}} (\tau) \boldsymbol {\Phi} ^ {\mathrm{T}} (t _ {1}, \tau) \mathrm{d} \tau$$

是正定的．这里 $\Phi(t,\tau)$ 是系统 $\dot{x}=A(t)x$ 的状态转移矩阵，即 $\Phi(t,\tau)$ 满足

$$\frac {\partial \Phi (t , \tau)}{\partial t} = A (t) \Phi (t, \tau), \quad \Phi (\tau , \tau) = I.$$

证明 充分性. 假设存在 $t_1 > t_0$ , 使得 $\pmb{W}(t_1, t_0) > 0$ , 因而它是非奇异的. 又设 $x_0$ 是系统 $(A(t), B(t))$ 在 $t_0$ 时刻的任意初始状态, 定义

$$u (t) = - \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\Phi} ^ {\mathrm{T}} (t _ {1}, t) \boldsymbol {W} ^ {- 1} (t _ {1}, t _ {0}) \boldsymbol {\Phi} (t _ {1}, t _ {0}) \boldsymbol {x} _ {0}, \quad t _ {0} \leqslant t \leqslant t _ {1}.$$

另一方面，由定理1.1.1，

$$x (t _ {1}) = \Phi (t _ {1}, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) u (\tau) \mathrm{d} \tau$$

将前面定义的控制输入 $u(\cdot)$ 代入这个解表达式中即得 $x(t_{1}) = 0$ 。于是，根据系统的能控性定义可知，系统 $(A(t), B(t))$ 在 $t_{0}$ 时刻是完全能控的。

必要性．用反证法证明之．假设系统 $(A(t),B(t))$ 是完全能控的，但不管t多么大， $W(t,t_{0})$ 总是奇异的．从能控性的定义可知，存在某时刻 $t_{1}>t_{0}$ ，使得对每个初始状态 $x_{0}$ ，都能找到一个定义在时间间隔 $[t_{0},t_{1}]$ 上的容许控制，使得系统在这个控制作用下，由 $x_{0}$ 出发的轨线，在 $t_{1}$ 时刻达到零状态，即 $x(t_{1})=0$ ．依假设，对 $t_{1},W(t_{1},t_{0})$ 是奇异的，于是有非零向量z，使得

$$\boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {W} (t _ {1}, t _ {0}) z = 0,$$

即

$$\int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {z} ^ {\mathrm{T}} \boldsymbol {\Phi} (t _ {1}, \tau) \boldsymbol {B} (\tau) \boldsymbol {B} ^ {\mathrm{T}} (\tau) \boldsymbol {\Phi} ^ {\mathrm{T}} (t _ {1}, \tau) \boldsymbol {z} \mathrm{d} \tau = 0.$$

由此得出

$$z ^ {T} \Phi (t _ {1}, \tau) B (\tau) \stackrel {\text { a.c. }} {=} 0, \quad t _ {0} \leqslant \tau \leqslant t _ {1},$$

其中 $\stackrel{\mathrm{a.e.}}{=}$ 表示几乎处处相等.

另一方面，由于系统 $(A(t), B(t))$ 完全能控，因此对初始状态 $x_0 = -\Phi(t_0, t_1)z$ 也能找到定义在时间间隔 $[t_0, t_1]$ 上的容许控制 $u_0(t)$ ，使得

$$0 = \Phi (t _ {1}, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) u _ {0} (\tau) d \tau .$$

将所取得的 $x_0$ 代入上式得

$$z = \int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) u _ {0} (\tau) \mathrm{d} \tau .$$

对上式两边左乘 $z^{\mathrm{T}}$ 有

$$\| \boldsymbol {z} \| ^ {2} = \int_ {t _ {0}} ^ {t _ {1}} \boldsymbol {z} ^ {T} \Phi (t _ {1}, \tau) \boldsymbol {B} (\tau) u _ {0} (\tau) \mathrm{d} \tau = 0.$$

由此推出 $z = 0$ ，而这与 $z$ 为非零向量矛盾。这个矛盾表明 $\pmb{W}(t_1, t_0)$ 是非奇异的，因而它是正定的。
