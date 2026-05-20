![](image/03e3cfdbd670f8846494fbb729bb5fa441623bc020e385294557a60376a654d2.jpg)

<details>
<summary>text_image</summary>

S(ε)
S(δ)
x₀
x₀
φ(t; x₀, t₀)
H(ε)
</details>

图4.1 李亚普诺夫意义下的稳定平衡状态

$x_{0}$ 的稳定并不意味着其为一致稳定；而且，从实际的角度而言，常要求一致稳定，以便在任一初始时刻 $t_{0}$ 出现的受扰运动都是李亚普诺夫意义下为稳定的。

渐近稳定 动力学系统(4.20)的一个孤立平衡状态 $x_{e}$ 称为是渐近稳定的，如果：(i) $x_{e}$ 是李亚普诺夫意义下为稳定的，即满足上述关于稳定的定义。(ii)对 $\delta(\varepsilon,t_{0})$ 和任意给定的实数 $\mu>0$ ，对应地存在实数 $T(\mu,\delta,t_{0})>0$ ，使得由满足不等式(4.24)的任一初态 $x_{0}$ 出发的受扰运动都同时满足不等式

$$\left\| \phi (t; x _ {0}, t _ {0}) - x _ {c} \right\| \leqslant \mu , \quad \forall t \geqslant t _ {0} + T (\mu , \delta , t _ {0}) \tag {4.26}$$

渐近稳定的直观含义，以二维情形为例，见图4.2。其中，图（a）反映了运动的有界性，而图（b）反映了运动随时间变化过程的渐近性。而且，随着 $\mu \rightarrow 0$ 显然有 $T\to \infty$ ，因此当原点平衡状态 $x_{e}$ 为渐近稳定时，必成立

$$\lim _ {t \rightarrow \infty} \phi (t; x _ {0}, t _ {0}) = 0, \quad \forall x _ {0} \in S (\delta) \tag {4.27}$$

进一步，如果在上述定义中，实数 $\delta$ 和 $T$ 的大小都不依赖于初始时刻 $t_0$ ，那么称平衡状态 $x_{i}$ 是一致渐近稳定的。对于时变系统，一致渐近稳定比之渐近稳定更有意义。

![](image/5bda70b90649bcb94cf690289ccaeecba80d0b60183817f3a8784d52454acf7f.jpg)

<details>
<summary>text_image</summary>

S(ε)
S(δ)
φ(t; x₀, t₀)
H(ε)
(x₀
x₀
(ρ)
</details>

![](image/6b8726e48ecd80df6deb67dcce92070535b92f382643617d9081303e104bb9b3.jpg)

<details>
<summary>text_image</summary>

S(ε)
S(δ)
φ(t; x₀, t₀)
x₀
T
S(μ)
t
(b)
</details>

图4.2 渐近稳定平衡状态

从工程观点而言,渐近稳定比之稳定更为重要。实际上,渐近稳定即为工程意义下的稳定,而李亚普诺夫意义下的稳定则是工程意义下的临界不稳定。此外,为了确定地判断系统的稳定性,确定使系统为渐近稳定的最大区域 $S(\delta)$ 无疑是必要的,通常称这个区域

为平衡状态 $x_{e}$ 的吸引区。

大范围渐近稳定 如果以状态空间的任一有限非零点为初始状态 $x_0$ 的受扰运动 $\phi(t; x_0, t_0)$ 都是有界的，且成立

$$\lim _ {t \rightarrow \infty} \phi (t; x _ {0}, t _ {0}) = 0 \tag {4.28}$$

则称系统（4.20）的原点平衡状态 $x_{e} = 0$ 是大范围渐近稳定的。通常，也称大范围渐近稳定为全局渐近稳定，而称小范围渐近稳定为局部渐近稳定。显然，系统为大范围渐近稳定的必要前提是除了原点平衡状态外，不存在其他孤立平衡状态。对于线性系统，由于其满足叠加原理,所以当它为渐近稳定时,就一定是大范围渐近稳定的。在工程问题中,通常总是希望具有大范围稳定的特性。

![](image/e69e4583dcb7b6dde537b2bd7ec336f51246e106ade88f93eb620bee86c41495.jpg)

<details>
<summary>text_image</summary>

S(ε)
S(δ)
H(ε)
φ(t; x₀, t₀)
x₀
xₑ
</details>

图4.3 不稳定平衡状态

不稳定 考察动力学系统(4.20)，如果对于不管取多么大的有限实数 $\varepsilon > 0$ ，都不可能找到相应的实数 $\delta(\varepsilon, t_0) > 0$ ，使得由满足不等式

$$\left\| \boldsymbol {x} _ {0} - \boldsymbol {x} _ {c} \right\| \leqslant \delta (\varepsilon , t _ {0}) \tag {4.29}$$

的任一初态 $x_0$ 出发的运动满足不等式

$$\left\| \phi (t; x _ {0}, t _ {0}) - x _ {c} \right\| \leqslant \varepsilon , \quad \forall t \geqslant t _ {0} \tag {4.30}$$

对于二维的情形，表征不稳定的几何含义如图4.3所示。由图示可以看出，如果平衡状态 $x_{e}$ 是不稳定的，那么不管把域 $S(\varepsilon)$ 取得多么大，也不管把域 $S(\delta)$ 取得如何的小，必定至少存在一个非零点 $x_{0}^{*}\in S(\delta)$ ，使得由 $x_{0}^{*}$ 出发的运动轨线越出域 $S(\varepsilon)$ 。
