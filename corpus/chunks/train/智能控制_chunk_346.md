# 7.2.3 BP网络的逼近

BP 网络逼近的结构如图 7-6 所示, 图中 k 为网络的迭代步骤, $u(k)$ 和 $y(k)$ 为逼近器的输入。BP 为网络逼近器, $y(k)$ 为被控对象的实际输出, $y_{n}(k)$ 为 BP 网络的输出。将系统输出 $y(k)$ 及输入 $u(k)$ 的值作为逼近器 BP 的输入, 将系统输出与网络输出的误差作为逼近器的调整信号。

用于逼近的 BP 网络如图 7-7 所示。

![](image/4034c4e1dd1a91f7b6b39ef1e5fcfbcaca7bf9d32b7e19308eb95272285486ea.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u(k)"] --> B["对象"]
    B --> C["y(k)"]
    C --> D["+"]
    D --> E["y_n(k)"]
    E --> F["BP"]
    F --> G["输出"]
    G --> A
```
</details>

图 7-6 BP 神经网络逼近

![](image/bf77fca7c45af0b081015c8cac1f2ffa9c3097c5c340a6b9e3e29c3622628499.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u(k)"] --> B["Node"]
    C["y(k)"] --> D["Node"]
    B --> E["Node"]
    D --> F["Node"]
    E --> G["..."]
    F --> H["..."]
    G --> I["Node"]
    H --> I
    I --> J["y_n(k)"]
    D --> K["x_i"]
    K --> L["x_j"]
    L --> M["x'_j"]
    M --> N["w_{ij}"]
    M --> O["w_{jo}"]
    style B fill:#fff,stroke:#000
    style D fill:#fff,stroke:#000
    style E fill:#fff,stroke:#000
    style F fill:#fff,stroke:#000
    style G fill:#fff,stroke:#000
    style H fill:#fff,stroke:#000
    style I fill:#fff,stroke:#000
    style J fill:#fff,stroke:#000
    style K fill:#fff,stroke:#000
    style L fill:#fff,stroke:#000
    style M fill:#fff,stroke:#000
    style N fill:#fff,stroke:#000
```
</details>

图 7-7 用于逼近的 BP 网络

BP算法的学习过程由正向传播和反向传播组成。在正向传播过程中，输入信息从输入层经隐层逐层处理，并传向输出层，每层神经元（节点）的状态只影响下一层神经元的状态。如果在输出层不能得到期望的输出，则转至反向传播，将误差信号（理想输出与实际输出之差）按连接通路反向计算，由梯度下降法调整各层神经元的权值，使误差信号减小。
