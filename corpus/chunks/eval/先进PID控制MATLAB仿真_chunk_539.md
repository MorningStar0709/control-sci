# 13.4.3 仿真实例

动力学模型取式（13.38）～式（13.40），模型参数取 $\rho=0.2211,\quad EI=2,\quad m=6.78$ ，L=0.60， $I_{h}=0.0139$ 。角度指令取 $\theta_{d}=0.5$ ，采用控制律式（13.44）和式（13.45），取 $k_{p}=30,\quad k_{d}=50,\quad k=10$ 。两个坐标轴按 nx=10，nt=40000 划分区间，仿真时间为 20。仿真结果如图 13-9～图 13-12 所示。

![](image/b0766a433186ca02655f7fa14abcb7f09aa45527c9e05a7185f4eb82e74df0b5.jpg)

<details>
<summary>line</summary>

| time(s) | thd | th |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | 0.5 | 0.5 |
| 10 | 0.5 | 0.5 |
| 15 | 0.5 | 0.5 |
| 20 | 0.5 | 0.5 |
| 25 | 0.5 | 0.5 |
</details>

![](image/30339b1981a43cca572e469196769cc2ef5dc1a08f53ed0e985c4aeb00d976e1.jpg)

<details>
<summary>line</summary>

| Time (s) | Angle speed response (rad/s) |
| --- | --- |
| 0 | 0.3 |
| 5 | 0.05 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
</details>

图 13-9 角度和角速度的响应

![](image/e66e779c57471cece80871ba2eeb8405a51464d9400269991169b5af5d2bf2fd.jpg)

<details>
<summary>surface_3d</summary>

| time(s) | deflection,y(x,t) |
| --- | --- |
| 0.6 | -0.1 |
| 0.4 | -0.05 |
| 0.2 | 0.0 |
| 0 | 0.05 |
| 5 | 0.1 |
| 10 | 0.1 |
| 15 | 0.1 |
| 20 | 0.1 |
</details>

![](image/d8858952db35cd1ab1ed053d86351862918a2e3ea785bba2fb8841b03cd22236.jpg)

<details>
<summary>surface_3d</summary>

| Time (s) | Deflection rate, dy(x,t) (m/s) |
| --- | --- |
| 0.6 | -0.2 |
| 0.4 | -0.1 |
| 0.2 | 0.0 |
| 0 | 0.1 |
| 5 | 0.2 |
| 10 | 0.2 |
| 15 | 0.2 |
| 20 | 0.2 |
</details>

图 13-10 机械臂上的分布式的弹性形变及变化率

![](image/65ff5588a3604c2ffe4878dd32c28ec93e0ff9c8fc97d792c0d24f8461d76c9d.jpg)

<details>
<summary>line</summary>

| Time (s) | y(L,t) |
| --- | --- |
| 0 | 0.0 |
| 1 | -0.07 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
| 11 | 0.0 |
| 12 | 0.0 |
| 13 | 0.0 |
| 14 | 0.0 |
| 15 | 0.0 |
| 16 | 0.0 |
| 17 | 0.0 |
| 18 | 0.0 |
| 19 | 0.0 |
| 20 | 0.0 |
</details>

![](image/62db8e9b4017af3d115715b9cfe88954cf5979873a3bf31e60be4ed82cd97f5a.jpg)

<details>
<summary>line</summary>

| Time (s) | y(x,t) at half of L (x 10⁻³) |
| --- | --- |
| 0 | -15 |
| 2 | 0 |
| 4 | -1 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| 18 | 0 |
| 20 | 0 |
</details>

图 13-11 机械臂上的弹性形变（x=0.5L 及 x=L 处）

![](image/22a2dcb0f47683abda1dca1af78e3e5eac68c6971a025c95adae49a47a8f0e2c.jpg)

<details>
<summary>line</summary>

| Time (s) | control input, tol |
| --- | --- |
| 0 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
</details>

![](image/1dd67f3b3eef71267b0d82c3084c8f4f18312ee7fafd023724a4f0b639101d4b.jpg)

<details>
<summary>line</summary>
