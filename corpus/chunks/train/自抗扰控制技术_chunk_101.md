$$\frac {1}{1 + \alpha} \frac {\mathrm{d} | x | ^ {1 + \alpha}}{\mathrm{d} t} = | x | ^ {\alpha} \operatorname{sign} (x) \frac {\mathrm{d} x}{\mathrm{d} t}$$

对(3.2.10)式两边乘 $|x|^{\alpha}\mathrm{sign}(x)$ ，得

$$
\begin{array}{l} \frac {1}{1 + \alpha} \frac {\mathrm{d} | x | ^ {1 + \alpha}}{\mathrm{d} t} = - k | x | ^ {2 \alpha} + | x | ^ {\alpha} \text {sign} (x) w (x, t) = \\ - k \left(\mid x \mid^ {\alpha} \operatorname{sign} (x) - \frac {w}{2 k}\right) ^ {2} + \frac {w ^ {2}}{4 k} \\ \end{array}
$$

欲使 $\frac{d\mid x\mid^{1+\alpha}}{dt}<0$ ,必须

$$\left| | x | ^ {a} \operatorname{sign} (x) - \frac {w (x , t)}{2 k} \right| > \frac {| w (x , t) |}{2 k} \tag {3.2.11}$$

但由于 $\left|x\right|^{\alpha}\mathrm{sign}(x)-\frac{w}{2k}>\left|x\right|^{\alpha}-\frac{|w|}{2k}$ ，因此只要

$$\mid x \mid^ {\alpha} > \frac {\mid w (x , t) \mid}{k}, \text {即} \mid x \mid > \left(\frac {\mid w (x , t) \mid}{k}\right) ^ {\frac {1}{\alpha}} (3. 2. 1 2)$$

就满足不等式(3.2.11)，从而有 $\frac{\mathrm{d}|x|^{1 + \alpha}}{\mathrm{d}t} < 0.$

现在进一步假定:存在两常数 $m, w_{0}$ ，使函数 $w(x, t)$ 满足

$$\left| w (x, t) \right| < w _ {0} + \left| \frac {x}{m} \right| ^ {\alpha}$$

那么，当 $|x|^{\alpha} > \frac{m^{\alpha}}{m^{\alpha} - 1 / k}\frac{w_{0}}{k}$ 时，即

$$\mid x \mid > \left(\frac {m ^ {\alpha}}{m ^ {\alpha} - 1 / k}\right) ^ {\frac {1}{\alpha}} \left(\frac {w _ {0}}{k}\right) ^ {\frac {1}{\alpha}} \tag {3.2.13}$$

时,满足不等式(3.2.12),从而就有 $\frac{d}{dt}\frac{x^{1n\alpha}}{dt}<0$ ,因此闭环系统(3.2.10)的解 $x(t)$ 最终都要进入区间 $\left[-\left(\frac{m^{\alpha}}{m^{\alpha}-1/k}\right)^{\frac{1}{\alpha}}\left(\frac{w_{0}}{k}\right)^{\frac{1}{\alpha}},\left(\frac{m^{\alpha}}{m^{\alpha}-1/k}\right)^{\frac{1}{\alpha}}\left(\frac{w_{0}}{k}\right)^{\frac{1}{\alpha}}\right]$ 之内,即 $x(t)$ 最终都要进入误差小于 $\left(\frac{m^{\alpha}}{m^{\alpha}-1/k}\right)^{\frac{1}{\alpha}}\left(\frac{w_{0}}{k}\right)^{\frac{1}{\alpha}}$ 的范围.

显然，在非线性反馈(3.2.9)之下，闭环系统的稳态误差是与量 $\left(\frac{w_{0}}{k}\right)$ 的 $\frac{1}{\alpha}$ 次方成正比。在通常情形都有 $k>|w_{0}|$ ，因此只要0 $\leqslant\alpha<1,\left(\frac{1}{\alpha}>1\right)$ ，就有

$$\left(\frac {w _ {0}}{k}\right) ^ {\frac {1}{a}} \ll \frac {w _ {0}}{k}$$

当反馈增益 $k$ 超过扰动 $w_{0}$ 的作用范围，非线性反馈(3.2.9）所留

下的稳态误差远小于线性反馈(3.2.2)留下的稳态误差.

如果假定 $w(x,t)=w_{0}=\text{const}>0$ ，闭环系统(3.2.8)变成

$$\dot {x} = - k \mid x \mid^ {\alpha} \mathrm{sign} (x) + w _ {0} \tag {3.2.14}$$

让右段函数等于零,得系统平衡点方程
