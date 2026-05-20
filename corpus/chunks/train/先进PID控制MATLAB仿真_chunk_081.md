# 【仿真之二】采用 S 函数进行 Simulink 仿真

不确定对象的表示、控制器的实现及输出由 S 函数完成。

被控对象为

$$G (s) = \frac {K}{s ^ {2} + J s}$$

被控对象的描述方式可转换为

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - J x _ {2} + K u$$

在 S 函数中，采用初始化、微分函数和输出函数，即 mdlInitializeSizes 函数、mdlDerivatives 函数和 mdlOutputs 函数。在初始化中采用 sizes 结构，选择 1 个输出。3 个输入，3 个输入实现了 P、I、D 三项的输入。S 函数嵌入在 Simulink 程序中。系统初始状态为： $x(0)=0,\quad\dot{x}(0)=0$ 。取 $k_{p}=10,\quad k_{i}=2,\quad k_{d}=1$ ，仿真结果如图 1-7 所示。

![](image/bef8ab730dd349d7a3f8908e2dfef5628d84f9b5b51b2ef026844d785e379960.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | 0.5 | 0.5 |
| 0.4 | 0.3 | 0.3 |
| 0.6 | -0.1 | -0.1 |
| 0.8 | -0.5 | -0.5 |
| 1.0 | -0.3 | -0.3 |
| 1.2 | 0.5 | 0.5 |
| 1.4 | 0.3 | 0.3 |
| 1.6 | -0.1 | -0.1 |
| 1.8 | -0.5 | -0.5 |
| 2.0 | 0.0 | 0.0 |
</details>

图 1-7 正弦响应
