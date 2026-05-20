# 10.2.3 矩阵对策存在极小极大解的条件

设对策的支付矩阵为 L，此时 v 方力图使 u 支付最大，而 u 方则试图使之最小。

$$
\boldsymbol {L} = \left[ \begin{array}{l l l l} L _ {1 1} & L _ {1 2} & \dots & L _ {1 n} \\ L _ {2 1} & L _ {2 2} & \dots & L _ {2 n} \\ L _ {m 1} & L _ {m 2} & \dots & L _ {m n} \end{array} \right] \tag {10-7}
$$

对局中人 v 来讲, 对 L 中的每一列取其中的最小值 $\min_{i}L_{ij}(j=1,2,\cdots,n)$ (最坏情况), 再从这些列的最小值中取最大值, 得 $\max_{j}\min_{i}L_{ij}$ (最坏情况下的最好的结果)。对局中人 u 来讲, 则对 L 中的每一行取其中的最大值 $\max_{j}L_{ij}(i=1,2,\cdots,m)$ , 再从这些行的最大值中取最小值, 得 $\min_{i}\max_{j}L_{ij}$ 。如果

$$\max _ {j} \min _ {i} L _ {i j} = \min _ {i} \max _ {j} L _ {i j} = V \tag {10-8}$$

$V$ 是对策值, 则称存在极小极大解, 对应的第 $i^{*}$ 行, 第 $j^{*}$ 列的对策 $(u_{i^{*}}, v_{j^{*}})$ 或简写为 $(i^{*}, j^{*})$ 称为对策的最优解 (或称最优纯策略)。注意, 对策的解不一定唯一, 即可能存在多于一个的 $i^{*}$ 或 $j^{*}$ 使式(10-8)成立。下面给出式(10-8)成立的条件。

引理 1 对任一对策(不一定最优)都有

$$\max _ {j} \min _ {i} L _ {i j} \leqslant \min _ {i} \max _ {j} L _ {i j} \tag {10-9}$$

上式可以表述为:最小中的最大值不大于最大中的最小值。

证明 由极值的定义,都有

$$\min _ {i} L _ {i j} \leqslant L _ {i j}L _ {i j} \leqslant \max _ {j} L _ {i j}$$

从而有

$$\min _ {i} L _ {i j} \leqslant L _ {i j} \leqslant \max _ {i} L _ {i j} \tag {10-10}$$

由于式(10-10)左端已与 $i$ 无关，故有

$$\min _ {i} \left(\min _ {i} L _ {i j}\right) = \min _ {i} L _ {i j} \leqslant \min _ {i} \max _ {j} L _ {i j}$$

又由于上式的右端与任何 $i,j$ 都无关，故有

$$\max _ {j} \min _ {i} L _ {i j} \leqslant \max _ {j} (\min _ {i} \max _ {j} L _ {i j}) = \min _ {i} \max _ {j} L _ {i j}$$

引理1得证。

定理 1 零和矩阵对策有极小极大解的充要条件是: 存在一个最优

对策解 $(i^{*},j^{*})$ 使

$$L _ {i \cdot j} \leqslant L _ {i \cdot j ^ {*}} \leqslant L _ {i j ^ {*}} \tag {10-11}$$

对一切 $i=1,2,\cdots,m; j=1,2,\cdots,n$ 都成立。

证明 先证充分性。因为对一切 $i, j$ 均有

$$L _ {i * j} \leqslant L _ {i * j *} \leqslant L _ {i j}.$$

故有

$$\min _ {i} L _ {i j ^ {*}} \geqslant L _ {i * j ^ {*}} \geqslant \max _ {j} L _ {i * j} \tag {10-12}$$

而由式(10-12)左边,可得

$$\max _ {j} \min _ {i} L _ {i j} \geqslant \min _ {i} L _ {i j}. \tag {10-13}$$

上式右端 $L_{ij}$ . 表示 $\pmb{v}$ 方先开局已选了 $j^{*}$ 策略, 使 $\pmb{L}$ 尽可能大 (可能不是保守的), $\pmb{u}$ 方再选择策略使 $L_{ij}$ . 尽可能小。

由式 $(10-12)$ 右边,可得

$$\max _ {j} L _ {i \cdot j} \geqslant \min _ {i} \max _ {j} L _ {i j} \tag {10-14}$$

从而可得

$$\max _ {j} \min _ {i} L _ {i j} \geqslant L _ {i \cdot j ^ {*}} \geqslant \min _ {i} \max _ {j} L _ {i j} \tag {10-15}$$

再结合引理1,可得

$$\max _ {j} \min _ {i} L _ {i j} = \min _ {i} \max _ {j} L _ {i j} = L _ {i * j *} \tag {10-16}$$

这就证明了,满足条件式(10-11)后,即可得到矩阵对策的最优解。

再来证明必要性。既然假设存在最优对策解，则 $\max_{j} L_{ij}$ 可找到在 $i = i^{*}$ 时达到最小，而 $\min_{i} L_{ij}$ 在 $j = j^{*}$ 时达到最大，即
