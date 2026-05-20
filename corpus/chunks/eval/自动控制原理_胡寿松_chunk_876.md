# 1）系统传递函数模型描述。

命令格式：sys = tf(num, den, Ts)

其中，num, den 分别为分子、分母多项式降幂排列的系数向量；Ts 表示采样时间，缺省时描述的是连续传递函数。图 B-1 中的 $G_{1}(s)$ 可描述为 $G_{1}=\operatorname{tf}([1], [1\ 1\ 0])$ 。

若传递函数的分子、分母为因式连乘形式，如图B-1中 $G_{2}(s)$ ，则可以考虑采用conv命令进行多项式相乘，得到展开后的分子、分母多项式降幂排列的系数向量，再用tf命令建模。如 $G_{2}(s)$ 可描述为 $\mathrm{num} = 1;\mathrm{den} = \mathrm{conv}([0.11],[13]);\mathrm{G}2 = \mathrm{tf}(\mathrm{num},\mathrm{den})$ 。
