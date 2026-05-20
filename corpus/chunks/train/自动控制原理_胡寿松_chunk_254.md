# 1. 频率特性的基本概念

首先以图 5-1 所示的 RC 滤波网络为例, 建立频率特性的基本概念。设电容 C 的初始电压为 $u_{v_{0}}$ , 取输入信号为正弦信号

$$u _ {i} = A \sin \omega t \tag {5-1}$$

记录网络的输入、输出信号。当输出响应 $u_{o}$ 呈稳态时，记录曲线如图 5-2 所示。

由图 5-2 可见, RC 网络的稳态输出信号仍为正弦信号, 频率与输入信号的频率相同, 幅值较输入信号有一定衰减, 其相位存在一定延迟。

![](image/b78be5a883a3e8b1dc4da039e1e688e56e3593b30ce83aed842797342ad6abba.jpg)

<details>
<summary>text_image</summary>

R
uᵢ
C
uₒ
</details>

图 5-1 RC 滤波网络

![](image/95dc8c251be93cc93454e82dd06cc78afd03faf2cf40ee39745e511b15abc7b1.jpg)

<details>
<summary>line</summary>

| Time (t) | u₁ (A) | u₀ (A) |
| --- | --- | --- |
| 0 | 0 | 0 |
| π/ω | π/ω | π/ω |
| 2π/ω | 2π/ω | 2π/ω |
| t | 0 | 0 |
</details>

图 5-2 RC 网络的输入和稳态输出信号

RC 网络的输入和输出的关系可由以下微分方程描述：

$$T \frac {\mathrm{d} u _ {o}}{\mathrm{d} t} + u _ {o} = u _ {i} \tag {5-2}$$

式中， $T = RC$ .为时间常数。取拉氏变换并代入初始条件 $u_{o}(0) = u_{u_{0}}$ ，得

$$U _ {o} (s) = \frac {1}{T s + 1} \left[ U _ {i} (s) + T u _ {o _ {0}} \right] = \frac {1}{T s + 1} \left(\frac {A \omega}{s ^ {2} + \omega^ {2}} + T u _ {o _ {0}}\right) \tag {5-3}$$

再由拉氏反变换求得

$$u _ {o} (t) = \left(u _ {v _ {0}} + \frac {A \omega T}{1 + T ^ {2} \omega^ {2}}\right) \mathrm{e} ^ {- \frac {t}{T}} + \frac {A}{\sqrt {1 + T ^ {2} \omega^ {2}}} \sin (\omega t - \arctan \omega T) \tag {5-4}$$

式中第一项，由于 $T > 0$ ，将随时间增大而趋于零，为输出的瞬态分量；而第二项正弦信号为输出的稳态分量

$$
\begin{array}{l} u _ {o _ {s}} (t) = \frac {A}{\sqrt {1 + T ^ {2} \omega^ {2}}} \sin (\omega t - \arctan \omega T) \\ = A \cdot A (\omega) \sin [ \omega t + \varphi (\omega) ] \tag {5-5} \\ \end{array}
$$

在式(5-5)中， $A(\omega)=\frac{1}{\sqrt{1+T^{2}\omega^{2}}},\varphi(\omega)=-\arctan\omega T$ ，分别反映RC网络在正弦信号作用下，输出稳态分量的幅值和相位的变化，称为幅值比和相位差，且皆为输入正弦信号频率 $\omega$ 的函数。

注意到RC网络的传递函数为

$$G (s) = \frac {1}{T s + 1} \tag {5-6}$$

取 $s = \mathrm{j}\omega$ ，则有

$$G (\mathrm{j} \omega) = G (s) \mid_ {s = \mathrm{j} \omega} = \frac {1}{\sqrt {1 + T ^ {2} \omega^ {2}}} \mathrm{e} ^ {- \mathrm{j} \arctan \omega T} \tag {5-7}$$

比较式(5-5)和式(5-7)可知， $A(\omega)$ 和 $\varphi(\omega)$ 分别为 $G(\mathrm{j}\omega)$ 的幅值 $|G(\mathrm{j}\omega)|$ 和相角 $\angle G(\mathrm{j}\omega)$ 。这一结论非常重要，反映了 $A(\omega)$ 和 $\varphi(\omega)$ 与系统数学模型的本质关系，具有普遍性。

设有稳定的线性定常系统，其传递函数为

$$G (s) = \frac {\sum_ {i = 0} ^ {m} b _ {i} s ^ {m - i}}{\sum_ {i = 0} ^ {n} a _ {i} s ^ {n - i}} = \frac {B (s)}{A (s)} \tag {5-8}$$

系统输入为谐波信号

$$r (t) = A \sin (\omega t + \varphi) \tag {5-9}R (s) = \frac {A (\omega \cos \varphi + s \sin \varphi)}{s ^ {2} + \omega^ {2}} \tag {5-10}$$

由于系统稳定,输出响应稳态分量的拉氏变换
