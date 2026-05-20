# 2. 仿真实例

设输入 $X \in [0,5]$ , $Y \in [0,10]$ ，将它们模糊化为两个模糊量，即“小”和“大”。输出 Z 为输入 $(X,Y)$ 的线性函数，模糊规则为

If X 为 small and Y 为 small then $Z = -X + Y - 3$

If X 为 small and Y 为 big then $Z = X + Y - 1$

If X 为 big and Y 为 small then $Z = -2Y + 2$

If X 为 big and Y 为 big then $Z = 2X + Y - 6$

仿真程序见本章附录程序 chap4\_8.m。模糊推理系统的输入隶属函数曲线及输入、输出曲线如图 4-30 和图 4-31 所示。

通过命令 showrule(ts2) 可显示模糊控制规则, 共有以下 4 条:

(1) If (X is small) and (Y is small) then (Z is first area) (1)   
(2) If (X is small) and (Y is big) then (Z is second area) (1)   
(3) If (X is big) and (Y is small) then (Z is third area) (1)   
(4) If (X is big) and (Y is big) then (Z is fourth area) (1)

![](image/63bca71f8837551af302f1b000888641fee934c0e066ae3104e3c353250e005b.jpg)

<details>
<summary>line</summary>

| x | MF Degree of input 1 (little) | MF Degree of input 1 (big) | MF Degree of input 2 (little) | MF Degree of input 2 (big) |
| --- | --- | --- | --- | --- |
| 0.0 | 1.0 | 0.0 | 1.0 | 0.0 |
| 0.5 | 0.9 | 0.1 | 0.9 | 0.1 |
| 1.0 | 0.8 | 0.2 | 0.8 | 0.2 |
| 1.5 | 0.7 | 0.3 | 0.7 | 0.3 |
| 2.0 | 0.6 | 0.4 | 0.6 | 0.4 |
| 2.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| 3.0 | 0.4 | 0.6 | 0.4 | 0.6 |
| 3.5 | 0.3 | 0.7 | 0.3 | 0.7 |
| 4.0 | 0.2 | 0.8 | 0.2 | 0.8 |
| 4.5 | 0.1 | 0.9 | 0.1 | 0.9 |
| 5.0 | 0.0 | 1.0 | 0.0 | 1.0 |
</details>

图 4-30 Sugeno 模糊推理系统的输入隶属函数曲线

![](image/0457b2fbd921f313d23646818f5bb09b1e147e700cd1eac68249e24e2be31bc6.jpg)

<details>
<summary>surface_3d</summary>

| X | Y | Z |
| --- | --- | --- |
| 0 | 0 | 10 |
| 1 | 0 | 5 |
| 2 | 0 | 0 |
| 3 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 0 | 0 |
</details>

图 4-31 Sugeno 模糊推理系统的输入、输出曲线
