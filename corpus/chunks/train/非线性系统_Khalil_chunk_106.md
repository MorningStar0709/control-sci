$$\frac {\partial g _ {i}}{\partial x _ {j}} = \frac {\partial g _ {j}}{\partial x _ {i}}, \forall i, j = 1, \dots , n$$

时, $g(x)$ 是某个标量函数 $V(x)$ 的梯度。在此条件下,首先选择 $g(x)$ ,使 $g^{\mathrm{T}}(x)f(x)$ 为负定的,然后由积分

$$V (x) = \int_ {0} ^ {x} g ^ {\mathrm{T}} (y) d y = \int_ {0} ^ {x} \sum_ {i = 1} ^ {n} g _ {i} (y) d y _ {i}$$

计算函数 $V(x)$ 。该积分路径是沿原点到 x 的任意路径 $^{①}$ ，一般取沿轴线的积分，即

$$
\begin{array}{l} V (x) = \int_ {0} ^ {x _ {1}} g _ {1} \left(y _ {1}, 0, \dots , 0\right) d y _ {1} + \int_ {0} ^ {x _ {2}} g _ {2} \left(x _ {1}, y _ {2}, 0, \dots , 0\right) d y _ {2} \\ + \dots + \int_ {0} ^ {x _ {n}} g _ {n} (x _ {1}, x _ {2}, \dots , x _ {n - 1}, y _ {n}) d y _ {n} \\ \end{array}
$$

上式中 $g(x)$ 的一些参数未定, 可通过选择这些参数以保证 $V(x)$ 正定。利用可变梯度法可得到例 4.4 中的李雅普诺夫函数。下面用更一般的系统说明此方法, 而不重复前面的例题。

例4.5 考虑二阶系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - h \left(x _ {1}\right) - a x _ {2} \\ \end{array}
$$

其中 $a > 0, h(\cdot)$ 为局部利普希茨函数， $h(0) = 0$ ，且当 $y \neq 0$ 时 $yh(y) > 0, y \in (-b, c), b$ 和 $c$ 为正常数。单摆方程是该系统的一个特例。为运用可变梯度法，选择一个二阶向量 $g(x)$ ，使其满足

$$\frac {\partial g _ {1}}{\partial x _ {2}} = \frac {\partial g _ {2}}{\partial x _ {1}}\dot {V} (x) = g _ {1} (x) x _ {2} - g _ {2} (x) [ h (x _ {1}) + a x _ {2} ] < 0, \quad \text {当} x \neq 0$$

且 $V(x) = \int_0^x g^{\mathrm{T}}(y)dy > 0,$ 当 $x\neq 0$

设 $g(x) = \left[ \begin{array}{l}\alpha (x)x_{1} + \beta (x)x_{2}\\ \gamma (x)x_{1} + \delta (x)x_{2} \end{array} \right]$

其中标量函数 $\alpha (\cdot),\beta (\cdot),\gamma (\cdot)$ 和 $\delta (\cdot)$ 待定。为了满足对称要求，有

$$\beta (x) + \frac {\partial \alpha}{\partial x _ {2}} x _ {1} + \frac {\partial \beta}{\partial x _ {2}} x _ {2} = \gamma (x) + \frac {\partial \gamma}{\partial x _ {1}} x _ {1} + \frac {\partial \delta}{\partial x _ {1}} x _ {2}$$

导数 $\dot{V} (x)$ 为

$$\dot {V} (x) = \alpha (x) x _ {1} x _ {2} + \beta (x) x _ {2} ^ {2} - a \gamma (x) x _ {1} x _ {2} - a \delta (x) x _ {2} ^ {2} - \delta (x) x _ {2} h (x _ {1}) - \gamma (x) x _ {1} h (x _ {1})$$

为了消去向量积项,选择

$$\alpha (x) x _ {1} - a \gamma (x) x _ {1} - \delta (x) h (x _ {1}) = 0$$

使

$$\dot {V} (x) = - [ a \delta (x) - \beta (x) ] x _ {2} ^ {2} - \gamma (x) x _ {1} h (x _ {1})$$

为了简化选择,令 $\delta(x)=\delta$ 为常数, $\gamma(x)=\gamma$ 为常数, $\beta(x)=\beta$ 为常数,那么 $\alpha(x)$ 仅与 $x_{1}$ 有关,同时选择 $\beta=\gamma$ 以满足对称性要求。这样,g(x)化简为

$$
g (x) = \left[ \begin{array}{c} a \gamma x _ {1} + \delta h (x _ {1}) + \gamma x _ {2} \\ \gamma x _ {1} + \delta x _ {2} \end{array} \right]
$$

通过积分,得到
