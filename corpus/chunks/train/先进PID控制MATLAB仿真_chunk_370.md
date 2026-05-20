# 7.4.3 仿真实例

设被控对象为 $\frac{133}{s^2 + 25s}$ ，指令为一大的阶跃信号10，控制输入限制在[0,10]范围内，分别采用控制器（7.19）和传统PID进行仿真。仿真中，当取 $M = 1$ 时为基于Anti-windup的PID控制，当 $M = 2$ 时为传统PID控制。针对连续系统，采用Simulink方式进行仿真，取 $\alpha = 1.0$ ， $k_{\mathrm{p}} = 50$ ， $k_{\mathrm{i}} = 10$ ， $k_{\mathrm{d}} = 1$ 。仿真结果如图7-9～图7-12所示。

![](image/e59c61a908a83056748b0b6bf3f85c9594dadfb2019571bfded36e6820eb9106.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 10.0 | 10.0 |
| 1.0 | 10.0 | 10.0 |
| 1.5 | 10.0 | 10.0 |
| 2.0 | 10.0 | 10.0 |
| 2.5 | 10.0 | 10.0 |
| 3.0 | 10.0 | 10.0 |
</details>

![](image/33aec7c7394f192faced2d7482a0847bcfe4d9146304ba63805333dc68021cd1.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking error |
| --- | --- |
| 0.0 | 10.0 |
| 0.5 | 0.0 |
| 1.0 | 0.0 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
</details>

图 7-9 基于 Anti-windup 的阶跃响应

![](image/1b2dc246a3801aadaf28a62bade00044f6c03633120b22443be58d84db6fa6dd.jpg)

<details>
<summary>line</summary>

| time(s) | before saturation | after saturation |
| --- | --- | --- |
| 0.0 | 500.0 | 0.0 |
| 0.5 | -50.0 | 0.0 |
| 1.0 | -20.0 | 0.0 |
| 1.5 | -10.0 | 0.0 |
| 2.0 | -5.0 | 0.0 |
| 2.5 | -2.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
</details>

图 7-10 基于 Anti-windup 的控制器输出

![](image/f46132ddbc6fd14cc0561dc5c7f25e45f060a5a78aea8e77589f6b61262ace11.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 11.0 | 11.0 |
| 1.0 | 11.0 | 11.0 |
| 1.5 | 11.0 | 11.0 |
| 2.0 | 11.0 | 11.0 |
| 2.5 | 11.0 | 11.0 |
| 3.0 | 11.0 | 11.0 |
</details>

![](image/3541f41eea6a21112887b9f606382190144fb54ac9af60d3affce30110e3d483.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking error |
| --- | --- |
| 0.0 | 10.0 |
| 0.5 | 0.0 |
| 1.0 | 0.0 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
</details>

图 7-11 基于传统 PID 的阶跃响应

![](image/1f113dba1133df14a12bba8339d83491276230a1d4c2dc9ac73dd518f8e0f28d.jpg)

<details>
<summary>line</summary>

| time(s) | before saturation | after saturation |
| --- | --- | --- |
| 0.0 | 500 | 0 |
| 0.5 | -50 | 0 |
| 1.0 | -60 | 0 |
| 1.5 | -70 | 0 |
| 2.0 | -80 | 0 |
| 2.5 | -90 | 0 |
| 3.0 | -100 | 0 |
</details>

图 7-12 传统 PID 方法的控制器输出
