9.17 考虑系统 $\dot{x}=A(t)x$ ，其中 $A(t)$ 是连续的。假设 $\lim_{t\to\infty}A(t)=\bar{A}$ 存在，且 $\bar{A}$ 是赫尔维茨的，证明原点是指数稳定的。  
9.18 当 $q(t)$ 有界, 且 t 趋于无穷, $q(t)$ 趋于零时, 重做习题 9.10 的 (b)。  
9.19 设系统为 $\dot{x}=f(t,x)$ ，其中对于所有 $t\geqslant0, x\in R^{2}$ ，有 $\|f(t,x)-f(0,x)\|_{2}\leqslant\gamma(t)\|x\|_{2}$ ，式中当 t 趋于无穷时， $\gamma(t)$ 趋于零。且有

$$
f (0, x) = A x - \left(x _ {1} ^ {2} + x _ {2} ^ {2}\right) B x, \quad A = \left[ \begin{array}{c c} - \alpha & - \omega \\ \omega & - \alpha \end{array} \right], \quad B = \left[ \begin{array}{c c} \beta & \Omega \\ - \Omega & \beta \end{array} \right]
$$

$\alpha,\beta,\omega$ 和 $\Omega$ 都是正常数,证明原点是全局指数稳定的。

9.20 考虑系统 $\dot{x}=f(x)+G(x)u+w(t)$ ，其中 $\|w(t)\|_{2}\leqslant\alpha+ce^{-t}$ 。假设存在正定对称矩阵 P，一个半正定函数 $W(x)$ 以及正常数 $\gamma$ 和 $\sigma$ ，使得

$$2 x ^ {\mathrm{T}} P f (x) + \gamma x ^ {\mathrm{T}} P x + W (x) - 2 \sigma x ^ {\mathrm{T}} P G (x) G ^ {\mathrm{T}} (x) P x \leqslant 0, \quad \forall x \in R ^ {n}$$

证明对于 $u = -\sigma G^{\mathrm{T}}(x)Px$ ，闭环系统的轨线是一致毕竟有界的，其最终边界为 $2ak\lambda_{\max}(P)/\gamma\lambda_{\min}(P), k > 1$ 。

9.21 考虑扰动系统(9.1)，假设存在一个李雅普诺夫函数 $V(t,x)$ ，满足式(9.11)至式(9.13)，扰动项满足 $\| g(t,x)\| \leqslant \delta (t),\forall t\geqslant 0,\forall x\in D$ 。证明对于任意 $\varepsilon >0$ 和 $\Delta >0$ ，存在 $\eta >0$ 和 $\rho >0$ 使得只要 $(1 / \Delta)\int_t^{t + \Delta}\delta (\tau)d\tau < \eta$ ，则当 $\| x(t_0)\| < \rho$ 时，扰动系统的每个解都满足 $\| x(t)\| < \varepsilon ,\forall t\geqslant t_0$ 。这个结果称为扰动存在情况下的总稳定性，扰动是均值有界的[107]。）

提示:选择 $W=\sqrt{V}$ ，在抽样点 $t_{0}+i\Delta$ 对时间区间离散化，其中 $i=0,1,2,\cdots$ ，并证明 $W(t_{0}+i\Delta)$ 满足差分不等式

$$W (t _ {0} + (i + 1) \Delta) \leqslant e ^ {- \sigma \Delta} W (t _ {0} + i \Delta) + k \eta \Delta$$

9.22 设 A 是 $n \times n$ 矩阵, 其中当 $i \neq j$ 时, $a_{ij} \leqslant 0$ , 而 $a_{ii} > \sum_{j \neq i} |a_{ij}|, i = 1, 2, \cdots, n$ 。证明 A 是一个 M 矩阵。

提示: 证明 $\sum_{j=i}^{n}a_{ii}>0$ , 其中 $i=1,2,\cdots,n$ 。用数学归纳法证明所有前主子式都是正的。

9.23 假设 $\phi_{i}(x_{i}) = \| x_{i}\| ,\quad c_{i1}\| x_{i}\|^{2}\leqslant V_{i}(t,x_{i})\leqslant c_{i2}\| x_{i}\|^{2}$

时定理 9.3 的条件满足,证明原点是指数稳定的。

9.24 （见文献[132]）用复合李雅普诺夫分析法研究系统

$$\dot {x} _ {1} = - x _ {1} ^ {3} - 1. 5 x _ {1} | x _ {2} | ^ {3}, \quad \dot {x} _ {2} = - x _ {2} ^ {5} + x _ {1} ^ {2} x _ {2} ^ {2}$$

的原点的稳定性。

9.25 用复合李雅普诺夫分析法研究系统

$$\dot {x} _ {1} = x _ {2} + x _ {2} x _ {3} ^ {3}, \quad \dot {x} _ {2} = - x _ {1} - x _ {2} + x _ {1} ^ {2}, \quad \dot {x} _ {3} = x _ {1} + x _ {2} - x _ {3} ^ {3}$$

的原点的稳定性。

9.26 考虑线性互联系统
