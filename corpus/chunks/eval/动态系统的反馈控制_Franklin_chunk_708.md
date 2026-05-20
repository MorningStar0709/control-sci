# 7. 卷积性质

在时域上进行卷积运算对应于频域上就是相乘运算。假设 $\mathcal{L}\{f_1(t)\} = F_1(s)$ 和 $\mathcal{L}\{f_2(t)\} = F_2(s)$ 。那么

$$\mathcal {L} \left\{f _ {1} (t) * f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} f _ {1} (t) * f _ {2} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \int_ {0} ^ {+ \infty} \left[ \int_ {0} ^ {t} f _ {1} (\tau) f _ {2} (t - \tau) \mathrm{d} \tau \right] \mathrm{e} ^ {- s t} \mathrm{d} t$$

我们看到 $t$ 从零到无穷， $\tau$ 从零到 $t$ 。借助图A.1，我们可以交换积分顺序，变换积分上下限使得 $\tau$ 从零到无穷并且 $\infty \geqslant t \geqslant \tau$ 可得

$$\mathcal {L} \left\{f _ {1} (t) * f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} \int_ {\tau} ^ {+ \infty} f _ {1} (\tau) f _ {2} (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t \mathrm{d} \tau$$

上式乘以 $\mathrm{e}^{-\pi}\mathrm{e}^{\pi}$ 得

$$\mathcal {L} \left\{f _ {1} (t) * f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} f _ {1} (\tau) \mathrm{e} ^ {- s \tau} \left[ \int_ {\tau} ^ {+ \infty} f _ {2} (t - \tau) \mathrm{e} ^ {- s (t - \tau)} \mathrm{d} t \right] \mathrm{d} \tau$$

如果坐标变换为 $t' \stackrel{\operatorname{def}}{=} t - \tau$ ，则

$$\mathcal {L} \left\{f _ {1} (t) * f _ {2} (t) \right\} = \int_ {0} ^ {+ \infty} f _ {1} (\tau) \mathrm{e} ^ {- s t} \mathrm{d} \tau \int_ {0} ^ {+ \infty} f _ {2} (t ^ {\prime}) \mathrm{e} ^ {- s t ^ {\prime}} \mathrm{d} t ^ {\prime}\mathscr {L} \left\{f _ {1} (t) * f _ {2} (t) \right\} = F _ {1} (s) F _ {2} (s)$$

这意味着

$$\mathcal {L} ^ {- 1} \left\{F _ {1} (s) F _ {2} (s) \right\} = f _ {1} (t) * f _ {2} (t) \tag {A.15}$$
