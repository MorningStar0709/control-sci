$$M = \frac {1}{\mathrm{e} ^ {1 . 3 7 4 3} h ^ {0 . 9 6 6 7}} \approx \frac {1}{3 . 9 5 h} \approx \frac {1}{4 h}\beta_ {0 1} \approx \frac {1}{h}\beta_ {0 2} = \frac {1}{\mathrm{e} ^ {0 . 8 8 9 6} h ^ {1 . 9 7 6 8}} \approx \frac {1}{2 . 4 h ^ {2}} \approx \frac {1}{3 h ^ {2}}\beta_ {0 3} = \frac {1}{\mathrm{e} ^ {2 . 7 4 2 5} h ^ {2 . 9 6 3 6}} \approx \frac {1}{1 5 . 5 h ^ {3}} = \frac {1}{2 0 h ^ {3}}$$

当然,这些拟合公式只能作为参考,实际需要用的参数是在这230

些公式给出的参数附近仔细寻找才能最后确定.

另一方面,对线性扩张状态观测器(4.7.5)实行“时间尺度”变换

$$\rho t = \tau \tag {4.7.6}$$

就得

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1}}{\mathrm{d} \tau} = \frac {1}{\rho} \frac {\mathrm{d} z _ {1}}{\mathrm{d} t} = \frac {z _ {2}}{\rho} - \frac {\beta_ {0 1}}{\rho} e \\ \frac {\mathrm{d} z _ {2}}{\mathrm{d} \tau} = \frac {1}{\rho} \frac {\mathrm{d} z _ {2}}{\mathrm{d} t} = \frac {z _ {3}}{\rho} - \frac {\beta_ {0 2}}{\rho} e + \frac {b}{\rho} u \\ \frac {\mathrm{d} z _ {3}}{\mathrm{d} \tau} = \frac {1}{\rho} \frac {\mathrm{d} z _ {3}}{\mathrm{d} t} = - \frac {\beta_ {0 3}}{\rho} e \end{array} \right. \tag {4.7.7}
$$

再实行坐标变换

$$\overline {{z _ {1}}} = z _ {1}, \overline {{z _ {2}}} = \frac {z _ {2}}{\rho}, \overline {{z _ {3}}} = \frac {z _ {3}}{\rho^ {2}} \tag {4.7.8}$$

就得

$$
\begin{array}{l} \overline {{z _ {1}}} - y = z _ {1} - y = e \\ \left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1}}{\mathrm{d} \tau} = \overline {{z _ {2}}} - \frac {\beta_ {0 1}}{\rho} e \\ \frac {\mathrm{d} z _ {2}}{\mathrm{d} \tau} = \overline {{z _ {3}}} - \frac {\beta_ {0 2}}{\rho^ {2}} e + \frac {b}{\rho^ {2}} u \\ \frac {\mathrm{d} z _ {3}}{\mathrm{d} \tau} = - \frac {\beta_ {0 3}}{\rho^ {3}} e \end{array} \right. \\ \end{array}
$$

去掉变量表示中的“一横”，得

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1}}{\mathrm{d} \tau} = z _ {2} - \frac {\beta_ {0 1}}{\rho} e \\ \frac {\mathrm{d} z _ {2}}{\mathrm{d} \tau} = z _ {3} - \frac {\beta_ {0 2}}{\rho^ {2}} e + \frac {b}{\rho^ {2}} u \\ \frac {\mathrm{d} z _ {3}}{\mathrm{d} \tau} = - \frac {\beta_ {0 3}}{\rho^ {3}} e \end{array} \right. \tag {4.7.9}
$$

这说明,在系统中实施“时间尺度”变换

$$\rho t = \tau$$

和坐标变换 $z_{1}^{-}=z_{1},z_{2}^{-}=\frac{z_{2}}{\rho},z_{3}^{-}=\frac{z_{3}}{\rho^{2}}$ 时，扩张状态观测器的参数

$$\beta_ {0 1}, \beta_ {0 2}, \beta_ {0 3}$$

将分别变成

$$\frac {\beta_ {0 1}}{\rho}, \frac {\beta_ {0 2}}{\rho^ {2}}, \frac {\beta_ {0 3}}{\rho^ {3}} \tag {4.7.10}$$

在这里,如果 t 的量纲为“秒”, $\tau$ 的量纲为“分”, 那么 $\rho$ 就等于 60; 如果 t 的量纲为“分”, $\tau$ 的量纲为“秒”, 那么 $\rho$ 就等于 1/60.

这里有如下几个问题：

(1) 对给定的对象
