# 2. 反馈网络

网络结构如图 6-3 所示,该网络结构在输出层到输入层存在反馈,即每一个输入节点都有可能接受来自外部的输入和来自输出神经元的反馈。这种神经网络是一种反馈动力学系统,它需要工作一段时间才能达到稳定。Hopfield 神经网络是反馈网络中最简单且应用最广泛的模型,它具有联想记忆的功能,如果将 Lyapunov 函数定义为寻优函数,Hopfield 神经网络还可以解决寻优问题。

![](image/58bfb16770fc84316a2e78a138d30dec756c5b3d68aa9c8b2553f743f1ee9ac9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["输入层"] --> B["节点1"]
    A --> C["节点2"]
    A --> D["..."]
    A --> E["节点N"]
    F["隐含层"] --> G["节点1"]
    F --> H["节点2"]
    F --> I["..."]
    F --> J["节点N"]
    K["输出层"] --> L["节点1"]
    K --> M["节点2"]
    K --> N["..."]
    K --> O["节点N"]
```
</details>

图 6-2 前向型神经网络

![](image/9e9ae0d4bdc83eabea4753c43f87ee3e2e34afd47b9d220b7d33d0bca1f05d26.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["输入"] --> B["节点1"]
    B --> C["输出"]
    C --> D["节点2"]
    D --> E["..."]
    E --> F["输出"]
    style A fill:#f9f,stroke:#333
    style F fill:#f9f,stroke:#333
```
</details>

图 6-3 反馈型神经网络
