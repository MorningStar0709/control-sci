$$
b = 1 4. 2 8 6, c = 1, m _ {0} = - \frac {1}{7}, m _ {1} = \frac {2}{7}, x _ {1} (0) = 1, x _ {2} (0) = 0,x _ {3} (0) = - 1.
\left\{ \begin{array}{l} \dot {x} _ {1} = a [ x _ {2} - \phi (x _ {1}) ] + u \\ \dot {x} _ {2} = x _ {1} - x _ {2} + x _ {3} \\ \dot {x} _ {3} = b x _ {2} \\ y = x _ {1} \end{array} \right. \tag {1}

\left\{ \begin{array}{l} \dot {x} _ {1} = a [ x _ {2} - \phi (x _ {1}) ] \\ \dot {x} _ {2} = x _ {1} - x _ {2} + x _ {3} + u \\ \dot {x} _ {3} = b x _ {2} \\ y = x _ {1} \end{array} \right. \tag {6.5.7}
$$

对这两个系统用式(6.5.3)，式(6.5.4)，式(6.5.5)决定的自抗扰控制器进行仿真的结果如图6.5.3、图6.5.4所示.

![](image/22a0ecbce51422f643637d1ae594192453083e64ee104d57a53e616bc2062188.jpg)

<details>
<summary>line</summary>

| v(t)=1 | Value |
| --- | --- |
| 0 | 0 |
| 5 | 0.5 |
| 10 | 1 |
| 15 | 1 |
| 20 | 1 |
| 25 | 1 |
| 30 | 1 |
| 35 | 1 |
| 40 | 1 |
| 45 | 1 |
| 50 | 1 |
| 55 | 1 |
</details>

![](image/133850c151a8fe4012c912318eb6a3bb6717d60d81dd33ffc5a97b8ceefd8142.jpg)

<details>
<summary>line</summary>

(2)
</details>

图6.5.3  
![](image/c2e3a2d3b7d73975d63509a84939e3d137e361cb3179de220aa959d12597299d.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 10 | -5 |
| 20 | 0 |
| 30 | -5 |
| 40 | 0 |
| 50 | -5 |
| 60 | 0 |
</details>

Chua   
![](image/f01ec99c17119491ba497f2fef747f83dabdfef09b9ccb44bcb14addded1a6c3.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 25 | -2 |
| 26 | 2 |
| 27 | 0 |
| 28 | -2 |
| 29 | 0 |
| 30 | 2 |
| 31 | 0 |
| 32 | -2 |
| 33 | 0 |
| 34 | -2 |
| 35 | 0 |
| 36 | 2 |
| 37 | 0 |
| 38 | -2 |
| 39 | 0 |
| 40 | -2 |
</details>

v(t)=2cos(t)+sin(t/2)

![](image/5502f334e888d03bf0b4f8fedbb3584cf590bdf2b6cb597f958fe7fd0b5586f2.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0 |
| 20 | -5 |
| 40 | 0 |
| 60 | 5 |
</details>

![](image/1109cdb198866203073b5211b6a515a3de0c7d1fb538422d68c5bea4ac9ec224.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 20 | -1 |
| 25 | 2 |
| 30 | -1 |
| 35 | -2 |
| 40 | 2 |
</details>

图6.5.4

下面我们来考察混沌系统跟踪混沌轨迹的问题.

假定我们随时能获取 Lorenz 混沌系统轨迹的一个输出值 $x_{1}(t)$ ，能否对另一混沌系统施加控制力的办法来跟踪这个混沌输出呢？

Lorenz 系统

$$
\left\{ \begin{array}{l l} \dot {x} _ {1} = 1 0 (x _ {2} - x _ {1}), & x _ {1} (0) = - 4. 4 7 \\ \dot {x} _ {2} = 2 8 x _ {1} - x _ {2} - x _ {1} x _ {3}, & x _ {2} (0) = - 0. 5 0 5 \\ \dot {x} _ {3} = - \frac {8}{3} x _ {3} + x _ {1} x _ {2}, & x _ {3} (0) = 2 8. 0 2 \\ v (t) = x _ {1} (t) \end{array} \right. \tag {6.5.8}
$$

的输出 $v(t)$ 作为被跟踪信号.

把 Lossler 系统改造成受控系统, 得
