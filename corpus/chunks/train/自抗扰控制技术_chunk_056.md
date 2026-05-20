当 $u(0) = \dot{u}(0) = 0$ 时，由于 $u(t)$ 缓变， $\ddot{u}(t)$ 很小，当 $t$ 足够大时， $\mathrm{e}^{-\alpha t}$ 也很小，于是就有近似表达式

$$y (t) \approx u (t) - \frac {1}{\alpha} \dot {u} (t) = u (t) - T \dot {u} (t)$$

于是当时间常数 T 足够小时,就有

$$y (t) \approx u (t) - T \frac {u (t) - u (t - T)}{T} = u (t - T)$$

因此

$$y (t) \Rightarrow u (t - T)$$

这就是说，当方程

$$\dot {y} = - \frac {1}{T} (y - u (t)) = - \alpha (y - u (t))$$

或传递关系 $y = \frac{1}{Ts + 1} u$ 中的输入项 $u(t)$ 的变化比较缓慢时，其解（系统输出）可近似地表示成

$$y (t) \approx u (t - T) \tag {2.1.5}$$

即系统的输出 $y(t)$ 将以时间常数 T 为延迟时间来跟踪输入信号 $u(t)$ .

这个解的近似式也可以从另一角度直接得到．实际上，上述惯性环节的传递函数，当时间常数 T 较小时，可近似成

$$\frac {1}{1 + T s} \approx e ^ {- T s}$$

而表达式 $\mathrm{e}^{-T}$ 是变量 $x(t)$ 延时(时滞) $T$ 时间的函数 $x(t - T)$ 的

拉普拉斯变换表达式,因此可以形象地推导出

$$\gamma (t) = \frac {1}{T s + 1} u (t) \approx \mathrm{e} ^ {- T s} u (t) = u (t - T)$$
