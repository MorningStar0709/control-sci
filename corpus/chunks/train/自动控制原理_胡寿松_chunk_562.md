# 4. 非线性系统稳定性分析的描述函数法

若非线性系统经过适当简化后,具有图 8-36 所示的典型结构形式,且非线性环节和线性部分满足描述函数法应用的条件,则非线性环节的描述函数可以等效为一个具有复变增益的比例环节。于是非线性系统经过谐波线性化处理后已变成一个等效的线性系统,可以应用线性系统理论中的频率域稳定判据分析非线性系统的稳定性。

![](image/22169e21a96c4d6acc6cca4a816bf790796acb7e6149aefdff2b6ed7896f2cf7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)=0"] --> B["+"]
    B --> C["G₁"]
    C --> D["+"]
    D --> E["G₂"]
    E --> F["c(t)"]
    F --> G["G₃"]
    G --> H["x(t)"]
    H --> I["N"]
    I --> J["y(t)"]
    J --> B
    D --> K["-"]
    K --> B
```
</details>

(a)

![](image/19d39bfc5a5bfe811b978594f45041c6110b55873e0fa6fc64f8ba6d84de0c87.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Input y(t)"] --> B["Summing Junction"]
    B --> C["G1"]
    C --> D["c(t)"]
    D --> E["G2"]
    E --> F["Summing Junction"]
    F --> G["N"]
    G --> H["x(t)"]
    H --> I["G3"]
    I --> J["Output"]
    J --> K["-"]
    K --> L["Summing Junction"]
    L --> M["+"]
    M --> N["Summing Junction"]
    N --> O["-"]
    O --> P["Summing Junction"]
```
</details>

(b)

![](image/eafdcebb536e6ef45d6ee4a47ef61a0db1cc8734dcbb1d9482a8713ace39ae27.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] -->|x(t)| B["N"]
    B -->|y(t)| C["\frac{G_2G_3}{1+G_1G_2}"]
    C --> D["c(t)"]
    D --> E["-"]
    E --> A
```
</details>

(c)   
图 8-42 非线性系统等效变换
