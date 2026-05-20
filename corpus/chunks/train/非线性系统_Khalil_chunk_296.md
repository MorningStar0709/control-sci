电路中有两个相似的 RC 节, 通过电阻 $R_{c}$ 连接。当 $R_{c}$ “相当大”时, 两个节之间的连接变得“很弱”。特别是, 当 $R_{c} = \infty$ 时, 连接为开路, 两节之间失去耦合。由该电路可推出其 $\varepsilon$ 耦合表达式, 即两节之间的耦合由一个小参数 $\varepsilon$ 确定。乍一看似乎选择 $\varepsilon$ 为 $\varepsilon = 1 / R_{c}$ 很合理。的确, 这样做就可以用 $\varepsilon$ 乘以上述方程中的耦合项, 然而该选择使 $\varepsilon$ 取决于物理参数的绝对值, 而这个物理参数的绝对值无论多小或多大, 在不考虑系统中其他物理参数的情况下都毫无意义。在一个完全由公式表示的扰动问题中, 把 $\varepsilon$ 选择为物理参数之间的一个比值, 这些物理参数能相对反映出 $\varepsilon$ “真的很小”。用该方法选择 $\varepsilon$ , 通常首先把状态变量或时间变量 (或两者) 选择为无量纲的量。在我们讨论的电路里, 显然应把状态变量选为 $v_{1}$ 和 $v_{2}$ 。但不用 $v_{1}$ 和 $v_{2}$ 进行计算, 而是按比例对它们进行缩放, 缩放后变量的极值应该接近 $\pm 1$ 。由于在这两个完全一样的电路之间存在弱耦合, 对于这两个状态变量, 应该使用相同的尺度因子 $\alpha$ 。定义状态变量为 $x_{1} = v_{1} / \alpha$ 和 $x_{2} = v_{2} / \alpha$ 。取无量纲的时间 $\tau = t / RC$ , 并记 $dx / d\tau = \dot{x}$ , 得状态方程为

$$\dot {x} _ {1} = \frac {E}{\alpha} - x _ {1} - \frac {R}{\alpha} \psi (\alpha x _ {1}) - \frac {R}{R _ {c}} (x _ {1} - x _ {2})\dot {x} _ {2} = \frac {E}{\alpha} - x _ {2} - \frac {R}{\alpha} \psi (\alpha x _ {2}) - \frac {R}{R _ {c}} (x _ {2} - x _ {1})$$

很明显,应当选择 $\varepsilon$ 为 $R/R_{c}$ 。假设 $R=1.5\times10^{3}\Omega,E=1.2\ V$ ，且非线性电阻是隧道二极管

$$\psi (v) = 1 0 ^ {- 3} \times \left(1 7. 7 6 v - 1 0 3. 7 9 v ^ {2} + 2 2 9. 6 2 v ^ {3} - 2 2 6. 3 1 v ^ {4} + 8 3. 7 2 v ^ {5}\right)$$

取 $\alpha = 1$ ，重写状态方程为

$$\dot {x} _ {1} = 1. 2 - x _ {1} - h \left(x _ {1}\right) - \varepsilon \left(x _ {1} - x _ {2}\right)\dot {x} _ {2} = 1. 2 - x _ {2} - h \left(x _ {2}\right) - \varepsilon \left(x _ {2} - x _ {1}\right)$$

其中， $h(v) = 1.5\times 10^{3}\times \psi (v)$ 。假设要解方程，其初始状态为

$$x _ {1} (0) = 0. 1 5; \quad x _ {2} (0) = 0. 6$$

令 $\varepsilon = 0$ ，可得去耦方程

$$\dot {x} _ {1} = 1. 2 - x _ {1} - h \left(x _ {1}\right), \quad x _ {1} (0) = 0. 1 5\dot {x} _ {2} = 1. 2 - x _ {2} - h \left(x _ {2}\right), \quad x _ {2} (0) = 0. 6$$

它们可以分别独立求解。设 $x_{10}(t)$ 和 $x_{20}(t)$ 是方程的解，根据定理10.1，它们给出了当 $\varepsilon$ 足够小时精确解的 $O(\varepsilon)$ 逼近。为了得到 $O(\varepsilon^2)$ 逼近，可以建立关于 $x_{11}$ 和 $x_{21}$ 的方程

$$\dot {x} _ {1 1} = - [ 1 + h ^ {\prime} (x _ {1 0} (t)) ] x _ {1 1} - [ x _ {1 0} (t) - x _ {2 0} (t) ], \quad x _ {1 1} (0) = 0\dot {x} _ {2 1} = - [ 1 + h ^ {\prime} (x _ {2 0} (t)) ] x _ {2 1} - [ x _ {2 0} (t) - x _ {1 0} (t) ], \quad x _ {2 1} (0) = 0$$

其中 $h'(\cdot)$ 是 $h(\cdot)$ 的导数。图 10.3 所示为当 $\varepsilon = 0.3$ 时的精确解与一阶和二阶逼近。

![](image/b439cd1b3d7e8f404e7d83af23c59b59f72d110f988c73de86b0b53e7a7982d0.jpg)

<details>
<summary>text_image</summary>

R
+
v₁
-
C
ψ(v₁)
ψ(v₂)
Rc
C
+
v₂
-
E
R
E
</details>

图10.2 例10.4的电路
