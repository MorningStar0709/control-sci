# 2. 傅里叶积分和傅里叶变换

任一周期函数, 只要满足狄利克雷条件, 便可以展开为傅氏级数。对于非周期函数, 因为其周期 T 趋于无穷大, 不能直接用傅氏级数展开式, 而要做某些修改, 这样就引出了傅里叶积分式。

若 $f(t)$ 为非周期函数，则可视其为周期 $T$ 趋于无穷大，角频率 $(\omega_0 = 2\pi / T)$ 趋于零的周期函数。这时，在傅氏级数展开式(A-1)～(A-5)中，各个相邻的谐波频率之差 $\Delta \omega = (n + 1)\omega_0 - n\omega_0 = \omega_0$ 便很小，谐波频率 $n\omega_0$ 须用一个变量 $\omega$ 代替[注意，此处 $\omega$ 不同于式(A-1)中的角频率]。这样，式(A-4)和式(A-5)可改写为

$$f (t) = \sum_ {\omega = - \infty} ^ {\infty} \alpha_ {\omega} \mathrm{e} ^ {\mathrm{j} \omega t} \tag {A-6}\alpha_ {\omega} = \frac {\Delta \omega}{2 \pi} \int_ {- T / 2} ^ {T / 2} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \tag {A-7}$$

将式(A-7)代入式(A-6)，得

$$f (t) = \sum_ {\omega = - \infty} ^ {\infty} \left[ \frac {\Delta \omega}{2 \pi} \int_ {- T / 2} ^ {T / 2} f (t) e ^ {- j \omega t} d t \right] e ^ {j \omega t} = \frac {1}{2 \pi} \sum_ {\omega = - \infty} ^ {\infty} \left[ \int_ {- T / 2} ^ {T / 2} f (t) e ^ {- j \omega t} d t \right] e ^ {j \omega t} \Delta \omega$$

当 $T \to \infty$ 时， $\Delta \omega \to \mathrm{d}\omega$ ，求和式变为积分式，上式可写为

$$f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \left[ \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \right] \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega \tag {A-8}$$

式(A-8)是非周期函数 $f(t)$ 的傅里叶积分形式之一。

在式(A-8)中,若令

$$F (\omega) = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t \tag {A-9}$$

则式(A-8)可写为

$$f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F (\omega) \mathrm{e} ^ {\mathrm{j} \omega t} \mathrm{d} \omega \tag {A-10}$$

式(A-9)和式(A-10)给出的两个积分式称为傅里叶(简称傅式)变换对, $F(\omega)$ 称为 $f(t)$ 的傅氏变换,记为 $F(\omega)=\mathcal{F}[f(t)]$ ,而 $f(t)$ 称为 $F(\omega)$ 的傅氏反变换,记为 $f(t)=\mathcal{F}^{-1}[F(\omega)]$ 。

非周期函数 $f(t)$ 必须满足狄利克雷条件才可进行傅氏变换，而且狄利克雷的第三条件这时应修改为积分 $\int_{-\infty}^{\infty}|f(t)|\mathrm{d}t$ 存在。

例 A-2 求图 A-2 方波的傅氏变换。

![](image/608205ebf7e77bce5f186e8679d73b78a2db95f28d096850a51bf27293fc1005.jpg)

<details>
<summary>line</summary>

| t | f(t) |
| --- | --- |
| -a | A |
| 0 | A |
| a | A |
</details>

图A-2 方波

![](image/66f60824295f74fd33f746fafcdd684be0efb42545ca000cda44b8733429d5d4.jpg)  
图A-3 方波的频谱

解 图 A-2 方波可用下式表示：

$$
f (t) = \left\{ \begin{array}{l l} A, & - a <   t <   a \\ 0, & t > a, t <   - a \end{array} \right.
$$

显然， $f(t)$ 不是周期函数。由式(A-9)得

$$F (\omega) = \int_ {- \infty} ^ {\infty} f (t) \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \int_ {- a} ^ {a} A \mathrm{e} ^ {- \mathrm{j} \omega t} \mathrm{d} t = \frac {2 A}{\omega} \sin a \omega$$

频谱函数 $F(\omega)$ 的模 $\left|F(\omega)\right|$ 称为频谱，方波的频谱 $\left|F(\omega)\right| = 2A\left|\sin a\omega /\omega \right|$ ，它与频率 $\omega$ 的关系曲线如图A-3所示。

工程技术上常用傅里叶方法分析线性系统,因为任何周期函数都可展开为含有许多正弦分量或余弦分量的傅氏级数,而任何非周期函数都可表示为傅氏积分,从而可将一个时间域的函数变换为频率域的函数。在我们研究输入为非正弦函数的线性系统时,应用傅氏级数和傅氏变换的这个性质,可以通过系统对各种频率正弦波的响应特性来了解系统对非正弦输入的响应特性。研究自动控制系统的频率域方法,就是建立在这个基础之上的。
