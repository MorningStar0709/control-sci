# 二次最优控制问题解的存在性

根据7.1节，如果Bellman方程存在“非零解”，则存在最优控制综合函数。因此我们只须检验Bellman方程有非零解的条件是否满足以及如何求得Bellman方程的解。

注意在式 (7.3.4) 中， $l(x,u,t)=\frac{1}{2}\left[x^{\mathrm{T}}Q(t)x+u^{\mathrm{T}}R(t)u\right]>0,\forall u\neq0$ ，从而注7.1.5的假设成立。再考察带终端条件的Bellman方程

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in \mathbb {R} ^ {r}} \left\{\frac {\partial J}{\partial x} (A (t) x + B (t) u) + \frac {1}{2} \left(x ^ {\mathrm{T}} Q (t) x + u ^ {\mathrm{T}} R (t) u\right) \right\} = 0, \\ J \left(x \left(t _ {f}\right), t _ {f}\right) = \frac {1}{2} x ^ {\mathrm{T}} \left(t _ {f}\right) F x \left(t _ {f}\right). \end{array} \right. \tag {7.3.12}
$$

易知

$$u \left(x, \frac {\partial J}{\partial x}, t\right) = - R ^ {- 1} (t) B ^ {T} (t) \left(\frac {\partial J}{\partial x}\right) ^ {T} \tag {7.3.13}$$

满足

$$
\begin{array}{l} \frac {\partial J}{\partial t} + \min _ {u \in \mathbb {R} ^ {r}} \left\{\frac {\partial J}{\partial x} [ A (t) x + B (t) u ] + \frac {1}{2} \left(x ^ {T} Q (t) x + u ^ {T} R (t) u\right) \right\} \\ = \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} A (t) x + \frac {1}{2} x ^ {T} Q (t) x - \frac {1}{2} \frac {\partial J}{\partial x} B (t) R ^ {- 1} (t) B ^ {T} (t) \left(\frac {\partial J}{\partial x}\right) ^ {T} = 0. \\ \end{array}
$$

于是我们考虑偏微分方程终值问题

$$
\left\{ \begin{array}{l} \frac {\partial J}{\partial t} + \frac {\partial J}{\partial x} A (t) x + \frac {1}{2} x ^ {T} Q (t) x - \frac {1}{2} \frac {\partial J}{\partial x} B (t) R ^ {- 1} (t) B ^ {T} (t) \left(\frac {\partial J}{\partial x}\right) ^ {T} = 0, \\ J (x (t _ {f}), t _ {f}) = \frac {1}{2} x ^ {T} (t _ {f}) F x (t _ {f}). \end{array} \right. \tag {7.3.14}
$$

如果取 $J(x,t) = \frac{1}{2} x^{\mathrm{T}}P(t)x, P(t)$ 为定义在 $[t_0,t_f]$ 的正定对称 $n\times n$ 可微矩阵值函数，则从方程(7.3.14）可得

$$\frac {1}{2} x ^ {\mathbf {T}} \left(\dot {P} (t) + P (t) A (t) + A ^ {\mathbf {T}} (t) P (t) + Q (t) - P (t) B (t) R ^ {- 1} (t) B ^ {\mathbf {T}} (t) P (t)\right) x = 0.$$

因此当终端值问题 (7.3.10) 在 $[t_0, t_f)$ 上存在正定对称解阵 $P^*(t)$ 时，有 $J^*(x, t) \stackrel{\mathrm{def}}{=} \frac{1}{2} x^{\mathbf{T}} P^*(t) x > 0$ ，且 $J^*(t_f, x(t_f)) = \frac{1}{2} x^{\mathbf{T}}(t_f) F x(t_f) \geqslant 0$ . 由此可见

$$u ^ {*} (x, t) \stackrel {\text { def }} {=} - R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P ^ {*} (t) x \tag {7.3.15}$$

和 $J^{*}(x,t)$ 一起构成带终值条件 Bellman 方程 (7.3.12) 的全局 $C^{1}$ “非零解”， $u^{*}(x,t)$ 是二次最优控制问题的综合函数.
