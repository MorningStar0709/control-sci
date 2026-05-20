```mermaid
graph TD
    e --> |+| A["Sum"]
    A --> e1["e₁"]
    e1 --> |-| B["Sum"]
    B --> u_c["u_c"]
    u_c --> |+| C["Output u_max"]
    u_c --> |-| D["Feedback to sum"]
    D --> e2["Sum"]
    e2 --> |+| E["Sum"]
    E --> u["u"]
    u --> F["Feedback to sum"]
    F --> e3["Sum"]
    e3 --> |+| G["Sum"]
    G --> u_c
    u_c --> |+| H["Output u"]
    u_c --> |-| I["Feedback to sum"]
    I --> e4["Sum"]
    e4 --> |+| J["Sum"]
    J --> u_c
    u_c --> |+| K["Output u"]
```
</details>

(a) 带抗漂移的PI控制器

![](image/ba2ba3e41c11128a7dc28a98ccb3da86ad0e76f2f4b5aa2b6b60533f90a89207.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    e["Input e"] --> A["Summing Junction"]
    A --> B["+"]
    B --> C["e1"]
    C --> D["k1/s"]
    D --> E["u1"]
    E --> F["+"]
    F --> G["uC"]
    G --> H["Phase portrait u_min/u_c"]
    H --> I["Output u"]
    I --> J["Feedback to K0"]
    J --> A
    K["p_kp"] --> F
    L["Ka"] --> A
```
</details>

(b) 带单非线性的抗漂移实现

![](image/2a164810b1e88ff7802c3f7e836ea9644a5089476f0208afe1a032ddda96b595.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    e --> +1["+"]
    +1 --> e1["e₁"]
    e1 --> k_p["kₚ"]
    k_p --> +2["+"]
    +2 --> u_c["u_c"]
    u_c --> +3["+"]
    +3 --> K_a["K_a"]
    K_a --> -["-"]
    - --> +1
    +3 --> u_max["u_max"]
```
</details>

(c) 饱和时的等效框图

![](image/6773c9d7f8c5e21b73aed5026263d29eb6a8bbe54c1f1734c6c8fe248440ed24.jpg)  
(d) 饱和时抗漂移积分器的一阶超前等效   
图 8-73 积分抗漂移方案

抗漂移的作用是在反馈系统中降低超调量和控制量。这种抗漂移方案的实现，在任何实际的积分控制应用中都是必需的，忽略这种方法可能导致系统响应的严重退化。从稳定性的角度来说，饱和作用是打开反馈回路，将留下的常量输入的开环对象和控制器当做系统误差为输入的开环系统。

抗漂移的目的是当主环被信号饱和打开时，提供一个局部的反馈使得控制器稳定。

现在,考虑一个对象,其针对小信号传递函数为

$$G (s) = \frac {1}{s}$$

且在单位反馈结构中的 PI 控制器为

$$G _ {c} (s) = k _ {p} + \frac {k _ {I}}{s} = 2 + \frac {4}{s}$$

设被控对象的输入被限制在 $\pm1.0$ ，试研究抗漂移控制对系统响应的影响。

解 假定采用一个反馈增益为 $K_{a} = 10$ 的抗漂移电路，如图8-74所示的Simulink框图。图8-75(a)给出了系统有抗漂移措施和没有抗漂移措施时的阶跃响应。图8-75(b)给出了相应的控制量。仿真结果表明，带抗漂移的系统实质上有更小的超调量和更小的控制量。

![](image/9d2bfaed649c753a7dd5ca2ab90aea9e807dad4b047086e1ea21b8f733cba5b2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["仿真时间 t"] --> B["工作空间1"]
    C["阶跃"] --> D["+"]
    D --> E["+"]
    E --> F["KP 2"]
    F --> G["+"]
    G --> H["饱和环节"]
    I["1/s"] --> J["积分器"]
    K["10 Ka"] --> L["+"]
    L --> M["+"]
    M --> N["被控对象"]
    O["u"] --> P["工作空间2"]
    Q["c"] --> R["工作空间3"]
    S["控制"] --> T["输出"]
    U["工作空间1"] --> V["+"]
    W["控制"] --> X["控制"]
    Y["控制"] --> Z["输出"]
```
</details>

图 8-74 抗漂移的例子(Simulink 框图)

![](image/0855beed405f47c41eb0ad2d9bb98486dd16bb02542ea50b0405ad69b7a88f3e.jpg)

<details>
<summary>line</summary>

| 时间/s | 不带抗漂移 | 带抗漂移 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.0 | 1.0 |
| 2 | 1.5 | 1.2 |
| 3 | 1.4 | 1.0 |
| 4 | 1.0 | 0.9 |
| 5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 |
| 7 | 1.0 | 1.0 |
| 8 | 1.0 | 1.0 |
| 9 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
</details>

(a) 阶跃响应

![](image/2f27a1813902713de09a47147fa250b787459ae6152ac815f669570b1bc942a0.jpg)

<details>
<summary>line</summary>

| 时间/s | 带抗漂移 | 不带抗漂移 |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 1 | 0.5 | 0.8 |
| 2 | -0.2 | -0.4 |
| 3 | -0.1 | -0.6 |
| 4 | 0.0 | 0.1 |
| 5 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 |
| 7 | 0.0 | 0.0 |
| 8 | 0.0 | 0.0 |
| 9 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 |
</details>

(b) 控制作用  
图 8-75 积分器抗漂移效果(Simulink)
