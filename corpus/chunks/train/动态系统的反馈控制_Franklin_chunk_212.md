# 4.2.1 跟踪的系统类型

在如图 4.2 所示的单位反馈系统中，系统误差可以由式(4.8)来描述。如果我们仅考虑参考输入且设定 W=V=0，那么误差方程简化为

$$E = \frac {1}{1 + G D _ {\mathrm{cl}}} R = \mathcal {S} R, \quad \mathcal {S} = \frac {1}{1 + G D _ {\mathrm{cl}}} \tag {4.27}$$

考虑到多项式输入，我们令 $r(t) = t^k / k!1(t)$ ，其拉普拉斯变换式为 $R = \frac{1}{s^{k + 1}}$ 。在不考虑实际信号的单位时，用机械系统的基本术语来描述，即 $k = 0$ 的阶跃输入为位置输入， $k = 1$ 的斜坡输入为速度输入，当 $k = 2$ 时为加速度信号输入，对误差公式分别应用终值定理得

$$\lim _ {t \rightarrow + \infty} e (t) = e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} s E (s) \tag {4.28}= \lim _ {s \rightarrow 0} \frac {1}{1 + G D _ {\mathrm{cl}}} R (s) \tag {4.29}= \lim _ {s \rightarrow 0} s \frac {1}{1 + G D _ {\mathrm{cl}}} \frac {1}{s ^ {k + 1}} \tag {4.30}$$

我们首先考虑这样一个系统，其传递函数 $GD_{\mathrm{cl}}$ 在原点处无极点，也就是没有积分项，且系统的输入为单位阶跃输入 $R(s) = 1 / s$ ，因此 $r(t)$ 是一个阶次为零的多项式。此时，方程(4.30)简化为

$$e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} \frac {1}{1 + G D _ {\mathrm{cl}}} \frac {1}{s} \tag {4.31}\frac {e _ {\mathrm{ss}}}{r _ {\mathrm{ss}}} = \frac {e _ {\mathrm{ss}}}{1} = e _ {\mathrm{ss}} = \frac {1}{1 + G D _ {\mathrm{cl}} (0)} \tag {4.32}$$

其中： $r_{ss}=\lim_{t\to+\infty}r(t)=1$ 。

根据系统类型的定义可知，该系统为0型系统，此时，令 $GD_{\mathrm{cl}}(0) \stackrel{\mathrm{def}}{=} K_{\mathrm{p}}$ 为位置误差常数。注意上述方程为相对误差，如果参考输入为阶次大于1的多项式，导致误差将会无界增长。0型系统能够完全跟踪最高阶次为0的多项式输入信号。如果 $GD_{\mathrm{cl}}(s)$ 在原点处有一个极点，继续用这一方法考虑阶次为1的多项式输入信号，但可以用一个常用的设定对式(4.30)直接进行估计。对于这种情况，有必要对当 $s$ 趋于0时控制器和被控对象的反应进行描述。为此，将极点 $(s)$ 不在原点的项合并为函数 $GD_{\mathrm{clo}}(s)$ ，该项在 $s = 0$ 时为有限值，因此定义常值 $GD_{\mathrm{clo}}(0) = K_{\mathrm{n}}$ ，且闭环传递函数写为

$$G D _ {\mathrm{cl}} (s) = \frac {G D _ {\mathrm{clo}} (s)}{s ^ {n}} \tag {4.33}$$

例如，如果 $GD_{cl}$ 中不含积分项，则 n=0 。如果含有一个积分项，则 n=1 ，依此类推。将式(4.33)代入式(4.30)中可得

$$e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} \frac {1}{1 + \frac {G D _ {\mathrm{clo}} (s)}{s ^ {n}}} \frac {1}{s ^ {k + 1}} \tag {4.34}= \lim _ {s \rightarrow 0} \frac {s ^ {n}}{s ^ {n} + K _ {\mathrm{n}}} \frac {1}{s ^ {k}} \tag {4.35}$$

由此方程可知：如果 $n > k$ ，则 $e = 0$ ；如果 $n < k$ ，则 $e \to +\infty$ ；如果 $n = k = 0$ ，则 $e_{\mathrm{ss}} = \frac{1}{1 + K_{\mathrm{o}}}$

如果 $n=k\neq0$ ，则 $e_{ss}=1/K_{n}$ 。如上所述，如果 n=k=0，其输入为 0 阶多项式，即阶跃信号或位置信号，常数 $K_{o}$ 称作位置常数，记为 $K_{p}$ ，系统被定义为 0 型系统。当 n=k=1 时，输入为 1 阶多项式即斜坡或速度输入信号，常数 $K_{1}$ 为速度常数，记为 $K_{v}$ ，系统被定义为 1 型（读作“一型”）。用相似的方法，可以定义 2 型甚至更高型的系统。图 4.4 清晰地给出了一个 1 型系统在斜坡参考输入下的响应情况，且明确标出了输入与输出之间的误差值为 $\frac{1}{K_{v}}$ 。
