# 例6.24 天线的灵敏度函数

天线的开环传递函数为 $G(s)=1/s(s+1)$ ，补偿部分的传递函数为 $D(s)=10(0.5s+$ 1)/(0.1s+1)。试确定系统的灵敏度函数并绘图。

解答。系统的灵敏度函数为

$$\mathcal {S} = \frac {s (s + 1) (s + 1 0)}{s ^ {3} + 1 1 s ^ {2} + 6 0 s + 1 0 0} \tag {6.65}$$

用 Matlab 绘图，如图 6.79 所示，其语句如下。

$$
\begin{array}{l} s = t f \left(^ {\prime} s ^ {\prime}\right); \\ \operatorname{sys} S = s ^ {*} (s + 1) ^ {*} (s + 1 0) / \left(s ^ {\wedge} 3 + 1 1 ^ {*} s ^ {\wedge} 2 + 6 0 ^ {*} s + 1 0 0\right); \\ [ \text { mag }, \text { ph }, \text { w } ] = \text { bode(sysS) }; \\ \operatorname{loglog} (\mathrm{w}, \text { squeeze } (\mathrm{mag})), \text { grid } \\ \end{array}
$$

由 $M=\max(\text{mag})$ 可求得 S 的最大值为 1.366，可计算出矢量裕度 VM=0.732。

![](image/7d1b20c7e1272020fcf2b664b45bbcf2de4cb8ef565f1f27c463a814d16b9d1a.jpg)  
图 6.79 例 6.24 中的灵敏度函数
