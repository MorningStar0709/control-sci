$$
A _ {0} = \underbrace {\left[ \begin{array}{c c c c c c c c c} * & 1 & & & * & & & \\ \vdots & 0 & & 1 & \vdots & 0 & & \\ * & & & 0 & * & & & \\ \hline * & & & & & \ddots & & \\ \vdots & 0 & & & & & & \\ * & & & & & \ddots & & \\ \hline \vdots & & & & & & & \\ \vdots & & & & & & & \\ l _ {1} & & & & \underbrace {\left[ \begin{array}{c c c c c} * & 1 & & \\ \vdots & 0 & & 1 \\ * & & & 0 \end{array} \right]} _ {l _ {p}} \end{array} \right] \Bigg \} l _ {1}} _ {l _ {p}}, B _ {0} = \underbrace {\left[ \begin{array}{c c c c c} 0 & & & \\ \vdots & & \\ 0 & & \\ 1 & & \\ - 1 & \ddots & \\ 0 & & \\ 0 & 1 \end{array} \right] \Bigg \} l _ {p}} _ {l _ {p}}

C _ {o} = \underbrace {\left[ \begin{array}{c c} * & \\ \vdots & \mathbf {0} \\ * & \end{array} \right|} _ {l _ {1}} \dots \underbrace {\left| \begin{array}{c c} * & \\ \vdots & \mathbf {0} \\ * & \end{array} \right|} _ {l _ {p}} \Bigg \} p \tag {9.172}
$$

③ 在 $(A_{o}, C_{o})$ 中， $A_{o}$ 中的第 i 个 \* 列等同于 $-D_{lr}D_{hr}^{-1}$ 的第 i 列， $C_{o}$ 中的第 i 个 \* 列等同于 $D_{hr}^{-1}$ 的第 i 列， $i=1,2,\cdots,p_{o}$

④ 若令 $B_{o} = [\bar{b}_{1}, \bar{b}_{2}, \cdots, \bar{b}_{p}]$ ，则有

$$[ \bar {b} _ {1} A _ {o} \bar {b} _ {1} \dots A _ {o} ^ {l _ {1} - 1} \bar {b} _ {1} | \dots | \bar {b} _ {p} \dots A _ {0} \bar {b} _ {p}, \dots A _ {o} ^ {l _ {p} - 1} \bar {b} _ {p} ] = \tilde {I} _ {\bullet}. \tag {9.173}$$

其中 $\tilde{I}_{\bullet}$ 为变形单位阵，即

$$
\widetilde {I} _ {s} = \left[ \begin{array}{c c} \underbrace {\left[ \begin{array}{c c c c c c c c c} & & & 1 \\ & & & & & & & & \\ 1 & & & & & & & & \\ \hline & & & & \ddots & & & & \\ & & & & & & & & \\ \hline l _ {1} & & & & & & & & \\ \end{array} \right]} _ {l _ {1}} & \underbrace {\left[ \begin{array}{c c c c c c c c c} & & & & & & \\ & & & & & & \\ \hline & & & & 1 & & \\ 1 & & & & l _ {p} \end{array} \right]} _ {l _ {p}} \end{array} \right] \Bigg \} l _ {1}, \sum_ {i = 1} ^ {p} l _ {i} = n \tag {9.174}
$$

且进而有 $\tilde{I}_{\bullet}^{-1} = \tilde{I}_{\bullet}$ 。

下面, 就可进而来导出能控性形实现 $(A_{co}, B_{co}, C_{co})$ 的有关结果, 并将此表为如下的一个结论。

结论 $q \times p$ 的严格真右 MFD $N(s) D^{-1}(s)$ ( $D(s)$ 为行既约) 的能控性形实现 $(A_{co}, B_{co}, C_{co})$ 可按下述关系式来确定：

$$A _ {c o} = \tilde {I} _ {n} A _ {o} \tilde {I} _ {n}, B _ {c o} = \tilde {I} _ {n} B _ {o}, C _ {c o} = [ N (s) C _ {o} \tilde {I} _ {n} ] _ {s \rightarrow A _ {c o}} \tag {9.175}$$

并且,进一步可知:

① $A_{co}$ 和 $B_{co}$ 具有如下的形式:
