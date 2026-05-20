| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.4 |
| 0.2 | 1.2 |
| 0.3 | 1.3 |
| 0.4 | 1.2 |
| 0.5 | 1.0 |
| 0.6 | 0.9 |
| 0.7 | 1.0 |
| 0.8 | 1.0 |
| 0.9 | 1.0 |
| 1.0 | 1.0 |
| 1.1 | 1.0 |
| 1.2 | 1.0 |
| 1.3 | 1.0 |
| 1.4 | 1.0 |
| 1.5 | 1.0 |
| 1.6 | 1.0 |
| 1.7 | 1.0 |
| 1.8 | 1.0 |
| 1.9 | 1.0 |
| 2.0 | 1.0 |
</details>

(b) 单位阶跃响应  
图 7-50 当 T=0.025s, K=13.6 时离散系统的时间响应(MATLAB)

$$\mathrm{T} = 0. 0 1; \mathrm{T} 1 = 0. 1; \mathrm{T} 2 = 0. 0 0 5; \mathrm{K} = 1 3. 6;\mathrm{G} = \mathrm{zpk} ([ ], [ 0 - 1 / \mathrm{T} 1 - 1 / \mathrm{T} 2 ]), 1 3. 6 / (\mathrm{T} 1 * \mathrm{T} 2));\mathrm{Gz} = \mathrm{c2d} (\mathrm{G}, \mathrm{T}, ^ {\prime} \mathrm{zoh} ^ {\prime});\text { sys } = \text { feedback } (\mathrm{Gz}, 1);\mathrm{t} = 0; \mathrm{T}: 2; \text { step } (\text { sys }, \mathrm{t}); \text { grid }$$

(a) MATLAB 文本  
![](image/fe74b1de12f58e8363e2717ef4cf49b3398f19ab35c3bc7f5b779c98bb5d4812.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.0 |
| 0.4 | 1.25 |
| 0.6 | 0.95 |
| 0.8 | 1.0 |
| 1.0 | 1.0 |
| 1.2 | 1.0 |
| 1.4 | 1.0 |
| 1.6 | 1.0 |
| 1.8 | 1.0 |
| 2.0 | 1.0 |
</details>

(b) 单位阶跃响应  
图 7-51 当 T=0.01s, K=13.6 时离散系统的时间响应(MATLAB)
