3.11 当 $\varepsilon$ 与其标称值不同时, 推导例 2.6 中范德波尔振荡器的灵敏度方程。要求使用 x 轴的状态方程。

3.12 使用 z 轴上的状态方程重复上面的习题。

3.13 当参数 a, b, c 与其标称值 $a_{0}=1, b_{0}=0, c_{0}=1$ 不同时，推导系统

$$\dot {x} _ {1} = \arctan (a x _ {1}) - x _ {1} x _ {2}, \quad \dot {x} _ {2} = b x _ {1} ^ {2} - c x _ {2}$$

的灵敏度方程。

3.14 考虑系统

$$\dot {x} _ {1} = - \frac {1}{\tau} x _ {1} + \tanh (\lambda x _ {1}) - \tanh (\lambda x _ {2})\dot {x} _ {2} = - \frac {1}{\tau} x _ {2} + \tanh (\lambda x _ {1}) + \tanh (\lambda x _ {2})$$

其中 $\lambda$ 和 $\tau$ 是正常数。

(a) 当 $\lambda$ 和 $\tau$ 与其标称值 $\lambda_{0}$ 和 $\tau_{0}$ 不同时, 推导系统的灵敏度方程。

(b) 证明 $r = \sqrt{x_1^2 + x_2^2}$ 满足微分不等式

$$\dot {r} \leqslant - \frac {1}{\tau} r + 2 \sqrt {2}$$

(c) 运用比较引理证明状态方程的解满足不等式

$$\| x (t) \| _ {2} \leqslant e ^ {- t / \tau} \| x (0) \| _ {2} + 2 \sqrt {2} \tau (1 - e ^ {- t / \tau})$$

3.15 运用比较引理证明状态方程

$$\dot {x} _ {1} = - x _ {1} + \frac {2 x _ {2}}{1 + x _ {2} ^ {2}}, \qquad \dot {x} _ {2} = - x _ {2} + \frac {2 x _ {1}}{1 + x _ {1} ^ {2}}$$

的解满足不等式 $\| x(t)\| _2\leqslant e^{-t}\| x(0)\| _2 + \sqrt{2}\left(1 - e^{-t}\right)$

3.16 运用比较引理求标量方程

$$\dot {x} = - x + \frac {\sin t}{1 + x ^ {2}}, \quad x (0) = 2$$

的解的上界。

3.17 考虑方程(3.1)的初值问题,并设 $D \subset R^{n}$ 是包含 x = 0 的定义域。假设对于所有 $t \geqslant t_{0}$ ，方程(3.1)的解 $x(t)$ 属于 D，且在 $[t_{0}, \infty) \times D$ 上有 $\|f(t, x)\|_{2} \leqslant L \|x\|_{2}$ 。证明

$$\left| \frac {d}{d t} \left[ x ^ {\mathrm{T}} (t) x (t) \right] \right| \leqslant 2 L \| x (t) \| _ {2} ^ {2} \tag {a}\| x _ {0} \| _ {2} \exp [ - L (t - t _ {0}) ] \leqslant \| x (t) \| _ {2} \leqslant \| x _ {0} \| _ {2} \exp [ L (t - t _ {0}) ] \tag {b}$$

3.18 设 $y(t)$ 是非负标量函数, 满足不等式

$$y (t) \leqslant k _ {1} e ^ {- \alpha (t - t _ {0})} + \int_ {t _ {0}} ^ {t} e ^ {- \alpha (t - \tau)} [ k _ {2} y (\tau) + k _ {3} ] d \tau$$

其中 $k_{1}, k_{2}$ 和 $k_{3}$ 是非负常数, $\alpha$ 是正常数, 且满足 $\alpha > k_{2}$ 。运用 Gronwall-Bellman 不等式证明

$$y (t) \leqslant k _ {1} e ^ {- (\alpha - k _ {2}) (t - t _ {0})} + \frac {k _ {3}}{\alpha - k _ {2}} \left[ 1 - e ^ {- (\alpha - k _ {2}) (t - t _ {0})} \right]$$

提示: 取 $z(t) = y(t)e^{\alpha(t - t_{0})}$ ，并求 z 满足的不等式。

3.19 设 $f: R^n \to R^n$ 在定义域 $D \subset R^n$ 内是局部利普希茨的, $S \subset D$ 是紧集。证明存在一个正常数 $L$ , 使得对于所有 $x, y \in S$ , 有

$$\| f (x) - f (y) \| \leqslant L \| x - y \|$$

提示:集 S 可由有限个邻域覆盖,即

$$S \subset N (a _ {1}, r _ {1}) \cup N (a _ {2}, r _ {2}) \cup \dots \cup N (a _ {k}, r _ {k})$$

分别考虑下面两种情况：

- 对于某个 $i$ ，有 $x, y \in S \cap N(a_i, r_i)$   
- 对于任何 $i$ , 有 $x, y \notin S \cap N(a_i, r_i)$ 。在这种情况下， $\| x - y \| \geqslant c, c > 0$

第二种情况要用到 $f(x)$ 在S上一致有界。

3.20 证明: 如果 $f: R^{n} \rightarrow R^{n}$ 在 $W \subset R^{n}$ 上是利普希茨的, 那么 $f(x)$ 在 W 上就是一致连续的。
