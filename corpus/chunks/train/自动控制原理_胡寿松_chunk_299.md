$$\omega_ {x} = \sqrt {3}$$

$K = 4$ 时

$$G (\mathrm{j} \omega_ {x}) = - 0. 5, \quad h = 2\omega_ {c} = \sqrt {1 6 ^ {\frac {1}{3}} - 1} = 1. 2 3 3, \quad \underline {{G (\mathrm{j} \omega_ {c})}} = - 1 5 2. 9 ^ {\circ}, \quad \gamma = 2 7. 1 ^ {\circ}$$

$K = 10$ 时

$$
\begin{array}{l} G (\mathrm{j} \omega_ {x}) = - 1. 2 5, \quad h = 0. 8 \\ \omega_ {c} = 1. 9 0 8, \quad \angle G (\mathrm{j} \omega_ {c}) = - 1 8 7. 0 ^ {\circ}, \quad \gamma = - 7. 0 ^ {\circ} \\ \end{array}
$$

![](image/250f20f7be4fbf4dd5cfbe8733f9f8d5790a4b10e296f347654b998975413dbd.jpg)

<details>
<summary>text_image</summary>

-1
0
+4
ω
10
j
</details>

图 5-41 例 5-13 K=4 和 K=10 时系统开环幅相曲线

分别作出 K=4 和 K=10 的开环幅相曲线即闭合曲线 $\Gamma_{G}$ ，如图 5-41 所示。由奈氏判据知：

K=4 时, 系统闭环稳定, h>1, γ>0;

K=10 时，系统闭环不稳定，h<1， $\gamma<0$ 。

上述根据 $\gamma>0$ 且 h>1 或 $h(\mathrm{dB})>0$ 判断系统的闭环稳定性方法可推广至半闭合曲线 $\Gamma_{GH}$ 分别与单位圆或负实轴至多只有一个交点，或 $L(\omega)>0, \Gamma_{\varphi}$ 与 $(2k+1)\pi$ 线 $(k=0,\pm1,\cdots)$ 至多只有一个交点，且开环传递函数无 s 开右半平面极点的情况。应注意的是，该结论对非最小相位系统并不都适用。此外，仅用相角裕度或幅值裕度，都不足以反映系统的稳定程度。

例 5-14 典型二阶系统如图 5-42 所示, 试确定系统的相角裕度 $\gamma$ 。

![](image/e19346f6f98a41e19a5dc6f949e828abd3bc5d955e4a5915cfe015beb1a70a5c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["ω²n / (s(s+2ζωn))"]
    C --> D["C'(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

图 5-42 典型二阶系统

解 典型二阶系统的开环频率特性为

$$G (\mathrm{j} \omega) = \frac {\omega_ {n} ^ {2}}{\mathrm{j} \omega (\mathrm{j} \omega + 2 \zeta \omega_ {n})} = \frac {\omega_ {n} ^ {2}}{\omega \sqrt {\omega^ {2} + 4 \zeta^ {2} \omega_ {n} ^ {2}}} \left\lfloor - \arctan \frac {\omega}{2 \zeta \omega_ {n}} - 9 0 ^ {\circ} \right.$$

设 $\omega_{c}$ 为截止频率，则有

$$\mid G (\mathrm{j} \omega_ {c}) \mid = \frac {\omega_ {n} ^ {2}}{\omega_ {c} \sqrt {\omega_ {c} ^ {2} + 4 \zeta^ {2} \omega_ {n} ^ {2}}} = 1$$

可求得 $\omega_{c} = \omega_{n}(\sqrt{4\zeta^{4} + 1} -2\zeta^{2})^{\frac{1}{2}}$ (5-85)

按相角裕度定义

$$
\begin{array}{l} \gamma = 1 8 0 ^ {\circ} + \underline {{{G (\mathrm{j} \omega_ {c})}}} = 9 0 ^ {\circ} - \arctan \frac {\omega_ {c}}{2 \zeta \omega_ {n}} \\ = \arctan \frac {2 \zeta \omega_ {n}}{\omega_ {c}} = \arctan \left[ 2 \zeta \left(\frac {1}{\sqrt {4 \zeta^ {4} + 1} - 2 \zeta^ {2}}\right) ^ {\frac {1}{2}} \right] \tag {5-86} \\ \end{array}
$$

因为 $\frac{\mathrm{d}}{\mathrm{d}\zeta} (\sqrt{4\zeta^4 + 1} -2\zeta^2) = \frac{4\zeta}{\sqrt{4\zeta^4 + 1}} (2\zeta^2 -\sqrt{4\zeta^4 + 1}) <   0$
