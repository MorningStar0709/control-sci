# 3.1.2 传递函数和频率响应

第 2 章提出了传递函数简要的概念。稍后，我们将用卷积积分给出这一概念的严谨表达式。直接求解卷积积分式(3.14)是比较困难的。然而，使用由式

$$Y (s) = \int_ {- \infty} ^ {+ \infty} y (t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

定义的拉普拉斯变换能够给出一个间接方法 $^{②}$ ，事实上，应用拉普拉斯变换到卷积公式，得到

$$Y (s) = \int_ {- \infty} ^ {+ \infty} \left[ \int_ {- \infty} ^ {+ \infty} h (\tau) u (t - \tau) \mathrm{d} \tau \right] \mathrm{e} ^ {- s t} \mathrm{d} t$$

91

接下来，交换积分顺序，首先对 $t$ 进行积分，即

$$Y (s) = \int_ {- \infty} ^ {+ \infty} \left[ \int_ {- \infty} ^ {+ \infty} u (t - \tau) \mathrm{e} ^ {- s t} \mathrm{d} t \right] h (\tau) \mathrm{d} \tau$$

对内层积分作变量替换 $t - \tau = \eta$ ，得到

$$Y (s) = \int_ {- \infty} ^ {+ \infty} \left[ \int_ {- \infty} ^ {+ \infty} u (\eta) \mathrm{e} ^ {- s (\eta + \tau)} \mathrm{d} t \right] h (\tau) \mathrm{d} \tau \tag {3.16}Y (s) = \left[ \int_ {- \infty} ^ {+ \infty} u (\eta) \mathrm{e} ^ {- s \eta} \mathrm{d} \eta \right] \int_ {- \infty} ^ {+ \infty} h (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tauY (s) = U (s) H (s)$$

在这个解中， $U(s)$ 是输入时间函数的拉普拉斯变换，并且 $H(s)$ 为脉冲响应的拉普拉斯变换，将其定义为传递函数，通过此变换，复杂的卷积积分被转换为简单变换的乘积。接下来要对变换和传递函数进行解释。首先，一般情况下，不是对于变量s的所有值，变换的积分都收敛。实际上，它们仅仅在s平面中的一个有限区域内有定义。

对于 $e^{st}$ 形式的输入，直接可得卷积结果为 $H(s)e^{st}$ 。注意，输入和输出都是指数形式的时间函数，并且输出和输入的不同仅仅在于输出具有幅值 $H(s)$ 。 $H(s)$ 定义为系统的传递函数。常数 s 可以为复数，可表示为 $s=\sigma_{1}+\mathrm{j}\omega$ 。所以，输入和输出都可以是复数。如果在式(3.13)中，令 $u(t)=\mathrm{e}^{st}$ ，那么

$$y (t) = \int_ {- \infty} ^ {+ \infty} h (\tau) u (t - \tau) \mathrm{d} \tauy (t) = \int_ {- \infty} ^ {+ \infty} h (\tau) \mathrm{e} ^ {s (t - \tau)} \mathrm{d} \tauy (t) = \int_ {- \infty} ^ {+ \infty} h (\tau) \mathrm{e} ^ {s t} \mathrm{e} ^ {- s \tau} \mathrm{d} \tauy (t) = \int_ {- \infty} ^ {+ \infty} h (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau \mathrm{e} ^ {s t}y (t) = H (s) \mathrm{e} ^ {- s t} \tag {3.17}$$

其中：

$$H (s) = \int_ {- \infty} ^ {+ \infty} h (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau^ {\ominus} \tag {3.18}$$

拉普拉斯定义了这个积分，所以称为拉普拉斯变换。注意，积分区间为从 $-\infty$ 到 $+\infty$ ，意味着 $h(t)$ 在任意时刻都可能有值。需要对式(3.18)进行解释②，注意，对于所有的时间 $t$ ，输入为指数形式，式(3.18)表示的是对所有时间的响应，因此没有初始条件。从而式(3.17)给出了系统的稳态行为。所以，如果对于所有时间系统输入是指数形式的，并且传递函数 $H(s)$ 已知，输出很容易通过乘法计算，而没必要使用卷积！一个重要的结论是如果输入是指数时间函数，那么输出也是指数时间函数，而它们的比值就是传递函数。对于任意的因果系统， $h(t) = 0$ ，如果 $t < 0$ ，那么积分的上下限可以变成在0到 $+\infty$ ，即：

$$H (s) = \int_ {0} ^ {+ \infty} h (\tau) \mathrm{e} ^ {- s \tau} \mathrm{d} \tau$$

对于因果系统，式(3.13)简化为

$$y (t) = \int_ {0} ^ {+ \infty} h (\tau) u (t - \tau) \mathrm{d} \tau \tag {3.19}$$
