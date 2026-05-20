\- 如果式(14.109)的原点是指数稳定的,在 $\mathcal{X}=0$ 的某邻域内, $f(\mathcal{X})$ 是连续可微的,那么存在 $\varepsilon_{4}^{*}>0$ ,使得对于每个 $0<\varepsilon\leqslant\varepsilon_{4}^{*}$ ,闭环系统的原点是指数稳定的,且 $\mathcal{S}\times\mathcal{Q}$ 是吸引区的子集。

证明: 见附录 C.23。

该定理说明当 $\varepsilon$ 足够小时, 输出反馈控制器能够重现状态反馈控制器的性能, 这种性能重现表现在三个方面: (1) 指数稳定的重现; (2) 吸引区的重现, 从这个意义上讲, 可重现吸引区内的任何紧集; (3) 当 $\varepsilon$ 趋于零时, 输出反馈下的解 $\mathcal{X}(t)$ 逼近状态反馈下的解。为了方便起见, 对于指数稳定情况只说明渐近稳定性的重现①, 但要注意定理的前三条, 即有界性、毕竟有界性和轨线收敛性, 在没有指数稳定性的假设时仍成立。

作为上述定理的推论,显然如果状态反馈控制器在局部指数稳定时,可实现全局或半全局稳定,那么对于足够小的 $\varepsilon$ ,输出反馈控制器在局部指数稳定下,可实现半全局稳定。

例14.19 在14.1节中设计了连续滑模状态反馈控制器

$$u = - k \mathrm{sat} \left(\frac {a _ {1} (\theta - \pi) + \dot {\theta}}{\mu}\right)$$

其中 $a_1 = 1, k = 4, \mu = 1$ ，该控制器在 $(\theta = \pi, \dot{\theta} = 0)$ 处可稳定单摆方程

$$m \ell^ {2} \ddot {\theta} + m g _ {0} \ell \sin \theta + k _ {0} \ell^ {2} \dot {\theta} = u$$

假设现在只测量 $\theta$ ，则输出反馈控制器可取为

$$u = - k \mathrm{sat} \left(\frac {a _ {1} (\hat {\theta} - \pi) + \hat {\omega}}{\mu}\right)$$

其中 $\hat{\theta}$ 和 $\hat{\omega}$ 是 $\theta$ 和 $\omega = \hat{\theta}$ 的估计值，由高增益观测器

$$
\begin{array}{l} \dot {\hat {\theta}} = \hat {\omega} + (2 / \varepsilon) (\theta - \hat {\theta}) \\ \dot {\hat {\omega}} = \phi_ {0} (\hat {\theta}, u) + (1 / \varepsilon^ {2}) (\theta - \hat {\theta}) \\ \end{array}
$$

给出,这里 $\phi_0 = -\hat{a}\sin \hat{\theta} +\hat{c} u$ 是 $\phi = -(g_0 / \ell)\sin \theta -(k_0 / m)\theta +(1 / m\ell^2)u$ 的标称模型,式中 $\hat{a}$ 和 $\hat{c}$ 分别是 $(g_0 / \ell)$ 和 $(1 / m\ell^2)$ 的标称值,而摩擦系数 $k_{0}$ 的标称值取为零,设计的观测器具有多重极点 $-1 / \varepsilon$ 。图14.22比较了 $\varepsilon = 0.05$ 和 $\varepsilon = 0.01$ 时状态反馈控制器和输出反馈控制器的性能,单摆参数为 $m = 0.15,\ell = 1.05,k_0 = 0.02$ ，初始条件为 $\theta (0) = \pi /4$ $\omega (0) = \hat{\theta} (0) = \hat{\omega} (0) = 0$ ，我们考虑观测器的三种情况。第一种情况，观测器用的标称值为 $\hat{a} = 9.81$ 和 $\hat{c} = 10$ ，分别对应于标称参数 $\hat{m} = 0.1$ 和 $\hat{\ell} = 1$ 。第二种情况，用 $\hat{a} = 9.3429$ 和 $\hat{c} = 6.0469$ ，对应于实际参数 $\hat{m} = m = 0.15$ 和 $\hat{\ell} = \ell = 1.05$ 。第三种情况，采用线性观测器，即设定 $\hat{a} = \hat{c} = 0$ 。从各情况可看出，随着 $\varepsilon$ 的减小，输出反馈下的响应逼近状态反馈下的响应。而当 $\varepsilon$ 较大时，在 $\phi$ 的模型比较准确的情况下，观测器中还能够包括 $\phi_0$ ，但如果 $\phi$ 模型不准确，那么线性观测器会更好。这里提醒注意的是，随着 $\varepsilon$ 的减小，三种观测器之间的差异将逐渐消失，这正是我们所期望的，因为 $\varepsilon$ 的减小抵消了对 $\phi$ 建模时不确定因素的影响。

![](image/efa6ca9f595981aaf91855d8a3ad5d87a018414a75cdbe99f0e4d0fb79d53722.jpg)
