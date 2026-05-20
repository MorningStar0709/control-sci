# (1) 周期信号的频谱

设 $f(t)$ 为周期函数, 其周期为 T, 可用下式描述:

$$f (t) = f (t + l T); \quad l = 0, \pm 1, \dots \tag {5-94}$$

若 $f(t)$ 在区间 $[0, T]$ 内有界，且仅有有限个极值，即满足狄利克雷条件，则 $f(t)$ 可展开为傅里叶级数

$$f (t) = \sum_ {k = - \infty} ^ {\infty} c _ {k} \mathrm{e} ^ {\mathrm{j} \frac {2 n k}{T} t} \tag {5-95}$$

其中 $c_{k}$ 为复数，称为傅里叶系数，

$$c _ {k} = \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f (t) \mathrm{e} ^ {- \mathrm{j} \frac {2 \pi k}{T} t} \mathrm{d} t = \frac {A _ {k}}{2} \mathrm{e} ^ {\mathrm{j} B _ {k}} \tag {5-96}$$

且有 $c_{0} = \frac{A_{0}}{2}, c_{-k} = \overline{c_{k}} = \frac{A_{k}}{2}\mathrm{e}^{-\mathrm{j}B_{k}}$

代入式(5-95)可得

$$f (t) = \frac {A _ {0}}{2} + \sum_ {k = 1} ^ {\infty} A _ {k} \cos \left(\frac {2 \pi k}{T} t + B _ {k}\right) \tag {5-97}$$

复系数表达式中的 $A_{k}$ 和 $B_{k}$ 表示 $f(t)$ 的第 $k$ 次谐波分量的幅值和相位，称复系数 $c_{k}$ 的集合为周期信号的频谱。频谱可以有不同的表示形式，有时只列出复系数的幅值谱。对于图5-43(a)所示的矩形波序列，其基波频率和复系数的幅值分别为

$$\Omega = \frac {2 \pi}{T}, \quad | c _ {k} | = \frac {A \tau}{T} \cdot \frac {\sin \left(\frac {\pi k \tau}{T}\right)}{\pi k \tau / T}$$

幅值谱如图 5-45(b) 所示。

![](image/6bab0a1e65391f65e3b8fe0a02d6d8c6f6cc6e43ebae4ed8068c45f828bc4ec1.jpg)  
图 5-45 矩形波及其幅值谱

由图 5-45 可知, 周期信号的幅值谱为一簇谱线, 随 k 增大, 即 $\omega = \frac{2\pi}{T} k$ 的增大, 幅值谱的包络线衰减。若系统的控制输入为矩形波时, 系统的跟踪能力取决于带宽覆盖矩形波频谱的范围, 带宽大则处于较高频率范围的谱线衰减小, 故失真小。
