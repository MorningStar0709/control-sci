# 2.8.1 基本原理

设图 2-24 是一般的系统阶跃响应曲线，采用该曲线可以分析非线性 PID 控制器增益参数的构造思想，实现 PID 的三个调节参数在一定范围内的整定。

![](image/68d995a737f61c7321e43a62a6f9ea5d1de7d63d7ca318d9d750b97dd17ea3fb.jpg)

<details>
<summary>line</summary>

| t | Y(t) |
| --- | --- |
| 0 | 0 |
| t₁ | ~1.2 |
| t₂ | ~1.4 |
| t₃ | ~1.0 |
| t₄ | ~1.0 |
</details>

图 2-24 一般系统阶跃响应曲线

参考文献[8]，非线性整定的基本原理如下。

（1）比例增益参数 $k_{\mathrm{p}}$ ：在响应时间 $0 \leqslant t \leqslant t_1$ 段，为保证系统有较快的响应速度，比例增益参数 $k_{\mathrm{p}}$ 在初始时应较大，同时为了减小超调量，希望误差 $e_{\mathrm{p}}$ 逐渐减小时，比例增益也随之减小；在 $t_1 \leqslant t \leqslant t_2$ 段，为了增大反向控制作用，减小超调，期望 $k_{\mathrm{p}}$ 逐渐增大；在 $t_2 \leqslant t \leqslant t_3$ 段，为了使系统尽快回到稳定点，并不再产生大的惯性，期望 $k_{\mathrm{p}}$ 逐渐减小；在 $t_3 \leqslant t \leqslant t_4$ 段，期望 $k_{\mathrm{p}}$ 逐渐增大，作用与 $t_1 \leqslant t \leqslant t_2$ 段相同。显然，按上述变化规律， $k_{\mathrm{p}}$ 随误差 $e_{\mathrm{p}}$ 变化的大致形状如图2-25（a）所示，根据该图可以构造如下非线性函数

$$k _ {\mathrm{p}} (e _ {\mathrm{p}} (t)) = a _ {\mathrm{p}} + b _ {\mathrm{p}} (1 - \operatorname{sech} (c _ {\mathrm{p}} e _ {\mathrm{p}} (t))) \tag {2.28}$$

式中， $a_{p}$ 、 $b_{p}$ 、 $c_{p}$ 为正实常数。当误差 $e_{p}\rightarrow\pm\infty$ 时， $k_{p}$ 取最大值为 $a_{p}+b_{p}$ ；当 $e_{p}=0$ 时， $k_{p}$ 取最小值为 $a_{p}$ ； $b_{p}$ 为 $k_{p}$ 的变化区间，调整 $c_{p}$ 的大小可调整 $k_{p}$ 变化的速率。

（2）微分增益参数 $k_{d}$ ：在响应时间 $0\leqslant t\leqslant t_{1}$ 段，微分增益参数 $k_{d}$ 应由小逐渐增大，这样可以保证在不影响响应速度的前提下，抑制超调的产生；在 $t_{1}\leqslant t\leqslant t_{2}$ 段，继续增大 $k_{d}$ ，从而增大反向控制作用，减小超调量。在 $t_{2}$ 时刻，减小微分增益参数 $k_{d}$ ，并在随后的 $t_{2}\leqslant t\leqslant t_{4}$ 段再次逐渐增大 $k_{d}$ ，抑制超调的产生。根据 $k_{d}$ 的变化要求，在构造 $k_{d}$ 的非线性函数时应考虑到误差变化速率 $e_{v}$ 的符号。 $k_{d}$ 的变化形状如图2-25（b）所示，所构造的非线性函数为

$$k _ {\mathrm{d}} (e _ {\mathrm{p}} (t)) = a _ {\mathrm{d}} + b _ {\mathrm{d}} / (1 + c _ {\mathrm{d}} \exp (d _ {\mathrm{d}} \cdot e _ {\mathrm{p}} (t))) \tag {2.29}$$

式中， $e_{v}=e_{p}$ 为误差变化速率； $a_{d}$ 、 $b_{d}$ 、 $c_{d}$ 、 $d_{d}$ 为正实常数； $a_{d}$ 为 $k_{d}$ 的最小值； $a_{d}+b_{d}$ 为 $k_{d}$ 的最大值，当 $e_{p}=0$ 时， $k_{d}=a_{d}+b_{d}/(1+c_{d})$ ，调整 $d_{d}$ 的大小可调整 $k_{d}$ 的变化速率。

（3）积分增益参数 $k_{i}$ ：当误差信号较大时，希望积分增益不要太大，以防止响应产生震荡，有利于减小超调量；而当误差较小时，希望积分增益增大，以消除系统的稳态误差。根据积分增益的希望变化特性，积分增益参数 $k_{i}$ 的变化形状如图2-25（c）所示，其非线性函数可表示为

$$k _ {\mathrm{i}} (e _ {\mathrm{p}} (t)) = a _ {\mathrm{i}} \operatorname{sech} (c _ {\mathrm{i}} e _ {\mathrm{i}} (t)) \tag {2.30}$$
