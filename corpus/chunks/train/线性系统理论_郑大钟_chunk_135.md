![](image/ab897692a498742e78646c57f4c1eeae553371f09bbe21ab5ea86e2e7a12e477.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> Bc["\(\bar{B}_c\)"]
    Bc --> add1["+"]
    add1 --> int["\(\int\)"]
    int --> \(\bar{x}_c\)
    \(\bar{x}_c\) --> Cc["\(\bar{C}_c\)"]
    Cc --> sum["\(y_1\)"]
    sum --> y["y"]
    y --> A12["\(\bar{A}_{12}\)"]
    A12 --> add2["+"]
    add2 --> int
    int --> \(\bar{x}_{\bar{c}}\)
    \(\bar{x}_{\bar{c}}\) --> Cc
    Cc --> sum
    sum --> y2["y"]
    y2 --> A12
    A12 --> add3["+"]
    add3 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
    y2 --> A12
    A12 --> add4["+"]
    add4 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
    y2 --> A12
    A12 --> add5["+"]
    add5 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
    y2 --> A12
    A12 --> add6["+"]
    add6 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
    y2 --> A12
    A12 --> add7["+"]
    add7 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
    y2 --> A12
    A12 --> add8["+"]
    add8 --> int
    int --> \(\bar{f}\)
    \(\bar{f}\) --> Cc
    Cc --> sum
    sum --> y2
```
</details>

图 3.6 系统按能控性分解后的方块图

（4）注意到（3.238）的变换阵 $P^{-1}$ 中，不管是从能控性判别阵 $Q_{e}$ 中选取的 $\{q_{1}, q_{2}, \cdots, q_{k}\}$ ，还是此外取定的 $\{q_{k+1}, \cdots, q_{n}\}$ ，都不是唯一的取法。因此，随着取法的不同，尽管（3.239）的规范表达式的形式不改变，但是各分块矩阵中的元的值则随之不同。从这个意义而言，对系统按能控性进行结构分解，可导出多个分解结果。

（5）规范表达式(3.239)同时也为能控性的判别提供了一个准则：线性定常系统是完全能控的，当且仅当它不能通过线性非奇异变换化为(3.239)的形式。考虑到这个变换过程可在计算机上采用行或列初等变换来完成，而且具有数值稳定性好的优点，因此这不失为判别维数较大的系统的能控性的一种较好方法。

线性定常系统按能观测性的结构分解 系统按能观测性的结构分解的所有结论和推论,都对偶于系统按能控性的结构分解的结果。给定不完全能观测的线性定常系统

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \tag {3.251}\mathbf {y} = C \mathbf {x}$$

其中，x 为 n 维状态向量， $\operatorname{rank} Q_{0} = m < n$ 。则通过在能观测性判别阵

$$
Q _ {o} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {s - 1} \end{array} \right] \tag {3.252}
$$

中任意地选取 m 个线性无关的行 $h_{1}, h_{2}, \cdots, h_{m}$ ，此外再任取 n - m 个与之线性无关的行向量 $h_{m+1}, \cdots, h_{n}$ ，就可构成变换阵

$$
F = \left[ \begin{array}{c} h _ {1} \\ \vdots \\ h _ {m} \\ \hdashline h _ {m + 1} \\ \vdots \\ h _ {n} \end{array} \right] \tag {3.253}
$$

从而，对应地有如下结论：

结论 对（3.251）的不完全能观测系统，引入线性非奇异变换 $\hat{x} = Fx$ ，即可导出系统结构按能观测性分解的规范表达式：
