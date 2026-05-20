对于任意 $x_0 \notin \Gamma = \Gamma^+ \cup \Gamma^-$ ，仅靠 $u^* = 1$ 或 $u^* = -1$ 都不能把 $x_0$ 最快地控制到原点。但是从 $x_0$ 开始在控制 $u^* = 1$ （或 $u^* = -1$ ）的作用下达到 $\Gamma^-(\Gamma^+)$ 后，再改为控制 $u^* = -1(u^* = 1)$ 作用，就能最快地达到原点。因此 $\Gamma$ 为系统的开关曲线，如图7.2.5所示。

注意 $\Gamma : x_{1} = -\frac{1}{2} x_{2}|x_{2}|$ 将相平面分为两部分 $R_{+}^{2}$ 和 $R_{-}^{2}$

$$\mathbb {R} _ {+} ^ {2}: x _ {1} < - \frac {1}{2} x _ {2} | x _ {2} |\mathbb {R} _ {-} ^ {2}: x _ {1} > - \frac {1}{2} x _ {2} | x _ {2} |$$

且当 $x_0 \in \mathbb{R}_+^2$ 时，有 $u^*(x_0) = 1$ ；当 $x_0 \in \mathbb{R}_-^2$ 时，有 $u^*(x_0) = -1$ ，而当 $x_0 \in \Gamma^+$ 时，有 $u^*(x_0) = 1$ ；当 $x_0 \in \Gamma^-$ 时有 $u^*(x_0) = -1$ 。从 $x_0 = (x_{10}, x_{20}) \in \mathbb{R}_+^2(\mathbb{R}_-^2)$ 开始的快速轨线示意如图7.2.6所示。

![](image/2096ada005ada622301329c6de63a6855d215885bc025c5aff6bb208b44916d6.jpg)

<details>
<summary>text_image</summary>

Γ
x₂
x₁
Γ⁺
</details>

图 7.2.5 开关曲线图

![](image/5f80b427ea68ccd1761eac97ab7627015caa4eb1ddc9675950884bd19cf7fbfc.jpg)

<details>
<summary>text_image</summary>

Γ⁻
(x₁₀, x₂₀)
u=−1
R²⁻
0
x₁
u=1
(x₁₀, x₂₀)
R⁺²
Γ⁺
</details>

图7.2.6

双积分系统快速控制综合函数 $u^{*}(x_{1},x_{2})$ 为

$$
u ^ {*} (x _ {1}, x _ {2}) = \left\{ \begin{array}{l l} 1, & \text {当} x _ {1} + \frac {1}{2} x _ {2} | x _ {2} | <   0, \text {或} x _ {1} + \frac {1}{2} x _ {2} | x _ {2} | = 0, x _ {2} <   0, \\ - 1, & \text {当} x _ {1} + \frac {1}{2} x _ {2} | x _ {2} | <   0, \text {或} x _ {1} + \frac {1}{2} x _ {2} | x _ {2} | = 0, x _ {2} > 0, \end{array} \right.
$$

或

$$u ^ {*} (x _ {1}, x _ {2}) = - \operatorname{sign} \left(x _ {1} + \frac {1}{2} x _ {2} | x _ {2} |\right)$$
