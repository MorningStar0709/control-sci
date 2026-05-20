| Point Type | Value |
| --- | --- |
| System G Gain | 25.5 |
| Pole | -4.49±7.7% |
| Damping | 0.5 |
| Overhoot | 16.3 |
| Frequency | 8.97 |
</details>

(a) s=0.5 时系统的主导极点

![](image/b146f0f4657e32e029c02e99f407613b6976f49173359b7146be8ca9c9b607fe.jpg)

<details>
<summary>line</summary>

| Point Type | Real Axis | Imaginary Axis |
| --- | --- | --- |
| Circle | -7 | 7 |
| Triangle | -30 | 0 |
| Circle | -5 | 8 |
| Triangle | -4 | -8 |
| Circle | -6 | -6 |
| Triangle | -4 | -9 |
| Circle | 0 | 0 |
| Triangle | 0 | 0 |
</details>

(b) 自动平衡秤系统根轨迹图

![](image/46232463c5194a5791801d29be943f60f6398c9ba6323fb590c50e5345b7c81e.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | 0.0290 |
| 1.0 | 0.0245 |
| 1.5 | 0.0250 |
| 2.0 | 0.0250 |
| 2.5 | 0.0250 |
| 3.0 | 0.0250 |
</details>

(c) 自动平衡秤系统时间响应(MATLAB)  
图 4-25 自动平衡秤系统根轨迹图(MATLAB)

MATLAB 文本：

$$\mathrm{G} = \mathrm{zpk} ([ - 6. 9 3 + 6. 9 3 \mathrm{i} - 6. 9 3 - 6. 9 3 \mathrm{i} ], [ 0. 0 - 1 3. 8 6 ], 1);z = 0. 5\text { figure } (1); \text { rlocus } (G);\operatorname{sgrid} \left(z, ^ {\prime} \text {new} ^ {\prime}\right); \text {axis} \left(\left[ - 1 0 ^ {\prime} 5 - 1 0 1 0 \right]\right)\text { figure } (2); \text { rlocus } (G); \text { hold on };\mathrm{K} = 2 5. 5; \text { rlocus } (\mathrm{G}, \mathrm{K})\mathrm{sys} = \mathrm{tf} ([ 3. 0 5 9 6 ], [ 0. 0 5 1. 9 6 8 8 1 7. 6 9 4 6 1 2 2. 3 8 3 8 ]);\text { figure } (3); t = 0: 0. 0 1: 3; \text { step } (\text { sys }, t); \text { grid }$$

% 绘制相应系统的要轨迹

$\%$ 取阻尼比为0.5

% 求阻尼比 0.5 对应的根轨迹增益

% 求阻尼比为 0.5 时系统的闭环特征根

% 闭环系统描述

% 系统的单位阶跃响应
