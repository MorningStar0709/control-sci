# 3.4.3 调节时间

暂态响应中我们感兴趣的最后一个参数为调节时间 $t_{s}$ 。它是指暂态衰减到最小值以使 $y(t)$ 几乎处于稳定状态所需的时间。为了便于说明，我们将采用 1% 作为一个较合理的测度，其他情况下可以使用 2% 或 5% 。作为分析计算，我们注意到 y 相对 1 的偏差为衰减指数项 $e^{-\sigma t}$ 与周期函数的正弦和余弦之积。这个偏差的持续时间基本上由暂态指数决定，所以，可以定义调节时间为衰减指数达到 1% 时 $t_{s}$ 的值，即

$$\mathrm{e} ^ {- \zeta \omega_ {\mathrm{n}} t _ {\mathrm{s}}} = 0. 0 1$$

因此，

$$\zeta \omega_ {\mathrm{n}} t _ {\mathrm{s}} = 4. 6$$

或者

$$t _ {\mathrm{s}} = \frac {4 . 6}{\zeta \omega_ {\mathrm{n}}} = \frac {4 . 6}{\sigma} \tag {3.73}$$

其中： $\sigma$ 为极点负实部，由图 3.18 可以看出。

式(3.68)、式(3.72)和式(3.73)可利用无阻尼自然频率 $\omega_{n}$ 、阻尼比 $\zeta$ 和负实部 $\sigma$ 来描述无有限零点和两个复极点的系统的暂态响应。在分析和设计过程中，它们可用来估算任何系统的上升时间，超调和调节时间。在设计综合过程中，我们希望指定 $t_{r}$ 、 $M_{p}$ 和 $t_{s}$ 以及极点位置，以便实际响应的指标小于或等于这些指标。对于指定的 $t_{r}$ 、 $M_{p}$ 和 $t_{s}$ 值，等式的综合形式为

$$\omega_ {\mathrm{n}} \geqslant \frac {1 . 8}{t _ {\mathrm{r}}} \tag {3.74}$$

$\zeta\geqslant\zeta(M_{p})$ （从图3.24可见） (3.75)

$$\sigma \geqslant \frac {4 . 6}{t _ {\mathrm{s}}} \tag {3.76}$$

这些方程式可以绘制在 s 平面内，如图 3.25a～图 3.25c 所示，它们将被用到以后的章节中指导极点和零点位置的选择以满足控制系统动态响应指标。

![](image/10cea09454b344c2ca5aae506b3f23a4e22234e2b35c9005b165d89544828c59.jpg)

<details>
<summary>text_image</summary>

Im(s)
ωₙ
Re(s)
</details>

a）上升时间

![](image/d018a9d578a5bfd289b91de520a10b19d498b90db89b69257f4807e5ff5a1002.jpg)

<details>
<summary>text_image</summary>

arcsinζ
Im(s)
Re(s)
</details>

b）超调

![](image/2208fc02b7f5de522646c09a6676174a6df4952086f0281c997b3f7bb8a0937a.jpg)

<details>
<summary>text_image</summary>

Im(s)
s
Re(s)
</details>

c）调节时间

![](image/b472755fbce639adb85cd26976c83104e10594b293f59ce6f417105216eb3a9e.jpg)

<details>
<summary>text_image</summary>

Im(s)
Re(s)
</details>

d）这三个条件的合成  
图 3.25 根据特定暂态要求绘制的 s 平面区域图

记住式(3.74)～式(3.76)是很重要的，这些式子只是定性指导而不作为精确的设计公式。这意味着它们仅仅为设计迭代提供一个初始点。控制系统设计完成以后，需要通过精确的计算检查时间响应，通常使用数字仿真的方法，以验证时间指标是否已经满足要求。如果不满足要求，需要重新进行设计。

对于一阶系统，有

$$H (s) = \frac {\sigma}{s + \sigma}$$

其阶跃响应的拉普拉斯变换为

$$Y (s) = \frac {\sigma}{s (s + \sigma)}$$

我们从表 A.2 中第 11 条可以看出 $Y(s)$ 对应于

$$y (t) = (1 - \mathrm{e} ^ {- \sigma t}) 1 (t) \tag {3.77}$$

与式(3.73)比较可知一阶系统的 $t_{s}$ 值同样

$$t _ {\mathrm{s}} = \frac {4 . 6}{\sigma}$$

因为可能不存在超调，所以 $M_{\mathrm{p}} = 0$ 。从图3.14可知，从 $y = 0.1$ 到 $y = 0.9$ 的上升时间为

$$t _ {\mathrm{r}} = \frac {\ln 0 . 9 - \ln 0 . 1}{\sigma} = \frac {2 . 2}{\sigma}$$

然而，更典型的方法是依据它的时间常数描述一阶系统，在图3.14中它被定义为 $\tau = 1 / \sigma$
