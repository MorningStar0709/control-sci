# 17.7.3 仿真实例

取被控对象为

$$
\begin{array}{l} \frac {\mathrm{d} x _ {1}}{\mathrm{d} t} = x _ {2} \\ J \frac {\mathrm{d} x _ {2}}{\mathrm{d} t} = u (t) + \Delta \\ \end{array}
$$

式中，J=1.0； $\Delta$ 取摩擦模型，表示为 $\Delta=0.5\dot{\theta}+1.5\mathrm{sgn}\left(\dot{\theta}\right)$ 。

位置指令信号取 $\sin t$ ，参数 $\theta$ 的变化范围取 $\theta_{\min}=0.5$ ， $\theta_{\max}=1.5$ 。控制参数取 c=15， $k_{s}=15$ ， $\gamma=500$ ， $\eta=D+0.01=2.01$ 。采用自适应鲁棒控制律式（17.41），如果自适应律取式（17.42），则仿真结果如图 17-19～图 17-21 所示；如果自适应律取式（17.43），则仿真结果如图 17-22～图 17-24 所示。可见，通过采用改进的自适应律，可限制参数 $\theta$ 的自适应变化范围，防止控制输入信号 $u(t)$ 过大。

![](image/bcb771ce884dc477d1184c45fdeef33a65b27369a4da5879a2f4cc6600045b1a.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | -1.0 | -1.0 |
| 10 | 0.0 | 0.0 |
| 15 | 1.0 | 1.0 |
| 20 | -1.0 | -1.0 |
| 25 | 0.0 | 0.0 |
| 30 | -1.0 | -1.0 |
</details>

![](image/312add8c720274c929690186bf951a0d1b162dbe69e417c32f436742f7f225d9.jpg)

<details>
<summary>line</summary>

| time(s) | ideal speed signal | Speed tracking |
| --- | --- | --- |
| 0 | 0 | 0 |
| 5 | -1 | -1 |
| 10 | 0 | 0 |
| 15 | -1 | -1 |
| 20 | 0 | 0 |
| 25 | -1 | -1 |
| 30 | 0 | 0 |
</details>

图 17-19 基于自适应律式（17.11）的位置和速度跟踪（M=1，N=1）

![](image/6c3116cd441f32ad1fc892e722f3622d2788e1b1b05f61d4328e614e0b9c231b.jpg)

<details>
<summary>line</summary>

| time(s) | Control input (x 10^4) |
| --- | --- |
| 0 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
| 25 | 0 |
| 30 | 0 |
</details>

图 17-20 基于自适应律式（17.11）的控制输入（M=1，N=1）

![](image/25254d1e98259f28dfb2ffbb542134eabbdd0c816d546c40543c3e8cfd98b39b.jpg)

<details>
<summary>line</summary>

| time(s) | J and its estimation |
| --- | --- |
| 0 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
| 25 | 0 |
| 30 | 0 |
</details>

图 17-21 基于自适应律式（17.11）的自适应参数变化过程（M=1，N=1）

![](image/a732260ec9e40989258c23daa17265c509ce2ffc81ee84b8ea48e85b6d9c7a3d.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking | ideal speed signal | speed tracking |
| --- | --- | --- | --- | --- |
| 0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 5 | -1.0 | -1.0 | -1.0 | -1.0 |
| 10 | 1.0 | 1.0 | 1.0 | 1.0 |
| 15 | -1.0 | -1.0 | -1.0 | -1.0 |
| 20 | 1.0 | 1.0 | 1.0 | 1.0 |
| 25 | -1.0 | -1.0 | -1.0 | -1.0 |
| 30 | 1.0 | 1.0 | 1.0 | 1.0 |
</details>

图 17-22 基于自适应律式（17.12）的位置和速度跟踪（M=1，N=2）  
![](image/072e9dde80e4fa6eb49fca530cbdaec07208ce47dd37b676784986a7d6f379bd.jpg)

<details>
<summary>line</summary>
