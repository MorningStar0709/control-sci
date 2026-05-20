# 【仿真之一】基于 Riccati 方程的 $H_{\infty}$ 控制

为了求解 Riccati 方程式（16.10），按 MATLAB 求解 $H_{\infty}$ 控制的 Riccati 方程帮助信息，需要将其转化为

$$
\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {X} + \boldsymbol {X} \boldsymbol {A} - \boldsymbol {X} \left[ \begin{array}{l l} \boldsymbol {B} _ {1} & \boldsymbol {B} _ {2} \end{array} \right] \left[ \begin{array}{l l} - \boldsymbol {I} & 0 \\ 0 & \boldsymbol {I} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {B} _ {1} ^ {\mathrm{T}} \\ \boldsymbol {B} _ {2} ^ {\mathrm{T}} \end{array} \right] \boldsymbol {X} + \boldsymbol {C} _ {1} ^ {\mathrm{T}} \boldsymbol {C} _ {1} = 0
$$

为了保证 $A + \left(B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}}\right)X$ 具有稳定的半正定解 $X \geqslant 0$ ，取 $B_{1} = \left[0 \quad 0 \quad 0.1 \quad 0.1\right]^{\mathrm{T}}$ 。取 $B = \left[B_{1} \quad B_{2}\right]$ ， $R = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ ， $C = C_{1}$ ， $X = \operatorname{care}(A, B, C^{\mathrm{T}}C, R)$ ，则可得到 $X \geqslant 0$ 的解，将 $X$ 代入可验证 $A + \left(B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}}\right)X$ 的稳定性，可知其特征值全在负半面。

运行仿真程序 chap16\_2riccati.m，由式（16.11）可得控制器增益 $K = -B_{2}^{T}X = [29.0040\ 1.0395\ 5.3031\ 2.2403]$ 。采用控制律式（16.12），倒立摆响应结果及控制器输出如图 16-1～图 16-3 所示。

![](image/9c9a233be85c417ab7232aa041ce7ebf416be323f5bb74b6ce6f361e47f87213.jpg)

图 16-1 摆的角度和角速度响应（Riccati 方程）  
![](image/e61ffd08cf004983dca2c8e40c08d6bff2da200904e405516a7f8875b333f93c.jpg)

<details>
<summary>line</summary>

| time(s) | Angle speed response of link |
| --- | --- |
| 0 | 2.0 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

![](image/ad2904a8fdb584efec82ffc131d444b6a76a9fdf9c08436b1eb44d7779a374f8.jpg)

<details>
<summary>line</summary>

| time(s) | Position speed response of cart |
| --- | --- |
| 0 | -1.5 |
| 5 | 0.4 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

图 16-2 小车的角度和角速度响应（Riccati 方程）

![](image/a8ea55643acd72425a7a42e56a6b36ef4ee031244c6b74d998f771698933eda2.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | 2 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
| 25 | 0 |
| 30 | 0 |
</details>

图 16-3 控制输入（Riccati 方程）
