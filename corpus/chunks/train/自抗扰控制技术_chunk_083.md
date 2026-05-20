# 2.6.9 相位超前功能的实现

利用跟踪微分器, 可以按图 2.6.16 方式来实现相位超前功能.

![](image/5c245a31c7fb22801e7f4063ff4dbd2500bc7e45bade8f3633319ee2b28e8422.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["v"] --> B["跟踪微分器"]
    B --> C["v1"]
    B --> D["v2"]
    C --> E["v1 + λh1v2"]
    D --> E
    E --> F["y"]
```
</details>

图2.6.16

其具体算法为

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (v _ {1} - v (t), v _ {2}, r, h _ {1}) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \end{array} \right. \tag {2.6.24}
\gamma (t) = \frac {1}{\gamma} (v _ {1} (t) + \lambda h _ {1} v _ {2} (t)), \gamma > 1
$$

参数取值和输入函数如下：

$$h = h _ {1} = 0. 0 1, v _ {1} (t) = \sin (t), \lambda = 1 1 0, \gamma = 1. 5$$

所作仿真结果显示于图 2.6.17. 参数 $\lambda$ 小, 超前的相位会小.

![](image/0e051781fa10993c70d44227d05e442ce160b9a3891b87e38547ff0c9a2c34b2.jpg)

<details>
<summary>line</summary>

| x | y(t) | u(t), v(t) |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 1 | 0.5 | 0.5 |
| 2 | 0.0 | 1.0 |
| 3 | -0.5 | 0.5 |
| 4 | -1.0 | 0.0 |
| 5 | -0.5 | -0.5 |
| 6 | 0.0 | -1.0 |
| 7 | 0.5 | -0.5 |
| 8 | 1.0 | 0.0 |
| 9 | 0.5 | 0.5 |
| 10 | 0.0 | 1.0 |
</details>

图2.6.17
