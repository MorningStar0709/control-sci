应该注意的是,当系统的多个环节具有相同交接频率时,该交接频率点处斜率的变化应为各个环节对应的斜率变化值的代数和。

以 $k=-20\nu$ dB/dec 的低频渐近线为起始直线，按交接频率由小到大顺序和由表 5-2 确定斜率变化，再逐一绘制直线，得到系统开环对数幅频渐近特性曲线。

例5-6 已知系统开环传递函数为

$$G (s) H (s) = \frac {2 0 0 0 s - 4 0 0 0}{s ^ {2} (s + 1) (s ^ {2} + 1 0 s + 4 0 0)}$$

试绘制系统开环对数幅频渐近特性曲线。

解 开环传递函数的典型环节分解形式为

$$G (s) H (s) = \frac {- 1 0 \left(1 - \frac {s}{2}\right)}{s ^ {2} (s + 1) \left(\frac {s ^ {2}}{2 0 ^ {2}} + \frac {1}{2} \times \frac {s}{2 0} + 1\right)}$$

开环系统由六个典型环节串联而成：非最小相位比例环节、两个积分环节、非最小相位一阶微分环节、惯性环节和振荡环节。

1) 确定各交接频率 $\omega_{i}, i=1,2,3$ 及斜率变化值

非最小相位一阶微分环节： $\omega_{2}=2$ ，斜率增加20dB/dec

惯性环节： $\omega_{1}=1$ ，斜率减小20dB/dec

振荡环节： $\omega_{3}=20$ ，斜率减小40dB/dec

最小交接频率 $\omega_{\min}=\omega_{1}=1$ 。

2）绘制低频段 $(\omega < \omega_{\mathrm{min}})$ 渐近特性曲线。因为 $\nu = 2$ ，则低频渐近线斜率 $k = -40\mathrm{dB / dec}$ ，按方法二得直线上一点 $(\omega_0,L_a(\omega_0)) = (1,20\mathrm{dB})$ 。

3）绘制频段 $\omega\geqslant\omega_{min}$ 渐近特性曲线

$$\omega_ {\mathrm{min}} \leqslant \omega < \omega_ {2}, \quad k = - 6 0 \mathrm{dB/dec}\omega_ {2} \leqslant \omega < \omega_ {3}, \qquad k = - 4 0 \mathrm{dB/dec}\omega \geqslant \omega_ {3}, \qquad k = - 8 0 \mathrm{dB/dec}$$

系统开环对数幅频渐近特性曲线如图 5-24 所示。

![](image/53454e030f72ba7d62364e87ead982735e7d8e73bc83db7c43384389bbd308cd.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | L(ω)/dB |
| --- | --- |
| 0.1 | 60 |
| 1 | 20 |
| 2 | 0 |
| 10 | -20 |
| 20 | -40 |
| 50 | -60 |
</details>

图 5-24 例 5-6 系统对数幅频渐近特性曲线 (MATLAB)

开环对数相频曲线的绘制,一般由典型环节分解下的相频特性表达式,取若干个频率点,列表计算各点的相角并标注在对数坐标图中,最后将各点光滑连接,即可得开环对数相频曲线。具体计算相角时应注意判别象限。例如在例 5-6 中

$$
\varphi (\omega) = \left\lfloor \frac {1}{1 - \frac {\omega^ {2}}{4 0 0} + j \frac {\omega}{4 0}} \right. = \left\{ \begin{array}{l l} - \arctan \frac {\frac {\omega}{4 0}}{1 - \frac {\omega^ {2}}{4 0 0}}, & 0 <   \omega \leqslant 2 0 \\ - \left(1 8 0 ^ {\circ} - \arctan \frac {\frac {\omega}{4 0}}{\frac {\omega^ {2}}{4 0 0} - 1}\right), & \omega > 2 0 \end{array} \right.
$$

例 5-7 已知系统开环传递函数为

$$G (s) = \frac {2 0 0 0 (s + 0 . 5)}{s (s + 1 0) (s + 5 0)}$$

试绘制系统开环伯德图。

解 按如下步骤绘制。

步骤 1 把传递函数变为如下的伯德形式：

$$G (\mathrm{j} \omega) = \frac {2 [ (\mathrm{j} \omega / 0 . 5) + 1 ]}{\mathrm{j} \omega [ (\mathrm{j} \omega / 1 0) + 1 ] [ (\mathrm{j} \omega / 5 0) + 1 ]}$$

步骤2 注意到项 $\mathrm{j}\omega$ 是一阶的，而且在分母中出现，所以 $k = -1(-20\mathrm{dB / dec})$ 。因此低频段的渐近线由第一项决定

$$G (\mathrm{j} \omega) = \frac {2}{\mathrm{j} \omega}$$
