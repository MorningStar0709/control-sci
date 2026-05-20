# 9.3.3 仿真实例

被控对象取单级倒立摆，其动态方程如下：

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (\boldsymbol {x}) + g (\boldsymbol {x}) u \\ \end{array}
$$

式中， $f(x)=\frac{g\sin x_{1}-mlx_{2}^{2}\cos x_{1}\sin x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $g(x)=\frac{\cos x_{1}/(m_{c}+m)}{l(4/3-m\cos^{2}x_{1}/(m_{c}+m))}$ ； $x_{1}$ 和 $x_{2}$ 分别为摆角和摆速； $g=9.8m/s^{2}$ ； $m_{c}$ 为小车质量， $m_{c}=1kg$ ； m 为摆杆质量， $m=0.1kg$ ； l 为摆长的一半， $l=0.5m$ ； u 为控制输入。

摆的角度指令为 $y_{\mathrm{d}}(t)=0.1\sin t$ ，倒立摆初始状态为 $[\pi/60,0]$ 。取 RBF 网络结构为 2-5-1。RBF 网络高斯基函数参数的取值对神经网络控制的作用很重要，如果参数取值不合适，将使高斯基函数无法得到有效的映射，从而导致 RBF 网络无效。故 $c_{ij}$ 按网络输入值的范围取值，取 $c=\begin{bmatrix}-0.2&-0.1&0&0.1&0.2\\-0.2&-0.1&0&0.1&0.2\end{bmatrix}$ ， $\sigma_{j}=0.50,\quad i=2,\quad j=5$ ，神经网络权值初始值取 0。

采用控制律（9.17），自适应律取（9.19），取 $Q=\begin{bmatrix}500&0\\ 0&500\end{bmatrix},\quad k_{d}=20,\quad k_{p}=10$ ，自适应参数取 $\gamma=100$ 。仿真结果如图9-8～图9-10所示。

![](image/3e34f8a11906b8b1f42c9b4f612ad986e3d2e6285eebb7aa206598cb21789498.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0 | 0.1 | 0.1 |
| 5 | -0.1 | -0.1 |
| 10 | 0.1 | 0.1 |
| 15 | -0.1 | -0.1 |
| 20 | 0.1 | 0.1 |
| 25 | -0.1 | -0.1 |
| 30 | 0.1 | 0.1 |
</details>

![](image/206b251e5b45669ae67f10788685346e25f99dc8d9443c8e387b93a224cd7d86.jpg)

<details>
<summary>line</summary>

| time(s) | ideal speed | speed tracking |
| --- | --- | --- |
| 0 | 0.1 | 0.05 |
| 5 | -0.1 | -0.05 |
| 10 | 0.1 | 0.05 |
| 15 | -0.1 | -0.05 |
| 20 | 0.1 | 0.05 |
| 25 | -0.1 | -0.05 |
| 30 | 0.1 | 0.05 |
</details>

图 9-8 角度和角速度跟踪

![](image/0b3c7d08864844c7f727f7b53995865ed5807dff781b69119ac1bd050da52c23.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | -0.6 |
| 5 | 1.2 |
| 10 | 1.2 |
| 15 | 1.2 |
| 20 | 1.2 |
| 25 | 1.2 |
| 30 | 1.2 |
</details>

图 9-9 控制输入信号

![](image/f4a212adf164da45ea0e61c63045283a397537e3695f153030d6d86fdf0eff51.jpg)

<details>
<summary>line</summary>

| time(s) | Practical fx | fx estimation |
| --- | --- | --- |
| 0 | 1.0 | 2.8 |
| 5 | -1.5 | -1.5 |
| 10 | -1.5 | -1.5 |
| 15 | -1.5 | -1.5 |
| 20 | -1.5 | -1.5 |
| 25 | -1.5 | -1.5 |
| 30 | -1.5 | -1.5 |
</details>

图9-10 $f(x)$ 及 $\hat{f} (x)$ 的变化
