$$\delta (t) = 0, \quad t \neq 0 \tag {3.9}\int_ {- \infty} ^ {+ \infty} \delta (t) \mathrm{d} t = 1 \tag {3.10}$$

在 $t = \tau$ 时刻，如果 $f(t)$ 是连续的，那么它具有筛选特性，即

$$\int_ {- \infty} ^ {+ \infty} f (\tau) \delta (\tau - \tau) \mathrm{d} \tau = f (t) \tag {3.11}$$

换句话说，脉冲时间相当短，强度相当大，因此 $f$ 只在 $\delta$ 存在的地方才有意义。因为积分是一个求和过程的极限，所以式(3.11)可以看作把函数 $f$ 表示成许多脉冲之和。如果用 $u$ 代替 $f$ ，那么式(3.11)表示的是由一系列强度为 $u(t - \tau)$ 的脉冲之和表示的输入 $u(t)$ 。为了求出任意输入的系统响应，叠加原理告诉我们，只需要求得单位脉冲响应即可。

如果系统是线性时不变(LTI)系统，因为在时刻 t 所求得的系统响应只取决于在时刻 $\tau$ 时的输入和我们观察响应时刻之间的时间差，所以其脉冲响应可表示为 $h(t-\tau)$ 。因此时不变系统也叫平移不变系统。对于时不变系统，对于一般输入下的输出可以由如下积分给出

$$y (t) = \int_ {- \infty} ^ {+ \infty} u (\tau) h (t - \tau) \mathrm{d} \tau \tag {3.12}$$

或通过坐标变换 $\tau_{1} = t - \tau$ ，得

$$y (t) = \int_ {+ \infty} ^ {- \infty} u (t - \tau_ {1}) h (\tau_ {1}) (- \mathrm{d} \tau_ {1}) = \int_ {- \infty} ^ {+ \infty} h (\tau) u (t - \tau) \mathrm{d} \tau \tag {3.13}$$

这就是卷积积分。
