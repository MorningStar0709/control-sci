提示: 将平衡点平移到原点处, 并利用 $V = k_{1}y_{1}^{2} + k_{2}y_{2}^{2} + k_{3}y_{1}^{4}$ , 其中 $(y_{1}, y_{2})$ 是新坐标。

4.50 考虑系统 $\dot{x}=f(t,x);\quad f(t,0)=0$

其中 $\left[\frac{\partial f}{\partial x}\right]$ 是有界的,在原点的邻域内是x的利普希茨函数,在所有 $t\geqslant t_{0}\geqslant0$ 时对t一致。假设在x=0处的线性化后的原点是指数稳定的,并且系统的解满足

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall t \geqslant t _ {0} \geqslant 0, \forall \| x (t _ {0}) \| < c \tag {4.59}$$

其中 $\beta$ 是 KL 类函数, c 为某个正常数。

(a) 证明存在K类函数 $\alpha$ 和正常数 $\gamma$ ，满足

$$\| x (t) \| \leqslant \alpha (\| x (t _ {0}) \|) \exp [ - \gamma (t - t _ {0}) ], \quad \forall t \geqslant t _ {0}, \forall \| x (t _ {0}) \| < c$$

(b) 证明存在正常数 M, 可能与 c 有关, 使下列不等式成立:

$$\| x (t) \| \leqslant M \| x (t _ {0}) \| \exp [ - \gamma (t - t _ {0}) ], \quad \forall t \geqslant t _ {0}, \quad \forall \| x (t _ {0}) \| < c \tag {4.60}$$

(c) 如果不等式(4.59)全局成立,能说明不等式(4.60)也全局成立吗?

4.51 假设当 $\alpha_{1}(r)=k_{1}r^{a},\alpha_{2}(r)=k_{2}r^{a}$ 和 $W(x)\geqslant k_{3}\parallel x\parallel^{a}$ 时，定理4.18中的假设条件都成立。 $k_{1},k_{2},k_{3}$ 和 a 都是正常数。证明：当 $\beta(r,s)=kr\exp(-\gamma s),\alpha_{1}^{-1}(\alpha_{1}(\mu))=k\mu$ 时，不等式(4.42)和不等式(4.43)都成立，其中 $k=(k_{2}/k_{1})^{1/a},\gamma=k_{3}/(k_{2}a)$ 。

4.52 在定理 4.18 中, $V(t,x)=V(x)$ , 并假设不等式 (4.40) 代换为

$$\frac {\partial V}{\partial x} f (t, x) \leqslant - W _ {3} (x), \quad \forall W _ {4} (x) \geqslant \mu > 0$$

其中 $W_{3}(x)$ 和 $W_{4}(x)$ 是连续正定函数。在这种情况下，证明：式(4.42)和式(4.43)对每个初始状态 $x(t_0)\in \{V(x)\leqslant c\} \subset D$ 都是成立的，假设 $\{V(x)\leqslant c\}$ 是紧曲面，且 $\max_{W_4(x)\leqslant \mu}V(x) < c$

4.53（见文献[72]）考虑系统 $\dot{x} = f(t,x)$ ，并假定存在函数 $V(t,x)$ 满足

$$W _ {1} (x) \leqslant V (t, x) \leqslant W _ {2} (x), \forall \| x \| \geqslant r > 0\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) < 0, \forall \| x \| \geqslant r _ {1} \geqslant r$$

其中 $W_{1}(x)$ 和 $W_{2}(x)$ 是连续正定函数。证明该系统的解是一致有界的。

提示: 注意 $V(t, x)$ 不必正定。

4.54 对于下列每个标量系统,检测输入状态的稳定性:

(1) $\dot{x}=-(1+u)x^{3}$

(2) $\dot{x} = -(1 + u)x^{3} - x^{5}$

(3) $\dot{x} = -x + x^{2}u$

(4) $\dot{x} = x - x^3 + u$

4.55 研究下列各系统的输入-状态稳定性：

(1) $\dot{x}_1 = -x_1 + x_1^2 x_2,$

$$\dot {x} _ {2} = - x _ {1} ^ {3} - x _ {2} + u$$

(2) $\dot{x}_{1} = -x_{1} + x_{2},$

$$\dot {x} _ {2} = - x _ {1} ^ {3} - x _ {2} + u$$

(3) $\dot{x}_1 = x_2,$

$$\dot {x} _ {2} = - x _ {1} ^ {3} - x _ {2} + u$$

(4) $\dot{x}_1 = (x_1 - x_2 + u)(x_1^2 - 1)$ ,

$$\dot {x} _ {2} = (x _ {1} + x _ {2} + u) (x _ {1} ^ {2} - 1)$$

(5) $\dot{x}_1 = -x_1 + x_1^2 x_2,$
