# 2.11.2 仿真实例

被控对象为

$$G (s) = \frac {5 0 s + 5 0}{s ^ {3} + s ^ {2} + s}$$

分两步来实现 PID 的整定：首先运行主程序 chap2\_13main.m，初始化的参数为 $k_{p}=0$ ， $k_{i}=0$ ， $k_{d}=0$ ，上下界分别取为 LB=[0 0 0]，UB=[100 100 100]。优化结果为 $k_{p}=1.0592$ ， $k_{i}=0.0185$ ， $k_{d}=0.1427$ ，优化后的阶跃响应如图 2-36 所示；然后采用优化参数运行 Simulink 程序 chap2\_13sim.mdl，在 NCD 环境下进行 PID 再优化， $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 优化范围设置如图 2-37 所示。优化过程中通过鼠标不断调整 NCD 响应指标，使阶跃响应性能指标尽量优化，经过多次调整得优化结果为 $k_{p}=9.7254$ ， $k_{i}=0.0011$ ， $k_{d}=4.7124$ ，优化前后的阶跃响应如图 2-38 和 2-39 所示。

![](image/3a0da1ac86345e2dba4aed2000134439853b25427e98d81048b2c8ab96829916.jpg)

<details>
<summary>line</summary>

| Time offset | Value |
| --- | --- |
| 0 | 1.2 |
| 5 | 1.0 |
| 10 | 1.0 |
| 15 | 1.0 |
| 20 | 1.0 |
| 25 | 1.0 |
| 30 | 1.0 |
| 35 | 1.0 |
| 40 | 1.0 |
| 45 | 1.0 |
| 50 | 1.0 |
| 55 | 1.0 |
| 60 | 1.0 |
| 65 | 1.0 |
| 70 | 1.0 |
| 75 | 1.0 |
| 80 | 1.0 |
| 85 | 1.0 |
| 90 | 1.0 |
| 95 | 1.0 |
| 100 | 1.0 |
</details>

图 2-36 采用优化函数的阶跃响应

![](image/8f6c734b1458b5d4c4ef90823e3f38ea61b19743087694369f62ed309fa6a033.jpg)

<details>
<summary>text_image</summary>

Optimization Parameters
Tunable Variables: kp ki kd
Lower bounds (optional): 0 0 0
Upper bounds (optional): 100.100 100
Discretization interval: 1
Variable Tolerance: 0.001
Constraint Tolerance: 0.001
✓ Display optimization information
☐ Stop optimization as soon as the constraints are achieved
✓ Compute gradients with better accuracy (slower)
Note: Simulation parameters are entered in the SIMULINK system.
</details>

图 2-37 Optimization Parameters 设置图

![](image/8100de417be4373ce44c278ebef37ad52963fb9c29f7a64444ee83c537501c88.jpg)

<details>
<summary>text_image</summary>

System: chap7_Af2, Outport: 1
File Edit Options Optimization Style
Hypothesis
Port: 1 Split Start Stop Help Close
</details>

图 2-38 NCD 优化前的界面

![](image/6dd46607a4cf30001d50d0338872c5331ec49e0210f769ddb05e70741a3f784f.jpg)

<details>
<summary>text_image</summary>

Scope
Time offset: 0
</details>

图 2-39 NCD 优化后的阶跃响应

〖仿真程序〗 分为主程序、M 函数子程序和 Simulink 子程序三个部分。

(1) 主程序: chap2\_13main.m

```txt
clear all;
close all;
```

```matlab
K_pid0=[0 0 0];
LB=[0.1 0.0 0.0];
UB=[100 100 100];
K_pid=lsqnonlin('chap2_13eq', K_pid0, LB, UB)
chap2_13sim
```

(2) M 函数子程序: chap2\_13eq.m
