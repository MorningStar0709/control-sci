$$J = \int_ {0} ^ {t _ {f}} (1 + \dot {x} ^ {2}) ^ {1 / 2} \mathrm{d} t$$

式中，末端时刻 $t_f$ 未给定。已知 $x(0) = 1$ ，要求

$$x (t _ {f}) = c (t _ {f}) = 2 - t _ {f}$$

求使泛函为极值的最优轨线 $x^{*}(t)$ 及相应的 $t_{f}^{*}$ 和 $J^{*}$ 。

解 本例为起点固定、 $t_{f}$ 自由、末端受约束的泛函极值问题。显然，所给出的指标泛函就是 $x(t)$ 的弧长，约束方程 $c(t)=2-t$ 为平面上的斜直线，如图10-3所示。本例问题的实质是求从 $x(0)$ 到直线 $c(t)$ 并使弧长最短的曲线 $x^{*}(t)$ 。图中， $x(t)$ 为一条任意的容许轨线。

由题意

$$L (x, \dot {x}, t) = (1 + \dot {x} ^ {2}) ^ {1 / 2}$$

其偏导数为

$$\frac {\partial L}{\partial x} = 0, \quad \frac {\partial L}{\partial \dot {x}} = \frac {\dot {x}}{(1 + \dot {x} ^ {2}) ^ {1 / 2}}$$

根据欧拉方程

$$\frac {\partial L}{\partial x} - \frac {\mathrm{d}}{\mathrm{d} t} \frac {\partial L}{\partial \dot {x}} = - \frac {\mathrm{d}}{\mathrm{d} t} \left[ \frac {\dot {x}}{\sqrt {1 + \dot {x} ^ {2}}} \right] = 0$$

求得

$$\frac {\dot {x}}{\sqrt {1 + \dot {x} ^ {2}}} = c, \quad \dot {x} ^ {2} = \frac {c ^ {2}}{1 - c ^ {2}} = a ^ {2}$$

式中，c 为积分常数，a 为待定常数。因而

$$\dot {x} (t) = a, \quad x (t) = a t + b$$

其中 $b$ 也是待定常数。

由 $x(0)=1$ ，求出 b=1；由横截条件

$$\left[ L + (\dot {c} - \dot {x}) ^ {\mathrm{T}} \frac {\partial L}{\partial \dot {x}} \right] \bigg | _ {t _ {f}} = \left[ \sqrt {1 + \dot {x} ^ {2}} + (- 1 - \dot {x}) \frac {\dot {x}}{\sqrt {1 + \dot {x} ^ {2}}} \right] \bigg | _ {t _ {f}} = 0$$

![](image/e7c312dfee74317195504324fc3f91ffc2db55e1b999354d025b9c65ef988fed.jpg)

<details>
<summary>text_image</summary>

x(t)
2
x*(t)
1
x(t)
0
t_f
1
2
t
</details>

图10-3 例10-4的最优轨线

解得 $\dot{x}(t_f) = 1$ 。因为 $\dot{x}(t) = a$ ，所以有 $a = 1$ 。从而最优轨线为

$$x ^ {*} (t) = t + 1$$

当 $t = t_{f}$ 时， $x(t_{f}) = c(t_{f})$ ，即

$$t _ {f} + 1 = 2 - t _ {f}$$

求出最优末端时刻 $t_{f}^{*}=0.5$ 。将 $x^{*}(t)$ 及 $t_{f}^{*}$ 代入指标泛函，可得最优性能指标 $J^{*}=0.707$ 。
