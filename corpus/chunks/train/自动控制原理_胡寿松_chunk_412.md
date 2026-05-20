# (2) 部分分式法

利用部分分式法求 z 变换时, 先求出已知连续时间函数 $e(t)$ 的拉氏变换 $E(s)$ , 然后将有理分式函数 $E(s)$ 展成部分分式之和的形式, 使每一部分分式对应简单的时间函数, 其相应的 z 变换是已知的, 于是可方便地求出 $E(s)$ 对应的 z 变换 $E(z)$ 。

例 7-7 设 $e(t)=\sin\omega t$ ，试求其 $E(z)$ 。

解 对 $e(t) = \sin \omega t$ 取拉氏变换，得

$$E (s) = \frac {\omega}{s ^ {2} + \omega^ {2}}$$

将上式展开为部分分式

$$E (s) = \frac {1}{2 \mathrm{j}} \left(\frac {1}{s - \mathrm{j} \omega} - \frac {1}{s + \mathrm{j} \omega}\right)$$

根据指数函数的 $z$ 变换表达式，可以得到

$$E (z) = \frac {1}{2 \mathrm{j}} \left(\frac {z}{z - \mathrm{e} ^ {\mathrm{j} \omega T}} - \frac {z}{z - \mathrm{e} ^ {- \mathrm{j} \omega T}}\right) = \frac {1}{2 \mathrm{j}} \left[ \frac {z (\mathrm{e} ^ {\mathrm{j} \omega T} - \mathrm{e} ^ {- \mathrm{j} \omega T})}{z ^ {2} - z (\mathrm{e} ^ {\mathrm{j} \omega T} + \mathrm{e} ^ {- \mathrm{j} \omega T}) + 1} \right]$$

化简后得 $E(z) = \frac{z\sin\omega T}{z^2 - 2z\cos\omega T + 1}$

常用时间函数的 $z$ 变换表如表7-2所示。由表可见，这些函数的 $z$ 变换都是 $z$ 的有理分式，且分母多项式的次数大于或等于分子多项式的次数。值得指出，表中各 $z$ 变换有理分式中，分母 $z$ 多项式的最高次数与相应传递函数分母 $s$ 多项式的最高次数相等。

表 7-2 z 变换表
