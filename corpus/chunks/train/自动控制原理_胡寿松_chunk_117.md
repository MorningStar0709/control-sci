![](image/2c0df88e256b533ecac14934aa658d1a4eda79fbb7ca2762b4c7fd387a6585a5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R["R(s)"] --> A["Sum"]
    A --> E["E(s)"]
    E --> B["Sum"]
    B --> C["G1(s)"]
    B --> D["G2(s)"]
    C --> E
    D --> E
    E --> C
    C --> G["C(s)"]
    D --> G
    G --> C
```
</details>

(b)   
图 2-58 题 2-21 系统结构图

2-22 试用梅森增益公式求图 2-59 中各系统信号流图的传递函数 $C(s)/R(s)$ 。

![](image/b4b92a2218c4971bdf8259255eb3dbdf8ea1b58306f661c27713529fbfda2e5d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] -->|1| G1
    G1 --> G2
    G2 --> G3
    G3 --> G4
    G4 --> G5
    G5 -->|1| C["s"]
    G6 -->|-H3| G3
    G6 -->|-H2| G2
    G3 -->|-H1| G4
```
</details>

(a)

![](image/e6df9bdec597587bb7523e30256019f1af759d31909a28ee10e7dac3ddbf0b09.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["R(s)"] -->|1| A
    A -->|G1| B
    B -->|-H1| C
    C -->|G3| D
    D -->|-H2| E
    E -->|-H3| F
    F -->|G6| G
    G -->|1| H
    H --> C
    G --> G7
    G --> G8
    G --> G4
    G --> G5
    G --> G6
    G --> G7
    G --> G8
    G --> G4
    G --> G5
    G --> G6
    G --> G7
    G --> G8
```
</details>

(b)   
![](image/d9211dcc68712a2344b6665d2c38abc1e1b4247564c0c6c27543b3840e7577ad.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["R(s)"] -->|1| B["5"]
    B -->|10| C["10"]
    C -->|2| D["1"]
    D -->|1| E["C(s)"]
    B -->|-1| C
    C -->|-2| D
    D -->|1| E
    E -->|1| F["End"]
    G["-0.5"] --> C
```
</details>

(c)

![](image/f337cb9550a89f2be0dce74c17fe20ac8d89779658b4403f475ad2768b62b80c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R_s["R(s)"] -->|1| A
    A -->|a| B
    B -->|b| C
    C -->|c| D
    D -->|d| E
    E --> C
    A -->|f| B
    B -->|g| C
    C -->|h| D
    D -->|e| E
```
</details>

(d)

![](image/3a67c8b79e15c85135070dd933ccc3cb817df380cb8f134c214264079ddc063f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R₁(s)"] -->|1| B
    B -->|b| C
    C -->|c| D
    D -->|d| E
    E -->|e| F
    F -->|l| G
    G -->|l| H
    H --> I["C(s)"]
    I -->|1| J
    J -->|-h| K
    K -->|-f| L
    L -->|a| B
    L -->|-g| M
```
</details>

(c)

![](image/77b2211f7ffb78d9491e4abf24d7a76f241223e91a6ae6db5d88a7c37f75a236.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R3[" R₃(s) "] -->|1| A(( ))
    A -->|a| R1[" R₁(s) "]
    A -->|d| B(( ))
    B -->|b| R1
    B -->|e| C(( ))
    C -->|h| D((C(s))|
    C -->|j| D
    C -->|i| E(( ))
    E -->|g| F(( ))
    F -->|c| R2[" R₂(s) "]
    F -->|1| G(( ))
    G --> R2
```
</details>

(f)   
图 2-59 题 2-22 系统信号流图
