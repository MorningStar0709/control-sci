# 【仿真之三】利用 S 函数实现 PID 离散控制器的 Simulink 仿真

被控对象为三阶传递函数 $G(s) = \frac{523500}{s^3 + 87.35s^2 + 10470s}$ ，在 S 函数中，采用初始化函数、更新函数和输出函数，即 mdlInitializeSizes 函数、mdlUpdates 函数和 mdlOutputs 函数。在初始化中采用 sizes 结构，选择 1 个输出、2 个输入。其中一个输入为误差信号，另一个输入为误差信号上一时刻的值。S 函数嵌入在 Simulink 程序中，采样时间为 1ms。仿真结果如图 1-12 所示。

![](image/6a7a28606644c977d599b78e278fb0858c290e887ac51d3acf8c2814f45f024e.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | 1.0 | 1.0 |
| 0.4 | 0.0 | 0.0 |
| 0.6 | -1.0 | -1.0 |
| 0.8 | 0.0 | 0.0 |
| 1.0 | 1.0 | 1.0 |
| 1.2 | 0.0 | 0.0 |
| 1.4 | -1.0 | -1.0 |
| 1.6 | 0.0 | 0.0 |
| 1.8 | 1.0 | 1.0 |
| 2.0 | 0.0 | 0.0 |
</details>

图 1-12 PID 正弦跟踪
