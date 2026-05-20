# 9.5.1 伯德图的含义与性质

图 9.5.1 所示的伯德图由上下两部分组成：上半部分是输出的振幅响应 $\left|G(j\omega_{i})\right|$ 随输入频率 $\omega_{i}$ 的变化，称为幅频图 (Magnitude Plot)，下半部分是输出的相位响应 $\angle G(j\omega_{i})$ 随输入频率 $\omega_{i}$ 的变化，称为相频图 (Phase Plot)。

![](image/56900a7d4c8c0b66a8993b7686430183b4de8693bde259ae9550e5a520e2f519.jpg)  
图9.5.1 伯德图示例

理解伯德图的含义,第一步是明确其横纵坐标轴的单位和意义。首先分析幅频图,其纵轴坐标是 $20 \log |G(j\omega_i)|$ , 单位是 dB, 即分贝 (Decibel)。各位读者对这个单位应该不陌生,在生活中分贝被用来描述噪声。例如, 60dB 是日常交流的声音强度, 80dB 是闹市区的声音强度, 二者之间差了 20dB, 而它们的功率相差了 100 倍。分贝最开始出现时被用来描述电话线路信号的丢失。Decibel 这个单词中的 “deci” 代表 1/10, “bel” 指的是 Alexander Bell——那位拥有电话专利的科学家。

分贝体现的是能量比值的概念,其定义为

$$
L _ {\mathrm{dB}} = 1 0 \log \frac {P _ {\mathrm{m}}}{P _ {\mathrm{r}}} \tag {9.5.1}
$$

其中， $\log$ 是以 10 为底的对数运算， $P_{\mathrm{m}}$ 是测量功率（Measurement Power）， $P_{\mathrm{r}}$ 是参考功率（Reference Power）。 $L_{\mathrm{dB}}$ 代表测量功率与参考功率的比值取对数再乘以 10，单位是 dB。例如，当 $P_{\mathrm{m}} = P_{\mathrm{r}}$ 时（测量功率等于参考功率），其结果为 $L_{\mathrm{dB}} = 10 \log 1 = 0 \mathrm{~dB}$ 。式(9.5.1)中取对数可以将很大的数量级用较小的数位表达，从而达到简化记录的效果。例如，测量功率是参考功率的 $\frac{P_{\mathrm{m}}}{P_{\mathrm{r}}} = 2.5 \times 10^{12}$ 倍，当使用式(9.5.1)时得到 $10 \log 2.5 \times 10^{12} \approx 124 \mathrm{~dB}$ 。另外，在图 9.5.1 中，幅频图的纵轴是 $20 \log |G(\mathrm{j} \omega_{\mathrm{i}})|$ ，而在式(9.5.1)中分贝的定义是 $10 \log \frac{P_{\mathrm{m}}}{P_{\mathrm{r}}}$ ，这是因为在频率响应中分析的是输出振幅 $M_{\mathrm{o}}$ 与输入振幅 $M_{\mathrm{i}}$ 之间的比值 $\frac{M_{\mathrm{o}}}{M_{\mathrm{i}}}$ ，而在式(9.5.1)中考虑的是功率之间的比值，而功率与振幅的平方成比例。因此使用振幅比时，式(9.5.1)变成

$$
L _ {\mathrm{dB}} = 1 0 \log \frac {P _ {\mathrm{m}}}{P _ {\mathrm{r}}} = 1 0 \log \left(\frac {M _ {\mathrm{o}}}{M _ {\mathrm{i}}}\right) ^ {2} = 2 0 \log \frac {M _ {\mathrm{o}}}{M _ {\mathrm{i}}} = 2 0 \log | G (\mathrm{j} \omega_ {\mathrm{i}}) | \tag {9.5.2}
$$

式(9.5.2)解释了伯德图中纵轴的由来, 当 $M_{\mathrm{o}} = M_{\mathrm{i}}$ 时, 输出与输入的振幅相同, 在伯德图中就是 $0 \mathrm{~dB}$ 。当 $M_{\mathrm{o}} = 10 M_{\mathrm{i}}$ 时, 输出振幅是输入振幅的 10 倍, 幅频图就显示 $20 \mathrm{~dB}$ 。而当 $M_{\mathrm{o}} = 0.1 M_{\mathrm{i}}$ 时, 幅频图则显示 $-20 \mathrm{~dB}$ 。幅频图的横轴是输入频率 $\omega_{\mathrm{i}}$ , 按照对数来分度 (10 倍分度)。

相较于幅频图,相频图就很容易理解,它的横轴与幅频图是一样的,纵轴以度为单位。

伯德图的一个重要性质来自对数的运算法则，即

$$
2 0 \log M N = 2 0 \log M + 2 0 \log N \tag {9.5.3}
$$

这个性质可以很好地运用在串联系统(控制或者滤波)中,如图9.5.2所示。其输入与输出的关系为

$$
\frac {X (s)}{U (s)} = G _ {1} (s) G _ {2} (s) \tag {9.5.4}
$$
