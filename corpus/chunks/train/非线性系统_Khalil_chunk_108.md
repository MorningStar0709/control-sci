$$V (0) = 0 \quad \text {且} \quad V (x) > 0, \forall x \neq 0 \tag {4.5}\| x \| \rightarrow \infty \Rightarrow V (x) \rightarrow \infty \tag {4.6}\dot {V} (x) < 0, \forall x \neq 0 \tag {4.7}$$

那么，x=0 是全局渐近稳定的。

证明:给定任意一点 $p \in R^{n}$ ，设 $c = V(p)$ 。条件(4.6)表示对于任意 c > 0，存在 r > 0，只要 $\|x\| > r$ ，则 $V(x) > c$ 。因此 $\Omega_{c} \subset B_{r}$ ，说明 $\Omega_{c}$ 有界。其余证明同定理 4.1。

定理 4.2 称为 Barbashin-Krasovskii 定理。习题 4.8 给出了一个反例,证明该定理的径向无界条件是必要的。

例 4.6 再次考虑例 4.5 的系统。但这次假设对于所有 $y \neq 0, yh(y) > 0$ 成立。李雅普诺夫函数

$$
V (x) = \frac {\delta}{2} x ^ {\mathrm{T}} \left[ \begin{array}{c c} k a ^ {2} & k a \\ k a & 1 \end{array} \right] x + \delta \int_ {0} ^ {x _ {1}} h (y) d y
$$

对于所有 $x \in R^{2}$ 都为正定的，且径向无界。由于 0 < k < 1，其导数

$$\dot {V} (x) = - a \delta (1 - k) x _ {2} ^ {2} - a \delta k x _ {1} h (x _ {1})$$

对于所有 $x \in R^{2}$ 都是负定的, 所以原点是全局渐近稳定的。

△

如果原点 $x = 0$ 是系统的一个全局渐近稳定平衡点，那么它必是系统唯一的平衡点。这是因为如果存在另一个平衡点 $\bar{x}$ ，那么始于 $\bar{x}$ 的轨线在 $t \geqslant 0$ 时就会保持在 $\bar{x}$ 处，因而轨线不会趋于原点，这与原点是全局渐近稳定的要求相矛盾。因此，全局渐近稳定性不研究多平衡点系统的问题，如单摆系统。

定理4.1和定理4.2是关于确定平衡点稳定性和渐近稳定性的定理，还有关于确定非稳定平衡点不稳定的定理。在这些定理中，最常用的是Chetaev定理，即定理4.3。在给出定理之前，我们先引入几个在定理叙述中将要用到的名词。设 $V: D \to R$ 是包含原点 $x = 0$ 的 $D \subset R^n$ 上的一个连续可微函数。假设 $V(0) = 0$ ，且存在任意接近原点的某一点 $x_0$ ，满足 $V(x_0) > 0$ 。选择 $r > 0$ ，使球 $B_r = \{x \in R^n | \| x \| \leqslant r\}$ 包含在 $D$ 内，并设

$$U = \{x \in B _ {r} \mid V (x) > 0 \} \tag {4.8}$$

集合 $U$ 是包含在 $B_{r}$ 内的非空集，其边界是曲面 $V(x) = 0$ 和球 $\| x\| = r$ 。由于 $V(0) = 0$ ，所以原点在 $B_{r}$ 内，位于 $U$ 的边界上。注意 $U$ 可能包含不止一个分量。图4.5所示为当 $V(x) = (x_1^2 -x_2^2) / 2$ 时的集合 $U$ 。如果 $V(0) = 0$ ，且存在任意接近原点的某一点 $x_0$ ，满足 $V(x_0) > 0$ 总可以构造集合 $U$ 。

![](image/4000c9ef4c94f047a7e5646264a4edb552f6d9f36e87273e70d031eaa1b076bb.jpg)

<details>
<summary>text_image</summary>

x₂
x₂=x₁
Bᵣ
x₁
x₂=-x₁
</details>

图4.5 $V(x) = \frac{1}{2} (x_1^2 - x_2^2)$ 时的集合 $U$

定理 4.3 设 x=0 是方程(4.1)的平衡点。设 $V:D\rightarrow R$ 是连续可微函数，满足 $V(0)=0$ ，且对于具有任意小 $\|x_{0}\|$ 的某一点 $x_{0}$ ，有 $V(x_{0})>0$ 。按照式(4.8)定义一个集合 U，并假设在 U 内有 $\dot{V}(x)>0$ ，那么 x=0 就是非稳定平衡点。

证明: 点 $x_{0}$ 在 U 内, 且有 $V(x_{0}) = a > 0$ 。始于 $x(0) = x_{0}$ 的轨线 $x(t)$ 一定会离开集合 U。为了说明这一点, 注意到只要 $x(t)$ 在 U 内, 就有 $V(x(t)) \geqslant a$ , 这是因为在 U 内有 $\dot{V}(x) > 0$ 。设

$$\gamma = \min \{\dot {V} (x) \mid x \in U \text {和} V (x) \geqslant a \}$$

由于连续函数 $\dot{V}(x)$ 在紧集 $\{x\in U$ 和 $V(x)\geqslant a\} = \{x\in B_r$ 和 $V(x)\geqslant a\}$ ①内有最小值，所以上式成立。那么 $\gamma >0$ ，且有

$$V (x (t)) = V (x _ {0}) + \int_ {0} ^ {t} \dot {V} (x (s)) d s \geqslant a + \int_ {0} ^ {t} \gamma d s = a + \gamma t$$
