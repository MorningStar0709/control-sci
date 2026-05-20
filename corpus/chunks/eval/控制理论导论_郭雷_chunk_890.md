```mermaid
graph TD
    A["3"] --> B["4"]
    B --> C["5"]
    C --> D["6"]
    D --> E["7"]
    E --> F["8"]
    F --> G["9"]
    G --> H["10"]
    H --> I["11"]
    I --> J["12"]
    J --> K["13"]
    K --> L["14"]
    L --> M["15"]
    M --> N["16"]
    N --> O["17"]
    O --> P["18"]
    P --> Q["19"]
    Q --> R["20"]
    R --> S["21"]
    S --> T["22"]
    T --> U["23"]
    U --> V["24"]
    V --> W["25"]
    W --> X["26"]
    X --> Y["27"]
    Y --> Z["28"]
    Z --> AA["29"]
    AA --> AB["30"]
    AB --> AC["31"]
    AC --> AD["32"]
    AD --> AE["33"]
    AE --> AF["34"]
    AF --> AG["35"]
    AG --> AH["36"]
    AH --> AI["37"]
    AI --> AJ["38"]
    AJ --> AK["39"]
    AK --> AL["40"]
```
</details>

图11.9.2 热轧生产线的双子模型的 $G(A)$

上图中 $G(A)$ 与 A 的关系如下： $G(A)$ 中有 $n+m+6$ 个点，用数字 $1,2,\cdots,n+m+6$ 表示 $G(A)$ 中的点。 $(A)_{ij} \neq [\varepsilon]$ 时，点 j 到点 i 存在一条弧，其权为 $(A)_{ij}$ ，这里用算子表示弧的权；当 $(A)_{ij} = [\varepsilon]$ 时，点 j 到点 i 不存在弧。令 $L_{1}$ 表示 $1 \rightarrow 2 \rightarrow 3 \rightarrow n+m+6 \rightarrow 1$ 所对应的回路， $L_{2}$ 表示 $3 \rightarrow 4 \rightarrow \cdots \rightarrow n+m+4 \rightarrow n+m+5 \rightarrow 3$ 所对应的回路。

现在来分析系统 (11.9.2). 由双子代数理论, 易得系统 (11.9.2) 的解为

$$\boldsymbol {x} = \boldsymbol {A} ^ {*} \boldsymbol {v},$$

这里 $A^{*}\stackrel{\operatorname{def}}{=} \sum_{k=0}^{+\infty}A^{k}$ . 由于 $A^{*}$ 含无限多项，所以分析问题的关键是找出 $A^{k}, k \geqslant k_{0}$ 的规律. 回忆 11.4 节关于特征值与分块周期阵的理论，我们企图建立相应的理论，但目前主要困难在于 A 的元素为算子，不好定义重量，因而也就难以用临界回路的均重来描写特征值 $\lambda$ . 我们先设 n 维向量 v 的第 i 个分量均为非负常数时间序列 $\langle v\rangle_{i}\stackrel{\operatorname{def}}{=} \langle c_{i}, c_{i}, \cdots \rangle$ ，并研究 $G(A)$ 为一条回路时解 x 的规律，得到类似于特征值的参数. 下面作一简要介绍.

记 $G(A)$ 中长为 $L$ 的回路为 $C, C$ 上第 $i$ 条弧的权为算子 $[\Delta^{v_i}] \otimes [d_i] \otimes [z^{-m_i}] \otimes [\Delta^{u_i}], i = 1, 2, \cdots, L$ . 令第 $i$ 条弧的起点为 $i - 1$ , 终点为 $i$ (0 与 $L$ 视为同一点). 这里路的权为起点到终点各弧的权从右向左复合运算所得的算子.

下面定义一个关键参数

$$P \stackrel {\text { def }} {=} P (C) = \prod_ {r = 1} ^ {L} u _ {r} / v _ {r},$$

这里 $\Pi$ 为普通乘法运算.

定义 11.9.3 对于序列 $\langle t_{0}, t_{1}, \cdots, t_{j}, \cdots \rangle$ ，若存在 $k_{0} \geqslant 0$ ，使得所有 $j > k_{0}$ 都有 $t_{j+N} = t_{j} + T$ ，则称为准周期序列， $\lambda \stackrel{\operatorname{def}}{=} T/N$ 称为斜率或周期；当 T = 0, N = 1 时称为准常数序列。

定理11.9.3 若 $G(A)$ 仅是一条长为 $L$ 的回路 $C$ . 则

(1) $P = 1$ 时，回路 $C$ 上的点 $i$ 对应的 $x$ 的分量 $\langle t\rangle_{i}$ 均为准周期序列，周期为 $\lambda (i)$ ，其值经有限步计算可得；

(2) $P > 1, m_{\tau} \geqslant v_{\tau}, 1 \leqslant r \leqslant L$ 时， $\langle t \rangle_{i} \stackrel{\mathrm{def}}{=} \langle t_{0}, t_{1}, \dots, t_{q}, \dots \rangle$ 的元素 $t_{q}$ ，在 $q$ 充分大时，满足
