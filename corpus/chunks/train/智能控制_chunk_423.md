# 9.5.2 自校正控制算法

考虑被控对象

$$y (k + 1) = g [ y (k) ] + \varphi [ y (k) ] u (k) \tag {9.8}$$

式中，u, y 分别为对象的输入、输出， $\varphi[\cdot]$ 为非零函数。

若 $g[\cdot]$ , $\varphi[\cdot]$ 已知, 则根据确定性等价原则, 自校正控制算法为

$$u (k) = \frac {- g [ \bullet ]}{\varphi [ \bullet ]} + \frac {r (k + 1)}{\varphi [ \bullet ]} \tag {9.9}$$

将控制器代入式(9.8)，则系统的输出 $y(k)$ 能精确地跟踪输入 $r(k)$ 。

若 $g[\cdot]$ , $\varphi[\cdot]$ 未知, 则可通过在线训练神经网络, 得到 $g[\cdot]$ , $\varphi[\cdot]$ 的估计值 $Ng[\cdot]$ , $N\varphi[\cdot]$ , 此时自校正控制算法为

$$u (k) = \frac {- N g [ \bullet ]}{N \varphi [ \bullet ]} + \frac {r (k + 1)}{N \varphi [ \bullet ]} \tag {9.10}$$

式中， $Ng[\cdot]$ ， $N\varphi[\cdot]$ 分别为神经网络的输出。
