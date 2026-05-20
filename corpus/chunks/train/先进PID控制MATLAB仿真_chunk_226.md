# 【仿真方法二】

采用 Simulink 进行数字化仿真，按 Smith 算法设计 Simulink 模块。在 PI 控制中， $k_{p}=0.5$ ， $k_{i}=0.01$ 。其响应结果如图 3-23 和图 3-24 所示。

![](image/16a10a3ec610f3e5793db584d2bd8e9974a509b816a5131bd23a9fd0829bbf32.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 200 | 1.0 | 0.8 |
| 400 | 1.0 | 1.0 |
| 600 | 1.0 | 1.0 |
| 800 | 1.0 | 1.0 |
| 1000 | 1.0 | 1.0 |
| 1200 | 1.0 | 1.0 |
| 1400 | 1.0 | 1.0 |
| 1600 | 1.0 | 1.0 |
| 1800 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
</details>

图 3-23 Smith 阶跃响应结果

![](image/b9f5e8c39ec7074d947d8670636a37db07adf3d01d773564f005bb02f835837b.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 200 | 1.0 | 1.45 |
| 400 | 1.0 | 0.8 |
| 600 | 1.0 | 1.1 |
| 800 | 1.0 | 1.05 |
| 1000 | 1.0 | 1.0 |
| 1200 | 1.0 | 1.0 |
| 1400 | 1.0 | 1.0 |
| 1600 | 1.0 | 1.0 |
| 1800 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
</details>

图 3-24 只采用 PI 控制时的阶跃响应结果
