# 【仿真之三】采用 Simulink 实现离散 PID 控制器

离散 PID 控制的封装界面如图 1-19 所示，在该界面中可设定 PID 的三个系数、采样时间及控制输入的上下界。仿真结果如图 1-20 所示。

![](image/76954249ca519433ac1bf387f378ee04b65a3b980407a529641110286dd673b0.jpg)

<details>
<summary>text_image</summary>

Function Block Parameters: Normal Discrete PID...
Subsystem (mask)
Parameters
Proportional Kp
0.5
Integrator Ki
0.001
Derivative Kd
0.001
Sampling period T
0.001
Actuator Limit
10
OK	Cancel	Help	Apply
</details>

图 1-19 离散 PID 控制的封装界面

![](image/3992e2fabc957e297851a726f5e7da320fc368f16b53a65cb51f35da96891de9.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 1.0 | 1.0 |
| 0.2 | 1.0 | 1.0 |
| 0.3 | 1.0 | 1.0 |
| 0.4 | 1.0 | 1.0 |
| 0.5 | 1.0 | 1.0 |
| 0.6 | 1.0 | 1.0 |
| 0.7 | 1.0 | 1.0 |
| 0.8 | 1.0 | 1.0 |
| 0.9 | 1.0 | 1.0 |
| 1.0 | 1.0 | 1.0 |
</details>

图 1-20 阶跃响应结果
