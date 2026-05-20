为非奇异的必要条件是 $\{A, C\}$ 为能观测和 $\{F, G\}$ 为能控。对于单输出 $(q = 1)$ 的情形，这个条件也是充分条件。

证 显然，此时全维观测器方法 II 的结论 2 证明中导出的式 (5.321) 仍然成立。差别仅在于，此处 $F$ 为 $(n - q) \times (n - q)$ 阵，相应地 $U_{F}$ 为 $(n - q) \times nq$ 阵。于是，由此就有：

$$
\begin{array}{l} P = \left[ \begin{array}{c} C \\ T \end{array} \right] = \left[ \begin{array}{c} C \\ - [ \alpha (F) ] ^ {- 1} U _ {F} \Lambda_ {a} V _ {A} \end{array} \right] \\ = \left[ \begin{array}{c c} I & 0 \\ 0 & - [ \alpha (F) ] ^ {- 1} \end{array} \right] \left[ \begin{array}{l} C \\ U _ {F} \Lambda_ {e} V _ {A} \end{array} \right] \tag {5.344} \\ \end{array}
$$

由上式可看出，若 $\{F, G\}$ 不完全能控即 $\operatorname{rank} U_P < (n - q)$ ，则导致 $\operatorname{rank} T < (n - q)$ 和 $P$ 为奇异；若 $\{A, C\}$ 为不完全能观测即 $\operatorname{rank} V_A < n$ ，则必存在一个 $n \times 1$ 非零向量 $v$ 使 $V_A v = 0$ ，这意味着必有 $C v = 0$ ，从而表明 $P v = 0$ 和 $P$ 为奇异。由此可知， $P$ 为非奇异的必要条件是 $\{A, C\}$ 能观测和 $\{F, G\}$ 能控。

现转而考虑单输出 $(q = 1)$ 的情况。定义

$$
\Lambda_ {1} V _ {A} \boldsymbol {v} \triangleq \beta = \left[ \begin{array}{l} \beta_ {1} \\ \beta_ {2} \\ \vdots \\ \beta_ {n} \end{array} \right] = \left[ \begin{array}{c c c c} \alpha_ {1} & \alpha_ {2} \dots \alpha_ {n - 1} & 1 \\ \alpha_ {2} & \alpha_ {3} \dots & 1 & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 1 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] \boldsymbol {v} = \left[ \begin{array}{l} * \\ * \\ \vdots \\ C \boldsymbol {v} \end{array} \right]
$$

其中，“\*”表示可能的非零元。由上式可以看出，如果 $Cv = 0$ ，则有 $\beta_{n} = 0$ 。再考虑

$$
\left[ \begin{array}{c} C \\ U _ {F} \Lambda_ {1} V _ {A} \end{array} \right] v = 0 \tag {5.345}
$$

那么，由此并考虑到 $\beta_{n} = 0$ ，又可导出：

$$0 = U _ {F} \Lambda_ {1} V _ {A} v = \sum_ {i = 1} ^ {n} \beta_ {i} F ^ {i - 1} G = \sum_ {i = 1} ^ {n - 1} \beta_ {i} F ^ {i - 1} G \tag {5.346}$$

但已知 $\{F, G\}$ 能控，故由此和 (5.346) 意味着进而有 $\beta_{i}=0, i=1,2,\cdots,n-1$ 。从而，当 $\{F, G\}$ 能控即 rank $U_{F}=n-1$ 时，式 (5.345) 意味着 $\beta=0$ 。进一步，由于 $\Lambda_{1}$ 为非奇异和 $\beta=\Lambda_{1}V_{A}v$ ，所以又可知 $\beta=0$ 意味着 $V_{A}v=0$ 。但知 $\{A, C\}$ 为能观测即 rank $V_{A}=n$ ，故 $V_{A}v=0$ 又意味着 v=0。这样，就证明了，当 $\{A, C\}$ 能观测和 $\{F, G\}$ 能控时，由 (5.345) 可知矩阵

$$
\left[ \begin{array}{c} C \\ U _ {F} \Lambda_ {1} V _ {A} \end{array} \right]
$$

为非奇异，而据此和(3.544)又可知 $P$ 为非奇异。表明，对于 $q = 1$ 情形，结论中指出的条件也为充分条件。至此，证明完成。

在上述讨论的基础上,下面来给出设计降维状态观测器(5.338)的算法。

算法

第1步：选取一个 $(n - q) \times (n - q)$ 实常阵 $F$ ，使 $F$ 的全部特征值均具有负实

部，且 F 和 A 没有公共的特征值。

第2步：选取一个 $(n - q) \times q$ 实常阵 $G$ ，使得 $\{F, G\}$ 为能控，即
