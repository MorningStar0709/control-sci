| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| 1 | -1 | 4.5 |
| 2 | -3 | 3.0 |
| 3 | -3.5 | -3.0 |
| 4 | -1 | -4.5 |
</details>

(b) $\beta$ 为可变参数

图 4-29 自动焊接头控制系统根轨迹图 (MATLAB)  
![](image/99e9bb67a02b077907b02a1333ac1dcb834e2c5f64ceec5d234544201b01ec8a.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.8 |
| 1.0 | 1.0 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

(a) 单位阶跃响应

![](image/2ba9d83380258be475a67629f70b59e03b6777b7c3dea1aaad75002b0f519117.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.5 |
| 1.0 | 1.0 |
| 1.5 | 1.5 |
| 2.0 | 2.0 |
| 2.5 | 2.5 |
| 3.0 | 3.0 |
| 3.5 | 3.5 |
| 4.0 | 4.0 |
| 4.5 | 4.5 |
| 5.0 | 5.0 |
</details>

(b) 单位斜坡响应  
图 4-30 自动焊接头控制系统的时间响应曲线 (MATLAB)

$$
\operatorname{sgrid} (0. 7 0 7, ^ {\prime} \text { new } ^ {\prime}); \text { axis } ([ - 8 2 - 5 5 ])\text { figure; rlocus(Gb);hold on; }\text { beta } = 4. 3 3; \text { rlocus } (\mathrm{Gb}, \text { beta })\% \text{取阻尼比为} 0.707\% \text{绘制相应系统的要轨迹}\% \text {求} \beta = 4.33 \text {时,系统的闭环特征根}
\begin{array}{l} \mathrm{K} 1 = 2 0; \mathrm{K} 2 = 0. 2 1 6 5; \\ \mathrm{G} 1 = \mathrm{zpk} ([ ], [ 0 - 2 ], \mathrm{K} 1); \mathrm{H} 1 1 = \mathrm{tf} ([ \mathrm{K} 2 1 ], [ 0 1 ]); \\ \mathrm{sys} = \text { feedback } (\mathrm{G1}, \mathrm{H11}) \quad \% \text { 系统的闭环传递函数 } \\ \mathrm{t} = 0: 0. 0 0 5: 5; \mathrm{u} = \mathrm{t}; \\ \text {figure}; \text {step(sys,t);grid} \% \text {单位阶跃输入响应} \\ \text {figure}; \operatorname{lsim} (\text {sys}, u, t); \text {grid} \quad \% \text {单位斜坡输入响应} \\ \end{array}
$$

% 以下进行系统动态性能分析
