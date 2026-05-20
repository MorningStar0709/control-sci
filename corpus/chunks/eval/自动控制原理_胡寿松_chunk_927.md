# (1) 里卡蒂方程的求解

在系统最优控制的设计过程中,经常会需要求解里卡蒂方程,MATLAB的控制工具箱提供了专门的命令函数来求解。

命令格式: $[P,1,g]=\text{care}(A,B,Q,R)$

其中，P 就是里卡蒂方程

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} - \boldsymbol {P B R} ^ {- 1} \boldsymbol {B} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {Q} = 0$$

的解。

![](image/939a38abf2dd38b03a98077fbe53c93ff94a4369e6f9ccb3b23096e6847647db.jpg)

<details>
<summary>line</summary>

| Time/sec | e(t) |
| --- | --- |
| 0.0 | 1.8 |
| 0.5 | -1.0 |
| 1.0 | 0.0 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

图 B-25 状态误差响应曲线
