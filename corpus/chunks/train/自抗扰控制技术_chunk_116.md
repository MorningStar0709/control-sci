![](image/cf5e4147653f149ed0892f8f9a1db29c3cb249f17a18398b74d6fb3eb34bd122.jpg)

<details>
<summary>line</summary>

| x | c=5 | c=1 |
| --- | --- | --- |
| -2 | 1.0 | -1.0 |
| -1 | 0.5 | -0.5 |
| 0 | 0.0 | 0.0 |
| 1 | -0.5 | -0.5 |
| 2 | -1.0 | -1.0 |
</details>

图3.3.8

考察二阶对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = f (x _ {1}, x _ {2}, t) + u \\ y = x _ {1} \end{array} \right.
$$

式中 $f(x_{1},x_{2},t)=x_{1}^{2}+x_{2}^{2}+\text{sign}(\sin(t))$ ，或 $f(x_{1},x_{2},t)=\text{sign}(\sin(t))$ 。控制目的是让y达到设定值v=2.0。对此分别取状态反馈u= $f\tan(x_{1}-v,cx_{2},r,h_{1})$ 与 $u=-r^{2}(x_{1}-v)-cx_{2}$ 来进行比较的仿真效果示于图3.3.9和图3.3.10控制这两个不同被控对象的控制器参数取了同一组，即用同一个控制器来控制两个不同对象，其仿真效果如下：当；反馈取为最速状态反馈控制形式 $f\tan(x_{1},cx_{2},r,h_{1})$ 时，控制器参数为h=0.001,r=40,c=2,h1=0.002，而反馈取为线性形式 $u=-r^{2}(x_{1}-v)-cx_{2}$ 时，控制器参数为h=0.001,r=100,c=3。两种响应均无超调。线性情形快速性好一些，但精度差一个数量级。但后者的比例增益比前者高 $100\times100:40=250$ 倍，而阻尼增益也高出 300:2 = 150, 近两个数量级. 这又一次说明, 适当选取的非线性反馈的效率远比线性反馈的高得多.

![](image/c7ac777e90ec0d8daf35709ea15edec85df64be8a164b0223fa27c80c27f8b29.jpg)

<details>
<summary>line</summary>

f(x,x₁)=x₁+x₂+sign(sin(t)),k=0.001
| x | y |
| --- | --- |
| 0 | 2 |
| 2 | 2 |
| 4 | 2 |
| 6 | 2 |
| 8 | 2 |
| 10 | 2 |
| 12 | 2 |
| 14 | 2 |
| 16 | 2 |
| 18 | 2 |
| 20 | 2 |

| u=-r²(x₁-v)-c r x₁,p=100, c=3 | 
| x₁ | y |
| --- | --- |
| 0 | 2 |
| 2 | 2 |
| 4 | 2 |
| 6 | 2 |
| 8 | 2 |
| 10 | 2 |
| 12 | 2 |
| 14 | 2 |
| 16 | 2 |
| 18 | 2 |
| 20 | 2 |

The chart displays a single series of functions (y) for different x values. The x-axis ranges from 0 to 20 and the y-axis ranges from -3 to 3. The function is defined as: f(x,x₁)=x₁+x₂+sign(sin(t)), k=0.001. The function is defined as u=-r²(x₁-v)-c r x₁,p=100, c=3.
</details>

图3.3.9  
![](image/28150f0b16749bed1e37a5cd738a7d6aa84a478f44d5616af4b4e79caa063dc0.jpg)

<details>
<summary>line</summary>

| x | f(x, x, t) = sign(sin(t)), h = 0.001 |
| --- | --- |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| 18 | 0 |
| 20 | 0 |

| u | u = -r*(x, -v), -c, r, x, t = 100, c = 3 |
| --- | --- |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| 18 | 0 |
| 20 | 0 |

| h | h = -r*(x, -v), -c, r, x, t = 100, c = 3 |
| --- | --- |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| 18 | 2 |
| 20 | 2 |

| h | h = -r*(x, -v), -c, r, x, t = 100, c = 3 |
| --- | --- |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
| 12 | 0 |
| 14 | 0 |
| 16 | 0 |
| ... | ... |
| ... | ... |
The chart displays a single line plot of the function f(x, x, t) = sign(sin(t)) for h < 0.001. The x-axis represents the input values (ranging from -2 to +2) and the y-axis represents the output values (ranging from -2 to +2). The legend indicates that 'h' denotes the input value and 'h' denotes the output value. The plot is labeled in English.
</details>

图3.3.10
