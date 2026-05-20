Bellman 方程 (动态规划方法的基础). 设式 (7.1.52), (7.1.53), (7.1.54) 的最优控制 $u^{*}(t)$ 存在, 且 $J^{*}(x_{0}, t_{0}) \stackrel{\mathrm{def}}{=} J[u^{*}]$ . 显然有 $J^{*}(0, t_{f}^{*}) = 0$ . 假定标量函数 $J^{*}(x, t)$ 二次连续可微. 设 $x^{*}(t)$ 是相应的最优轨线. 任取 $t \in (t_{0}, t_{f}^{*})$ , 依“最优性原理”有

$$J ^ {*} (x _ {0}, t _ {0}) = \int_ {t _ {0}} ^ {t _ {f} ^ {*}} l (x ^ {*} (t), u ^ {*} (t)) \mathrm{d} t = \int_ {t _ {0}} ^ {t} l (x ^ {*} (\tau), u ^ {*} (\tau)) \mathrm{d} \tau + J ^ {*} (x ^ {*} (t), t).$$

由此不难得到

$$0 = l (x ^ {*} (t), u ^ {*} (t)) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial x} f (x ^ {*} (t), u ^ {*} (t)) + \frac {\partial J ^ {*} (x ^ {*} (t) , t)}{\partial t}. \tag {7.1.57}$$

现假定系统 (7.1.52) 从 $t_0$ 时刻初始状态 $x_0$ 开始按如下方式运动：

(1) 对任意固定 $t \in \Omega(t_0, t_f; u^*)$ 式 (7.1.52) 在区间 $[t_0, t]$ 上以最优方式运动. 相应的性能指标值（或花费的代价）为 $\int_{t_0}^{t} l(x^*(\tau), u^*(\tau)) \mathrm{d}\tau$ ;  
(2) 任取 $\Delta t > 0$ 和 $v \in \mathbb{U}_r$ , (7.1.52) 在 $v$ 的作用下, $t$ 时刻以 $x^*(t)$ 为初态开始运动, 运行至 $t + \Delta t$ 时刻的状态 $x(t + \Delta t)$ 为

$$x (t + \Delta t) = x ^ {*} (t) + \int_ {t} ^ {t + \Delta t} f (x (\tau), v) \mathrm{d} \tau . \tag {7.1.58}$$

显然

$$
\begin{array}{l} \Delta x (t) \stackrel {\mathrm{def}} {=} x (t + \Delta t) - x ^ {*} (t) = \int_ {t} ^ {t + \Delta t} f (x (\tau), v) \mathrm{d} \tau \\ = f (x ^ {*} (t), v) \Delta t + o (\Delta t). \tag {7.1.59} \\ \end{array}
$$

在时段 $[t, t + \Delta t]$ 上相应的性能指标值为 $\int_{t}^{t + \Delta t} l(x(\tau), v) \mathrm{d}\tau$ ;

(3) 从 $t + \Delta t$ 开始，式 (7.1.52) 以 $x^{*}(t) + \Delta x(t)$ 为初态按最优方式运行至终端状态 $x(t_{f}^{*})$ 达到目标集 $S_{0} = \{0\}$ ，即 $x(t_{f}) = 0$ 。相应的性能指标值为 $J^{*}(x^{*}(t) + \Delta x(t), t + \Delta t)$ 。图示如下：

![](image/2e998ec8804b0b778629b431c8f0af8155205bec7bcc591456c69ebdaa6b932c.jpg)

<details>
<summary>text_image</summary>

在时刻 t+Δt 以后的最优轨线
在时段 [t, t+Δt] 上在 v 作用下的轨线 x(s)
x(t+Δt)
x*(t)
x*(t_f)=0
在时段 [t_0, t_f] 上的最优轨线
x_{(t)}
</details>

图7.1.3

于是系统 (7.1.52) 从 $t_0$ 时刻初态 $x_0$ 开始按 (1), (2), (3) 方式运动至目标集 $S_0$ , 且相应的性能指标值为三个时段上性能指标之和

$$\int_ {t _ {0}} ^ {t} l (x ^ {*} (s), u ^ {*} (s)) \mathrm{d} s + \int_ {t} ^ {t + \Delta t} l (x (s), v) \mathrm{d} s + J ^ {*} (x ^ {*} (t) + \Delta x (t), t + \Delta t).$$

由于 $(x^{*}(t), u^{*}(t))$ 是最优过程，所以有

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t} l (x ^ {*} (s), u ^ {*} (s)) \mathrm{d} s + J ^ {*} (x ^ {*} (t), t) \\ \leqslant \int_ {t _ {0}} ^ {t} l (x ^ {*} (s), u ^ {*} (s)) \mathrm{d} s + \int_ {t} ^ {t + \Delta t} l (x (s), v) \mathrm{d} s + J ^ {*} (x ^ {*} (t) + \Delta x (t), t + \Delta t), \\ \end{array}
$$

即
