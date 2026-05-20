# 5. 时域微分性质

一个信号的导数的拉普拉斯变换与该信号的拉普拉斯变换以及它的初始条件有关：

$$\mathscr {L} \left\{\frac {\mathrm{d} f}{\mathrm{d} t} \right\} = \int_ {0 ^ {-}} ^ {+ \infty} \left(\frac {\mathrm{d} f}{\mathrm{d} t}\right) \mathrm{e} ^ {- s t} \mathrm{d} t = - f (0 ^ {-}) + s F (s) \tag {3.41}$$

由式(3.41)可得

$$\mathscr {L} \{\ddot {f} \} = s ^ {2} F (s) - s f \left(0 ^ {-}\right) - \dot {f} \left(0 ^ {-}\right) \tag {3.42}$$

再次应用式(3.41)，可得

$$\mathscr {L} \left\{f ^ {(m)} (t) \right\} = s ^ {m} F (s) - s ^ {m - 1} f \left(0 ^ {-}\right) - s ^ {m - 2} \dot {f} \left(0 ^ {-}\right) - \dots - f ^ {(m - 1)} \left(0 ^ {-}\right) \tag {3.43}$$

这里 $f^{(m)}(t)$ 表示 $f(t)$ 对时间的 $m$ 阶导数。
