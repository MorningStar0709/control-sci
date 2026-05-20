# 1. 傅里叶级数

周期函数的傅里叶级数(简称傅氏级数)是由正弦和余弦项组成的三角级数。

周期为 T 的任一周期函数 $f(t)$ ，若满足下列狄利克雷条件：

1) 在一个周期内只有有限个不连续点；  
2）在一个周期内只有有限个极大和极小值；  
3）积分 $\int_{-T / 2}^{T / 2}|f(t)|\mathrm{d}t$ 存在。

则 $f(t)$ 可展开为如下的傅氏级数：

$$f (t) = \frac {1}{2} a _ {0} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n \omega t + b _ {n} \sin n \omega t) \tag {A-1}$$

式中，系数 $a_{n}$ 和 $b_{n}$ 由下式给出：

$$a _ {n} = \frac {2}{T} \int_ {- T / 2} ^ {T / 2} f (t) \cos n \omega t \mathrm{d} t; \quad n = 0, 1, 2, \dots , \infty \tag {A-2}b _ {n} = \frac {2}{T} \int_ {- T / 2} ^ {T / 2} f (t) \sin n \omega t \mathrm{d} t; \qquad n = 1, 2, \dots , \infty \tag {A-3}$$

式中， $\omega=2\pi/T$ 称为角频率。

周期函数 $f(t)$ 的傅氏级数还可以写为复数形式(或指数形式):

$$f (t) = \sum_ {n = - \infty} ^ {\infty} \alpha_ {n} \mathrm{e} ^ {\mathrm{j} n \omega t} \tag {A-4}$$

式中系数

$$\alpha_ {n} = \frac {1}{T} \int_ {- T / 2} ^ {T / 2} f (t) \mathrm{e} ^ {- \mathrm{j} n \omega t} \mathrm{d} t \tag {A-5}$$

如果周期函数 $f(t)$ 具有某种对称性质，如为偶函数、奇函数，或只有奇次或偶次谐波，则傅氏级数中的某些项为零，系数公式可以简化。表A-1列出了具有几种对称性质的周期函数 $f(t)$ 的傅氏级数简化结果。

例 A-1 试求图 A-1 所示周期方波的傅氏级数展开式。

解 首先写出方波在一个周期内的数学表达式

$$
f (t) = \left\{ \begin{array}{l l} 0, & - \frac {T}{2} <   t <   - \frac {T}{4} \\ A, & - \frac {T}{4} <   t <   \frac {T}{4} \\ 0, & \frac {T}{4} <   t <   \frac {T}{2} \end{array} \right.
$$

表 A-1 周期函数 $f(t)$ 的对称性质

<table><tr><td></td><td>对称性</td><td>傅氏级数特点</td><td>an</td><td>bn</td></tr><tr><td>f1(t)</td><td>偶函数 f1(t)=f1(-t)</td><td>只有余弦项</td><td> $\frac{4}{T}\int_{0}^{T/2}f_1(t)\cos n\omega tdt$ </td><td>0</td></tr><tr><td>f2(t)</td><td>奇函数 f2(t)=-f2(-t)</td><td>只有正弦项</td><td>0</td><td> $\frac{4}{T}\int_{0}^{T/2}f_2(t)\sin n\omega tdt$ </td></tr><tr><td>f3(t)</td><td>只有偶次谐波 f3(t± $\frac{T}{2}$ )=f3(t)</td><td>只有偶数n</td><td> $\frac{4}{T}\int_{0}^{T/2}f_3(t)\cos n\omega tdt$ </td><td> $\frac{4}{T}\int_{0}^{T/2}f_3(t)\sin n\omega tdt$ </td></tr><tr><td>f4(t)</td><td>只有奇次谐波 f4(t± $\frac{T}{2}$ )=-f4(t)</td><td>只有奇数n</td><td> $\frac{4}{T}\int_{0}^{T/2}f_4(t)\cos n\omega tdt$ </td><td> $\frac{4}{T}\int_{0}^{T/2}f_4(t)\sin n\omega tdt$ </td></tr></table>

因为 $f(t) = f(-t)$ ，为偶函数，故只需计算系数 $a_{n}$ 。由表A-1有

$$
\begin{array}{l} a _ {n} = \frac {4}{T} \int_ {0} ^ {T / 4} f (t) \cos n \omega t d t = \frac {4}{T} \int_ {0} ^ {T / 4} A \cos n \omega t d t \\ = \frac {2 A}{n \pi} \sin \left(\frac {n \pi}{2}\right) \\ \end{array}
$$

依次取 $n = 0,1,2,3,\dots$ 计算，得 $a_0 = A,a_1 = 2A / \pi ,$ $a_{2} = 0,a_{3} = -2A / 3\pi ,a_{4} = 0,a_{5} = 2A / 5\pi ,\dots$ 其中 $a_0$

是应用洛必达法则求得的。由式(A-1)可求出方波的傅氏级数展开式

$$f (t) = \frac {A}{2} + \frac {2 A}{\pi} \left(\cos \omega t - \frac {1}{3} \cos 3 \omega t + \frac {1}{5} \cos 5 \omega t - \dots\right)$$

![](image/3db473b8a9156acc0009f4c9fb0f02882737e1e3a85b7983f4455fd2cd463349.jpg)

<details>
<summary>bar</summary>

| t | f(t) |
| --- | --- |
| -√T/2 | A |
| -T/4 | A |
| T/4 | A |
| √T/2 | A |
</details>

图A-1 周期方波

上式表明,方波可以分解为各种频率的谐波分量。换句话说,用不同频率的谐波合成可以得到方波。
