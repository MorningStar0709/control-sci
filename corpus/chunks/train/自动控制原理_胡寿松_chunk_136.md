# 2. 二阶系统的单位阶跃响应

式(3-13)表明,二阶系统特征根的性质取决于 $\zeta$ 值的大小。若 $\zeta < 0$ , 则二阶系统具有两个正实部的特征根, 其单位阶跃响应为

$$c (t) = 1 - \frac {\mathrm{e} ^ {- \zeta \omega_ {n} t}}{\sqrt {1 - \zeta^ {2}}} \sin (\omega_ {n} \sqrt {1 - \zeta^ {2}} t + \beta), \quad - 1 < \zeta < 0, t \geqslant 0$$

式中， $\beta=\arctan(\sqrt{1-\zeta^{2}}/\zeta)$ 。或者

$$
\begin{array}{l} c (t) = 1 + \frac {\mathrm{e} ^ {- (\zeta + \sqrt {\zeta^ {2} - 1}) \omega_ {n} t}}{2 \sqrt {\zeta^ {2} - 1} (\zeta + \sqrt {\zeta^ {2} - 1})} - \frac {\mathrm{e} ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t}}{2 \sqrt {\zeta^ {2} - 1} (\zeta - \sqrt {\zeta^ {2} - 1})}, \\ \zeta <   - 1, t \geqslant 0 \\ \end{array}
$$

由于阻尼比 $\zeta$ 为负，指数因子具有正幂指数，因此系统的动态过程为发散正弦振荡或单调发散的形式，从而表明 $\zeta < 0$ 的二阶系统是不稳定的。如果 $\zeta = 0$ ，则特征方程有一对纯虚根， $s_{1,2} = \pm j\omega_{n}$ ，对应于 $s$ 平面虚轴上一对共轭极点，可以算出系统的阶跃响应为等幅振荡，此时系统相当于无阻尼情况。如果 $0 < \zeta < 1$ ，则特征方程有一对具有负实部的共轭复根， $s_{1,2} = -\zeta\omega_{n} \pm j\omega_{n}\sqrt{1 - \zeta^{2}}$ ，对应于 $s$ 平面左半部的共轭复数极点，相应的阶跃响应为衰减振荡过程，此时系统处于欠阻尼情况。如果 $\zeta = 1$ ，则特征方程具有两个相等的负实根， $s_{1,2} = -\omega_{n}$ ，对应于 $s$ 平面负实轴上的两个相等实极点，相应的阶跃响应非周期地趋于稳态输出，此时系统处于临界阻尼情况。如果 $\zeta > 1$ ，则特征方程有两个不相等的负实根， $s_{1,2} = -\zeta\omega_{n} \pm \omega_{n}\sqrt{\zeta^{2} - 1}$ ，对应于 $s$ 平面负实轴上的两个不等实极点，相应的单位阶跃响应也是非周期地趋于稳态输出，但响应速度比临界阻尼情况缓慢，因此称为过阻尼情况。上述各种情况的闭环极点分布，如图3-9所示。

![](image/4a962f002b3dcf3bac6cd4e4b8ec03b9137e980667024ed62282d636e8a35544.jpg)  
图 3-9 二阶系统的闭环极点分布

由此可见， $\zeta$ 值的大小决定了系统的阻尼程度。对于图3-6所示的位置控制系统，有

$$\zeta = \frac {1}{2 \sqrt {T _ {m} K}} = \frac {F}{F _ {c}}$$

式中， $F_{c}=2\sqrt{JK_{1}}$ 为 $\zeta=1$ 时的阻尼系数。所以， $\zeta$ 是阻尼系数 F 与临界阻尼系数 $F_{c}$ 之比，故称为阻尼比或相对阻尼系数。

下面分别研究欠阻尼、临界阻尼、过阻尼二阶系统的单位阶跃响应。

(1) 欠阻尼 $(0<\zeta<1)$ 二阶系统的单位阶跃响应

若令 $\sigma = \zeta \omega_{\mathrm{n}},\omega_{\mathrm{d}} = \omega_{\mathrm{n}}\sqrt{1 - \zeta^{2}}$ ，则有

$$s _ {1, 2} = - \sigma \pm \mathrm{j} \omega_ {d}$$

式中， $\sigma$ 称为衰减系数， $\omega_{d}$ 叫做阻尼振荡频率。

当 $R(s)=1/s$ 时，由式(3-11)得

$$C (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \cdot \frac {1}{s} = \frac {1}{s} - \frac {s + \zeta \omega_ {n}}{(s + \zeta \omega_ {n}) ^ {2} + \omega_ {d} ^ {2}} - \frac {\zeta \omega_ {n}}{(s + \zeta \omega_ {n}) ^ {2} + \omega_ {d} ^ {2}}$$

对上式取拉氏反变换，求得单位阶跃响应为
