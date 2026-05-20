定理 1.3.1 说明判断一个线性系统的能控性问题，归结为判别矩阵 $\boldsymbol{W}(t, t_{0})$ 在某时刻 $t_{1}$ 的正定性问题。矩阵 $\boldsymbol{W}(t, t_{0})$ 叫做系统 $(\boldsymbol{A}(t), \boldsymbol{B}(t))$ 的能控性矩阵。

如果存在某时刻 $t_1$ ，使得 $\pmb{W}(t_1, t_0)$ 非奇异的话，那么控制函数

$$u _ {0} (t) = - \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {\Phi} ^ {\mathrm{T}} (t _ {1}. t) \boldsymbol {W} ^ {- 1} (t _ {1}, t _ {0}) \boldsymbol {\Phi} (t _ {1}, t _ {0}) x _ {0} \tag {1.3.2}$$

能把系统 $(A(t), B(t))$ 的初始状态 $x(t_0) = x_0$ 控制到 $x(t_1) = 0$ . 其实, 能够实现这样的状态转移的控制函数并非唯一, 但是可以证明, 由式 (1.3.2) 定义的容许控制是实现这种状态转移的所有控制函数中所消耗的“能量”最小的一个. 即, 若令 $u(t)$ 是任意一个实现上述状态转移的容许控制, 则

$$\int_ {t _ {0}} ^ {t _ {1}} \| u (t) \| ^ {2} \mathrm{d} t \geqslant \int_ {t _ {0}} ^ {t _ {1}} \| u _ {0} (t) \| ^ {2} \mathrm{d} t = \boldsymbol {x} _ {0} ^ {\mathrm{T}} \boldsymbol {\Phi} ^ {\mathrm{T}} (t _ {1}, t _ {0}) \boldsymbol {W} ^ {- 1} (t _ {1}, t _ {0}) \boldsymbol {\Phi} (t _ {1}, t _ {0}) \boldsymbol {x} _ {0}. \tag {1.3.3}$$

事实上，已经知道由式(1.3.2)定义的容许控制将 $x_0$ 转移到0，而 $u(t)$ 是把另一个 $x_0$ 转移到零状态的容许控制，因此有

$$0 = \Phi (t _ {1}, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) u _ {0} (\tau) \mathrm{d} \tau$$

和

$$0 = \Phi (t _ {1}, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) u (\tau) d \tau .$$

上两式的左右两边分别相减得

$$\int_ {t _ {0}} ^ {t _ {1}} \Phi (t _ {1}, \tau) B (\tau) (u (\tau) - u _ {0} (\tau)) \mathrm{d} \tau = 0.$$

对上式的两边左乘 $x_0^{\mathrm{T}}\Phi^{\mathrm{T}}(t_1,t_0)\pmb{W}^{-1}(t_1,t_0)$ 并利用式 (1.3.2) 得

$$\int_ {t _ {0}} ^ {t _ {1}} u _ {0} (\tau) (u (\tau) - u _ {0} (\tau)) \mathrm{d} \tau = 0,$$

即

$$\int_ {t _ {0}} ^ {t _ {1}} u _ {0} ^ {\mathrm{T}} (\tau) u (\tau) \mathrm{d} \tau = \int_ {t _ {0}} ^ {t _ {1}} \| u _ {0} (\tau) \| ^ {2} \mathrm{d} \tau .$$

进而，由

$$0 \leqslant \int_ {t _ {0}} ^ {t _ {1}} \| u (\tau) - u _ {0} (\tau) \| ^ {2} \mathrm{d} \tau = \int_ {t _ {0}} ^ {t _ {1}} [ \| u (\tau) \| ^ {2} - 2 u _ {0} ^ {\mathrm{T}} (\tau) u (\tau) + \| u _ {0} (\tau) \| ^ {2} ] \mathrm{d} \tau$$

知

$$0 \leqslant \int_ {t _ {0}} ^ {t _ {1}} [ \| u (\tau) \| ^ {2} - \| u _ {0} (\tau) \| ^ {2} ] \mathrm{d} \tau ,$$

故式 (1.3.3) 成立.

当 $(A(t), B(t))$ 为定常系统时，还有更方便的判别准则。首先介绍一个引理。

引理1.3.1 设定常线性系统 $(A, B)$ 在 $t_0$ 时刻完全能控，则它在 $[0, \infty)$ 上完全能控.

证明 由于系统 $(A, B)$ 是定常的，因此它的状态转移矩阵为 $\mathrm{e}^{A(t - \tau)}$ 。因为它在 $t_0$ 时刻完全能控，所以对某 $t_1 > t_0$ 矩阵
