# 例 4.5 电动机速度的 PID 控制

考虑直流电动机速度控制，给定参数如下 $^{①}$ 。

$$J _ {\mathrm{m}} = 1. 1 3 \times 1 0 ^ {- 2} \mathrm{N} \cdot \mathrm{m} \cdot \mathrm{s} ^ {2} / \mathrm{rad}, b = 0. 0 2 8 \mathrm{N} \cdot \mathrm{m} \cdot \mathrm{s} / \mathrm{rad}, L _ {\mathrm{a}} = 1 0 ^ {- 1} \mathrm{H},R _ {\mathrm{a}} = 0. 4 5 \Omega , \quad K _ {\mathrm{t}} = 0. 0 6 7 \mathrm{N} \cdot \mathrm{m} / \mathrm{amp}, \quad K _ {\mathrm{e}} = 0. 0 6 7 \mathrm{V} \cdot \mathrm{s} / \mathrm{rad} \tag {4.78}$$

第 2 章 2.14 节对这些参数进行了定义。控制器参数为

$$k _ {\mathrm{P}} = 3, \quad k _ {\mathrm{I}} = 1 5 \mathrm{s}, \quad k _ {\mathrm{D}} = 0. 3 \mathrm{s} \tag {4.79}$$

当系统存在阶跃干扰转矩和阶跃参考输入时，分别使用三个控制器：P，PI 和 PID 来研究系统的阶跃响应。令未使用的控制器参数为零。

解答。图 4.11a 表示系统在 P、PI 和 PID 反馈控制的下阶跃干扰输入响应。注意加入积分项后增加了系统的振荡，但是消除了稳态误差。

![](image/7c9635a4aae3c07e15318b55c470a21f2a22f07e3a305bef94c733723f53bd10.jpg)

<details>
<summary>line</summary>

| 时间/ms | P | PID | PI |
| --- | --- | --- | --- |
| 0 | 6.0 | -4.0 | 0.0 |
| 1 | 2.0 | -2.0 | 0.0 |
| 2 | 0.0 | 0.0 | 0.0 |
| 3 | 0.0 | 0.0 | 0.0 |
| 4 | 0.0 | 0.0 | 0.0 |
| 5 | 0.0 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 | 0.0 |
</details>

a）阶跃干扰输入

![](image/ecec817437f48fe89cba9566419d457685e590f746a8db3fedd3ad8d744348dc.jpg)

<details>
<summary>line</summary>

| 时间/ms | PID | PI |
| --- | --- | --- |
| 0.0 | 1.7 | 1.3 |
| 0.5 | 0.4 | 1.0 |
| 1.0 | 1.5 | 1.2 |
| 1.5 | 0.6 | 1.0 |
| 2.0 | 1.2 | 1.1 |
| 2.5 | 0.9 | 1.0 |
| 3.0 | 1.1 | 1.0 |
| 3.5 | 1.0 | 1.0 |
| 4.0 | 1.0 | 1.0 |
| 4.5 | 1.0 | 1.0 |
| 5.0 | 1.0 | 1.0 |
| 5.5 | 1.0 | 1.0 |
| 6.0 | 1.0 | 1.0 |
</details>

b）阶跃参考输入  
图 4.11 系统 P、PI、PID 控制的响应

当保持零稳态误差时，增加微分项后减小了振荡。图 4.11b 显示在 P，PI，PID 控制下阶跃参考响应显示出相似的结果。阶跃响应可以通过构造分子和分母的系数矢量（按 s 的阶次降序排列），应用 Matlab 中的阶跃函数进行计算。
