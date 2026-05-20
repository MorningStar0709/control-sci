$$\int_ {- \pi} ^ {\pi} f _ {T} (x) \cos m x \mathrm{d} x = \int_ {- \pi} ^ {\pi} a _ {0} ^ {*} \cos m x \mathrm{d} x + \int_ {- \pi} ^ {\pi} \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {*} \cos n x \cos m x + b _ {n} \sin n x \cos m x\right) \mathrm{d} x= \int_ {- \pi} ^ {\pi} a _ {0} ^ {*} \cos m x d x + \sum_ {n = 1} ^ {\infty} a _ {n} ^ {*} \int_ {- \pi} ^ {\pi} \cos n x \cos m x d x +\sum_ {n = 1} ^ {\infty} b _ {n} \int_ {- \pi} ^ {\pi} \sin n x \cos m x d x \tag {B.2.7}$$

注意式（B.2.7）等号右边，根据三角函数的正交性， $\int_{-\pi}^{\pi}a_{0}^{*}\cos mx\,dx=0$ 且 $\sum_{n=1}^{\infty}b_{n}\int_{-\pi}^{\pi}\sin nx\cos mx dx=0$ ，而在 $\sum_{n=1}^{\infty}a_{n}^{*}\int_{-\pi}^{\pi}\cos nx\cos mx dx$ 中，所有的加和项里只有当m=n时才不为0。此时式(B.2.7)可以写成

$$\int_ {- \pi} ^ {\pi} f _ {T} (x) \cos n x \mathrm{d} x = a _ {n} ^ {*} \int_ {- \pi} ^ {\pi} \cos n x \cos n x \mathrm{d} x = a _ {n} ^ {*} \pi \tag {B.2.8a}$$

其中， $\int_{-\pi}^{\pi}\cos nx\cos nx\mathrm{d}x = \pi$ （参考式(B.1.9))。得到

$$a _ {n} ^ {*} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f _ {T} (x) \cos n x d x, \quad n = 1, 2, 3, \dots \tag {B.2.8b}$$

请注意,在式(B.2.8b)中,当n=0时, $a_{n=0}^{*}=\frac{1}{\pi}\int_{-\pi}^{\pi}f_{T}(x)\cos nx\mathrm{d}x$ 。它与式(B.2.6)中所得出的结果并不相同。因此,为了避免不一致带来的疑惑,定义

$$
\left\{ \begin{array}{l} a _ {0} = 2 a _ {0} ^ {*} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f _ {T} (x) \mathrm{d} x \\ a _ {n} = a _ {n} ^ {*} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f _ {T} (x) \cos n x \mathrm{d} x, \quad n = 1, 2, 3, \dots \end{array} \right. \tag {B.2.9}
$$

将式(B.2.9)代入式(B.2.4)，可得

$$f _ {T} (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right) \tag {B.2.10}$$

以上表达和式(B.2.2)一致。

对于 $b_{n}$ ，令式(B.2.4)等号两边乘以 $\sin mx$ 后再从一π到π做定积分，可得

$$b _ {n} = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f _ {T} (x) \sin n x \mathrm{d} x, \quad n = 1, 2, 3, \dots \tag {B.2.11}$$

将式(B.2.9)、式(B.2.10)和式(B.2.11)整理在一起,可以得到周期为 $2\pi$ 的函数展开为傅里叶级数的表达形式,即

$$f _ {T} (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right) \tag {B.2.12a}$$

其中， $\left\{\begin{aligned}a_{n}&=\frac{1}{\pi}\int_{-\pi}^{\pi}f_{T}(x)\cos nx\mathrm{d}x\quad n=0,1,2,\cdots\\ b_{n}&=\frac{1}{\pi}\int_{-\pi}^{\pi}f_{T}(x)\sin nx\mathrm{d}x\quad n=1,2,3,\cdots\end{aligned}\right.$ (B.2.12b)

需要注意的是,从纯数学角度来看, $f_{T}(x)$ 不一定在 $-\pi$ 到 $\pi$ 之间可积,即 $\int_{-\pi}^{\pi}f_{T}(x)\mathrm{d}x$ 不一定存在,所以周期函数不一定都可以展开为式(B.2.12)的形式(傅里叶级数有可能不收敛)。但从工程角度分析,不管是控制工程还是信号处理,所处理的函数大都是可积的,所以

在本附录中不考虑数学中的特殊情况。
