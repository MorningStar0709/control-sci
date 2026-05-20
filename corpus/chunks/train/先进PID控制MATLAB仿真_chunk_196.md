Optimization Parameters
Tunable Variables: kp ki kd
Lower bounds (optional): 0.00
Upper bounds (optional): 100 100 100
Discretization interval: 1
Variable Tolerance: 0.001
Constraint Tolerance: 0.001
✓ Display optimization information
☐ Stop optimization as soon as the constraints are achieved
✓ Compute gradients with better accuracy (slower)
Note: Simulation parameters are entered in the SIMULINK system.
</details>

图 2-31 Optimization Parameters 设置图

② 选择 Uncertainty 项，定义不确定变量及有关参数，如图 2-32 所示。

输入：不确定变量 $a_{1}$ 、 $a_{2}$ 的上下限，可取为

下限：1.5 40

上限：6.0 50

![](image/dc5d3f623ba469741dce3e7f3939968cc3d25fb6c54e8b9bf5ae0842fd833480.jpg)

<details>
<summary>text_image</summary>

Uncertain Variables
Uncertain variables:
a1 a2
Lower bounds:
1.5 40
Upper bounds:
6.0 50
Number of Monte Carlo simulations:
0
✓ Constrain nominal simulation
□ Constrain lower bound simulation
□ Constrain upper bound simulation
□ Constrain Monte Carlo simulations
Total simulations per step = 1
Done	Revert	Help
</details>

图 2-32 Uncertain Variables 设置图

③ 选择 Start 命令，进行调整变量的优化，直到阶跃响应指标达到要求为止。优化时 NCD 约束窗口不断显示阶跃响应的优化过程，MATLAB COMMAND 窗口也不断显示有关信息。

在 NCD 优化过程中，如果将性能指标设计得过高，如上升时间取得过小（比如取 10s），可能会造成死机。通过调整 NCD 优化边界，可实现优化指标的调整，从而可得到更好或更合理的优化结果。阶跃响应性能限制可以直接由鼠标在 NCD Blockset 约束窗口设置。

每次优化结果需要通过 NCD 环境下的 Save 功能保存在\*.mat 文件中，例如可命名为 chap2\_12save.mat，以供下一次调用。

初始 PID 参数为 $k_{p}=1.0$ ， $k_{i}=0.10$ ， $k_{d}=10$ ，NCD 优化参数如下： $k_{p}=1.477$ ， $k_{i}=0.0858$ ， $k_{d}=9.4283$ ，优化过程及优化前后的响应曲线如图 2-33～图 2-35 所示。

![](image/e7130d9688f576e2333579214aae53139f789065009762a57705f9d8a1eee4dd.jpg)

<details>
<summary>line</summary>

| Time (s) | Response |
| --- | --- |
| 0 | 0.0 |
| 10 | 0.5 |
| 20 | 1.0 |
| 30 | 0.8 |
| 40 | 1.1 |
| 50 | 1.0 |
| 60 | 1.0 |
| 70 | 1.0 |
| 80 | 1.0 |
| 90 | 1.0 |
| 100 | 1.0 |
</details>

图 2-33 NCD 优化过程界面

![](image/52c6196e6bc1b4854c8ead239ba65e7b90482c1ce3d3decc286261c155093320.jpg)

<details>
<summary>text_image</summary>

Restore saved axes settings
Time offset: 0
</details>

图 2-34 NCD 优化前阶跃响应曲线

![](image/5190d20c13b533ab865c3fd572e2e891d641ce20637eb7c36a9355841408e4c7.jpg)

<details>
<summary>line</summary>

| Time offset | Value |
| --- | --- |
| 0 | 0.0 |
| 10 | 0.8 |
| 20 | 1.0 |
| 30 | 1.0 |
| 40 | 1.0 |
| 50 | 1.0 |
| 60 | 1.0 |
| 70 | 1.0 |
| 80 | 1.0 |
| 90 | 1.0 |
| 100 | 1.0 |
</details>

图 2-35 优化后阶跃响应曲线
