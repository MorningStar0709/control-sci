# 2. 微分器信号处理

输入信号取 $v(t)=\sin t$ ，则可得 C=1.0，按式（4.4），取 $\alpha=18$ ，则 $\lambda^{2}\geqslant4C\frac{\alpha+C}{\alpha-C}=4\frac{18+1}{18-1}=4.4706$ ，则可取 $\lambda=6$ 。扰动为随机信号。采用连续系统仿真，信号跟踪及导数估计如图 4-10 和图 4-11 所示。图 4-10 中，上图为带有噪声的单位正弦信号，下图为 Levant 微分器输出 $x_{1}$ 和理想的正弦信号。图 4-11 中，上图为采用 Matlab 工具对信号求导的输出，下图为 Levant 微分器导数估计输出 $x_{2}$ 。采用离散系统仿真可得到同样结果，见仿真程序 chap4\_7.m。

![](image/f7bc9c3e5f84ad6b2a9a8d52b7e137a838f36f2d6bca2eb96b320a7c28f9f9e1.jpg)

图4-10 信号跟踪  
![](image/dedb8a40c06d673ea4305a4b82f1401fbce5daee82441932c976a497091b1f52.jpg)

<details>
<summary>line</summary>

| time(s) | ideal derivative signal | derivative signal by Matlab |
| --- | --- | --- |
| 0 | ~0 | ~0 |
| 1 | ~0 | ~0 |
| 2 | ~0 | ~0 |
| 3 | ~0 | ~0 |
| 4 | ~0 | ~0 |
| 5 | ~0 | ~0 |
| 6 | ~0 | ~0 |
| 7 | ~0 | ~0 |
| 8 | ~0 | ~0 |
| 9 | ~0 | ~0 |
| 10 | ~0 | ~0 |
</details>

![](image/3718ce2d58fed3b2d62694afa9de2cee6c4ba7571259ed785762561bcf49bed7.jpg)

<details>
<summary>line</summary>

| time(s) | ideal derivative signal | x2 by Levant TD |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 1 | 0.5 | 0.5 |
| 2 | -0.5 | -0.5 |
| 3 | -1.0 | -1.0 |
| 4 | -0.5 | -0.5 |
| 5 | 0.5 | 0.5 |
| 6 | 1.0 | 1.0 |
| 7 | 0.5 | 0.5 |
| 8 | 0.0 | 0.0 |
| 9 | -0.5 | -0.5 |
| 10 | -1.0 | -1.0 |
</details>

图4-11 导数求取
