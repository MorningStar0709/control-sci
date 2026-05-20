# 2.6.1 基本原理

由 2.5 节的内容可知，由频率测试法或时域法可获得对象的精确模型。本节介绍一种基于精确模型极点配制的 PD 控制器设计方法。

假设被控对象为一电机模型传递函数：

$$G (s) = \frac {1 3 3}{s ^ {2} + 2 5 s} \tag {2.24}$$

取 a=25，b=133，则被控对象可表示为

$$\ddot {\theta} = - a \dot {\theta} + b u$$

式中， $\theta$ 为位置信号；u 为控制输入。

假设理想位置指令为 $\theta_{d}$ ，且跟踪误差为 $e=\theta-\theta_{d}$ ，则有 $\dot{\theta}=\dot{e}+\dot{\theta}_{d}$ ， $\ddot{\theta}=\ddot{e}+\ddot{\theta}_{d}$ ，则被控对象可写为

$$\ddot {e} + \ddot {\theta} _ {\mathrm{d}} = - a (\dot {e} + \dot {\theta} _ {\mathrm{d}}) + b u$$

将控制律设计为 PD 控制+前馈的形式，即

$$u = \frac {1}{b} \left(- k _ {\mathrm{p}} e - k _ {\mathrm{d}} \dot {e} + a \dot {\theta} _ {\mathrm{d}} + \ddot {\theta} _ {\mathrm{d}}\right) \tag {2.25}$$

将控制律代入式（2.24），可得闭环系统：

$$\ddot {e} + \ddot {\theta} _ {\mathrm{d}} = - a (\dot {e} + \dot {\theta} _ {\mathrm{d}}) + (- k _ {\mathrm{p}} e - k _ {\mathrm{d}} \dot {e} + a \dot {\theta} _ {\mathrm{d}} + \ddot {\theta} _ {\mathrm{d}})$$

整理得

$$\ddot {e} + \left(k _ {\mathrm{d}} + a\right) \dot {e} + k _ {\mathrm{p}} e = 0$$

为了使闭环系统稳定，需要满足 $s^{2}+(k_{\mathrm{d}}+a)s+k_{\mathrm{p}}$ 为 Hurwitz，即需要使

$s^{2}+(k_{\mathrm{d}}+a)s+k_{\mathrm{p}}=0$ 的特征根为负实部。

对于 k > 0，取特征根为 -k，由 $(s + k)^{2} = 0$ 可得 $s^{2} + 2ks + k^{2} = 0$ ，从而可设计 $k_{d} + a = 2k$ ， $k_{p} = k^{2}$ ，即 $k_{d} = 2k - a$ ， $k_{p} = k^{2}$ 。因此，可以通过 k 的设计得到 $k_{p}$ 和 $k_{d}$ ，从而实现控制律（2.25）的设计。

另外，也可采用Hurwitz判据进行设计，二阶系统 $a_2s^2 + a_1s + a_0 = 0$ 的稳定性充要条件为

$$
\left\{ \begin{array}{l} a _ {0}, a _ {1}, a _ {2} > 0 \\ \Delta_ {1} = a _ {1} > 0 \\ \Delta_ {1} = \left| \begin{array}{c c} a _ {1} & 0 \\ a _ {2} & a _ {0} \end{array} \right| = a _ {1} a _ {0} > 0 \end{array} \right.
$$

针对本问题，Hurwitz 判据对应的充要条件为 $k_{p} > 0$ ， $k_{d} + a > 0$ 。

![](image/5beb4f58bf5b46dda98621530bd6e21e19e81dbfca638965f9a08c8f6505dcfc.jpg)
