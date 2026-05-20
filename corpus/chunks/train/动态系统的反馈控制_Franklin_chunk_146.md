# 例 3.18 用 Matlab 建立巡航控制传递函数

求例 2.1 中巡航控制系统的输入 u 和汽车位置 x 之间的传递函数。

解答。由例 2.1 我们求得系统的传递函数为

$$H (s) = \frac {0 s ^ {2} + 0 s + 0 . 0 0 1}{s ^ {2} + 0 . 0 5 s + 0} = \frac {0 . 0 0 1}{s (s + 0 . 0 5)}$$

在 Matlab 中，分子多项式的系数表示成行矢量 num 将分母多项式表示成行矢量 den。该例结果为

$$
\mathrm{num} = \left[ \begin{array}{l l l} 0 & 0 & 0. 0 0 1 \end{array} \right], \quad \mathrm{den} = \left[ \begin{array}{l l l} 1 & 0. 0 5 & 0 \end{array} \right]
$$

结果能够用 Matlab 中 (num, den) 形式的命令返回。零极点的描述可以用 Matlab 命令计算，即

$$[ z, p, k ] = \text { tf2zp(num,den) }$$

并且得到传递函数的分解形式，其中： $z=[]$ ， $p=[0-0.05]^{\mathrm{T}}$ ，k=0.001。

113
