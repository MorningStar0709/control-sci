$$\mathrm{e} ^ {\mathrm{j} a t} - \mathrm{e} ^ {- \mathrm{j} a t} = 2 \mathrm{j} \sin a t\Rightarrow \sin a t = \frac {\mathrm{e} ^ {\mathrm{j} a t} - \mathrm{e} ^ {- \mathrm{j} a t}}{2 \mathrm{j}} \tag {2.2.7}$$

根据例 2.2.2 的线性叠加性质,与例 2.2.1 所求指数函数的拉普拉斯变换,可得

$$
\begin{array}{l} \mathcal {L} [ \sin a t ] = \mathcal {L} \left[ \frac {\mathrm{e} ^ {\mathrm{j} a t} - \mathrm{e} ^ {- \mathrm{j} a t}}{2 \mathrm{j}} \right] \\ = \frac {1}{2 \mathrm{j}} \left(\mathcal {L} \left[ \mathrm{e} ^ {\mathrm{j} a t} \right] - \mathcal {L} \left[ \mathrm{e} ^ {- \mathrm{j} a t} \right]\right) \\ = \frac {1}{2 \mathrm{j}} \left(\frac {1}{s - a \mathrm{j}} - \frac {1}{s + a \mathrm{j}}\right) = \frac {1}{2 \mathrm{j}} \left(\frac {s + a \mathrm{j}}{s ^ {2} + a ^ {2}} - \frac {s - a \mathrm{j}}{s ^ {2} + a ^ {2}}\right) \\ = \frac {1}{2 \mathrm{j}} \left(\frac {2 a \mathrm{j}}{s ^ {2} + a ^ {2}}\right) \\ = \frac {a}{s ^ {2} + a ^ {2}} \tag {2.2.8} \\ \end{array}
$$

例 2.2.4 $\mathcal{L}\left[\frac{\mathrm{d}f(t)}{\mathrm{d}t}\right]=sF(s)-f(0)$ 。

证：

$$
\begin{array}{l} \mathcal {L} \left[ \frac {\mathrm{d} f (t)}{\mathrm{d} t} \right] = \int_ {0} ^ {\infty} \frac {\mathrm{d} f (t)}{\mathrm{d} t} \mathrm{e} ^ {- s t} \mathrm{d} t = f (t) \mathrm{e} ^ {- s t} \left| _ {0} ^ {\infty} - \int_ {0} ^ {\infty} f (t) (- s \mathrm{e} ^ {- s t}) \mathrm{d} t \right. \\ = \lim _ {t \rightarrow \infty} f (t) \mathrm{e} ^ {- s t} - f (0) \mathrm{e} ^ {0} + s \int_ {0} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = s F (s) - f (0) \tag {2.2.9} \\ \end{array}
$$

其中， $f(0)$ 是函数的初始条件(Initial Condition)。

例 2.2.5 $\mathcal{L}[f(t)*g(t)]=F(s)G(s)$ 。

证：

$$
\begin{array}{l} \mathcal {L} [ f (t) * g (t) ] = \int_ {0} ^ {\infty} f (t) * g (t) \mathrm{e} ^ {- s t} \mathrm{d} t \\ = \int_ {0} ^ {\infty} \int_ {0} ^ {t} f (\tau) g (t - \tau) \mathrm{d} \tau \mathrm{e} ^ {- s t} \mathrm{d} t \tag {2.2.10a} \\ \end{array}
$$

这是一个二重积分,可以通过交换积分顺序与上下限的方式来进行化简。交换之后,式(2.2.10a)可以写成

$$\int_ {0} ^ {\infty} \int_ {0} ^ {t} f (\tau) g (t - \tau) \mathrm{d} \tau \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {0} ^ {\infty} \int_ {\tau} ^ {\infty} f (\tau) g (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t \mathrm{d} \tau \tag {2.2.10b}$$

对式(2.2.10b)里面的积分 $\int_{\tau}^{\infty}f(\tau)g(t - \tau)\mathrm{e}^{-st}\mathrm{d}t$ 项使用换元法，令 $t - \tau = u$ ，可得
