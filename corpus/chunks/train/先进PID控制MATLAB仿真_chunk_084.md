# 1.3.1 位置式 PID 控制算法

按模拟 PID 控制算法，以一系列的采样时刻点 kT 代表连续时间 t，以矩形法数值积分近似代替积分，以一阶后向差分近似代替微分，即

$$
\left\{ \begin{array}{l} t \approx k T \quad (k = 0, 1, 2, \dots) \\ \int_ {0} ^ {t} \operatorname{error} (t) \mathrm{d} t \approx T \sum_ {j = 0} ^ {k} \operatorname{error} (j T) = T \sum_ {j = 0} ^ {k} \operatorname{error} (j) \\ \frac {\operatorname{derror} (t)}{\mathrm{d} t} \approx \frac {\operatorname{error} (k T) - \operatorname{error} ((k - 1) T)}{T} = \frac {\operatorname{error} (k) - \operatorname{error} (k - 1)}{T} \end{array} \right. \tag {1.4}
$$

可得离散 PID 表达式

$$
\begin{array}{l} u (k) = k _ {\mathrm{p}} (\text { error } (k) + \frac {T}{T _ {\mathrm{I}}} \sum_ {j = 0} ^ {k} \text { error } (j) + \frac {T _ {\mathrm{D}}}{T} (\text { error } (k) - \text { error } (k - 1))) \\ = k _ {\mathrm{p}} \operatorname{error} (k) + k _ {\mathrm{i}} \sum_ {j = 0} ^ {k} \operatorname{error} (j) T + k _ {\mathrm{d}} \frac {\operatorname{error} (k) - \operatorname{error} (k - 1)}{T} \\ \end{array}
$$

式中， $k_{i}=\frac{k_{p}}{T_{I}}$ ; $k_{d}=k_{p}T_{D}$ ; T 为采样周期；k 为采样序号， $k=1,2,\cdots$ ; error(k-1) 和 error(k) 分别为第 $(k-1)$ 和第 k 时刻所得的偏差信号。

位置式 PID 控制系统如图 1-8 所示。

根据位置式 PID 控制算法得到其程序框图如图 1-9 所示。

![](image/7720a9b1b05b343a0ef2cf45764042e03d28b4d2daa4d02f59657ec2569294b5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["y_d(k)"] --> B["+"]
    B --> C["PID 控制算法"]
    C --> D["D/A"]
    D --> E["执行机构"]
    E --> F["被控对象"]
    F --> G["y(k)"]
    G --> H["-"]
    H --> B
```
</details>

图 1-8 位置式 PID 控制系统

![](image/2d58733cac6a5e4deae7c29277f6874cd92d3ef1b080d38697c01b968877fba6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["开始"] --> B["参数初始化"]
    B --> C["采入y_d(k)及y(k)"]
    C --> D["计算偏差值"]
    D --> E["计算控制器输出"]
    E --> F["参数更新"]
    F --> G["返回"]
```
</details>

图 1-9 位置式 PID 控制算法程序框图

在仿真过程中，可根据实际情况，对控制器的输出进行限幅： $[-10, +10]$ 。

![](image/7ba4c6bbff0099121f917e6ae0fbcc34721ab2875f696dba73056adecb25ba2d.jpg)
