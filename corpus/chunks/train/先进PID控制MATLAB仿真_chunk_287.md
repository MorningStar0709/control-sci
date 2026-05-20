# 5.4.3 仿真实例

考虑如下对象

$$J \ddot {\theta} = u (t) - d (t) \tag {5.46}$$

式中，J 为转动惯量；u 为控制输入； $\theta$ 为实际角度； $d(t)$ 为外加干扰； $\theta$ 为角度信号。

在扩张观测器仿真中，对象信息取 $d(t)=3\sin(t)$ ，J=10， $u(t)=0.1\sin t$ ，取观测器参数为 $\alpha_{1}=6$ ， $\alpha_{2}=11$ ， $\alpha_{3}=6$ ，为了防止峰值现象，按式（5.44）或式（5.45）设计 $\varepsilon$ ，以连续系统仿真为例，仿真结果如图 5-19～图 5-21 所示。

![](image/915b82d90ef169fc7e92f8063142a44b5b218900d67a9e126d195f71f4468fa7.jpg)

<details>
<summary>line</summary>

| time(s) | angle practical value | angle estimation |
| --- | --- | --- |
| 0 | 0.5 | 0.5 |
| 5 | -1.2 | -1.2 |
| 10 | -2.8 | -2.8 |
| 15 | -4.5 | -4.5 |
| 20 | -6.2 | -6.2 |
| 25 | -7.8 | -7.8 |
| 30 | -9.0 | -9.0 |
</details>

图 5-19 $\theta$ 及其观测信号

![](image/1e2e9ae2b8cb46c038cd562f2fa5a65f16ef645821d62c5407702575f4396062.jpg)

<details>
<summary>line</summary>

| time(s) | angle speed practical value | angle speed estimation |
| --- | --- | --- |
| 0 | 0.0 | 1.2 |
| 5 | -0.6 | 0.8 |
| 10 | -0.6 | 0.4 |
| 15 | -0.6 | 0.0 |
| 20 | -0.6 | -0.4 |
| 25 | -0.6 | -0.8 |
| 30 | -0.6 | -1.2 |
</details>

图 5-20 $\dot{\theta}$ 及其观测信号  
![](image/c68791a4bfe396ecb4c1167eb0c4d7782afe849dec40661d108dc5a1b899f899.jpg)

<details>
<summary>line</summary>

| time(s) | fx practical value | fx estimation |
| --- | --- | --- |
| 0 | 0.0 | -4.0 |
| 5 | 0.2 | -1.0 |
| 10 | 0.1 | 0.0 |
| 15 | 0.3 | 0.1 |
| 20 | 0.1 | -0.1 |
| 25 | 0.2 | 0.0 |
| 30 | 0.3 | 0.1 |
</details>

图 5-21 不确定性及其观测结果

为了显示扩张观测器的控制补偿效果，以连续系统仿真为例，考虑如下对象

$$\ddot {\theta} = 1 0 0 u (t) - 2 5 \dot {\theta} - 1 0 0 \mathrm{sgn} (\dot {\theta}) \tag {5.47}$$

对应于式（5.33），b=100， $f(t)=-25\dot{\theta}-100\mathrm{sgn}\left(\dot{\theta}\right)$ 。基于扩张观测器实现状态和干扰的观测及补偿，采用PD控制，取 $k_{p}=10,\quad k_{d}=10$ ，为了防止峰值现象，按式（5.44）或（5.45）设计 $\varepsilon$ ，仿真结果如图5-22～图5-24所示。以式（5.46）为被控对象，离散形式的控制系统仿真见程序chap5\_9.m。

![](image/0533e8ccacd6881e2c230c6671eb15598f79b6998428fd857922b8d4eb2fbe24.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position | Position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.0 | 0.8 |
| 2 | 0.8 | 0.7 |
| 3 | 0.0 | 0.0 |
| 4 | -1.0 | -1.0 |
| 5 | -1.0 | -1.0 |
| 6 | 0.0 | 0.0 |
| 7 | 1.0 | 1.0 |
| 8 | 0.8 | 0.8 |
| 9 | 0.0 | 0.0 |
| 10 | -0.5 | -0.5 |
</details>

图 5-22 正弦位置跟踪  
![](image/994323d95086e77fd740a069e4ba6c7a2ce05f9499512c4d31fb64f76de0342c.jpg)

<details>
<summary>line</summary>
