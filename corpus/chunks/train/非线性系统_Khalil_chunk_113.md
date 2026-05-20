$$\dot {x} _ {i} = \frac {1}{C _ {i}} h _ {i} (x _ {i}) \left[ \sum_ {j} T _ {i j} x _ {j} - \frac {1}{R _ {i}} g _ {i} ^ {- 1} (x _ {i}) + I _ {i} \right]$$

其中 $i=1,2,\cdots,n$ ，状态变量 $x_{i}$ 是各放大器的输出电压，其值只能取自

$$H = \{x \in R ^ {n} \mid - V _ {M} < x _ {i} < V _ {M} \}$$

函数 $g_{i}:R\to (-V_{M},V_{M})$ 是S形函数，

$$h _ {i} (x _ {i}) = \left. \frac {d g _ {i}}{d u _ {i}} \right| _ {u _ {i} = g _ {i} ^ {- 1} (x _ {i})} > 0, \forall x _ {i} \in (- V _ {M}, V _ {M})$$

$I_{i}$ 是恒定电流输入， $R_{i} > 0,C_{i} > 0$ 。假设满足对称条件 $T_{ij} = T_{ji}$ ，则系统在 $H$ 内可能有几个平衡点。假设 $H$ 内的所有平衡点都是孤立的，由对称性 $T_{ij} = T_{ji}$ ，可知向量的第 $i$ 个分量

$$- \left[ \sum_ {j} T _ {i j} x _ {j} - \frac {1}{R _ {i}} g _ {i} ^ {- 1} (x _ {i}) + I _ {i} \right]$$

是标量函数的梯度向量。类似可变梯度法，通过积分可以证明标量函数为

$$V (x) = - \frac {1}{2} \sum_ {i} \sum_ {j} T _ {i j} x _ {i} x _ {j} + \sum_ {i} \frac {1}{R _ {i}} \int_ {0} ^ {x _ {i}} g _ {i} ^ {- 1} (y) d y - \sum_ {i} I _ {i} x _ {i}$$

该函数是连续可微的,但(典型地)不是正定的。将状态方程重写为

$$\dot {x} _ {i} = - \frac {1}{C _ {i}} h _ {i} (x _ {i}) \frac {\partial V}{\partial x _ {i}}$$

现在以 $V(x)$ 作为备选函数运用定理4.4。 $V(x)$ 沿系统轨线的导数为

$$\dot {V} (x) = \sum_ {i = 1} ^ {n} \frac {\partial V}{\partial x _ {i}} \dot {x} _ {i} = - \sum_ {i = 1} ^ {n} \frac {1}{C _ {i}} h _ {i} \left(x _ {i}\right) \left(\frac {\partial V}{\partial x _ {i}}\right) ^ {2} \leqslant 0$$

且 $\dot{V} (x) = 0\Rightarrow \frac{\partial V}{\partial x_i} = 0\Rightarrow \dot{x}_i = 0,\forall i$

因此，仅在平衡点处有 $\dot{V}(x)=0$ 。为了运用定理4.4，需要构造集合 $\Omega$ 。设

$$\Omega (\varepsilon) = \{x \in R ^ {n} \mid - (V _ {M} - \varepsilon) \leqslant x _ {i} \leqslant (V _ {M} - \varepsilon) \}$$

其中， $\varepsilon > 0$ 任意小， $\Omega(\varepsilon)$ 是有界闭集，且在 $\Omega(\varepsilon)$ 内有 $\dot{V}(x) \leqslant 0$ 。下面要证明 $\Omega(\varepsilon)$ 是正的不变集，即始于 $\Omega(\varepsilon)$ 内的每条轨线在所有未来时刻都始终在 $\Omega(\varepsilon)$ 内。为了简化分析，假设一种 S 形函数 $g_i(\cdot)$ 的特殊形式。设

$$g _ {i} \left(u _ {i}\right) = \frac {2 V _ {M}}{\pi} \arctan \left(\frac {\lambda \pi u _ {i}}{2 V _ {M}}\right), \quad \lambda > 0$$

则 $\dot{x}_i = \frac{1}{C_i} h_i(x_i)\left[\sum_j T_{ij}x_j - \frac{2V_M}{\lambda\pi R_i}\tan \left(\frac{\pi x_i}{2V_M}\right) + I_i\right]$

当 $|x_{i}|\geqslant V_{M}-\varepsilon$ 时，有

$$\left| \tan \left(\frac {\pi x _ {i}}{2 V _ {M}}\right) \right| \geqslant \tan \left(\frac {\pi (V _ {M} - \varepsilon)}{2 V _ {M}}\right) \to \infty , \quad \text {当} \varepsilon \to 0$$

由于 $x_{i}$ 和 $I_{i}$ 有界，可选择 $\varepsilon$ 足够小，以保证
