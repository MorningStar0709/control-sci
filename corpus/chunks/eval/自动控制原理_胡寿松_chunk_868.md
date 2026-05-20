# (8) 卷积定理

设 $F_{1}(s) = \mathcal{L}[f_{1}(t)], F_{2}(s) = \mathcal{L}[f_{2}(t)]$ ，则有

$$F _ {1} (s) F _ {2} (s) = \mathscr {L} \left[ \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) d \tau \right]$$

式中， $\int_0^t f_1(t - \tau)f_2(\tau)\mathrm{d}\tau$ 叫做 $f_{1}(t)$ 和 $f_{2}(t)$ 的卷积，可写为 $f_{1}(t)*f_{2}(t)$ 。因此，上式表示，两个原函数的卷积相应于它们象函数的乘积。

证明 由式(A-11),有

$$\mathcal {L} \left[ \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau \right] = \int_ {0} ^ {\infty} \left[ \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau \right] \mathrm{e} ^ {- t} \mathrm{d} t$$

为了变积分限为0到 $\infty$ ，引入单位阶跃函数 $1(t - \tau)$ ，即有

$$
f _ {1} (t - \tau) 1 (t - \tau) = \left\{ \begin{array}{l l} 0, & t <   \tau \\ f _ {1} (t - \tau), & t > \tau \end{array} \right.
$$

因此 $\int_0^t f_1(t - \tau)f_2(\tau)\mathrm{d}\tau = \int_0^\infty f_1(t - \tau)1(t - \tau)f_2(\tau)\mathrm{d}\tau$

所以 $\mathcal{L}\left[\int_{0}^{t}f_{1}(t - \tau)f_{2}(\tau)\mathrm{d}\tau \right] = \int_{0}^{\infty}\int_{0}^{\infty}f_{1}(t - \tau)1(t - \tau)f_{2}(\tau)\mathrm{d}\tau \mathrm{e}^{-s}\mathrm{d}t$

$$= \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{d} \tau \int_ {0} ^ {\infty} f _ {1} (t - \tau) 1 (t - \tau) \mathrm{e} ^ {- t} \mathrm{d} t= \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{d} \tau \int_ {\tau} ^ {\infty} f _ {1} (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t$$

令 $t - \tau = \lambda$ ，可得

$$
\begin{array}{l} \mathcal {L} \left[ \int_ {0} ^ {t} f _ {1} (t - \tau) f _ {2} (\tau) \mathrm{d} \tau \right] = \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{d} \tau \int_ {0} ^ {\infty} f _ {1} (\lambda) \mathrm{e} ^ {- s \lambda} \mathrm{e} ^ {- \pi} \mathrm{d} \lambda \\ = \int_ {0} ^ {\infty} f _ {2} (\tau) \mathrm{e} ^ {- \pi} \mathrm{d} \tau \int_ {0} ^ {\infty} f _ {1} (\lambda) \mathrm{e} ^ {- \lambda} \mathrm{d} \lambda = F _ {2} (s) F _ {1} (s) \\ \end{array}
$$

表 A-2 简要列出拉氏变换的基本特性, 表 A-3 列出常用函数的拉氏变换式, 可供查用。

表 A-2 拉普拉斯变换的基本特性
