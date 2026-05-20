# (2) 由系统结构图绘制信号流图

在结构图中,由于传递的信号标记在信号线上,方框则是对变量进行变换或运算的算子。因此,从系统结构图绘制信号流图时,只需在结构图的信号线上用小圆圈标志出传递的信号,便得到节点;用标有传递函数的线段代替结构图中的方框,便得到支路,于是,结构图也就变换为相应的信号流图了。例如,由图2-23(h)的结构图绘制信号流图的过程示于图2-33(a)、(b)中。

![](image/9f5dc92f2f4672320ae67b2d671bb2533d9fb7a8a13f269a24afb25c6ff5a400.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E1 --> E
    E --> Ka
    Ka --> Ua
    Ua --> Cm
    Cm --> Ms
    Ms --> 1/(Ca*s)
    1/(Ca*s) --> θm
    θm --> r
    r --> L
    L --> K1
    K1 --> E2
    E2 -->|feedback| E
    E -->|-| A
    A --> Ma
    Ma --> Jm*s2
    Jm*s2 --> fms
    fms -->|feedback| Ma
```
</details>

(a)

![](image/bb751fe552e5e77ed8b75621d5cc3beee505511e1d2330d80b1969428a4e87f3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E1 -->|1| E
    E -->|K0| Uo
    Uo --> Cm
    Cm -->|1/(Cm)s| R
    R --> L
    L --> K1
    K1 --> E2
    E2 -->|-1| E
    E -->|Mx| Mm
    Mm -->|-1| E
    Mm -->|Jmr s^2| R
    R -->|θm| Mm
    Mm -->|fmr s| R
```
</details>

(b)   
图 2-33 由结构图绘制信号流图的过程

从系统结构图绘制信号流图时应尽量精简节点的数目。例如，支路增益为1的相邻两个节点，一般可以合并为一个节点，但对于源节点或阱节点却不能合并掉。例如，图2-33(b)中的节点 $M_{s}$ 和节点 $M_{m}$ 可以合并成一个节点，其变量是 $M_{s}-M_{m}$ ；但源节点 $E_{1}$ 和节点E却不允许合并。又例如，在结构图比较点之前没有引出点(但在比较点之后可以有引出点)时，只需在比较点后设置一个节点便可，如图2-34(a)所示；但若在比较点之前有引出点时，就需在引出点和比较点各设置一个节点，分别标志两个变量，它们之间的支路增益是1，如图2-34(b)所示。

![](image/02983e3fa260e819ae6e590f4137a9a81fd4ce1b4301281b2e2d902e00fef553.jpg)  
图 2-34 比较点与节点对应关系

例 2-13 试绘制图 2-35 所示系统结构图对应的信号流图。

![](image/f8b3ba88dbb60be9209953cec7ee66e259b984bf3ee925d726dfbe2102e75df3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] --> Sum1((+))
    Sum1 --> G2["G₂(s)"]
    G2 --> Sum2((+))
    Sum2 --> G3["G₃(s)"]
    G3 --> Sum3((+))
    Sum3 --> G4["G₄(s)"]
    G4 --> H["H(s)"]
    H --> Sum1
    G2 --> Sum2
    G3 --> Sum3
    Sum2 --> G4
    Sum3 --> G2
    Sum3 --> G3
```
</details>

图 2-35 例 2-13 系统的结构图

解 首先, 在系统结构图的信号线上, 用小圆圈标注各变量对应的节点, 如图 2-36(a) 所示。其次, 将各节点按原来顺序自左向右排列, 连接各节点的支路与结构图中的方框相对应, 即将结构图中的方框用具有相应增益的支路代替, 并连接有关的节点, 便得到系统的信号流图, 如图 2-36(b) 所示。

![](image/5346edb3a8a4d895500778cc191ccb19a4d613c22179dd277ab53cadf08df125.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["R(s)"] -->|e| G1["G₁(s)"]
    R -->|-| e1["e₁"]
    e1 --> G2["G₂(s)"]
    e1 --> e2["e₂"]
    e2 --> G3["G₃(s)"]
    e2 --> G4["G₄(s)"]
    G3 --> C["C(s)"]
    G4 --> H["H(s)"]
    H --> e1
    G2 --> e2
```
</details>

(a)

![](image/a64ad0490811289a56a51d0011b778f679b3b2c37c6ac9ae31e25d7ef82baaff.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] -->|1| e["e"]
    e --> G1["G₁(s)"]
    G1 --> e1["e₁"]
    e1 --> G2["G₂(s)"]
    G2 --> e2["e₂"]
    e2 --> G3["G₃(s)"]
    G3 --> C["C(s)"]
    e1 -->|−H(s)| e1
    e2 -->|G₄(s)| C
```
</details>

(b)   
图 2-36 例 2-13 系统的信号流图
