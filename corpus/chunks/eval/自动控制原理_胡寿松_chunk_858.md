$$f (t) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} F _ {\sigma} (\omega) \mathrm{e} ^ {(\sigma + \mathrm{j} \omega) t} \mathrm{d} \omega$$

以 $s = \sigma +\mathrm{j}\omega$ 代之，可得

$$f (t) = \frac {1}{2 \pi \mathrm{j}} \int_ {\sigma - \mathrm{j} \infty} ^ {\sigma + \mathrm{j} \infty} F (s) \mathrm{e} ^ {s t} \mathrm{d} s \tag {A-12}$$

在式(A-11)和式(A-12)中， $s=\sigma+j\omega$ 是复数，只要其实部 $\sigma>0$ 足够大，式(A-12)的积分就存在。式(A-11)和式(A-12)的两个积分式称为拉氏变换对。 $F(s)$ 叫做 $f(t)$ 的拉氏变换，也称象函数, 记为 $F(s) = \mathcal{L}[f(t)]$ ; $f(t)$ 叫做 $F(s)$ 的拉氏反变换, 也称原函数, 记为 $f(t) = \mathcal{L}^{-1}[F(s)]$ 。

例 A-3 求正弦函数 $f(t)=\sin\omega t$ 的拉氏变换。

解 由欧拉公式

$$\sin \omega t = \frac {1}{2 \mathrm{j}} (\mathrm{e} ^ {\mathrm{j} \omega t} - \mathrm{e} ^ {- \mathrm{j} \omega t})$$

计及式(A-11)可得

$$
\begin{array}{l} F (s) = \mathscr {L} [ \sin \omega t ] = \int_ {0} ^ {\infty} \sin \omega t e ^ {- s t} d t = \int_ {0} ^ {\infty} \frac {1}{2 j} \left(e ^ {j a t} - e ^ {- j a t}\right) e ^ {- s t} d t \\ = \frac {1}{2 \mathrm{j}} \left[ \frac {1}{s - \mathrm{j} \omega} - \frac {1}{s + \mathrm{j} \omega} \right] = \frac {\omega}{s ^ {2} + \omega^ {2}} \\ \end{array}
$$

例 A-4 求单位脉冲函数 $\delta(t)$ 的拉氏变换。

解 将 $f(t) = \delta (t) = \lim_{t_0 \to 0} [1(t) - 1(t - t_0)] / t_0$ 代入式(A-11)，可得

$$
\begin{array}{l} \mathscr {A} [ \delta (t) ] = \int_ {0} ^ {\infty} \lim _ {t _ {0} \rightarrow 0} \frac {1}{t _ {0}} [ 1 (t) - 1 (t - t _ {0}) ] e ^ {- s t} d t \\ = \lim _ {t _ {0} \rightarrow 0} \frac {1}{t _ {0}} \int_ {0} ^ {\infty} [ 1 (t) - 1 (t - t _ {0}) ] e ^ {- s t} d t \\ = \lim _ {t _ {0} \rightarrow 0} \frac {1}{t _ {0} s} \left(1 - \mathrm{e} ^ {- t _ {0} s}\right) = \lim _ {t _ {0} \rightarrow 0} \frac {\mathrm{d} \left(1 - \mathrm{e} ^ {- t _ {0} s}\right) / \mathrm{d} t _ {0}}{\mathrm{d} t _ {0} s / \mathrm{d} t _ {0}} = 1 \\ \end{array}
$$

因此，单位脉冲函数 $\delta(t)$ 的拉氏变换为 1。显然，强度为 A 的脉冲函数 $A\delta(t)$ 的拉氏变换就等于它的强度 A，即 $\mathcal{L}[A\delta(t)]=A$ 。
