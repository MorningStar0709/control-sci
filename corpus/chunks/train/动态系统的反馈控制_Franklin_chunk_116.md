# 例3.5 RC电路的传递函数

计算如图 3.3 所示电源驱动的 RC 电路的传递函数。

解答。由基尔霍夫电压定律得系统方程为

$$R i (t) + y (t) = u (t)i (t) = C \frac {\mathrm{d} y (t)}{\mathrm{d} t}$$

或者

$$R C \dot {y} + y = u (t)$$

![](image/fc60f1350968f8c7f5712f1b2922d544349cd8c7607e2661849d4fb3b8cc5a83.jpg)

<details>
<summary>text_image</summary>

R
→ i(t)
+   +
u(t) ~   C = y(t)
-   -
</details>

图3.3 RC电路图

93

如果输入电压是单位脉冲信号，即

$$R C \dot {y} + y = \delta (t)$$

并且对上述方程两边取拉普拉斯变换(附录 A)，得

$$R C (s Y (s) - y (0 ^ {-})) + Y (s) = U (s) = 1$$

然后在零初始条件 $(y(0^{-})=0)$ 下，得到

$$H (s) = \frac {Y (s)}{U (s)} = Y (s) = \frac {1}{R C s + 1}$$

输出，就是脉冲响应也就是 $Y(s)$ 的拉普拉斯反变换

$$y (t) = h (t) = \frac {1}{R C} \mathrm{e} ^ {- \frac {t}{R C}} 1 (t)$$

所以，此系统的传递函数为

$$H (s) = \mathcal {L} \{h (t) \} = \frac {1}{R C s + 1}$$

线性时不变系统的指数响应往往用于求频率响应或者正弦信号响应。首先，我们将正弦信号的频率响应表示成两个指数表达式之和(欧拉(Euler)方程):

$$A \cos (\omega t) = \frac {A}{2} \left(\mathrm{e} ^ {\mathrm{j} \omega t} + \mathrm{e} ^ {- \mathrm{j} \omega t}\right)$$

如果在基本响应式(3.17)中令 $s=\mathrm{j}\omega$ ，那么对于输入 $u(t)=\mathrm{e}^{\mathrm{j}\omega t}$ 的响应为 $y(t)=H(\mathrm{j}\omega)\mathrm{e}^{\mathrm{j}\omega t}$ ；类似地，对于 $u(t)=\mathrm{e}^{-\mathrm{j}\omega t}$ 的响应为 $H(-\mathrm{j}\omega)\mathrm{e}^{-\mathrm{j}\omega t}$ ，由叠加原理得该余弦信号的响应为这两个指数响应之和，即

$$y (t) = \frac {A}{2} [ H (\mathrm{j} \omega) \mathrm{e} ^ {\mathrm{j} \omega t} + H (- \mathrm{j} \omega) \mathrm{e} ^ {- \mathrm{j} \omega t} ] \tag {3.27}$$

传递函数 $H(\mathrm{j}\omega)$ 为复数时，可以表示为极坐标 $H(\mathrm{j}\omega)=M(\omega)\mathrm{e}^{\mathrm{j}\varphi(\omega)}$ 形式，简记为 $H=M\mathrm{e}^{\mathrm{j}\varphi}$ 的形式或振幅-相位形式。将此代入到式(3.27)中，得到

$$
\begin{array}{l} y (t) = \frac {A}{2} M \left(\mathrm{e} ^ {\mathrm{j} (\omega t + \varphi)} + \mathrm{e} ^ {- \mathrm{j} (\omega t + \varphi)}\right) \\ = A M \cos (\omega t + \varphi) \tag {3.28} \\ \end{array}
$$

其中：

$$M = | H (\mathrm{j} \omega) |, \quad \varphi = \angle H (\mathrm{j} \omega)$$

这意味着，传递函数为 $H(s)$ 的系统，其输入是幅值为 A 的正弦信号，那么输出也是同频率的幅值为 AM 的正弦信号，且存在 $\varphi$ 角相移动。
