# 5.2.4 仿真实例

考虑如下被控对象

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = f (\boldsymbol {x}) + u$$

式中， $f(x)=10x_{1}x_{2}$ 。

位置指令为 $x_{\mathrm{d}}(t) = \sin (t)$ ，取以下5种隶属函数对模糊系统输入 $x_{i}$ 进行模糊化： $\mu_{\mathrm{NM}}(x_i) = \exp [ - ((x_i + \pi / 3) / (\pi / 12))^2 ]$ ， $\mu_{\mathrm{NS}}(x_i) = \exp [ - ((x_i + \pi / 6) / (\pi / 12))^2 ]$ ， $\mu_{\mathrm{Z}}(x_i) = \exp [ - (x_i / (\pi / 12))^2 ]$ ， $\mu_{\mathrm{PS}}(x_i) = \exp [ - ((x_i - \pi / 6) / (\pi / 12))^2 ]$ ， $\mu_{\mathrm{PM}}(x_i) = \exp [ - ((x_i - \pi / 3) / (\pi / 12))^2 ]$ 。则用于逼近 $f$ 的模糊规则有25条。

根据隶属函数设计程序 chap5\_3mf.m, 可得到隶属函数图, 如图 5-8 所示。

![](image/3117c42a1aeb496c0dc148e3d579b4136ab0c087389ff3553cce123214bba4e4.jpg)

<details>
<summary>line</summary>

| x | Membership function degree |
| --- | --- |
| -1.5 | 0.0 |
| -1.0 | 1.0 |
| -0.5 | 0.0 |
| 0.0 | 1.0 |
| 0.5 | 0.0 |
| 1.0 | 1.0 |
| 1.5 | 0.0 |
</details>

图5-8 $x_{i}$ 的隶属函数

在控制器程序中，分别用 $\mathrm{FS}_2$ 、 $\mathrm{FS}_1$ 和 FS 表示模糊系统 $\xi(x)$ 的分子、分母及 $\xi(x)$ 。被控对象初始值取[0.15,0]，控制律采用式(5.16)，自适应律采用式(5.17)，向量 $\hat{\theta}$ 中各个元素的初值取 0.10，取 $\gamma = 500, \eta = 0.50$ 。仿真结果如图 5-9 和图 5-10 所示。

![](image/e823ba57624a392df8db87d1e4e11dd0d4a2c941842decbe23c60c6cb615228d.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.0 |
| 4 | -1.0 |
| 6 | 0.0 |
| 8 | 1.0 |
| 10 | -1.0 |
| 12 | 0.0 |
| 14 | 1.0 |
| 16 | -1.0 |
| 18 | 0.0 |
| 20 | 1.0 |
</details>

![](image/6e491adc3524cf2b2606a1594f147378e8465e6c1c86b033d0ce995b37099cf0.jpg)

<details>
<summary>line</summary>

| time(s) | speed tracking |
| --- | --- |
| 0 | 1.0 |
| 2 | -1.0 |
| 4 | -1.0 |
| 6 | 1.0 |
| 8 | -1.0 |
| 10 | -1.0 |
| 12 | 1.0 |
| 14 | -1.0 |
| 16 | -1.0 |
| 18 | 1.0 |
| 20 | 0.0 |
</details>

图5-9 位置和速度跟踪

![](image/e79e96b90e21fdf0a44f430ebfdd7e8ed97d5f5bc6a8810cff2f3c867d295536.jpg)

<details>
<summary>line</summary>

| time(s) | f approximation |
| --- | --- |
| 0 | 15.0 |
| 2 | 2.0 |
| 4 | -3.0 |
| 6 | 3.0 |
| 8 | -2.0 |
| 10 | -5.0 |
| 12 | 3.0 |
| 14 | -3.0 |
| 16 | -5.0 |
| 18 | 3.0 |
| 20 | 4.0 |
</details>

图5-10 $f(x)$ 及其模糊逼近

简单的自适应模糊控制程序有5个:①隶属函数设计程序 chap5\_3mf.m;②Simulink 主程序 chap5\_3sim.mdl;③被控对象 S 函数程序 chap5\_3plant.m;④控制器 S 函数程序 chap5\_3s.m;⑤作图程序: chap5\_3plot.m。程序见附录。
