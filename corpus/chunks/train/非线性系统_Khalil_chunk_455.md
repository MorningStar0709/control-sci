逼近，上式是在忽略 $\varepsilon \delta$ 时得到的。设 $V(x)$ 是慢模型的李雅普诺夫函数， $W(\eta) = \eta^{\mathrm{T}}P_{0}\eta$ 是快模型的李雅普诺夫函数，其中 $P_{0}$ 是李雅普诺夫方程 $P_{0}A_{0} + A_{0}^{\mathrm{T}}P_{0}^{\mathrm{T}} = -I$ 的解。定义集合 $\Omega_{c}$ 为 $\Omega_{c} = \{V(x)\leqslant c\}$ ， $\Sigma$ 为 $\Sigma = \{W(\eta)\leqslant \rho \varepsilon^{2}\}$ ，选择 $c > 0$ ，使得 $\Omega_{c}$ 在式(14.91)和式(14.92)的吸引区内。具体分析可按如下两个基本步骤进行：第一步证明对于足够大的 $\rho$ ，存在 $\varepsilon_1^* > 0$ ，使得对于每个 $0 < \varepsilon \leqslant \varepsilon_1^*$ ，闭环系统的原点是渐近稳定的，且集合 $\Omega_{c} \times \Sigma$ 是吸引区的正不变子集。证明中要用到 $\eta$ 在 $\Omega_{c} \times \Sigma$ 中为 $O(\varepsilon)$ 。第二步证明对于任意有界 $\hat{x}(0)$ 和任意 $x(0) \in \Omega_{b}, 0 < b < c$ ，在 $\varepsilon_2^* > 0$ 时使得对于每个 $0 < \varepsilon \leqslant \varepsilon_2^*$ ，轨线在有限时间内进入集合 $\Omega_{c} \times \Sigma$ 。证明中要用到 $\Omega_{b}$ 在 $\Omega_{c}$ 内，且 $\gamma (\hat{x})$ 是全局有界的。因此存在一个时间 $T_{1} > 0$ ，与 $\varepsilon$ 无关，使得对于所有 $t\in [0,T_1]$ ，始于 $\Omega_{b}$ 的轨线都保持在 $\Omega_{c}$ 内。利用 $\eta$ 比指数模型 $(1 / \varepsilon)e^{-at / \varepsilon}$ 衰减快的结论，可证明在时间区间 $[0,T(\varepsilon)]$ 内轨线将进入集合 $\Omega_c\times \Sigma$ ，其中 $\lim_{\varepsilon \to 0}T(\varepsilon) = 0$ 。这样只要选择足够小的 $\varepsilon$ ，就可以保证 $T(\varepsilon) < T_{1}$ ，图14.21说明了这一特性。

全阶观测器(14.93)～(14.94)给出了在反馈控制律中代换 $(x_{1},x_{2})$ 的估计值 $(\hat{x}_{1},\hat{x}_{2})$ 。由于 $y=x_{1}$ 可测，因此在控制律中可以直接使用 $x_{1}$ ，而只用 $\hat{x}_{2}$ 代替 $x_{2}$ ，这样做并不影响闭环系统的分析，并可得到与前面相同的结论。另一方面，还可以采用降阶观测器

$$\dot {w} = - h (w + h y) + \phi_ {o} (\hat {x}, u) \tag {14.101}\hat {x} _ {2} = w + h y \tag {14.102}$$

估计 $\hat{x}_{2}$ ，其中对于某个正常数 $\alpha$ 和 $\varepsilon$ 且 $\varepsilon \ll 1$ ，有 $h = \alpha / \varepsilon$ 。不难看出，高增益降阶观测器（14.101）～（14.102）表现出峰化现象，且状态反馈控制的全局有界性与其在全阶观测器中的作用相同。

![](image/825c710c65b7db1c9b8271f20f9185e9ea80f07c69874dec2e8ee936983a1116.jpg)

<details>
<summary>text_image</summary>

η
O(1/ε)
O(ε)
x
Ωb
Ωc
</details>

图14.21 快速收敛到集合 $\Omega_{c} \times \Sigma$ 的示意图

高增益观测器基本上近似为一个微分器,这一点从一个特例,即标称函数 $\phi_{0}$ 取零时很容易看出,此时观测器是线性的。对于全阶观测器(14.93)\~(14.94),从y到 $\hat{x}$ 的传递函数为

$$
\frac {\alpha_ {2}}{(\varepsilon s) ^ {2} + \alpha_ {1} \varepsilon s + \alpha_ {2}} \left[\begin{array}{c}{{1 + (\varepsilon \alpha_ {1} / \alpha_ {2}) s}}\\{{s}}\end{array}\right]\rightarrow   \left[\begin{array}{c}{{1}}\\{{s}}\end{array}\right]    \text {当}   \varepsilon \rightarrow 0
$$

对于降阶观测器(14.101)\~(14.102)，从 $y$ 到 $\hat{x}_2$ 的传递函数为

$$\frac {s}{(\varepsilon / \alpha) s + 1} \rightarrow s \text {当} \varepsilon \rightarrow 0$$

因此,在一个小的频率区间内,当 $\varepsilon$ 足够小时,高增益观测器逼近 $\dot{y}$ 。

认识到高增益观测器基本近似于一个微分器后, 就可以理解测量噪声和未建模的高频传感器动力学因素对 $\varepsilon$ 的实际限制应为多小。尽管有这样的限制, 仍有高增益观测器的成功应用, 允许 $\varepsilon$ 在某一范围内取值 $^{①}$ 。
