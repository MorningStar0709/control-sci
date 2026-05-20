第 6 章动态反馈控制器设计表现了其用途。补偿灵敏度函数被定义为(闭环传递函数另一种表述)

$$T \stackrel {\text { def }} {=} \frac {G D _ {\mathrm{cl}}}{1 + G D _ {\mathrm{cl}}} = 1 - S \tag {4.24}$$

这两个传递函数对反馈控制的设计非常重要，它们显示出反馈系统的基本关系（将在第6章中进一步研究），即

$$\mathcal {S} + \mathcal {T} = 1 \tag {4.25}$$

目前为止，我们所讨论的关于稳态误差的计算，都是在参考输入或干扰输入是常值的前提下得到的。当参考输入或干扰信号是正弦信号时，我们也可以得到极为相似的结论。这一点很重要，例如，在电力系统中，经常会出现由于电力线的干扰而产生的60Hz干扰信号。由于更加复杂的信号都是由一定频率范围内的不同频率的正弦信号组成的，并且可使用频率叠加来分析，这是此概念重要的另一个原因。又如，众所周知，人类听觉被限制在60Hz到15000Hz频率范围内，因而为声音高保真而设计的反馈放大器、扩音器系统必须能对这一频率范围内的正弦(单纯声调)信号实现准确跟踪。如果我们令图4.2所示反馈系统控制器的传递函数为 $D_{\mathrm{cl}}(s)$ ，被控对象的传递函数为 $G(s)$ ，那么整个系统对频率为 $\omega_{0}$ 的正弦信号的稳态开环增益为 $\left|G(\mathrm{j}\omega_{0})D_{\mathrm{cl}}(\mathrm{j}\omega_{0})\right|$ ，从而可知反馈系统的误差将为

$$\left| E \left(\mathrm{j} \omega_ {0}\right) \right| = \left| R \left(\mathrm{j} \omega_ {0}\right) \right| \left| \frac {1}{1 + G \left(\mathrm{j} \omega_ {0}\right) D _ {\mathrm{cl}} \left(\mathrm{j} \omega_ {0}\right)} \right| \tag {4.26}$$

为了使反馈系统误差在 $\omega_{\mathrm{o}}$ 频率输入时降到 $1\%$ ，就必须使 $\left|1 + GD_{\mathrm{cl}}\right|\geqslant 100$ ，或 $\left|G(\mathrm{j}\omega_{\mathrm{o}})D_{\mathrm{cl}}(\mathrm{j}\omega_{\mathrm{o}})\right|\geqslant 100$ 。因此对一个好的高保真放大器来说，在频率为 $2\pi \times 60\leqslant \omega \leqslant 2\pi \times 15000$ 的范围内，必须都能保持很高的回路增益。我们将在第6章中深入分析基于频率响应方法的设计。
