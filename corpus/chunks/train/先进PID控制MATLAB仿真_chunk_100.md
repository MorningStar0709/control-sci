# 1.3.5 积分分离 PID 控制算法及仿真

在普通 PID 控制中引入积分环节的目的，主要是为了消除静差，提高控制精度。但在过程的启动、结束或大幅度增减设定时，短时间内系统输出有很大的偏差，会造成 PID 运算的积分积累，致使控制量超过执行机构可能允许的最大动作范围对应的极限控制量，引起系统较大的超调，甚至引起系统较大的振荡。这在生产中是绝对不允许的。

积分分离控制基本思路是：当被控量与设定值偏差较大时，取消积分作用，以免由于积分作用使系统稳定性降低，超调量增大；当被控量接近给定值时，引入积分控制，以便消除静差，提高控制精度。其具体实现步骤如下：

（1）根据实际情况，人为设定阈值 $\varepsilon>0$ ；  
(2) 当 $\left|\text{error}(k)\right| > \varepsilon$ 时，采用 PD 控制，可避免产生过大的超调，又使系统有较快的响应；  
（3）当 $\left|\text{error}(k)\right| \leqslant \varepsilon$ 时，采用PID控制，以保证系统的控制精度。

积分分离控制算法可表示为

$$u (k) = k _ {\mathrm{p}} \operatorname{error} (k) + \beta k _ {\mathrm{i}} \sum_ {j = 0} ^ {k} \operatorname{error} (j) T + k _ {\mathrm{d}} (\operatorname{error} (k) - \operatorname{error} (k - 1)) / T \tag {1.8}$$

式中，T 为采样时间； $\beta$ 为积分项的开关系数。

$$
\beta = \left\{ \begin{array}{l l} 1 & | \text { error } (k) | \leqslant \varepsilon \\ 0 & | \text { error } (k) | > \varepsilon \end{array} \right. \tag {1.9}
$$

根据积分分离式 PID 控制算法得到其程序框图如图 1-22 所示。

![](image/5a1a26df64c7c898d6ca27b592f8a99f512c2e09e5b3b66dfd3925d9d2cfaf41.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["开始"] --> B["参数初始化"]
    B --> C["采入y_d(k)及y(k)"]
    C --> D["计算偏差值 error(k)"]
    D --> E{error(k)≤ε?}
    E -->|是| F["PID控制"]
    E -->|否| G["PD控制"]
    F --> H["控制器输出"]
    G --> H
    H --> I["参数更新"]
    I --> J["返回"]
```
</details>

图 1-22 积分分离式 PID 控制算法程序框图
