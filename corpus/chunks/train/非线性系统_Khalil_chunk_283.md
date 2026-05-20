# 9.5 （见文献[101]）考虑扰动系统

$$\dot {x} = A x + B u + D g (t, y), \quad y = C x$$

其中 $g(t,y)$ 是连续可微的,并且对于 r>0 满足 $\|g(t,y)\|_{2}\leqslant k\|y\|_{2},\forall t\geqslant0,\forall\|y\|_{2}\leqslant r$ 。假设方程

$$P A + A ^ {\mathrm{T}} P + \varepsilon Q - \frac {1}{\varepsilon} P B B ^ {\mathrm{T}} P + \frac {1}{\gamma} P D D ^ {\mathrm{T}} P + \frac {1}{\gamma} C ^ {\mathrm{T}} C = 0$$

有一个正定解 $P = P^{T} > 0$ ，方程中 $Q = Q^{T} > 0, \varepsilon > 0, 0 < \gamma < 1/k$ 。证明 $u = -(1/2 \varepsilon) B^{T} P x$ 使得扰动系统的原点是稳定的。

9.6 考虑系统 $\dot{x}_{1} = -\alpha x_{1} - \omega x_{2} + (\beta x_{1} - \gamma x_{2})(x_{1}^{2} + x_{2}^{2})$

$$\dot {x} _ {2} = \omega x _ {1} - \alpha x _ {2} + (\gamma x _ {1} + \beta x _ {2}) (x _ {1} ^ {2} + x _ {2} ^ {2})$$

其中 $\alpha > 0, \beta, \gamma$ 和 $\omega > 0$ 都是常数。

(a) 把该系统看成线性系统

$$\dot {x} _ {1} = - \alpha x _ {1} - \omega x _ {2}, \quad \dot {x} _ {2} = \omega x _ {1} - \alpha x _ {2}$$

的一个扰动,证明若 $|\beta|$ 和 $|\gamma|$ 足够小,则扰动系统的原点是指数稳定的, $\{\|x\|_{2}\leqslant r\}$ 包含于吸引区内。

(b) 用 $V(x) = x_{1}^{2} + x_{2}^{2}$ 作为该扰动系统的一个备选李雅普诺夫函数, 证明当 $\beta \leqslant 0$ 时, 原点是全局指数稳定的；而当 $\beta > 0$ 时，原点是指数稳定的， $\{\|x\|_2 < \sqrt{\alpha/\beta}\}$ 包含于吸引区。

(c) 比较(a)和(b)的结果,并讨论(a)的结果的保守特性。

9.7 考虑扰动系统

$$\dot {x} = f (x) + g (x)$$

假设标称系统 $\dot{x}=f(x)$ 的原点是渐近(而不是指数)稳定的。证明对于任何 $\gamma>0$ ，存在一个函数 $g(x)$ ，在原点的某邻域内满足 $\|g(x)\|\leqslant\gamma\|x\|$ ，使得扰动系统的原点是非稳定的。

9.8 (见文献[66])考虑扰动系统 $\dot{x} = f(x) + g(x)$

其中对于所有 $\| x\| < r, f(x)$ 和 $g(x)$ 是连续可微的，且 $\| g(x)\| \leqslant \gamma \| x\|$ 。假设标称系统 $\dot{x} = f(x)$ 的原点是渐近稳定的，存在一个李雅普诺夫函数 $V(x)$ ，对于所有 $\| x\| < r$ 满足不等式(9.11)至不等式(9.13)。设 $\Omega = \{V(x)\leqslant c\}$ ，其中 $c < \alpha_{1}(r)$ 。

(a) 证明存在一个正常数 $\gamma^{*}$ , 使得当 $\gamma < \gamma^{*}$ 时, 扰动系统始于 $\Omega$ 内的解对于所有 $t \geqslant 0$ 都保持在 $\Omega$ 内, 而且是毕竟有界的, 由 $\gamma$ 的 $\kappa$ 类函数确定。

(b) 假设标称系统有一个附加性质, 即 $A = \left[\frac{\partial f}{\partial x}\right]$ (0) 是赫尔维茨矩阵。证明存在一个 $\gamma_{1}^{*}$ , 使得当 $\gamma < \gamma_{1}^{*}$ 时, 扰动系统始于 $\Omega$ 内的解随 t 趋于无穷而收敛于原点。

(c) 如果 A 不是赫尔维茨矩阵, 那么 (b) 是否成立? 设

$$
f (x) = \left[ \begin{array}{c} {- x _ {2} - (2 x _ {1} + x _ {3}) ^ {3}} \\ {x _ {1}} \\ {x _ {2}} \end{array} \right], g (x) = a \left[ \begin{array}{c} {x _ {1} - x _ {3} - (2 x _ {1} + x _ {3}) ^ {3}} \\ {0} \\ {0} \end{array} \right], a \neq 0
$$

提示:例如(c),用

$$V (x) = x _ {1} ^ {2} + \frac {1}{2} x _ {2} ^ {2} + \frac {1}{2} x _ {3} ^ {2} + x _ {1} x _ {3}$$

证明 $\dot{x}=f(x)$ 的原点是渐近稳定的,然后再应用定理 4.16 得到一个满足式(9.11)至式(9.13)的李雅普诺夫函数。

9.9 考虑系统
