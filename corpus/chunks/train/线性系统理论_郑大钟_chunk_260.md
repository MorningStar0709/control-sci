# 6.11 既约性

列既约和行既约 一个 $p \times p$ 的非奇异多项式矩阵 $M(s)$ 称为是列既约的, 如果

$$\deg \det M (s) = \sum_ {i = 1} ^ {p} \delta_ {c i} M (s) \tag {6.78}$$

而称 $M(s)$ 是行既约的，如果

$$\deg \det M (s) = \sum_ {i = 1} ^ {p} \delta_ {r i} M (s) \tag {6.79}$$

例 给定非奇异多项式矩阵 $M(s)$ 如下:

$$
M (s) = \left[ \begin{array}{c c} 3 s ^ {2} + 2 s & 2 s + 4 \\ s ^ {2} + s - 3 & 7 s \end{array} \right]
$$

容易定出：deg det $M(s)=3$

$$k _ {c 1} = 2, k _ {c 2} = 1, \Sigma k _ {c i} = 3k _ {r 1} = 2, k _ {r 2} = 2, \Sigma k _ {r i} = 4$$

因此，根据上述定义可知，此多项式矩阵 $M(s)$ 是列既约的，但不是行既约的。

既约性判据 下面，我们来给出判别方多项式矩阵为列既约和行既约的一些准则。

判据1 给定 $p$ 维方多项式矩阵 $M(s)$ ，令 $M_{he}$ 和 $M_{hr}$ 分别为其列次和行次系数矩阵， $k_{ei}$ 和 $k_{ri}$ 为其列次数和行次数。则

(1) $M(s)$ 为列既约, 当且仅当 $M_{he}$ 为非奇异。  
(2) $M(s)$ 为行既约,当且仅当 $M_{hr}$ 为非奇异。

证 根据 $M(s)$ 的列次表示式, 有

$$\det M (s) = \left(\det M _ {h e}\right) s ^ {\Sigma k _ {c l}} + \text {低次项} \tag {6.80}$$

表明，当且仅当 $\operatorname{det} M_{ke} \neq 0$ 即 $M_{ke}$ 为非奇异时，成立 $\deg \operatorname{det} M(s) = \Sigma k_{el}$ ，也即 $M(s)$ 为列既约。由此结论1得证。按类同方式，也可证明结论(2)成立。于是证明完成。

例 给定非奇异多项式矩阵 $M(s)$ 如下:

$$
M (s) = \left[ \begin{array}{c c} 3 s ^ {2} + 2 s & 2 s + 4 \\ s ^ {2} + s - 3 & 7 s \end{array} \right]
$$

容易定出

$$
M _ {b c} = \left[ \begin{array}{l l} 3 & 2 \\ 1 & 7 \end{array} \right], M _ {b r} = \left[ \begin{array}{l l} 3 & 0 \\ 1 & 0 \end{array} \right]
$$

于是，由 $M_{ke}$ 为非奇异和 $M_{kr}$ 为奇异，就可确定 $M(s)$ 是列既约的，但它不是行既约的。

判据2 给定 $p$ 维非奇异多项式矩阵 $M(s)$ ，令 $k_{si}$ 和 $k_{rj}$ 分别为其第 $i$ 列和第 $j$ 行的次数，则有如下结论：

(1) $M(s)$ 为列既约，当且仅当对所有非零的 $p \times 1$ 的多项式向量 $\pmb{p}(s)$ ，使得如下的列多项式向量

$$\boldsymbol {q} (s) = M (s) \boldsymbol {p} (s) \tag {6.81}$$

满足关系式

$$\deg q (s) = \max _ {i: p _ {i} (s) \geqslant 0} [ \deg p _ {i} (s) + k _ {s i} ] \tag {6.82}$$

其中 $p_{i}(s)$ 是 $p(s)$ 的第 i 个元。

(2) $M(s)$ 为行既约, 当且仅当对所有非零的 $1 \times p$ 的多项式向量 $\pmb{f}(s)$ , 使得如下的行多项式向量

$$\boldsymbol {h} (s) = \boldsymbol {f} (s) M (s) \tag {6.83}$$

满足关系式

$$\deg h (s) = \max _ {j: f _ {i} (s) \geqslant 0} [ \deg f _ {i} (s) + k _ {i j} ] \tag {6.84}$$

其中 $f_{i}(s)$ 是 $\pmb{f}(s)$ 的第 $j$ 个元。

证 考虑到结论(4)和(2)是对偶的,所以下面只限于证明结论(1)。为此,先引人如下表示式:

$$
d = \max _ {i: p _ {i} (s) \geqslant 0} [ \deg p _ {i} (s) + k _ {s i} ] \tag {6.85}q (s) = q _ {d} s ^ {d} + \dots + q _ {1} s + q _ {0} \tag {6.86}M (s) = M _ {k e} H _ {e} (s) + M _ {l e} (s) \tag {6.87}p _ {i} (s) = \alpha_ {i} s ^ {d - k _ {c l}} + \text {低次项} \tag {6.88}
\alpha = \left[ \begin{array}{c} \alpha_ {1} \\ \vdots \\ \alpha_ {p} \end{array} \right], \alpha_ {1}, \dots , \alpha_ {p} \text {不全为零} \tag {6.89}
$$

于是，利用上述关系式，就可由(6.81)导出

$$q _ {d} = M _ {\lambda c} \alpha \tag {6.90}$$
