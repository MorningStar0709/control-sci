# 例3.22 由简单框图求传递函数

求解图 3.11a 所示系统的传递函数。

![](image/37e8eaf9cb2ba8486b1fe967f5268552a601cbb519e5de7b50d4ab60f455e3b3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum1["Σ"]
    Sum1 -->|−| Sum2["4/s"]
    Sum2 -->|+| Sum3["Σ"]
    Sum3 -->|+| Sum4["1/s"]
    Sum4 --> Y
    Sum1 -->|2| Sum3
    Sum3 -->|+| Sum4
```
</details>

a)

![](image/86ea95b439529892a99565ecf2df95cb878809963c08c86f2d43a42a29f496b8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum --> A["2s + 4/s"]
    A --> B["1/s"]
    B --> Y
    Y -->|-| Sum
```
</details>

b)   
图 3.11 二阶系统的框图

解答。首先我们通过减少控制器路径上的并联环节来简化框图。所得结果如图 3.11b 所示，并且使用反馈规则获取闭环传递函数为

$$T (s) = \frac {Y (s)}{R (s)} \frac {\frac {2 s + 4}{s ^ {2}}}{1 + \frac {2 s + 4}{s ^ {2}}} = \frac {2 s + 4}{s ^ {2} + 2 s + 4}$$
