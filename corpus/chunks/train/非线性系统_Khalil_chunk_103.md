$$\| x \| \leqslant \delta \Rightarrow V (x) < \beta$$

那么， $B_{\delta}\subset \Omega_{\beta}\subset B_{r}$

并且 $x(0)\in B_{\delta}\Rightarrow x(0)\in \Omega_{\beta}\Rightarrow x(t)\in \Omega_{\beta}\Rightarrow x(t)\in B_r$

因此 $\| x(0)\| < \delta \Rightarrow \| x(t)\| < r\leqslant \varepsilon ,\forall t\geqslant 0$

说明平衡点 $x = 0$ 是稳定的。现在假设式(4.4)也成立，为证明渐近稳定性，需要证明当 $t$ 趋于无穷时， $x(t)$ 趋于零，即对于每个 $a > 0$ ，存在 $T > 0$ ，使对于所有 $t > T$ 都有 $\| x(t)\| < a$ 。重复前面的证明过程可知，对于每个 $a > 0$ ，可选择 $b > 0$ ，满足 $\Omega_b\subset B_a$ 。因此，足以证明当 $t$ 趋于无穷时， $V(x(t))$ 趋于零。由于 $V(x(t))$ 是单调递减函数，且下界为零

$$V (x (t)) \to c \geqslant 0 \text {当} t \to \infty$$

为证明 $c = 0$ ，采用反证法。假设 $c > 0$ ，由 $V(x)$ 的连续性可知，存在 $d > 0$ 使 $B_{d} \subset \Omega_{c}$ 。极限 $V(x(t)) \to c > 0$ 是指对于所有 $t \geqslant 0$ ，轨线 $x(t)$ 位于球 $B_{d}$ 之外。设 $-\gamma = \max_{d \leqslant \| x \| \leqslant r} \dot{V}(x)$ ，该式是成立的，因为连续函数 $\dot{V}(x)$ 在紧集 $\{d \leqslant \| x \| \leqslant r\}^{①}$ 上有最大值。由式(4.4)可知， $-\gamma < 0$ ，从而有

$$V (x (t)) = V (x (0)) + \int_ {0} ^ {t} \dot {V} (x (\tau)) d \tau \leqslant V (x (0)) - \gamma t$$

该不等式的右边最终为负,故与假设 c>0 相矛盾。

满足式(4.2)和式(4.3)的连续可微函数 $V(x)$ 称为李雅普诺夫函数。对于某个c>0，曲面 $V(x)=c$ 称为李雅普诺夫面或等位面。图4.2的李雅普诺夫面使定理更直观明了，它显示了当c增大时李雅普诺夫面的变化情况。条件 $\dot{V}\leqslant0$ 是指当轨线与李雅普诺夫面 $V(x)=c$ 相交，并会向 $\Omega_{c}=\{x\in R^{n}|V(x)\leqslant c\}$ 内运动，而永远不会再运动到该区域以外。当 $\dot{V}<0$ 时，轨线从一个李雅普诺夫面向内部c较小的李雅普诺夫面运动。随

![](image/450ea80b94da88622e62c5af6a9e1d82a63407352bfe1f4013ab9c60ac65c9b3.jpg)

<details>
<summary>text_image</summary>

c₁<c₂<c₃
V(x)=c₁
c₂
c₃
</details>

图 4.2 李雅普诺夫函数的等位面

着 c 的减小, 李雅普诺夫面 $V(x) = c$ 最终缩小到原点, 这说明轨线随着时间增加而趋于原点。如果只知道 $\dot{V} \leqslant 0$ , 并不能确定轨线是否趋于原点 $^{②}$ , 但可以肯定原点是稳定的, 因为通过要求初始条件 $x(0)$ 位于包含于任意球域 $B_{\varepsilon}$ 内的李雅普诺夫面内, 轨线就可以包含于该球域内。

满足条件(4.2)的函数 $V(x)$ 称为是正定的, 即 $V(x)$ 满足 $V(0) = 0$ , 且当 $x \neq 0$ 时 $V(x) > 0$ 。如果当 $x \neq 0$ 时 $V(x) \geqslant 0$ , 那么称 $V(x)$ 是半正定的。如果 $-V(x)$ 是正定的或半正定的, 那么称 $V(x)$ 是负定的或半负定的。如果 $V(x)$ 不属于上述四种情况中的任何一种, 那么称 $V(x)$ 为不定的。有了上述定义, 李雅普诺夫定理可重述为: 如果存在一个连续可微的正定函数 $V(x)$ , 使 $\dot{V}(x)$ 为半负定的, 那么原点是稳定的; 如果使 $\dot{V}(x)$ 为负定的, 那么原点是渐近稳定的。

有一类标量函数很容易确定其正定性,即二次型

$$V (x) = x ^ {\mathrm{T}} P x = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} p _ {i j} x _ {i} x _ {j}$$
