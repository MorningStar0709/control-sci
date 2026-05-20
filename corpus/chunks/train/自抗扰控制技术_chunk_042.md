<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.3 |
| 2 | 0.9 |
| 3 | 1.0 |
| 4 | 0.95 |
| 5 | 0.95 |
</details>

图1.4.3

从图 1.4.3 中明显看出, $k_{1}$ 的加大,虽能加快过渡过程,但超调却显著增大.

作为对比,我们来看看 P 的增益 $k_{1}$ 对已安排的过渡过程作为输入的系统(1.4.8)的影响. 取过渡过程时间分别为 $T_{0}=2,1$ , 而分别取 P 的增益为 $k_{1}=800,400$ (由于安排的过渡过程和系统输出之间的误差始终都很小, 要有足够的推动力来启动系统, 必须增益 $k_{1}$ 要足够大). 这个仿真结果(图 1.4.4)表明, 在这里, 快速性和超调并不对立, 而且系统的响应效果对一定范围的增益 $k_{1}$ 的变化并不敏感, 因此一个固定的增益 $k_{1}$ 能够适应较大范围内的对象参数 $a_{1}$ (如, 当 $k_{1}=400$ 时, $a_{1}$ 取区间 [0,400] 范围内的值并不改变响应效果). 安排过渡过程也能扩大增益 $k_{1}$ 对对象参数 $a_{2}$ 的适应范围. 图 1.4.5 显示的是 $T_{0}=1, k_{1}=600$ , 而 $a_{2}$ 分别取 2,10,30,50 的仿真结果. 比起图 1.4.3 的结果, 这里的参数 $a_{2}$ 的适应范围扩大了一个数量级.

![](image/d91512fbffcf6ca11703864008b621c25c588af7cae5bb7ebfb1aed97679690a.jpg)

<details>
<summary>line</summary>

| x | k=800,T₀=2 | k=400,T₀=1 | k=400,T₀=1 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 1 | 0.8 | 0.6 | 0.8 |
| 2 | 1.2 | 1.0 | 1.2 |
| 3 | 1.4 | 1.2 | 1.4 |
| 4 | 1.4 | 1.4 | 1.4 |
The chart displays three separate line graphs for α²=2,α=2. The x-axis ranges from 0 to 5, and the y-axis ranges from 0 to 1.4. Each graph contains two lines representing different parameter values: k=800,T₀=2 (top-left), k=400,T₀=1 (middle-right), and k=400,T₀=1 (bottom-right). The top-left curve shows the steepest initial rise, while the bottom-right curve remains relatively flat after x=5. No explicit numerical values are provided for the top and bottom curves.
</details>

图1.4.4  
![](image/6068c090be122a04b4d52d8a784fb637a08d5cae4e7ba21745348123ae784409.jpg)  
图1.4.5

既然我们事先安排了过渡过程,那么我们也能够得到安排的过渡过程的微分信号,如对式(1.4.7)定义的 $\mathrm{trns}(T_{0},t)$ 而言,其微分信号为

$$
\mathrm{d} \operatorname{trns} (T _ {0}, t) = \left\{ \begin{array}{l l} \frac {\pi}{2 T _ {0}} \cos \left(\pi \left(\frac {t}{T _ {0}} - \frac {1}{2}\right)\right), & t \leqslant T _ {0} \\ 0, & t > T _ {0} \end{array} \right. \tag {1.4.9}
$$

如果系统输出的微分信号 $\dot{x}$ 能获取，那么误差信号 $e = v_{0}\mathrm{trms}(T_0,t) - x$ 的微分信号 $\dot{e} = v_0\mathrm{dtrms}(T_0,t) - \dot{x}$ 也能够得到，从而PID的D反馈 $-k_{2}\dot{e}$ 就能实现．这时，实现了PD反馈的系统

$$
\left\{ \begin{array}{l} a _ {1} = a _ {1} + k _ {1}, a _ {2} = a _ {2} + k _ {2} \\ \ddot {x} = - \overline {{a _ {1}}} (x - v _ {0} \operatorname{trns} (T _ {0}, t)) - \overline {{a _ {2}}} (\dot {x} - v _ {0} \operatorname{dtrns} (T _ {0}, t)) \\ y = x \end{array} \right. \tag {1.4.10}
$$

对系统(1.4.10)来说,可适应的对象参数 $a_{1},a_{2}$ 的范围就更为扩大了.
