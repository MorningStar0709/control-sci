# 定义 4.6 对于系统(4.32)

\- 如果存在一个与 $t_0$ 无关的正常数 $c, t_0 \geqslant 0$ , 对于每个 $a \in (0, c)$ , 存在与 $t_0$ 无关的 $\beta = \beta(a) > 0$ , 满足

$$\| x (t _ {0}) \| \leqslant a \Rightarrow \| x (t) \| \leqslant \beta , \forall t \geqslant t _ {0} \tag {4.33}$$

则系统的解是一致有界的。

\- 如果式(4.33)对于任意大的 $a$ 都成立,则系统的解是全局一致有界的。

\- 如果存在与 $t_0$ 无关的正常数 $b$ 和 $c, t_0 \geqslant 0$ , 对于每个 $a \in (0, c)$ , 存在 $T = T(a, b) \geqslant 0$ 与 $t_0$ 无关, 满足

$$\| x (t _ {0}) \| \leqslant a \Rightarrow \| x (t) \| \leqslant b, \forall t \geqslant t _ {0} + T \tag {4.34}$$

则系统的解是一致毕竟有界的,且最终边界为 b。

\- 如果式(4.34)对于任意大的 $a$ 都成立, 则系统的解是全局一致毕竟有界的。

在自治系统的情况中,我们可能不再使用“一致”一词,因为自治系统的解仅与 $t - t_{0}$ 有关。

为理解李雅普诺夫分析法如何用于研究有界性和毕竟有界性,考虑一个连续可微的正定函数 $V(x)$ , 并假设对于某个 c > 0, $\{V(x) \leqslant c\}$ 是紧集。并设对于某个正常数 $\varepsilon < c$ , 有

$$\Lambda = \{\varepsilon \leqslant V (x) \leqslant c \}$$

假设 V 沿系统 $\dot{x}=f(t,x)$ 的轨线的导数满足

$$\dot {V} (t, x) \leqslant - W _ {3} (x), \quad \forall x \in \Lambda , \forall t \geqslant t _ {0} \tag {4.35}$$

其中 $W_{3}(x)$ 是连续正定函数。不等式(4.35)表明，集合 $\Omega_{c} = \{V(x)\leqslant c\}$ 和 $\Omega_{\varepsilon} = \{V(x)\leqslant \varepsilon \}$ 是两个正不变集，因为在边界 $\partial \Omega_c$ 和 $\partial \Omega_{\varepsilon}$ 上， $\dot{V}$ 为负。集合 $\Lambda, \Omega_c$ 和 $\Omega_{\varepsilon}$ 的示意图如图4.8所示。由于在 $\Lambda$ 内 $\dot{V}$ 为负，所以始于 $\Lambda$ 内的轨线一定沿 $V(x(t))$ 减小的方向运动。实际上， $V$ 在 $\Lambda$ 内满足定理4.8的不等式(4.22)和定理4.9的不等式(4.24)，因此轨线特性就好像原点是一致渐近稳定的，且对于某个KL类函数 $\beta$ ，满足形如

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0})$$

![](image/2384be33739aa68420701d6a01bcbd4ca88f578f407131ecff363b5dc5a04bf7.jpg)

<details>
<summary>text_image</summary>

Λ
Ωε
Ωc
</details>

图 4.8 集合 $\Lambda, \Omega_{\varepsilon}$ 和 $\Omega_{c}$

的不等式。函数 $V(x(t))$ 在有限时间内将连续递减，直到轨线进入 $\Omega_{\varepsilon}$ 内，且在未来时间始终保持在其内。轨线在有限时间内进入 $\Omega_{\varepsilon}$ 内可证明如下：设 $k = \min_{x\in \Lambda}W_3(x) > 0$ ，由于 $W_{3}(x)$ 连续，且 $\Lambda$ 为紧集，所以存在最小值。又由于 $W_{3}(x)$ 是正定的，所以最小值为正。于是

$$W _ {3} (x) \geqslant k, \quad \forall x \in \Lambda \tag {4.36}$$

不等式(4.35)和不等式(4.36)表示

$$\dot {V} (t, x) \leqslant - k, \quad \forall x \in \Lambda , \forall t \geqslant t _ {0}$$

因此 $V(x(t))\leqslant V(x(t_0)) - k(t - t_0)\leqslant c - k(t - t_0)$

上式说明 $V(x(t))$ 在时间区间 $[t_{0}, t_{0} + (c - \varepsilon)/k]$ 内减小到 $\varepsilon$ 。

在许多问题中,利用范数不等式可得到不等式 $\dot{V} \leqslant -W_{3}$ 。这种情况下,对于 $\mu > 0$ ,更可能得到
