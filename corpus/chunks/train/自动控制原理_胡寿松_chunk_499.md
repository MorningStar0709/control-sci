# 7-10 试求图 7-62 闭环离散系统的脉冲传递函数 $\Phi(z)$ 或输出 z 变换 $C(z)$ 。

![](image/661faa56675e677d525a7ba6bab26e06df14b50ac65b272ae133ee81dcf72842.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["2/(s+2)"]
    B --> C["5/(s+5)"]
    C --> D["C(s)"]
    
    E["R(s)"] --> F["2/(s+2)"]
    F --> G["5/(s+5)"]
    G --> H["C(s)"]
```
</details>

图 7-61 开环离散系统

![](image/92c37156e099af0f8032f4825bc89d48af5a08e63310f819fe0fa177151586e3.jpg)  
图 7-62 闭环离散系统
