# 9.3 考虑系统

$$\dot {x} = f (t, x) + B u, y = C x, u = - g (t, y)$$

其中对于所有 $t \geqslant 0$ ，有 $f(t,0) = 0, g(t,0) = 0$ 和 $\|g(t,y)\| \leqslant \gamma \|y\|$ 。假设 $\dot{x} = f(t,x)$ 的原点是全局指数稳定的，并设 $V(t,x)$ 是一个李雅普诺夫函数，全局满足式(9.3)至式(9.5)。求 $\gamma$ 的一个边界 $\gamma^{*}$ ，使得当 $\gamma < \gamma^{*}$ 时，给定系统的原点是全局指数稳定的。

9.4 考虑扰动系统 $\dot{x} = Ax + B[u + g(t,x)]$

其中 $g(t,x)$ 是连续可微的,并且对于 r>0 满足 $\|g(t,x)\|_{2}\leqslant k\|x\|_{2},\forall t\geqslant0,\forall x\in B_{r}$ 。设 $P=P^{T}>0$ 是里卡蒂方程

$$P A + A ^ {\mathrm{T}} P + Q - P B B ^ {\mathrm{T}} P + 2 \alpha P = 0$$

的解,其中 $Q \geqslant k^{2}I, \alpha > 0$ 。证明 $u = -B^{T}Px$ 使得扰动系统的原点是稳定的。
