$$\| x (t) \| \leqslant \beta (\| x _ {0} \|, t) + \gamma \left(\sup _ {0 \leqslant t \leqslant \tau} \| u (t) \|\right) \tag {5.21}$$

其中 $\beta$ 与 $\gamma$ 分别为 KL 类函数和 K 类函数。利用式(5.20)可得

$$
\begin{array}{l} \| y (t) \| \leqslant \alpha_ {6} \left(\beta \left(\| x _ {0} \|, t\right) + \gamma \left(\sup _ {0 \leqslant t \leqslant \tau} \| u (t) \|\right)\right) + \alpha_ {7} (\| u (t) \|) + \eta \\ \leqslant \alpha_ {6} (2 \beta (\| x _ {0} \|, t)) + \alpha_ {6} \left(2 \gamma \left(\sup _ {0 \leqslant t \leqslant \tau} \| u (t) \|\right)\right) + \alpha_ {7} (\| u (t) \|) + \eta \\ \end{array}
$$

其中应用了K类函数的一般性质①

$$\alpha (a + b) \leqslant \alpha (2 a) + \alpha (2 b)$$

所以， $\| y_{\tau}\|_{\mathcal{L}_{\infty}} \leqslant \gamma_0 (\| u_{\tau}\|_{\mathcal{L}_{\infty}}) + \beta_0$ (5.22)

其中

$$\gamma_ {0} = \alpha_ {6} \circ 2 \gamma + \alpha_ {7}, \quad \beta_ {0} = \alpha_ {6} (2 \beta (\| x _ {0} \|, 0)) + \eta$$

应用定理 4.16（逆李雅普诺夫定理）证明存在李雅普诺夫函数，满足式(5.16)到式(5.18)，从而得出以下推论。

推论5.3 假设在 $(x = 0, u = 0)$ 的某个邻域内，函数 $f(t, x, u)$ 连续可微，雅可比矩阵 $[\partial f / \partial x]$ 和

$[\partial f / \partial u]$ 有界，对 $t$ 一致，且 $h(t,x,u)$ 满足式(5.20)。如果无激励系统(5.5)在原点 $x = 0$ 有一致渐近稳定的平衡点，则系统(5.3）\~(5.4)是小信号 $\mathcal{L}_{\infty}$ 稳定的。

为推广定理5.2的证明以证明 $\mathcal{L}_{\infty}$ 稳定性，需要证明对任意初始状态 $x_0 \in R^n$ 和任意有界输入，式(5.21)成立。如4.9节所述，当定理5.2全局满足时，甚至当系统(5.5)的原点全局一致渐近稳定时，此不等式也不能自行成立。但它仍遵循系统(5.3)的输入-状态稳定性，可由定理4.19验证。

定理 5.3 考虑系统(5.3)～(5.4)， $D=R^{n},D_{u}=R^{m}$ 。假设

- 系统(5.3)是输入-状态稳定的。  
- 对于所有 $(t, x, u) \in [0, \infty) \times R^n \times R^m$ , $\mathcal{K}$ 类函数 $\alpha_1$ 和 $\alpha_2$ 以及非负常数 $\eta, h$ 满足不等式

$$\left\| h (t, x, u) \right\| \leqslant \alpha_ {1} (\| x \|) + \alpha_ {2} (\| u \|) + \eta \tag {5.23}$$

则对每个 $x_0 \in R^n$ ，系统(5.3)～(5.4)是 $\mathcal{L}_{\infty}$ 稳定的。

证明:输入-状态稳定性证明了一个与式(5.21)相似的不等式对任意 $x_{0} \in R^{n}$ 和 $u \in L_{\infty e}$ 成立。其余证明与定理 5.2 的证明相同。

例 5.6 考虑一阶单输入-单输出系统

$$
\begin{array}{l} \dot {x} = - x - 2 x ^ {3} + (1 + x ^ {2}) u ^ {2} \\ y = x ^ {2} + u \\ \end{array}
$$

由例 4.26 可知, 状态方程是输入-状态稳定的。输出函数 h 全局满足式(5.23), 其中 $\alpha_{1}(r)=r^{2}, \alpha_{2}(r)=r, \eta=0$ 。因此, 系统是 $L_{\infty}$ 稳定的。

例 5.7 考虑二阶单输入-单输出系统

$$
\begin{array}{l} \dot {x} _ {1} = - x _ {1} ^ {3} + g (t) x _ {2} \\ \dot {x} _ {2} = - g (t) x _ {1} - x _ {2} ^ {3} + u \\ y = x _ {1} + x _ {2} \\ \end{array}
$$

其中，对于 $t \geqslant 0, g(t)$ 是连续且有界的。取 $V = (x_1^2 + x_2^2)$ ，则有

$$\dot {V} = - 2 x _ {1} ^ {4} - 2 x _ {2} ^ {4} + 2 x _ {2} u$$
