$$\min _ {i} \max _ {j} L _ {i j} = \max _ {j} L _ {i * j}\max _ {j} \min _ {i} L _ {i j} = \min _ {i} L _ {i j}.$$

而 $L_{i*j*} = \max_j\min_iL_{ij} = \min_i\max_jL_{ij}$

从而有

$$L _ {i * j *} = \min _ {i} \max _ {j} L _ {i j} = \max _ {j} L _ {i * j} \geqslant L _ {i * j}L _ {i * j *} = \max _ {j} \min _ {i} L _ {i j} = \min _ {i} L _ {i j *} \leqslant L _ {i j}.$$

这就得出了

$$L _ {i * j} \leqslant L _ {i * j *} \leqslant L _ {i j *}$$

对一切 $i=1,2,\cdots,m; j=1,2,\cdots,n$ 成立。定理完全得证。

例10-1 给定矩阵对策的支付矩阵为

$$
\boldsymbol {L} = \left[ \begin{array}{c c c c} 6 & 1 & 8 & 0 \\ \textcircled {5} & 4 & \textcircled {5} & 2 \\ 6 & 2 & 7 & 6 \\ \textcircled {5} & - 1 & \textcircled {5} & 2 \end{array} \right]
$$

由于各列中的极小为 $(5, -1, 5, 0)$ ，其中的最大值为 $5$ ，故

$$\max _ {j} \min _ {i} L _ {i j} = L _ {i * j *} = 5, \quad i ^ {*} = 2, 4; j ^ {*} = 1, 3$$

又由于各行中的极大为(8,5,7,5)，其中的最小值为5，故

$$\min _ {i} \max _ {j} L _ {i j} = L _ {i * j *} = 5, \quad i ^ {*} = 2, 4; j ^ {*} = 1, 3$$

显然有

$$\min _ {i} \max _ {j} L _ {i j} = \max _ {j} \min _ {i} L _ {i j} = 5$$

即存在极小极大解，而 $(u_{2},v_{1})$ 、 $(u_{2},v_{3})$ 、 $(u_{4},v_{1})$ 、 $(u_{4},v_{3})$ 且都是对策解，即

$$\left(u _ {i ^ {*}}, v _ {j ^ {*}}\right) = \left(u _ {2}, v _ {1}\right) = \left(u _ {2}, v _ {3}\right) = \left(u _ {4}, v _ {1}\right) = \left(u _ {4}, v _ {3}\right)$$

由上例可见,对策的值为 5 这是唯一的,而对策的解却可以是不唯一的。
