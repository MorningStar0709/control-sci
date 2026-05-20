# 3. 定义隶属函数

选用如下三角形隶属函数可实现污泥的模糊化。

$$
\mu_ {\mathrm{污泥}} = \left\{ \begin{array}{l l} \mu_ {\mathrm{SD}} (x) = (5 0 - x) / 5 0 & 0 \leqslant x \leqslant 5 0 \\ \mu_ {\mathrm{MD}} (x) = \left\{ \begin{array}{l l} x / 5 0 & 0 \leqslant x \leqslant 5 0 \\ (1 0 0 - x) / 5 0 & 5 0 <   x \leqslant 1 0 0 \end{array} \right. \\ \mu_ {\mathrm{LD}} (x) = (x - 5 0) / 5 0 & 5 0 <   x \leqslant 1 0 0 \end{array} \right.
$$

采用 Matlab 进行仿真, 污泥隶属函数设计仿真程序见附录程序 chap4\_4.m, 仿真结果如图 4-14 所示。

![](image/4e30d5380c10f7b17e4ca7ec0c388e61e0e03a3069950096f0f2ebc4bdc240e2.jpg)

<details>
<summary>line</summary>

| 污泥质量 x (g) | Degree of membership |
| --- | --- |
| 0 | 1.0 |
| 20 | 0.6 |
| 50 | 0.0 |
| 70 | 0.6 |
| 90 | 1.0 |
| 100 | 1.0 |
</details>

图 4-14 污泥隶属函数

选用如下三角形隶属函数实现油脂的模糊化,如图 4-15 所示。

$$
\mu_ {\text {油脂}} = \left\{ \begin{array}{l l} \mu_ {\mathrm{NG}} (y) = (5 0 - y) / 5 0 & 0 \leqslant y \leqslant 5 0 \\ \mu_ {\mathrm{MG}} (y) = \left\{ \begin{array}{l l} y / 5 0 & 0 \leqslant y \leqslant 5 0 \\ (1 0 0 - y) / 5 0 & 5 0 <   y \leqslant 1 0 0 \end{array} \right. \\ \mu_ {\mathrm{LG}} (y) = (y - 5 0) / 5 0 & 5 0 <   y \leqslant 1 0 0 \end{array} \right.
$$

仿真程序同 chap4\_4.m。

![](image/9b0c17084ecfee6c213fe3721c0ac2d5308455ac875a608dd0196bbd0e8b86f4.jpg)

<details>
<summary>line</summary>

| 油脂质量 y (g) | Degree of membership |
| --- | --- |
| 0 | 1.0 |
| 20 | 0.5 |
| 50 | 0.0 |
| 70 | 0.5 |
| 100 | 1.0 |
</details>

图 4-15 油脂隶属函数

选用如下三角形隶属函数实现洗涤时间的模糊化,如图 4-16 所示。

$$
\mu_ {\mathrm{洗涤时间}} = \left\{ \begin{array}{l l} \mu_ {\mathrm{VS}} (z) = (1 0 - z) / 1 0 & 0 \leqslant z \leqslant 1 0 \\ \mu_ {\mathrm{S}} (z) = \left\{ \begin{array}{l l} z / 1 0 & 0 \leqslant z \leqslant 1 0 \\ (2 5 - z) / 1 5 & 1 0 <   z \leqslant 2 5 \end{array} \right. \\ \mu_ {\mathrm{M}} (z) = \left\{ \begin{array}{l l} (z - 1 0) / 1 5 & 1 0 \leqslant z \leqslant 2 5 \\ (4 0 - z) / 1 5 & 2 5 <   z \leqslant 4 0 \end{array} \right. \\ \mu_ {\mathrm{L}} (z) = \left\{ \begin{array}{l l} (z - 2 5) / 1 5 & 2 5 \leqslant z \leqslant 4 0 \\ (6 0 - z) / 2 0 & 4 0 <   z \leqslant 6 0 \end{array} \right. \\ \mu_ {\mathrm{VL}} (z) = (z - 4 0) / 2 0 & 4 0 \leqslant z \leqslant 6 0 \end{array} \right.
$$

![](image/81de60099259a5c0b35c7160d86d46fe1c7d06bbd26022c3a28323b381997b23.jpg)

<details>
<summary>line</summary>

| 洗涤时间 z (min) | VS | S | M | L | VL |
| --- | --- | --- | --- | --- | --- |
| 0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 10 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 |
| 20 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 |
| 30 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |
| 40 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| 50 | 0.0 | 0.0 | 0.0 | 0.5 | 0.5 |
| 60 | 1.0 | 0.0 | 0.0 | 1.0 | 1.0 |
</details>

图4-16 洗涤时间隶属函数

采用 Matlab 仿真, 可实现洗涤时间隶属函数的设计, 洗涤时间隶属函数的设计仿真程序见本章附录程序 chap4\_5.m。
