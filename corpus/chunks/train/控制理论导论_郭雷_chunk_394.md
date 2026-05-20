# 解析半群

下面我们假定 $X$ 是复Banach空间.

定义5.3.6 对于 $0 < \theta < \pi$ ，设 $\Sigma_{\theta}$ 表示复平面上的扇形部分：

$$\Sigma_ {\theta} = \left\{z \in \mathbb {C} \mid z \neq 0, | \arg z | < \theta \right\}.$$

$X$ 上的解析半群是指 $X$ 中满足下列条件的一族有界线性算子 $\{T(z) \mid z \in \Sigma_{\theta} \cup \{0\}\}$ :

(1) $T(z_{1} + z_{2}) = T(z_{1})T(z_{2}),\forall z_{1},z_{2}\in \Sigma_{\theta};$   
(2) $T(0) = I, \lim_{z \in \Sigma_{\theta}, z \to 0} T(z)x = x, \forall x \in X;$

(3) $T(z)$ 在 $\Sigma_{\theta}$ 中是解析的.

从定义5.3.6可知 $\{T(t) \mid t \geqslant 0\}$ 是 $X$ 上的 $C_0$ 半群. 设 $A$ 是 $\{T(t) \mid t \geqslant 0\}$ 的生成算子, 也称为 $\{T(z) \mid z \in \Sigma_\theta\}$ 的生成算子. 我们想知道在什么情形下, 一个 $C_0$ 半群能够延拓为某扇形域 $\Sigma_\theta$ 中一解析半群.

设 $A$ 是 $X$ 中一闭稠定线性算子. 我们说 $A$ 满足假设 (H), 是指它满足:

(H1) 对于某个 $\delta_0 \in (0, \pi/2)$ 和 $\omega \in \mathbb{R}$ , $\Sigma_{\delta_0 + \pi/2}(\omega) \subset \rho(A)$ , 其中

$$\Sigma_ {\delta_ {0} + \pi / 2} (\omega) \stackrel {{\mathrm{def}}} {{=}} \left\{\lambda = \omega + r e ^ {i \varphi} \mid r > 0, | \varphi | < \delta_ {0} + \pi / 2 \right\};$$

(H2) 存在一正常数 $M$ 使得

$$\| R (\lambda ; A) \| \leqslant \frac {M}{| \lambda - \omega |}, \quad \forall \lambda \in \Sigma_ {\delta_ {0} + \pi / 2} (\omega).$$

对于满足假设 (H) 的算子 $A$ , 当 $t > 0$ 时我们定义 $(T(0) = I)$

$$T (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\varepsilon , \theta}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda , \qquad t > 0, \tag {5.3.47}$$

其中 $\Gamma_{\varepsilon, \theta}$ 在 $\Sigma_{\delta_0 + \pi / 2}(\omega)$ 中的积分路径由如下三部分组成 (图5.3.1):

$$
\begin{array}{l} \Gamma_ {\epsilon , \theta} ^ {1} = \left\{\lambda \in \mathbb {C} \mid \lambda = \omega + r e ^ {- i \theta}, r \geqslant \varepsilon \right\}, \\ \Gamma_ {\varepsilon , \theta} ^ {2} = \left\{\lambda \in \mathbb {C} \mid \lambda = \omega + \varepsilon \mathrm{e} ^ {\mathrm{i} \varphi}, | \varphi | \leqslant \theta \right\}, \\ \Gamma_ {\varepsilon , \theta} ^ {3} = \left\{\lambda \in \mathbb {C} \mid \lambda = \omega + r e ^ {i \theta}, r \geqslant \varepsilon \right\}, \\ \end{array}
$$

其中 $\varepsilon > 0, \theta = \pi / 2 + \delta, 0 < \delta < \delta_0$ ，并且 $\Gamma_{\varepsilon, \theta}$ 的定向为沿着 $\operatorname{Im} \lambda$ 增加的方向。注意，由于 $\pi / 2 < \theta < \pi$ ，(5.3.47) 中的积分是收敛的，而且与 $\varepsilon$ 和 $\theta$ 的选择无关，这一点容易从正则函数的 Cauchy 定理推出。

![](image/44756835ba59b677651467b4f31484f7569c59a75d09b2ea7610bcc3209dd617.jpg)

<details>
<summary>text_image</summary>

Γ¹ε,θ
Γ²ε,θ
Γ¹ε,θ
</details>
