# 6.10 列次数和行次数

几个定义 一个多项式向量的次数, 被规定为这个向量的所有多项式元中, s 的最高幂次。如果用 $\beta(s)$ 来表示一个多项式向量, $\beta_{i}(s)$ 表示它的多项式元, 则 $\beta(s)$ 的次数可表为

$$\delta \beta (s) = \max _ {i} \left\{\deg \beta_ {i} (s), i = 1, 2, \dots , p \right\} \tag {6.73}$$

对于 $q \times p$ 的多项式矩阵 $M(s)$ ，则其列次数和行次数分别规定为：

第 i 个列次数 $\delta_{ci}M(s)=k_{ci}\triangleq M(s)$ 的第 i 个列向量的次数， $i=1,2,\cdots,p$

第 $i$ 个行次数 $\delta_{r,i}M(s) = k_{r,i}\triangleq M(s)$ 的第 $i$ 个行向量的次数， $j = 1,2,\dots,q$

例 给定多项式矩阵 $M(s)$ 为

$$
M (s) = \left[ \begin{array}{c c c} s ^ {2} + 4 s + 1 & 2 s ^ {2} + s + 1 & s + 4 \\ s + 3 & s ^ {3} - 2 s & 3 \end{array} \right],
$$

那么，根据定义，即可定出：

$$k _ {s 1} = 2, k _ {s 2} = 3, k _ {s 3} = 1k _ {r 1} = 2, k _ {r 2} = 3$$

多项式矩阵的列次表示式 给定 $q \times p$ 的多项式矩阵 $M(s)$ ，令 $\delta_{ei} M(s) = k_{si} (i = 1, 2, \cdots, p)$ ，则可把 $M(s)$ 表述为如下的列次表示式：

$$M (s) = M _ {h e} H _ {e} (s) + M _ {l e} (s) \tag {6.74}$$

其中： $H_{c}(s)=\mathrm{diag}\{s^{k_{c_{1}}},s^{k_{c_{2}}},\cdots,s^{k_{c_{p}}}\}$ ;

$M_{bc}$ 为 $q \times p$ 常阵，称为列次系数矩阵，它的第 i 列即为 $M(s)$ 的第 i 列中相应于 $s^{k_{ci}}$ 的系数组成的列；

$M_{lc}(s)$ 为低次剩余多项式矩阵，且必有 $\delta_{ci}M_{lc}(s) < k_{si}, i = 1,2,\dots ,p_{\bullet}$

例 给定多项式矩阵 $M(s)$ 为

$$
M (s) = \left[ \begin{array}{c c c} s ^ {2} + 4 s + 1 & 2 s ^ {2} & s + 4 \\ s + 3 & 4 s ^ {3} - 2 s & 3 s + 1 \end{array} \right]
$$

则其列次表示式即为

$$
M (s) = \left[ \begin{array}{l l l} 1 & 0 & 1 \\ 0 & 4 & 3 \end{array} \right] \left[ \begin{array}{c c c} s ^ {2} & & \\ & s ^ {3} & \\ & & s \end{array} \right] + \left[ \begin{array}{c c c} 4 s + 1 & 2 s ^ {2} & 4 \\ s + 3 & - 2 s & 1 \end{array} \right]
$$

现在，如果限于考虑 $M(s)$ 为方多项式矩阵也即 $q = p$ 的情况，则由(6.74)还可导出如下的一个有用的关系式：

$$\det M (s) = \left(\det M _ {h c}\right) s ^ {\Sigma k _ {c i}} + \text {次数低于} \Sigma k _ {c i} \text {的各项} \tag {6.75}$$

多项式矩阵的行次表示式 类似地，也可将一个多项式矩阵表示成行次表示式。对于 $q \times p$ 的多项式矩阵 $M(s)$ ，令 $\delta_{ri}M(s) = k_{ri}(i = 1,2,\dots ,q)$ ，则其行次表示式具有如下的形式：

$$M (s) = H _ {r} (s) M _ {h r} + M _ {l r} (s) \tag {6.76}$$

其中： $H_{r}(s)=\mathrm{diag}\{s^{k_{r1}},s^{k_{r2}},\cdots,s^{k_{rq}}\}$ ;

$M_{h}$ ，为 $q \times p$ 常阵，称为行次系数矩阵，它的第 i 行即为 $M(s)$ 的第 i 行中相应于 $s^{k_{r1}}$ 的系数组成的行；

$M_{lr}(s)$ 为低次剩余多项式矩阵，且必有 $\delta_{ri}M_{lr}(s)<k_{ri}, i=1,2,\cdots,q.$

并且，当 $q = p$ 即 $M(s)$ 为方阵时，也可导出和(6.75)相类同的一个关系式：

$$\det M (s) = (\det M _ {k r}) s ^ {\Sigma k _ {r i}} + \text { 次数低于 } \Sigma k _ {r i} \text { 的各项 } \tag {6.77}$$
