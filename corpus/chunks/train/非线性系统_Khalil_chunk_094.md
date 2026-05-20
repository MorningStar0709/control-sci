# 3.4 比较原理

研究状态方程 $\dot{x} = f(t,x)$ 时，常常需要计算其解 $x(t)$ 的边界，而不是解本身。Gronwall-Bellman不等式(见引理A.1)是用于这一目的的方法之一，另一方法就是比较引理。比较引理用于某一时间区间内，标量可微函数 $v(t)$ 的导数对于所有 $t$ 都满足形如 $\dot{v}(t)\leqslant f(t,v(t))$ 的不等式，该不等式称为微分不等式，满足这一不等式的函数 $v(t)$ 称为微分不等式的解。比较引理把微分不等式 $\dot{v}(t)\leqslant f(t,v(t))$ 的解与微分方程 $\dot{u} = f(t,u)$ 的解相比较。该引理甚至可用于当 $v(t)$ 不可微，但有一个满足微分不等式的上右导数 $D^{+}v(t)$ 时的情况。上右导数 $D^{+}v(t)$ 的定义见附录C.2。我们只需要知道下面两点：

\- 如果 $v(t)$ 对于 $t$ 可微, 那么 $D^{+}v(t) = \dot{v}(t)$ 。

\- 如果 $\frac{1}{h} |v(t + h) - v(t)| \leqslant g(t, h), \forall h \in (0, b]$

且 $\lim_{h\to 0^{+}}g(t,h) = g_0(t)$

那么, $D^{+}v(t)\leqslant g_{0}(t)$ 。

极限 $h \rightarrow 0^{+}$ 是指 h 从上面趋于零。

引理 3.4（比较引理） 考虑标量微分方程

$$\dot {u} = f (t, u), \quad u (t _ {0}) = u _ {0}$$

对于所有 $t \geqslant 0$ 和所有 $u \in J \subset R, f(t, u)$ 对于 $t$ 连续可微，且对于 $u$ 是局部利普希茨的。设 $[t_0, T)(T$ 可以是无限的）是解 $u(t)$ 存在的最大区间，并且假设对于所有 $t \in [t_0, T)$ ，有 $u(t) \in J$ 。设 $v(t)$ 是连续函数，其上右导数 $D^+ v(t)$ 对于所有 $t \in [t_0, T), v(t) \in J$ 满足微分不等式

$$D ^ {+} v (t) \leqslant f (t, v (t)), \quad v (t _ {0}) \leqslant u _ {0}$$

那么，对于所有 $t \in [t_0, T)$ ，有 $v(t) \leqslant u(t)$ 。

◇

证明: 见附录 C.2。

□

例3.8 标量微分方程 $\dot{x} = f(x) = -(1 + x^2)x, \quad x(0) = a$

对于某一 $t_1 > 0$ 在 $[0, t_1)$ 上有唯一解，这是因为 $f(x)$ 对 $x$ 是局部利普希茨的。设 $v(t) = x^2(t)$ ，则函数 $v(t)$ 是可微的，其导数为

$$\dot {v} (t) = 2 x (t) \dot {x} (t) = - 2 x ^ {2} (t) - 2 x ^ {4} (t) \leqslant - 2 x ^ {2} (t)$$

因此 $v(t)$ 满足微分不等式 $\dot{v}(t) \leqslant -2v(t), v(0) = a^2$

设 $u(t)$ 是微分方程 $\dot{u} = -2u, u(0) = a^2 \Rightarrow u(t) = a^2 e^{-2t}$

的解。所以根据比较引理, 解 $x(t)$ 对于所有 $t \geqslant 0$ 都有定义, 且满足

$$| x (t) | = \sqrt {v (t)} \leqslant e ^ {- t} | a |, \quad \forall t \geqslant 0$$

△

例3.9 标量微分方程 $\dot{x} = f(t,x) = -(1 + x^2)x + e^t,\quad x(0) = a$

对于某一 $t_1 > 0$ 在 $[0, t_1)$ 上有唯一解，这是因为 $f(t, x)$ 对于 $x$ 是局部利普希茨的。与上例相似，我们求 $|x(t)|$ 的上界。与例3.8一样，从 $v(t) = x^2(t)$ 开始。 $v$ 的导数为

$$\dot {v} (t) = 2 x (t) \dot {x} (t) = - 2 x ^ {2} (t) - 2 x ^ {4} (t) + 2 x (t) e ^ {t} \leqslant - 2 v (t) + 2 \sqrt {v (t)} e ^ {t}$$

可对此微分不等式应用比较引理,但得到的微分方程不易求解。考虑选择另一个 $v(t)$ ，设 $v(t)=|x(t)|$ ，当 $x(t)\neq0$ 时，函数 $v(t)$ 是可微的，其导数为

$$\dot {v} (t) = \frac {d}{d t} \sqrt {x ^ {2} (t)} = \frac {x (t) \dot {x} (t)}{| x (t) |} = - | x (t) | [ 1 + x ^ {2} (t) ] + \frac {x (t)}{| x (t) |} e ^ {t}$$

由于 $1 + x^{2}(t) \geqslant 1$ ，因此有 $-|x(t)|[1 + x^{2}(t)] \leqslant -|x(t)|$ 和 $v(t) \leqslant -v(t) + e^{t}$ 。而当 $x(t) = 0$ 时，有
