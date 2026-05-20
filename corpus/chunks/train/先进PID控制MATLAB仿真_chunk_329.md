# 6.4.2 仿真实例

被控对象为

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

取位置指令为1.0，采用控制律式（6.7），控制律参数按参考文献[2,4]，取采样时间为 $h = 0.001$ ， $\alpha_{1} = \frac{3}{4}$ ， $\alpha_{2} = \frac{3}{2}$ ， $\delta = 2h$ ， $\beta_{1} = 150$ ， $\beta_{2} = 1.0$ ，仿真结果如图6-14所示。如果采用线性PD控制， $k_{\mathrm{p}}$ 和 $k_{\mathrm{d}}$ 不变，仿真结果如图6-15所示。

![](image/065ccf5f8c5fbc1af285f80a61ad52daf3841b6dc8858136f32d7e3065b208f0.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 0.0 |
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

![](image/ca4b67bb0d335fa2158edeebb12a56904ee27f98370ab5739919a7e69f7368f1.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking error |
| --- | --- |
| 0.0 | 1.0 |
| 0.1 | 0.0 |
| 0.2 | 0.0 |
| 0.3 | 0.0 |
| 0.4 | 0.0 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
| 0.9 | 0.0 |
| 1.0 | 0.0 |
</details>

图 6-14 非线性 PID 控制阶跃响应 (M=1)

![](image/e3e8784ca1a81fa1d8dd3de452a7fefacd81450bde93d5e0c463c9bcc949c709.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 1.0 |
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

![](image/a1e40ab335ba9eb872595c3c57dcdc1673860a69d7b163fa2c2495d5c21fc180.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking error |
| --- | --- |
| 0.0 | 1.0 |
| 0.1 | 0.0 |
| 0.2 | 0.0 |
| 0.3 | 0.0 |
| 0.4 | 0.0 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
| 0.9 | 0.0 |
| 1.0 | 0.0 |
</details>

图 6-15 线性 PID 控制阶跃响应 (M=2)
