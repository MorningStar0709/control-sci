# 习题

1-1 图 1-21 是液位自动控制系统原理示意图。在任意情况下，希望液面高度 c 维持不变，试说明系统工作原理并画出系统方块图。

![](image/98535b8a52a19f4133cee6c88d124219bd883730d978334bc7847d7636b8560a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["浮子"] --> B["用户"]
    B --> C["用水开关"]
    C --> D["Q2"]
    D --> E["Q1"]
    E --> F["控制阀"]
    F --> G["电位器"]
    G --> H["减速器"]
    H --> I["电动机"]
    I --> J["SM"]
    J --> K["+"]
    J --> L["-"]
    J --> M["电流表"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#cfc,stroke:#333
    style H fill:#fcc,stroke:#333
    style I fill:#cfc,stroke:#333
    style J fill:#fcc,stroke:#333
    style K fill:#cfc,stroke:#333
    style L fill:#fcc,stroke:#333
```
</details>

图 1-21 液位自动控制系统

![](image/8374d64a2695477b533e3c5e29af8b9d2ca094a0c28d1fadad2543a930cc34fb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["放大器"] -->|u| B["伺服电动机"]
    B --> C["绞盘"]
    C --> D["门"]
    D --> E["开门开关"]
    D --> F["关门开关"]
```
</details>

图 1-22 仓库大门自动开闭控制系统

1-2 图 1-22 是仓库大门自动控制系统原理示意图。试说明系统自动控制大门开闭的工作原理并画出系统方块图。  
1-3 图 1-23(a) 和 (b) 均为自动调压系统。设空载时, 图 (a) 与图 (b) 的发电机端电压均为 110V。试问带上负载后, 图 (a) 与图 (b) 中哪个系统能保持 110V 电压不变? 哪个系统的电压会稍低于 110V? 为什么?

![](image/b56a0ac2df73d18124cda651f6f22732cd07f8a3656bafc8bc8656797777040d.jpg)

<details>
<summary>text_image</summary>

+
uf
if
G
负载
SM
K
</details>

(a)

![](image/e88fdea88d357691ad7de8c99fef75c948a900f17d26f188bfe5dd5793049da7.jpg)

<details>
<summary>text_image</summary>

If
+
-
负载
Δ K
+
</details>

(b)   
图 1-23 自动调压系统

1-4 图 1-24 为水温控制系统示意图。冷水在热交换器中由通入的蒸汽加热，从而得到一定温度的热水。冷水流量变化用流量计测量。试绘制系统方块图，并说明为了保持热水温度为期望值，系统是如何工作的？系统的被控对象和控制装置各是什么？

1-5 图 1-25 是电炉温度控制系统原理示意图。试分析系统保持电炉温度恒定的工作过程，指出系统的被控对象、被控量以及各部件的作用，最后画出系统方块图。

![](image/d6c2044ddcc3f2222d9949d3dfec8a0fdd2f01c4a5038f6e1e67cc90f76698dd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["蒸汽"] --> B["阀门"]
    C["冷水"] --> D["阀门"]
    B --> E["热交换器"]
    D --> E
    E --> F["按流量顺馈"]
    G["温度控制器"] --> H["温度测量"]
    H --> I["热水"]
    J["流量计"] --> E
```
</details>

图 1-24 水温控制系统示意图

![](image/2cd3c85e357b6794a7a2581b1117181f1aed58b221a710bde3480515df075a27.jpg)

<details>
<summary>flowchart</summary>
