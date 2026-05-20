# 习题

5-1 设系统闭环稳定, 闭环传递函数为 $\Phi(s)$ , 试根据频率特性的定义证明: 输入为余弦函数 $r(t) = A\cos(\omega t + \varphi)$ 时, 系统的稳态输出为

$$c _ {s} (t) = A \cdot | \Phi (\mathrm{j} \omega) | \cos [ \omega t + \varphi + \underline {{{\Phi (\mathrm{j} \omega)}}} ]$$

5-2 若系统单位阶跃响应

$$c (t) = 1 - 1. 8 \mathrm{e} ^ {- 4 t} + 0. 8 \mathrm{e} ^ {- 9 t}$$

试确定系统的频率特性。

![](image/6db1080e8d7a3450e812d9c36b89a5465d42a649c7ce6d00e0004d9a9fe56e61.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["E(s)"]
    C --> D["1/(s+1)"]
    D --> E["C(s)"]
    E --> F["-"]
    F --> B
```
</details>

图 5-62 题 5-3 控制系统结构图

5-3 设控制系统结构图如图 5-62 所示, 试确定在输入信号

$$r (t) = \sin (t + 3 0 ^ {\circ}) - \cos (2 t - 4 5 ^ {\circ})$$

作用下，系统的稳态误差 $e_{s}(t)$ 。

5-4 典型二阶系统的开环传递函数

$$G (s) = \frac {\omega_ {n} ^ {2}}{s (s + 2 \zeta \omega_ {n})}$$

当取 $r(t) = 2\sin t$ 时，系统的稳态输出

$$c _ {s} (t) = 2 \sin (t - 4 5 ^ {\circ})$$

试确定系统参数 $\omega_{n}, \zeta$ 。

5-5 已知系统开环传递函数

$$G (s) H (s) = \frac {K (\tau s + 1)}{s ^ {2} (T s + 1)}; \quad K, \tau , T > 0$$

试分析并绘制 $\tau > T$ 和 $T > \tau$ 情况下的概略开环幅相曲线。

5-6 已知系统开环传递函数

$$G (s) H (s) = \frac {1}{s ^ {\nu} (s + 1) (s + 2)}$$

试分别绘制 $\nu=1,2,3,4$ 时系统的概略开环幅相曲线。

5-7 已知系统开环传递函数

$$G (s) = \frac {K (- T _ {2} s + 1)}{s (T _ {1} s + 1)}; \qquad K, T _ {1}, T _ {2} > 0$$

当取 $\omega = 1$ 时， $\underline{G(j\omega)} = -180^{\circ}$ ， $|G(j\omega)| = 0.5$ 。当输入为单位速度信号时，系统的稳态误差为0.1，试写出系统开环频率特性表达式 $G(j\omega)$ 。

5-8 已知系统开环传递函数

$$G (s) H (s) = \frac {1 0}{s (2 s + 1) \left(s ^ {2} + 0 . 5 s + 1\right)}$$

试分别计算 $\omega=0.5$ 和 $\omega=2$ 时，开环频率特性的幅值 $A(\omega)$ 和相位 $\varphi(\omega)$ 。

5-9 已知系统开环传递函数

$$G (s) H (s) = \frac {1 0}{s (s + 1) \left(s ^ {2} / 4 + 1\right)}$$

试绘制系统概略开环幅相曲线。

5-10 已知系统开环传递函数

$$G (s) H (s) = \frac {(s + 1)}{s \left(\frac {s}{2} + 1\right) \left(\frac {s ^ {2}}{9} + \frac {s}{3} + 1\right)}$$

要求选择频率点,列表计算 $A(\omega)$ , $L(\omega)$ 和 $\varphi(\omega)$ , 并据此在半对数坐标纸上绘制系统开环对数频率特性曲线。

5-11 绘制下列传递函数的对数幅频渐近特性曲线：

(1) $G(s) = \frac{2}{(2s + 1)(8s + 1)};$

(2) $G(s)=\frac{200}{s^{2}(s+1)(10s+1)}$ ;

(3) $G(s) = \frac{8\left(\frac{s}{0.1} + 1\right)}{s(s^2 + s + 1)\left(\frac{s}{2} + 1\right)}$ ;

(4) $G(s)=\frac{10\left(\frac{s^{2}}{400}+\frac{s}{10}+1\right)}{s(s+1)\left(\frac{s}{0.1}+1\right)}$ 。

5-12 已知最小相位系统的对数幅频渐近特性曲线如图 5-63 所示, 试确定系统的开环传递函数。

![](image/5040d962cd89018fb0f2c8b811fd16a507ae1d9f4b54bbba0d6f93174ef57811.jpg)

<details>
<summary>line</summary>

| ω | L(ω) |
| --- | --- |
| 0 | 40 |
| ω₁ | 40 |
| ω₂ | -20 |
| 100 | -20 |
</details>

(a)
