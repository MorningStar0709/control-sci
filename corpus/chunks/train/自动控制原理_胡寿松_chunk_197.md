<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> +1["+"]
    +1 --> E["s"]
    E["s"] --> 100["100"]
    100 --> +2["+"]
    N["s"] --> +2
    +2 --> Transfer["1/(s(s+12))"]
    Transfer --> C["s"]
    C["s"] --> -["-"]
    - --> +1
```
</details>

(a) 所设计的系统

![](image/dbb5641f9751d350abeb18b048e00ddfb2bd2488d55fa4e016a4617787dfdc76.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.8 |
| 0.4 | 1.1 |
| 0.6 | 1.0 |
| 0.8 | 1.0 |
| 1.0 | 1.0 |
| 1.2 | 1.0 |
| 1.4 | 1.0 |
| 1.6 | 1.0 |
| 1.8 | 1.0 |
| 2.0 | 1.0 |
</details>

(b) 系统对单位阶跃输入(实线)和单位阶跃扰动(虚线)的时间响应  
图 3-55 哈勃太空望远镜指向系统设计结果 (MATLAB)

MATLAB 文本：

$$\mathrm{Ka} = 1 0 0; \mathrm{K} 1 = 1 2;\mathrm{G} 1 = \mathrm{zpk} ([ ], [ 0 - \mathrm{K} 1 ], 1);\mathrm{sys} = \text { feedback } (\mathrm{Ka} * \mathrm{G1}, 1); \quad \% \text { 输入端闭环传递函数描述 }\mathrm{sysn} = \text { feedback } (\mathrm{G1}, \mathrm{Ka}); \quad \% \text { 扰动端闭环传递函数描述 }t = 0; 0. 0 1; 2;\text {step} (\text {sys}, t); \text {hold on}; \quad \% \text {单位阶跃输入响应曲线}\text {step} (\text {sysn}, t); \text {grid} \quad \% \text {单位阶跃扰动响应曲线}$$
