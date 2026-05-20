$\dot{x}_2 = x_2(\| x\| _2^2 -1),\qquad y = x_1$

(4) $\dot{x}_1 = -x_1 - x_2 + u_1,$

$\dot{x}_2 = x_1 - x_2^3 + u_2, \quad y = x_1(x_2 + u_1)$

(5) $\dot{x}_{1} = -x_{1} + x_{1}^{2}x_{2},$

$\dot{x}_2 = x_1 - x_2 + u,$ $y = x_{1} + u$

(6) $\dot{x}_{1}=x_{2},$

$\dot{x}_2 = -x_1^3 - x_2 + u, \quad y = x_2$

(7) $\dot{x}_1 = -x_1 - x_2,$

$\dot{x}_2 = x_1 - x_3 + u,$ $y(t) = x_{1}(t - T)$

其中 T > 0。

5.12 考虑系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = -y - h(y) + u, \quad y = x_1 + x_2$

其中 $h$ 连续可微， $h(0) = 0$ ，且对于所有 $z \in R$ 及某个 $a > 0, zh(z) > az^2$ 。证明对于每个 $p \in [1, \infty]$ ，系统为有限增益 $\mathcal{L}_p$ 稳定的。

5.13 (见文献[192])考虑时不变系统

$$\dot {x} = f (x, u), \quad y = h (x, u)$$

其中 $f$ 是局部利普希茨函数， $h$ 连续，且 $f(0,0) = 0, h(0,0) = 0$ 。假设存在连续可微、正定的径向无界函数 $V(x)$ ，满足

$$\frac {\partial V}{\partial x} f (x, u) \leqslant - W (x) + \psi (u), \forall (x, u)$$

其中 $W(x)$ 是连续、正定且径向无界的函数， $\psi(u)$ 连续，且 $\psi(0)=0$ 。证明系统是 $L_{\infty}$ 稳定的。

5.14 设 $H(s)$ 为严格赫尔维茨正常传递函数, $h(t) = \mathcal{L}^{-1}\{H(s)\}$ 是其相应的脉冲响应函数。证明

$$\sup _ {\omega \in R} | H (j \omega) | \leqslant \int_ {0} ^ {\infty} | h (t) | d t$$

5.15 证明下列各系统是有限增益(或小信号有限增益) $L_{2}$ 稳定的,并求出其 $L_{2}$ 增益的上界。

$$
\begin{array}{l} \begin{array}{r c l} \dot {x} _ {1} & = & x _ {2} \\ \dot {x} _ {2} & = & - a \sin x _ {1} - k x _ {2} + u \end{array} \tag {1} \\ \begin{array}{r l} y & = x _ {2} \\ & a > 0, k > 0 \end{array} \\ \end{array}

\begin{array}{l} \begin{array}{r c l} \dot {x} _ {1} & = & x _ {2} \\ \dot {x} _ {2} & = & x _ {1} - \operatorname{sat} (2 x _ {1} + x _ {2}) + u \end{array} \tag {3} \\ y = x _ {1} \\ \end{array}
$$

(2)

$$
\begin{array}{l} \dot {x} _ {1} = - x _ {2} \\ \begin{array}{r c l} \dot {x} _ {2} & = & x _ {1} - x _ {2} \operatorname{sat} (x _ {2} ^ {2} - x _ {3} ^ {2}) + x _ {2} u \\ \dot {x} _ {3} & = & x _ {3} \operatorname{sat} (x _ {2} ^ {2} - x _ {3} ^ {2}) - x _ {3} u \end{array} \\ y = x _ {2} ^ {2} - x _ {3} ^ {2} \\ \end{array}
$$

(4)

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - \left(1 + x _ {1} ^ {2}\right) x _ {2} - x _ {1} ^ {3} + x _ {1} u \\ y = x _ {1} x _ {2} \\ \end{array}
$$

5.16 考虑系统 $\dot{x}_1 = -x_1 + x_2, \quad \dot{x}_2 = -x_1 - \sigma(x_1) - x_2 + u, \quad y = x_2$

其中 $\sigma$ 是局部利普希茨函数, $\sigma(0)=0$ , 且对于所有 $z\in R$ , 有 $z\sigma(z)\geqslant0$ 。

(a) 系统是否为 $\mathcal{L}_{\infty}$ 稳定的？  
(b) 系统是否为有限增益 $L_{2}$ 稳定的？如果是，求出其 $L_{2}$ 增益的上界。

5.17 (见文献[77])考虑系统

$$\dot {x} = f (x) + G (x) u, \quad y = h (x) + J (x) u$$

其中f,G,h和J是x的光滑函数。假设存在正常数 $\gamma$ ，满足 $\gamma^{2}I-J^{\mathrm{T}}(x)J(x)>0$ ，且对于任意x满足
