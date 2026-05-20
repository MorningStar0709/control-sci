现先来证明必要性：已知 $M(s)$ 为列既约，故知 $M_{k}$ 为非奇异，从而由(6.90)即知，对所有非零 $\pmb{p}(s)$ 即所有 $\pmb{\alpha} \neq \mathbf{0}$ 一定有 $\pmb{q}_d \neq \mathbf{0}$ ，表明式(6.82)成立。必要性得证。再来证明充分性：已知式(6.82)成立，所以对所有非零 $\pmb{p}(s)$ 即所有 $\pmb{\alpha} \neq \mathbf{0}$ 成立 $\pmb{q}_d \neq \mathbf{0}$ ，由此从(6.90)即知 $M_{k}$ 为非奇异，从而 $M(s)$ 为列既约。充分性得证。于是证明完成。

几点推论 下面,对非奇异多项式矩阵的既约性,作如下的几点推论。

（1）一般地说，一个非奇异多项式矩阵的列既约性和行既约性之间，没有必然的关系。

这个事实已由前面给出的一个例子为证。

（2）当非奇异多项式矩阵具有对角阵形式时，如果其为列既约，则必然也是行既约的。反之亦然。

(3) 一个非奇异多项式矩阵的埃尔米特形不一定既是列既约的,也是衍既约的。

(4) 列(行)既约矩阵的列(行)次数在单模变换下是不变的。即：设 $M(s)$ 和 $\overline{M}(s)$

均为列既约，且它们的列次数按非降顺序排列

$$k _ {c 1} \leqslant k _ {c 2} \leqslant \dots \leqslant k _ {c p}, \bar {k} _ {c 1} \leqslant \bar {k} _ {c 2} \leqslant \dots \leqslant \bar {k} _ {c p} \tag {6.91}$$

则当 $M(s) = \overline{M}(s)U(s), U(s)$ 为单模阵时，必成立

$$k _ {c i} = \bar {k} _ {c i}, i = 1, 2, \dots , p \tag {6.92}$$

证 采用反证法。反设存在某个位置指数 $l \leqslant p$ ，使有

$$
\left\{ \begin{array}{l} k _ {c i} = \bar {k} _ {c i}, i \leqslant l - 1 \\ k _ {c i} <   \bar {k} _ {c i}, i \geqslant l \end{array} \right. \tag {6.93}
$$

同时将 $M(s) = \overline{M} (s)U(s)$ 相应地表示为

$$
\begin{array}{l} [ m _ {1} (s), \dots , m _ {l} (s): m _ {l + 1} (s), \dots , m _ {p} (s) ] \\ = \left[ \bar {m} _ {1} (s), \dots , \bar {m} _ {l - 1} (s) \mid \bar {m} _ {l} (s), \dots , \bar {m} _ {p} (s) \right] \left[ \begin{array}{l l} U _ {1 1} (s) & U _ {1 2} (s) \\ U _ {2 1} (s) & U _ {2 2} (s) \end{array} \right] \tag {6.94} \\ \end{array}
$$

其中， $U_{11}(s)$ 、 $U_{12}(s)$ 、 $U_{21}(s)$ 和 $U_{22}(s)$ 分别为 $(l-1)\times l$ 、 $(l-1)\times(p-l)$ 、 $(p-l+1)\times l$ 和 $(p-l+1)\times(p-l)$ 的多项式矩阵。进而，由(6.94)又可导出

$$
\begin{array}{l} [ \boldsymbol {m} _ {1} (s), \dots ,: \boldsymbol {m} _ {l} (s) ] = [ \bar {\boldsymbol {m}} _ {1} (s), \dots , \bar {\boldsymbol {m}} _ {l - 1} (s) ] U _ {1 1} (s) \\ + \left[ \bar {m} _ {l} (s), \dots , \bar {m} _ {p} (s) \right] U _ {2 1} (s) \tag {6.95} \\ \end{array}
$$

而由(6.91)和反设(6.93)可知

$$k _ {c 1} \leqslant \dots \leqslant k _ {c l} < \bar {k} _ {c l} \leqslant \dots \leqslant \bar {k} _ {c p} \tag {6.96}$$

这表明，仅当 $U_{21}(s) \equiv 0$ 时，(6.95)和(6.96)才能同时成立。由此，进一步有

$$
\begin{array}{l} \max (\operatorname{rank} U (s)) = \max (\operatorname{rank} U _ {1 1} (s)) + \max (\operatorname{rank} U _ {2 2} (s)) \\ = (l - 1) + (p - l) = p - 1 \tag {6.97} \\ \end{array}
$$

表明 $U(s)$ 不是单模阵，这是和已知条件相矛盾的。所以反设不成立，因而(6.92)成立。于是证明完成。
