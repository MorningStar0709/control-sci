# 例6.2 一个超前补偿器的频率响应特性

回顾第 5 章(式(5.70))的超前补偿的传递函数，它等价于

$$D _ {\mathrm{c}} (s) = K \frac {T s + 1}{\alpha T s + 1}, \quad \alpha < 1 \tag {6.8}$$

(1) 以解析的方法确定其频率响应特性并从结果讨论希望得到什么结论?

（2）对 $0.1 \leqslant \omega \leqslant 10$ ，用 Matlab 绘制 $D_{c}(j\omega)$ ，令 K = 1，T = 1， $\alpha = 0.1$ 。并验证由（1）问中的分析所预测出的特性。

解答。

(1) 解析求值。将 $s = j\omega$ 代入式(6.8)中，得

$$D _ {\mathrm{c}} (\mathrm{j} \omega) = K \frac {T \mathrm{j} \omega + 1}{\alpha T \mathrm{j} \omega + 1} \tag {312}$$

根据式 $(6.5)$ 和式 $(6.6)$ 可得幅值为

$$M = | D _ {\mathrm{c}} | = | K | \frac {\sqrt {1 + (\omega T) ^ {2}}}{\sqrt {1 + (\alpha \omega T) ^ {2}}}$$

且相位为

$$\phi = \angle (1 + \mathrm{j} \omega T) - \angle (1 + \mathrm{j} \alpha \omega T) = \arctan (\omega T) - \arctan (\alpha \omega T)$$

在很低的频率处，幅值恰好为 $|K|$ ，而在很高的频率处，幅值为 $|K / \alpha|$ 。因此，在非常高的频率处，幅值会更高。在很低的频率处，相位为零，且在很高的频率处相位又回到零。在中间频率处， $\arctan (\cdot)$ 函数的取值表明 $\phi$ 为正值。这些正是超前补偿的一般特性。

（2）计算机求值。前面曾经给出了为例3.6进行频率响应计算的一个Matlab语句。类似超前补偿的频率响应的语句如下。

```matlab
s = tf('s');
sysD = (s + 1) / (s / 10 + 1);
w = logspace(-1, 2); % determines frequencies over range of interest
[mag, phase] = bode(sysD, w); % computes magnitude and phase over frequency range of interest
loglog(w, squeeze(mag)), grid;
axis([0.1 100 1 10])
semilogx(w, squeeze(phase)), grid;
axis([0.1 100 0 60]) 
```

运行产生频率响应的幅值与相位的曲线如图 6.2 所示。

![](image/f9a9c7a760b4e3ec171f0c666fc9193d7d1c4a75e0a9791d930237cd83882ba4.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 幅值 (dB) |
| --- | --- |
| 0.1 | 1 |
| 1 | 10 |
| 10 | 20 |
| 100 | 20 |
</details>

![](image/c713a32085c1dda9c25ff856b315f457bb53afd6cc9a76cf1d296dea443bb630.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | φ(°) |
| --- | --- |
| 0.1 | 5 |
| 1 | 40 |
| 10 | 55 |
| 100 | 5 |
</details>

图 6.2 例 6.2 中超前补偿的幅值和相位

分析表明，低频幅值应该为 $K(=1)$ ，高频幅值应该为 $K/\alpha(=10)$ ，这两个结论都可以被幅值图证实。相位图也可以证实相位在高频处和低频处接近 0，且在中间值处为正。

在一些情况下，我们并不能得到好的系统模型，于是就希望通过用实验的方法来确定频率响应的幅值和相位，这时我们可以用带有变化频率的正弦曲线来激励系统。幅值 $M(\omega)$ 由测量在稳态下的任意频率的输出正弦曲线对输入正弦曲线的比值给出。相位 $\phi (\omega)$ 是输入与输出信号的相位测量差值。

许多关于系统动态响应的信息可从传递函数的幅值 $M(\omega)$ 和相位 $\phi (\omega)$ 的信息中得知。在最简单的情况下，如果信号是正弦曲线，那么 $M$ 和 $\phi$ 就可完全描述其响应。此外，如果输入是周期性的，则可构造傅里叶级数将输入分解为正弦曲线的和，根据每一部分的正弦曲线，计算 $M(\omega)$ 与 $\phi (\omega)$ ，这样就可以构建整体的响应。对于暂态输入，理解 $M$ 和 $\phi$ 意义的最好途径就是，将频率响应 $G(\mathrm{j}\omega)$ 与由拉普拉斯变换计算出的暂态响应相联系。例如，在图3.19b所示曲线中，我们描绘了系统的阶跃响应对于变化的 $\zeta$ 值的传递函数为
