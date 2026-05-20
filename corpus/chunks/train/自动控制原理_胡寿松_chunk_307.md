# (2) 非周期函数的频谱

非周期函数可以看做是周期 $T \to \infty$ 的周期函数。若 $f(t)$ 为绝对可积函数，则 $f(t)$ 可以表示为傅氏积分

$$f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F (\mathrm{j} \omega) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega \tag {5-98}F (\mathrm{j} \omega) = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \tag {5-99}$$

$f(t)$ 和 $F(\mathrm{j}\omega)$ 构成傅氏变换对，而 $F(\mathrm{j}\omega)$ 表示 $f(t)$ 谐波的分布特性，也简称为频谱。与周期信号的频谱不同，非周期信号的频谱为连续谱，单个方波的幅值谱特性如图5-46所示。

![](image/b9a62c058f9871b58fbe7b6999b91ffabded34699a06b3dc45ae1745a29dca57.jpg)

<details>
<summary>line</summary>

| t | f(t) |
| --- | --- |
| -τ/2 | A |
| 0 | A |
| τ/2 | A |
</details>

(a) 单个方波

![](image/9800708a970b35c97157cc64ea46a418fff1afbc23536ca26f80a0dd26f616dc.jpg)  
(b) 频谱特性  
图 5-46 单个方波及其频谱特性

由图 5-46 可知, 当控制输入信号频谱特性具有收敛形式时, 可按跟踪要求选定常数 $\varepsilon$ , 若 $\omega > \omega_{b}$ 时, $|F(j\omega)| < \varepsilon$ , 从而确定系统所需要的带宽频率 $\omega_{b}$ 。

综上所述,系统的分析应区分输入信号的性质、位置,根据其频谱或谱密度以及相应的传递函数选择合适带宽,而系统的设计则主要围绕带宽来进行。为了设计合适的系统带宽,需要确定系统的闭环频率特性。
