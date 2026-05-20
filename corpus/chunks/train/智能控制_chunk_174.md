# 4. 求模糊关系

模糊控制规则是一个多条语句,它可以表示为 $U \times V$ 上的模糊子集,即模糊关系 R 为

$$\boldsymbol {R} = (\mathrm{NBe} \times \mathrm{NBu}) \cup (\mathrm{NSe} \times \mathrm{NSu}) \cup (\mathrm{ZOe} \times \mathrm{ZOu}) \cup (\mathrm{PSe} \times \mathrm{PSu}) \cup (\mathrm{PBe} \times \mathrm{PBu})$$

其中规则内的模糊集运算取交集,规则间的模糊集运算取并集,即

$$
\mathrm{NBe} \times \mathrm{NBu} = \left[ \begin{array}{l} 1 \\ 0. 5 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] \times \left[ \begin{array}{l l l l l l l l l l} 1 & 0. 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right] = \left[ \begin{array}{l l l l l l l l l} 1. 0 & 0. 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right]

\mathrm{NS} e \times \mathrm{NS} u = \left[ \begin{array}{l} 0 \\ 0. 5 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] \times \left[ \begin{array}{l l l l l l l l l l} 0 & 0. 5 & 1 & 0. 5 & 0 & 0 & 0 & 0 & 0 \end{array} \right] = \left[ \begin{array}{l l l l l l l l l} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0. 5 & 0. 5 & 0. 5 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0. 5 & 1. 0 & 0. 5 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right]

\mathrm{ZOe} \times \mathrm{ZOu} = \left[ \begin{array}{l} 0 \\ 0 \\ 0. 5 \\ 1. 0 \\ 0. 5 \\ 0 \\ 0 \end{array} \right] \times \left[ \begin{array}{l l l l l l l l l} 0 & 0 & 0 & 0. 5 & 1 & 0. 5 & 0 & 0 & 0 \end{array} \right] = \left[ \begin{array}{l l l l l l l l l} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0. 5 & 0. 5 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0. 5 & 1. 0 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0. 5 & 0. 5 & 0. 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right]

\mathrm{PSe} \times \mathrm{PSu} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ 1. 0 \\ 0. 5 \\ 0 \end{array} \right] \times [ 0 0 0 0 0 0. 5 1. 0 0. 5 0 ] = \left[ \begin{array}{l l l l l l l l l} 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0. 5 & 1. 0 & 0. 5 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0. 5 & 0. 5 & 0. 5 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right]

\mathrm{PBe} \times \mathrm{PBu} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0.
5 \\ 1.
0 \end{array} \right] \times [ 0 0 0 0 0 0 0 0 0.
5 1.
