(i) $V(\pmb{x})$ 为正定；  
(ii) $\dot{V}(\boldsymbol{x}) \triangleq dV(\boldsymbol{x}) / dt$ 为负半定；  
(iii) 对任意 $x_0 \in X, V(\phi(t; x_0, 0)) \neq 0$ ;  
(iv) 当 $\| x\| \to \infty$ 时, 有 $V(x)\to \infty$ 。

则系统的原点平衡状态是大范围渐近稳定的。

例 给定连续时间的定常系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - x _ {1} - (1 + x _ {2}) ^ {2} x _ {2} \end{array} \right.
$$

易知 $(x_{1} = 0, x_{2} = 0)$ 为其唯一的平衡状态。现取 $V(x) = x_{1}^{2} + x_{2}^{2}$ ，且有：

(i) $V(x) = x_{1}^{2} + x_{2}^{2}$ 为正定。

$$
\begin{array}{l} = \left[ \begin{array}{l l} 2 x _ {1} & 2 x _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {2} \\ - x _ {1} - (1 + x _ {2}) ^ {2} x _ {2} \end{array} \right] \\ = - 2 x _ {2} ^ {2} \left(1 + x _ {2}\right) ^ {2} \\ \end{array}
$$

(ii) $\dot{V}(\boldsymbol{x})=\left[\frac{\partial V(\boldsymbol{x})}{\partial x_{1}}\quad\frac{\partial V(\boldsymbol{x})}{\partial x_{2}}\right]\left[\begin{matrix}\dot{x}_{1}\\ \dot{x}_{2}\end{matrix}\right]$

容易看出,除了两种情况

(a) $x_{1}$ 任意， $x_{2} = 0$   
(b) $x_{1}$ 任意， $x_{2} = -1$

时 $\dot{V} (x) = 0$ 以外，均有 $\dot{V} (x) < 0$ 。所以， $\dot{V} (x)$ 为负半定。

(iii) 检查是否 $\dot{V}(\phi(t; x_0, 0)) \neq 0$ 。考虑到使得 $\dot{V}(x) = 0$ 的可能性只有上述两种情况，所以问题归结为判断这两种情况是否为系统的受扰运动解。先考察情况 (a): 表 $\bar{\phi}(t; x_0, 0) = [x_1(t), 0]^T$ ，则由于 $x_2(t) \equiv 0$ 可导出 $\dot{x}_2(t) = 0$ ，将此代入系统的方程可得：

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) = 0 \\ 0 = \dot {x} _ {2} (t) = - (1 + x _ {2} (t)) ^ {2} x _ {2} (t) - x _ {1} (t) = - x _ {1} (t) \\ \end{array}
$$

这表明，除了点 $(x_{1} = 0, x_{2} = 0)$ 外， $\bar{\phi}(t; x_{0}, 0) = [x_{1}(t), 0]^{T}$ 不是系统的受扰运动解。再考察情况 (b)：表 $\tilde{\phi}(t; x_{0}, 0) = [x_{1}(t), -1]^{T}$ ，则由 $x_{2}(t) = -1$ 可导出 $\dot{x}_{2}(t) = 0$ ，将此代入系统的方程可得：

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) = - 1 \\ 0 = \dot {x} _ {2} (t) = - (1 + x _ {2} (t)) ^ {2} x _ {2} (t) - x _ {1} (t) = - x _ {1} (t) \\ \end{array}
$$

显然这是一个矛盾的结果，表明 $\bar{\phi}(t; x_0, 0) = [x_1(t), -1]^T$ 也不是系统的受扰运动解。综上分析可知， $\dot{V}(\phi(t; x_c, 0)) \neq 0$ 。

(iv) 当 $\| x\| = \sqrt{x_1^2 + x_2^2}\to \infty$ 时，显然有 $V(x) = \| x\| ^2\to \infty$

于是，根据结论3可以断言，此系统的原点平衡状态是大范围渐近稳定的。

李亚普诺夫意义下的稳定的判别定理 现来讨论系统平衡状态为李亚普诺夫意义下稳定的判别问题。对于时变系统的情况,其相应的判别定理为:

结论1[时变系统稳定的判别定理] 对于时变系统(4.31)，如果存在一个对 $\pmb{x}$ 和 $t$ 具有连续一阶偏导数的标量函数 $V(\pmb {x},t),V(\pmb {0},t) = 0$ ，和围绕原点的一个吸引区 $\Omega$ 使对一切 $\pmb {x}\in \Omega$ 和一切 $t\geqslant t_0$ 满足如下的条件：

(i) $V(x, t)$ 为正定且有界，

(ii) $\dot{V}(\pmb{x}, t)$ 为负半定且有界，

则系统原点平衡状态为 $\Omega$ 域内一致稳定。

对于定常系统的情况,其判别定理具有如下的形式:
