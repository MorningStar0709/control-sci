$$y _ {1} ^ {*} = \cos (t), y _ {2} ^ {*} = 2 \sin (t) \tag {6.1.13}$$

所得的仿真结果如图6.1.3所示.在这里控制器的参数是和前面的完全相同,只是由于要跟踪时变轨迹,安排过渡过程的参数 $r_{0}$ 取得大一些.

![](image/4c494feb8386e59db235ceeaa6f4775cf4b081ea182477a2b26859778f5d838e.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 5 | -1.0 |
| 10 | 0.0 |
| 15 | -1.0 |
| 20 | 1.0 |
</details>

![](image/731a247bd5e885c33dba39af96a4da54e7c3eb1ab73f513f3c00443060ce26fc.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 5 | -2 |
| 10 | 0 |
| 15 | -2 |
| 20 | 0 |
</details>

![](image/697639191c076c1daa825474bc09e95962e302b9686b360e2c512833e3d80a91.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 5 | 5.0 |
| 10 | 0.0 |
| 15 | 5.0 |
| 20 | 0.0 |
</details>

![](image/5fe2df2a0c868b40a7cb32d6a0facf5e317866e8503820a7954d660a22b116ac.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 4.0 |
| 5 | 1.0 |
| 10 | 5.0 |
| 15 | 3.0 |
| 20 | 4.0 |
</details>

图6.1.3

如果“静态耦合”矩阵 $B(t)$ 的奇异性只在个别离散时刻上出现,如

$$
\boldsymbol {B} (t) = \left[ \begin{array}{c c} \cos (0. 9 t) & \sin (0. 8 t) \\ \sin (t) & \cos (0. 7 t) \end{array} \right] \tag {6.1.14}
$$

那么其行列式和逆矩阵的表达式为

$$
\mathrm{bb} (t) = \cos (0. 9 t) \cos (0. 7 t) - \sin (0. 8 t) \sin (t) \tag {6.1.15}
\boldsymbol {B} ^ {- 1} (t) = \frac {1}{\mathrm{bb}} \left[ \begin{array}{c c} \cos (0. 7 t) & - \sin (0. 8 t) \\ - \sin (t) & \cos (0. 9 t) \end{array} \right] \tag {6.1.16}
$$

但行列式 $\mathrm{bb}(t)$ 的曲线如图6.1.4所示.此曲线过0的时刻矩阵 $\pmb {B}(t)$ 都是不可逆的，但是每个采样时刻 $\mathrm{bb(kh)}$ 不一定等于零，因此在采样时刻上矩阵 $\pmb {B}(t)$ 是可逆的.

对系统(6.1.5)的静态耦合矩阵(6.1.6)换成矩阵(6.1.14)所作的仿真结果如图6.1.5所示.

以上是静态耦合矩阵 $B(t)$ 完全已知的假定下进行的仿真.

![](image/cc7513256bacb29efabd15a9c55bb847c461bdc756479abb2c664bd0e2104ff5.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 5 | -1.0 |
| 10 | 0.5 |
| 15 | -0.5 |
| 20 | 0.0 |
| 25 | -1.0 |
| 30 | 0.5 |
| 35 | -1.0 |
| 40 | 0.0 |
</details>

图6.1.4  
![](image/8671af94a934c1328e9ccd232242924666fbbfa3c8632e2312eccd51191a34e2.jpg)

<details>
<summary>line</summary>

| x | y1 (v₀₁v₁) | y2 (v₀₂v₂) | y3 (fᵢ,π₁₁) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 10 | -2 | 2 | 1 |
| 20 | 0 | 0 | 0 |
| 30 | -2 | 2 | 1 |
| 40 | 0 | 0 | 0 |
</details>

图6.1.5

如果我们不完全知道静态耦合矩阵 $B(t)$ 的真值, 只知道其近似矩阵 $B_{0}$ , 那么式(6.1.12) 只能改成

$$
\left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] = \boldsymbol {B} _ {0} ^ {- 1} \left[ \begin{array}{l} U _ {1} \\ U _ {2} \end{array} \right] \tag {6.1.17}
$$
