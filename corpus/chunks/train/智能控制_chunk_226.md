图4-25 $k_{\mathrm{i}}$ 的隶属函数

(7) If (e is P) and (ec is N) then (kp is P)(ki is Z) (1)   
(8) If (e is P) and (ec is Z) then (kp is P)(ki is Z) (1)   
(9) If (e is P) and (ec is P) then (kp is P)(ki is Z) (1)

另外,针对模糊推理系统 fuzzpid.fis, 运行 fuzzy 命令可进行规则库和隶属函数的编辑, 如图 4-26 所示, 运行命令 ruleview 可实现模糊系统的动态仿真, 如图 4-27 所示。

![](image/0fcaba78b4844e9d6ce4161068fdbbbe0795e9620e8853d2dd407dda08ed5b50.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["e(3)"] --> C["fuzzpid (Mamdani) 9 rules"]
    B["e_c(3)"] --> C
    D["k_p(3)"] --> C
    E["k_t(3)"] --> C
```
</details>

System fuzzpid; 2 inputs, 2 outputs, 9 rules

图 4-26 模糊系统 fuzzpid.fis 的结构

在程序 chap4\_7b.m 中, 利用所设计的模糊系统 fuzzpid.fis 进行 PI 控制参数的整定。为了显示模糊规则调整效果, 取 $k_{p}$ 、 $k_{i}$ 的初始值为零, 响应结果及 PI 控制参数的自适应变化如图 4-28 至图 4-29 所示。

![](image/a78e91a1b342a3d1b60ab196e251459373d4b1ffbf442e9101da4ebd858b604f.jpg)

<details>
<summary>text_image</summary>

Rule Viewer: fuzzpid
File Edit View Options
e = 0
ec = 0
kp = 2.67
ki = 0.0811
Input: [0,0]
Plot points: 101
Move: left right down up
Opened system fuzzpid, 9 rules
Help Close
</details>

图 4-27 模糊推理系统的动态仿真环境  
![](image/8a007c0fde3b58d2adabeff3367b198cd7cd23d9682834c543531981d78ba80e.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position | Practical position |
| --- | --- | --- |
| 0.0 | 1.0 | 0.0 |
| 0.1 | 1.0 | 0.8 |
| 0.2 | 1.0 | 1.05 |
| 0.3 | 1.0 | 1.0 |
| 0.4 | 1.0 | 1.0 |
| 0.5 | 1.0 | 1.0 |
| 0.6 | 1.0 | 1.0 |
| 0.7 | 1.0 | 1.0 |
| 0.8 | 1.0 | 1.0 |
| 0.9 | 1.0 | 1.0 |
| 1.0 | 1.0 | 1.0 |
</details>

图 4-28 模糊 PI 控制阶跃响应  
![](image/eeb73de7a168b21b8b3e47ccd742011fc790fb6dbc64df4dab0edc434b8b7c3b.jpg)

<details>
<summary>line</summary>

| time(s) | k_p | k_i |
| --- | --- | --- |
| 0.0 | 2.65 | 0.00 |
| 0.1 | 2.45 | 0.08 |
| 0.2 | 2.65 | 0.08 |
| 0.3 | 2.65 | 0.08 |
| 0.4 | 2.65 | 0.08 |
| 0.5 | 2.65 | 0.08 |
| 0.6 | 2.65 | 0.08 |
| 0.7 | 2.65 | 0.08 |
| 0.8 | 2.65 | 0.08 |
| 0.9 | 2.65 | 0.08 |
| 1.0 | 2.65 | 0.08 |
</details>

图 4-29 $k_{p}$ 和 $k_{i}$ 的模糊自适应调整
