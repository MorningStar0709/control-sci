# 例 5-19 磁盘驱动读取系统（续）

图1-16所示的磁盘驱动器是用弹性簧片来悬挂磁头的。当考虑簧片的弹性影响时，磁头位置控制系统如图5-57所示。磁头与簧片的典型参数： $\zeta = 0.3,\omega_{n} = 18.85\times 10^{3}\mathrm{rad / s}$ 。要求确定开环增益 $K = 100$ 时，磁盘驱动读取系统的幅值裕度 $h(\mathrm{dB})$ 、相角裕度 $\gamma$ 及闭环系统的带宽频率 $\omega_{b}$ ，并估算系统单位阶跃响应的 $\sigma \%$ 和 $t_s$ 。

![](image/fcf5865999443431c515a1a0800e410a385e29ea44528539434ced4129e6831b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["PD控制器 Gc(s)"]
    C --> D["K1(s+1)"]
    D --> E["电机线圈 G1(s)"]
    E --> F["1/(T1s+1)"]
    F --> G["T1=10^-3s"]
    G --> H["支撑臂 G2(s)"]
    H --> I["0.05/(T2s+1)"]
    I --> J["T2=1/20s"]
    J --> K["磁头与簧片 G3(s)"]
    K --> L["C(s)"]
    L --> M["反馈"]
    M --> B
    style A fill:#f9f,stroke:#333
    style L fill:#ccf,stroke:#333
```
</details>

图 5-57 磁头位置控制系统(包括簧片的弹性影响)

解 取 $K_{1}=2000$ ，则开环增益 K=100，根据对数幅频特性表达式

$$2 0 \lg | K _ {1} (\mathrm{j} \omega + 1) G _ {1} (\mathrm{j} \omega) G _ {2} (\mathrm{j} \omega) G _ {3} (\mathrm{j} \omega) |$$

在一些选定的频率点上，画出开环系统对数幅频渐近特性，如图5-58所示。由图可见，在簧片自然频率 $\omega_{n}$ 附近，幅频特性曲线比渐近线高约5dB。

![](image/8abe31b8f403bc5d60ae44ba1fc63c9dd0a217bcfdcfc0d8717b008751746aa8.jpg)

<details>
<summary>line</summary>

| Frequency (ω) | Value (dB) |
| --- | --- |
| ω_r=1 | 60 |
| ω_2 | 40 |
| ω_1 | 20 |
| ω_1000 | -20 |
| ω_n | -80 |
</details>

图 5-58 磁盘驱动读取系统开环对数幅频特性

利用 MATLAB 软件包, 可以画出开环系统的对数频率特性, 如图 5-59 所示。由图 5-59 可以确定: $h(\mathrm{dB}) = 22.8\mathrm{dB}, \gamma = 37.3^{\circ}, \omega_{c} = 1200\mathrm{rad/s}$ 。

为了确定闭环系统带宽频率 $\omega_{b}$ ，绘制磁盘驱动读取系统准确的闭环对数幅频特性，如图 5-60所示。由图5-60可以确定 $\omega_{b} = 2000\mathrm{rad / s}$ 。显然，只要取 $K_{1} = 2000$ ，簧片自然频率 $\omega_{n}$ 及 $\omega_{n}$ 附近的系统谐振频率 $\omega_{r}$ 就会位于闭环带宽 $\omega_{b}$ 之外，从而使簧片弹性对系统动态性能的影响甚微。

![](image/0a8a5884f9e9aab134c3808bf25f93e5e8fb025251e0330ac7217d8bae7477bf.jpg)

图 5-59 磁盘驱动读取系统开环对数频率特性图 (MATLAB)  
![](image/de1fa0bad993e0128b5ad73c3f34ca08f7f5cfb80c86c77f7dbf892dca6df123.jpg)

<details>
<summary>line</summary>

| ω/(rad/s) | 20lgΦ/dB | α(°) |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 1 | 0 | 0 |
| 10 | 0 | 0 |
| 100 | 0 | 0 |
| 1000 | -50 | -90 |
| 10000 | -150 | -180 |
| 100000 | -250 | -270 |
| 1000000 | -360 | -360 |
</details>

图 5-60 磁盘驱动读取系统闭环对数频率特性(MATLAB)

系统单位阶跃响应的动态性能指标,可以利用下列式子估算:
