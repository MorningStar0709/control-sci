$$
\begin{array}{l} G (s) = \frac {\left[ \left(\frac {s}{1 0 0}\right) ^ {2} + 0 . 0 1 \left(\frac {s}{1 0 0}\right) + 1 \right]}{\left[ \left(\frac {s}{1 0}\right) ^ {2} + \left(\frac {s}{1 0}\right) + 1 \right] \left[ \frac {s}{5} + 1 \right]} \\ \times \frac {1}{\left[ \left(\frac {s}{1 0 0}\right) ^ {2} + 0 . 1 \left(\frac {s}{1 0 0}\right) + 1 \right]} \\ \end{array}
$$

如果该系统的输入为阶跃信号，估算上升时间，调节时间和超调是多少？并简单叙述一下理由。

3.45 三个闭环传递函数。分别为

$$\frac {Y (s)}{R (s)} = T _ {1} (s) = \frac {2}{s ^ {2} + 2 s + 2}\frac {Y (s)}{R (s)} = T _ {2} (s) = \frac {2 (s + 3)}{2 \left(s ^ {2} + 2 s + 2\right)}\frac {Y (s)}{R (s)} = T _ {3} (s) = \frac {6}{(s + 3) (s ^ {2} + 2 s + 2)}$$

当输入为单位阶跃信号时，估算每个传递函数的上升时间，调节时间和超调。

3.46 下面给出了五个传递函数，分别为

$$G _ {1} (s) = \frac {4 0}{s ^ {2} + 4 s + 4 0}G _ {2} (s) = \frac {4 0}{(s + 1) (s ^ {2} + 4 s + 4 0)}G _ {3} (s) = \frac {1 2 0}{(s + 3) (s ^ {2} + 4 s + 4 0)}G _ {4} (s) = \frac {2 0 (s + 2)}{(s + 1) (s ^ {2} + 4 s + 4 0)}G _ {5} (s) = \frac {3 6 0 4 0 / 4 0 1 \left(s ^ {2} + s + 4 0 1\right)}{\left(s ^ {2} + 4 s + 4 0\right) \left(s ^ {2} + s + 9 0 1\right)}$$

(a) 哪个传递函数满足超调 $M_{p} \leqslant 5\%$ ?   
(b) 哪个传递函数满足上升时间 $t_{r} \leqslant 0.5s$ ?  
(c) 哪个传递函数满足调节时间 $t_{s} \leqslant 2.5s$ ?

3.47 考虑两个非最小相位系统，分别为

$$G _ {1} (s) = \frac {2 (s - 1)}{(s + 1) (s + 2)} \tag {3.98}G _ {2} (s) = \frac {3 (s - 1) (s - 2)}{(s + 1) (s + 2) (s + 3)} (3. 9 9)$$

(a) 画出 $G_{1}(s)$ 和 $G_{2}(s)$ 的单位阶跃响应，特别注意相应的暂态部分。  
(b) 说明与零点位置相关的这两个响应的

特性有何不同。

(c) 考虑一个稳定且严格恰当的系统(也就是说，m 个零点和 n 个极点，其中 m < n)。 $y(t)$ 表示系统阶跃响应。如果该响应在开始阶段朝“错误”方向运动，那么阶跃响应会有负超调。证明当且仅当系统的传递函数在 RHP(右半平面)中有奇数个实数零点时，该稳定且严格恰当的系统具有负超调。

3.48 求与式(3.65)相对应的脉冲响应和阶跃响应之间的关系，其中：

(a) 具有重根。  
(b) 都是实根。用双曲线(正弦, 余弦)表示答案以便更好的表明系统响应的性质。  
(c) 阻尼系数 $\zeta$ 值为负。

3.49 考虑如下带有附加极点的二阶系统：

$$H (s) = \frac {\omega_ {\mathrm{n}} ^ {2} p}{(s + p) (s ^ {2} + 2 \zeta \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2})}$$

单位阶跃响应为

$$y (t) = 1 + A \mathrm{e} ^ {- p t} + B \mathrm{e} ^ {- \sigma t} \sin (\omega_ {\mathrm{d}} t - \theta)$$

其中：

$$
\begin{array}{l} A = \frac {- \omega_ {\mathrm{n}} ^ {2}}{\omega_ {\mathrm{n}} ^ {2} - 2 \zeta \omega_ {\mathrm{n}} p + p ^ {2}} \\ B = \frac {p}{\sqrt {(p ^ {2} - 2 \zeta \omega_ {\mathrm{n}} p + \omega_ {\mathrm{n}} ^ {2}) (1 - \zeta^ {2})}} \\ \theta = \arctan \frac {\sqrt {1 - \zeta^ {2}}}{- \zeta} + \arctan \frac {\omega_ {n} \sqrt {1 - \zeta^ {2}}}{p - \zeta \omega_ {n}} \\ \end{array}
$$
