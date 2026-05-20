其中 $\pmb {A} = \left[ \begin{array}{cc}0 & 1\\ -2 & -3 \end{array} \right],\quad \pmb {b} = \left[ \begin{array}{c}0\\ 1 \end{array} \right],\quad c = [2\quad 0]$

显然，系统可控可观测。n=2,q=1，输出反馈向量 h 为 $2 \times 1$ 向量。全维状态观测器系统矩阵为

$$
\mathbf {A} - \mathbf {h c} = \left[ \begin{array}{l l} 0 & 1 \\ - 2 & - 3 \end{array} \right] - \left[ \begin{array}{l} h _ {0} \\ h _ {1} \end{array} \right] [ 2 \quad 0 ] = \left[ \begin{array}{l l} - 2 h _ {0} & 1 \\ - 2 - 2 h _ {1} & - 3 \end{array} \right]
$$

观测器特征方程为

$$\mid \lambda I - (A - h c) \mid = \lambda^ {2} + (2 h _ {0} + 3) \lambda + (6 h _ {0} + 2 h _ {1} + 2) = 0$$

期望特征方程为

$$(\lambda + 1 0) ^ {2} = \lambda^ {2} + 2 0 \lambda + 1 0 0 = 0$$

令两特征方程同次项系数相等,可得

$$2 h _ {0} + 3 = 2 0, \quad 6 h _ {0} + 2 h _ {1} + 2 = 1 0 0$$

因而有

$$h _ {0} = 8. 5, \quad h _ {1} = 2 3. 5$$

$h_{0}, h_{1}$ 分别为由 $(\hat{y}-y)$ 引至 $\dot{x}_{1}, \dot{x}_{2}$ 的反馈系数。被控对象及全维状态观测器的状态变量图如图 9-27 所示。

![](image/a66d1903f172bc31b6d7b6cae79cba96c78e0ed3df2bfcfefb1b33536d8ca4d2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["+"]
    B --> C["1/s"]
    C --> D["+"]
    D --> E["1/s"]
    E --> F["+"]
    F --> G["2"]
    G --> H["y"]
    H --> I["23.5"]
    I --> J["8.5"]
    J --> K["+"]
    K --> L["1/s"]
    L --> M["+"]
    M --> N["1/s"]
    N --> O["+"]
    O --> P["2"]
    P --> Q["+"]
    Q --> R["23.5"]
    R --> S["8.5"]
    S --> T["+"]
    T --> U["1/s"]
    U --> V["+"]
    V --> W["1/s"]
    W --> X["+"]
    X --> Y["2"]
    Y --> Z["+"]
    Z --> AA["23.5"]
    AA --> AB["8.5"]
    AB --> AC["+"]
    AC --> AD["1/s"]
    AD --> AE["+"]
    AE --> AF["1/s"]
    AF --> AG["+"]
    AG --> AH["2"]
    AH --> AI["+"]
    AI --> AJ["23.5"]
    AJ --> AK["8.5"]
    AK --> AL["+"]
    AL --> AM["1/s"]
    AM --> AN["+"]
    AN --> AO["1/s"]
    AO --> AP["+"]
    AP --> AQ["2"]
    AQ --> AR["+"]
    AR --> AS["23.5"]
    AS --> AT["8.5"]
    AT --> AU["+"]
    AU --> AV["1/s"]
    AV --> AW["+"]
    AW --> AX["1/s"]
    AX --> AY["+"]
    AY --> AZ["2"]
    AZ --> BA["+"]
    BA --> BB["23.5"]
    BB --> BC["8.5"]
    BC --> BD["+"]
    BD --> BE["1/s"]
    BE --> BF["+"]
    BF --> BG["1/s"]
    BG --> BH["+"]
    BH --> BI["2"]
    BI --> BJ["+"]
    BJ --> BK["23.5"]
    BK --> BL["8.5"]
    BL --> BM["+"]
    BM --> BN["1/s"]
    BN --> BO["+"]
    BO --> BP["1/s"]
    BP --> BQ["+"]
    BQ --> BR["2"]
    BR --> BS["+"]
    BS --> BT["23.5"]
    BT --> BU["8.5"]
    BU --> BV["+"]
    BV --> BW["1/s"]
    BW --> BX["+"]
    BX --> BY["1/s"]
    BY --> BZ["+"]
    BZ --> CA["2"]
    CA --> CB["+"]
    CB --> CC["23.5"]
```
</details>

图 9-27 全维状态观测器及被控对象的状态变量图
