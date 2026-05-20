\Psi_ {L} (s) = \left[ \begin{array}{c c c c} s ^ {l _ {1} - 1} \dots s & 1 & & \\ \hdashline & & \ddots & \\ & & & \vdots \\ & & & s ^ {l _ {q} - 1} \dots s & 1 \end{array} \right];
$$

$D_{h}$ 为 $D_{L}(s)$ 的行次系数阵，且 $\operatorname{det} D_{h}, \neq 0$ ;

$D_{l}$ 为 $D_{L}(s)$ 的低次系数阵；

$N_{lr}$ 为 $N_{L}(s)$ 的系数阵。

结论1 $D_{L}^{-1}(s)N_{L}(s)$ 的核实现 $(A_{o}^{o}, B_{o}^{o}, C_{o}^{o})$ 的各个系数矩阵具有如下形式：

$$
A _ {o} ^ {o} = \left[ \begin{array}{c c c c c c c c} 0 & 1 & & & & & \\ & \ddots & \ddots & \ddots & 1 & & \\ & & & & 0 & & \\ \hline & & & \ddots & & & \\ & & & & 0 & 1 & \\ & & & & & \ddots & 1 \\ & & & & & & 0 \\ \hline & l _ {1} & & & l _ {q} \end{array} \right] \left\{ \begin{array}{l} l _ {1} \\ B _ {o} ^ {o} = I _ {n}, C _ {o} ^ {o} = \left[ \begin{array}{c c c c c c c c} 1 & 0 & \dots & 0 \\ \hline & & & & \ddots & & \\ & l _ {1} & & 1 & 0 & \dots & 0 \\ \hline l _ {q} \end{array} \right] \end{array} \right. \tag {9.155}
$$

结论 2 $q \times p$ 的严格真 $D_{L}^{-1}(s)N_{L}(s)$ 的观测器形实现 $(A_{o}, B_{o}, C_{o})$ 的各系数矩阵可按下述关系式来确定：

$$A _ {o} = A _ {o} ^ {o} - D _ {l r} D _ {h r} ^ {- 1} C _ {o} ^ {o}, B _ {o} = N _ {l r}, C _ {o} = D _ {h r} ^ {- 1} C _ {o} ^ {o} \tag {9.156}$$

其中核实现 $(A_{o}^{o}, B_{o}^{o}, C_{o}^{o})$ 如(9.155)所示。

推论1 $D_{L}^{-1}(s)N_{L}(s)$ 的观测器形实现 $(A_{o}, B_{o}, C_{o})$ 的各系数矩阵具有如下的形式：

$$
A _ {o} = \left[ \begin{array}{c c c c c c c c c} * & 1 & & & * & & & & \\ \vdots & 0 & \ddots & 1 & \vdots & 0 & \dots & & \\ * & & & 0 & * & & & & \\ \hline * & & & & & & & & \\ \vdots & 0 & & & \ddots & & & & \\ * & & & & & \ddots & & \\ \hline \vdots & & & & & & & \\ \vdots & & & & & \vdots & 1 & \\ \vdots & & & & & 0 & 1 \\ \vdots & & & & * & & 0 \\ \hline l _ {1} \end{array} \right] \left\{ \begin{array}{l} l _ {1} \\ C _ {o} = \underbrace {\left[ \begin{array}{c c c c} * & 1 & & * \\ \vdots & 0 & \cdots & 0 \\ \vdots & 0 & 1 \\ * \end{array} \right]} _ {l _ {1}} \underbrace {\left[ \begin{array}{c c c c} * & 1 \\ \vdots & 0 \\ * \end{array} \right]} _ {l _ {q}} \end{array} \right\} q
B _ {o} = N _ {l r} \text {无特别的形式} \tag {9.157}
$$

其中，用“\*”表示的元为可能的非零元。

推论2 在观测器形实现中， $A_{o}$ 中的第 $i$ 个 $*$ 列等同于 $-D_{lr}D_{hr}^{-1}$ 的第 $i$ 列， $B_{o}$ 中的第 $i$ 个 $*$ 列则等同于 $D_{hr}^{-1}$ 的第 $i$ 列， $i = 1,2,\dots ,q_{o}$

此外,根据对偶关系,我们还可进一步导出观测器形实现 $(A_{o}, B_{o}, C_{o})$ 的如下性质。

性质1 对于一般的左 MFD $D_{L}^{-1}(s)N_{L}(s)$ ，其观测器形实现 $(A_{o}, B_{o}, C_{o})$ 中， $\{A_{o}, C_{o}\}$ 必是能观测的，但 $\{A_{o}, B_{o}\}$ 不能保证必是完全能控的。

性质2 左 MFD $D_{L}^{-1}(s)N_{L}(s)$ ( $D_{L}(s)$ 为行既约)和其观测器形实现 $(A_{o}, B_{o}, C_{o})$ 之间存在如下的关系式:
