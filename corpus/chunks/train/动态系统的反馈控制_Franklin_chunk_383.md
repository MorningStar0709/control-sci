$$\omega_ {\mathrm{BW}} = \omega_ {\mathrm{n}} \sqrt {1 - 2 \zeta^ {2} + \sqrt {2 + 4 \zeta^ {4} - 4 \zeta^ {2}}}$$

假设 $\omega_{\mathrm{n}} = 1$ ，对 $0\leqslant \zeta \leqslant 1$ ，画出。

6.14 考虑系统具有传递函数

$$G (s) = \frac {A _ {0} \omega_ {0} s}{s ^ {2} + \frac {\omega_ {0}}{Q} s + \omega_ {0} ^ {2}}$$

这是一个带有品质因子 $Q$ 的调谐电路的模型。

(a) 解析计算传递函数的幅值和相位，将其表示成归一化频率 $\omega/\omega_{0}$ 的函数并进行绘图。其中 Q=0.5, 1, 2 和 5。

(b) 如果定义带宽为幅值在 $\omega_{0}$ 两侧各下降 3dB 时对应两频率之间的距离。请证明带宽由下式给出：

$$B W = \frac {1}{2 \pi} \left(\frac {\omega_ {0}}{Q}\right)$$

(c) Q 和 $\zeta$ 之间的关系是什么?

6.15 一个直流电压表如图 6.86 所示。因为指针有阻尼，所以其对阶跃输入的最大超调为 10%。

![](image/d90072f9995252bea0b2b662f3e4de5d0362564b041ec20bbf26eb53124477a8.jpg)

<details>
<summary>text_image</summary>

θ
I
T
k
v
</details>

$$I = 4 0 \times 1 0 ^ {- 6} \mathrm{kg} \cdot \mathrm{m} ^ {2}k = 4 \times 1 0 ^ {- 6} \mathrm{kg} \cdot \mathrm{m} ^ {2} / \mathrm{s} ^ {2}$$

T为输入力矩， $T=K_{m}v$

v为输入电压

$$K _ {\mathrm{m}} = 4 \times 1 0 ^ {- 6} \mathrm{N} \cdot \mathrm{m/V}$$

图 6.86 电压表

(a) 系统的无阻尼自然频率是多少?

(b) 系统的阻尼自然频率是多少?

(c) 用 Matlab 画出该系统的频率响应，确定怎样的输入频率可以产生最大幅值的输出？

(d) 现在用该电压表测量 1V 的交流输入，频率为 2rad/s。那么经过最初的过渡过程后，指针的指示值为多少？相对于输入，输出的相位滞后是多少？请利用系统的伯德图来回答这些问题。在 Matlab 中调用 lsim 命令来验证你在 (d) 问中的答案。
