# 1. 微分器频域分析

通过采用扫频测试的方法对 Levant 微分器进行频域分析，可得该微分器的频域特性。扫频测试原理见文献[1]中的第 2 章 2.3 节。

采样时间为 T=0.001s，令输入信号为 $v(t)=\sin(2\pi t)$ ， $v(t)$ 导数的上界为 $2\pi$ ，取 $C=2\pi$ ，采用 $0\sim30Hz$ 的正弦信号进行扫频。则按式（4.4），取 Levant 参数为 $\alpha=15$ ， $\lambda=10$ ，频域特性如图 4-9(a) 所示，取 Levant 参数为 $\alpha=15$ ， $\lambda=20$ ，频域特性如图 4-9(b)

![](image/767f0d0ad76407ff8ea8e6861b83ecb69cd11891cc032ce015aac327f9ef1a59.jpg)

<details>
<summary>line</summary>

| rad./s | Mag.(dB.) |
| --- | --- |
| 0.1 | 0 |
| 1 | 0 |
| 10 | -5 |
| 100 | -20 |
| 1000 | -28 |
</details>

![](image/87273687bfaa288d37e68549fd105956037847dd658f409a8db9df75abdb640e.jpg)

<details>
<summary>line</summary>

| rad./s | Phase(Deg.) |
| --- | --- |
| 10^-1 | 0 |
| 10^0 | 0 |
| 10^1 | -50 |
| 10^2 | -80 |
| 10^3 | -90 |
</details>

(a) $\alpha=15,\lambda=10$   
![](image/00362fc965e2e0bf062c2fc1ef74edc61f02ac22b91f65e2da554dcd247bfb97.jpg)

<details>
<summary>line</summary>

| rad./s | Mag.(dB.) |
| --- | --- |
| 10^-1 | 0 |
| 10^0 | 0 |
| 10^1 | 0 |
| 10^2 | -10 |
| 10^3 | -20 |
</details>

![](image/f8b719f94878ffeda261f11b098235cee3ea5175884d645acdb6dfd6f24704ec.jpg)

<details>
<summary>line</summary>

| rad./s | Phase(Deg.) |
| --- | --- |
| 0.1 | 0 |
| 1 | 0 |
| 10 | -50 |
| 100 | -100 |
| 1000 | -100 |
</details>

(b) $\alpha=15,\lambda=20$   
图 4-9 不同参数下 Levant 微分器的频域特性

所示。可见，Levant 微分器具有很好低频跟踪效果以及较强的抑制噪声能力，如果增大 $\lambda$ 值，可以拓宽频带，但同时增加了 Levant 微分器切换增益，加大了抖振。
