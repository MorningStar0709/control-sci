$$
\begin{array}{l} x _ {\mathrm{ss}} (t) = \frac {1}{2} | G (\mathrm{j} \omega_ {\mathrm{i}}) | [ 2 B \cos (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) + 2 A \sin (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) ] \\ = \left| G \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| \sqrt {A ^ {2} + B ^ {2}} \\ \left[ \frac {B}{\sqrt {A ^ {2} + B ^ {2}}} \cos (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) + \frac {A}{\sqrt {A ^ {2} + B ^ {2}}} \sin (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) \right] \tag {9.2.16} \\ \end{array}
$$

将式 $(9.2.3)$ 代入式 $(9.2.16)$ ，可得

$$
x _ {\mathrm{ss}} (t) = \left| G (\mathrm{j} \omega_ {\mathrm{i}}) \right| M _ {\mathrm{i}} \sin \left(\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t + \varphi_ {\mathrm{i}}\right) \tag {9.2.17}
$$

定义稳态输出为

$$
x _ {\mathrm{ss}} (t) = M _ {\mathrm{o}} \sin (\omega_ {\mathrm{i}} t + \varphi_ {\mathrm{o}}) \text {其中:} \frac {M _ {\mathrm{o}}}{M _ {\mathrm{i}}} = | G (\mathrm{j} \omega_ {\mathrm{i}}) |, \quad \varphi_ {\mathrm{o}} = \angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \varphi_ {\mathrm{i}} \tag {9.2.18}
$$

$M_{o}, \varphi_{o}$ 代表输出(下标 o 为 Output)的振幅与相位。对比式(9.2.18)和式(9.2.3)，会发现在经过了上面一系列复杂的运算后得出了一个简单的结论：

当正弦输入 $u(t) = M_{\mathrm{i}}\sin (\omega_{\mathrm{i}}t + \varphi_{\mathrm{i}})$ 通过线性时不变系统 $G(s)$ 后，输出的稳态值 $x_{\mathrm{ss}}(t)$ 与输入保持同样的频率 $\omega_{\mathrm{i}}$ ，但振幅变化了 $\left|G(\mathrm{j}\omega_{\mathrm{i}})\right|$ 倍（振幅响应），相位移动了 $\angle G(\mathrm{j}\omega_{\mathrm{i}})$ （相位响应）。这是系统频率响应中最重要的结论。

以积分器为例,其框图如图 9.2.5(a) 所示,传递函数为 $G(s)=\frac{1}{s}$ , 可得

$$
G (\mathrm{j} \omega_ {\mathrm{i}}) = \frac {1}{\mathrm{j} \omega_ {\mathrm{i}}} = - \frac {1}{\omega_ {\mathrm{i}}} \mathrm{j} \tag {9.2.19}
$$

$G(\mathrm{j}\omega_{\mathrm{i}})$ 在复平面中的表达如图9.2.5(b)所示。根据图形可以得到 $|G(\mathrm{j}\omega_{\mathrm{i}})| = \frac{1}{\omega_{\mathrm{i}}},\angle G(\mathrm{j}\omega_{\mathrm{i}}) = -\frac{\pi}{2}$ 。使用式(9.2.18)，当输入 $u(t) = M_{\mathrm{i}}\sin (\omega_{\mathrm{i}}t + \varphi_{\mathrm{i}})$ 时，系统的稳态输出为

$$
x _ {\mathrm{ss}} (t) = \frac {1}{\omega_ {\mathrm{i}}} M _ {\mathrm{i}} \sin \left(\omega_ {\mathrm{i}} t + \varphi_ {\mathrm{i}} - \frac {\pi}{2}\right) \tag {9.2.20}
$$

![](image/e79144c2b56b854038155c7813fa13b65500913b736c0b19c3a357ba4ee7a212.jpg)  
图 9.2.5 积分器频率响应

式(9.2.20)表明,输入 $u(t)$ 通过积分器之后振幅缩小到原来的 $\frac{1}{\omega_{i}}$ ,且输入的频率越高,输出的振幅就越小,所以从信号处理的角度来看,积分器是低通滤波器(Low Pass Filter)。其相位则有一 $\frac{\pi}{2}$ 的偏移。例如系统输入为 $u(t)=\sin(2t)$ ,根据式(9.2.20),可以得到稳态输出为

$$
x _ {\mathrm{ss}} (t) = 0. 5 \sin \left(2 t - \frac {\pi}{2}\right) \tag {9.2.21}
$$

输出与输入的图形如图 9.2.5(c) 所示。同样，也可以通过对 $u(t)$ 进行积分来验证，得到

$$
\int \sin (2 t) \mathrm{d} t = - 0. 5 \cos (2 t) = 0. 5 \sin \left(2 t - \frac {\pi}{2}\right) \tag {9.2.22}
$$

它与式 $(9.2.21)$ 得出的结果一致。
