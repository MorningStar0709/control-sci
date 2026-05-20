$$
\pmb {Q} ^ {- 1} = [ \begin{array}{c c c} {\overline {{{\pmb {C}}}} _ {1}} & {\vdots} & {\overline {{{\pmb {C}}}} _ {2}} \\ {r \text {列}} & {n - r \text {列}} \end{array} ] q \text {行} \tag {9-195}
$$

展开式(9-194)，有

$$\dot {\pmb {x}} _ {c} = \overline {{{{\pmb {A}}}}} _ {1 1} \pmb {x} _ {c} + \overline {{{{\pmb {A}}}}} _ {1 2} \pmb {x} _ {c} + \overline {{{{\pmb {B}}}}} _ {1} \pmb {u}\dot {\boldsymbol {x}} _ {\bar {c}} = \overline {{\boldsymbol {A}}} _ {2 2} \boldsymbol {x} _ {\bar {c}}\mathbf {y} = \overline {{C}} _ {1} \mathbf {x} _ {c} + \overline {{C}} _ {2} \mathbf {x} _ {c}$$

将输出向量进行分解，令 $y = y_{1} + y_{2}$ ，则可得子系统动态方程，其中可控子系统动态方程为

$$\dot {\boldsymbol {x}} _ {c} = \overline {{{\boldsymbol {A}}}} _ {1 1} \boldsymbol {x} _ {c} + \overline {{{\boldsymbol {A}}}} _ {1 2} \boldsymbol {x} _ {c} + \overline {{{\boldsymbol {B}}}} _ {1} \boldsymbol {u}, \quad \boldsymbol {y} _ {1} = \overline {{{\boldsymbol {C}}}} _ {1} \boldsymbol {x} _ {c} \tag {9-196}$$

不可控子系统动态方程为

$$\dot {\boldsymbol {x}} _ {c} = \overline {{\boldsymbol {A}}} _ {2 2} \boldsymbol {x} _ {c}, \quad \boldsymbol {y} _ {2} = \overline {{\boldsymbol {C}}} _ {2} \boldsymbol {x} _ {c} \tag {9-196}$$

上述系统结构分解方式称为可控性规范分解,系统方块图如图 9-21 所示。

![](image/52d99b032d6400e8f275bc920d770eeb143ed8a152e60f64c8b60ae00c4eb90b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> B1["\overline{B}_1"]
    B1 --> add1["+"]
    add1 --> x_c["\dot{x}_c"]
    x_c --> I_s["\frac{I}{s}"]
    I_s --> x_c
    x_c --> C1["\overline{C}_1"]
    C1 --> sum["+"]
    y1["y_1"] --> sum
    y2["y_2"] --> sum
    x_c --> A11["\overline{A}_{11}"]
    A11 --> add1
    x_c --> A12["\overline{A}_{12}"]
    A12 --> add1
    x_c --> I_s["\frac{I}{s}"]
    I_s --> x_c
    x_c --> C2["\overline{C}_2"]
    C2 --> sum
    x_c --> A22["\overline{A}_{22}"]
    A22 --> add1
    x_c --> x̂_c["\dot{x}_c"]
    x̂_c --> add1
```
</details>

图 9-21 可控性规范分解方块图

系统结构的可控性规范分解具有下列特点：

① 不可控系统与其可控子系统具有相同的传递函数矩阵。

由于
