# B.4 傅里叶级数的复数表达形式

傅里叶级数的复数表达形式可以帮助分析非周期函数的傅里叶表达。首先复习欧拉恒等式：

$$\cos \varphi + j \sin \varphi = e ^ {j \varphi} \tag {B.4.1a}$$

用 $-\varphi$ 替换 $\varphi$ , 得到

$$\cos (- \varphi) + j \sin (- \varphi) = e ^ {- j \varphi}\Rightarrow \cos \varphi - j \sin \varphi = e ^ {- j \varphi} \tag {B.4.1b}$$

令式(B.4.1a)加式(B.4.1b)，得到

$$2 \cos \varphi = \mathrm{e} ^ {\mathrm{j} \varphi} + \mathrm{e} ^ {- \mathrm{j} \varphi}\Rightarrow \cos \varphi = \frac {1}{2} \left(\mathrm{e} ^ {\mathrm{j} \varphi} + \mathrm{e} ^ {- \mathrm{j} \varphi}\right) \tag {B.4.2a}$$

令式(B.4.1a)减式(B.4.1b)，得到

$$2 \mathrm{j} \sin \varphi = \mathrm{e} ^ {\mathrm{j} \varphi} - \mathrm{e} ^ {- \mathrm{j} \varphi}\Rightarrow \sin \varphi = - \frac {1}{2} \mathrm{j} \left(\mathrm{e} ^ {\mathrm{j} \varphi} - \mathrm{e} ^ {- \mathrm{j} \varphi}\right) \tag {B.4.2b}$$

将式(B.4.2a)和式(B.4.2b)代入式(B.3.8a)，得到

$$
\begin{array}{l} f _ {T} (t) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n \omega_ {T} t x + b _ {n} \sin n \omega_ {T} t\right) \\ = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \left(\frac {1}{2} \left(\mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} + \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t}\right) - b _ {n} \left(\frac {1}{2} \mathrm{j} \left(\mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} - \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t}\right) \right. \right. \right. \\ = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(\frac {a _ {n} - \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} + \frac {a _ {n} + \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t}\right) \\ = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \frac {a _ {n} - \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} + \sum_ {n = 1} ^ {\infty} \frac {a _ {n} + \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \tag {B.4.3} \\ \end{array}
$$

其中， $\frac{a_{0}}{2}$ 可以调整写成

$$\frac {a _ {0}}{2} = \sum_ {n = 0} ^ {0} \frac {a _ {0}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.4.4a}$$

对于 $\sum_{n=1}^{\infty} \frac{a_n + \mathrm{j}b_n}{2} \mathrm{e}^{-\mathrm{j}n \omega_T t}$ 项，用 $-n$ 代替 $n$ ，可以调整为
