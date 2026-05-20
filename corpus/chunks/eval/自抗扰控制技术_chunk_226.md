$$
\left\{ \begin{array}{l} \dot {x} _ {1 1} = x _ {1 2} \\ \dot {x} _ {1 2} = \gamma_ {1} \operatorname{sign} (\sin (\omega_ {1} t)) + x _ {2 1} \\ \dot {x} _ {2 1} = x _ {2 2} \\ \dot {x} _ {2 2} = \gamma_ {2} \operatorname{sign} (\cos (\omega_ {2} t)) + u \\ y _ {1} = x _ {1 1} \\ y _ {2} = x _ {2 1} \end{array} \right. \tag {6.4.17}
$$

这里把 $x_{21} = x_2$ 当作控制 $x_{11} = x_1$ 的虚拟控制变量 $u_{1} = x_{2}$ 这时的整个具体控制算法为

$$
\left\{ \begin{array}{l} \mathrm{fh} = \text { fhan } (v _ {1 1} - v (t), v _ {1 2}, r _ {0}, h) \\ v _ {1 1} = v _ {1 1} + h v _ {1 2} \\ v _ {1 2} = v _ {1 2} + h \mathrm{fh} \\ e = z _ {1 1} - y _ {1}, \mathrm{fe} = \text { fal } (e, 0. 5, h), \mathrm{fe} _ {1} = \text { fal } (e, 0. 2 5, h) \\ z _ {1 1} = z _ {1 1} + h (z _ {1 2} - \beta_ {0 1} e) \\ z _ {1 2} = z _ {1 2} + h (z _ {1 3} - \beta_ {0 2} \mathrm{fe} + u _ {1}) \\ z _ {1 3} = z _ {1 3} + h (- (\beta_ {0 3} - 3 0 0) \mathrm{fe} _ {1}) \\ e _ {1} = v _ {1 1} - z _ {1 1}, e _ {2} = v _ {1 2} - z _ {1 2} \\ u _ {1} = \text { fhan } (e _ {1}, c _ {1} e _ {2}, r _ {1}, h _ {1}) - z _ {1 3} \end{array} \right. \tag {6.4.18}

\left\{ \begin{array}{l} e = u _ {1} - y _ {2}, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {2 1} = z _ {2 1} + h \left(z _ {2 2} - \beta_ {0} e\right) \\ z _ {2 2} = z _ {2 2} + h \left(z _ {2 3} - \beta_ {0} \mathrm{fe} + u\right) \\ z _ {2 3} = z _ {2 3} + h \left(- \beta_ {0} \mathrm{fe} _ {1}\right) \\ e _ {1} = u _ {1} - z _ {2 1}, e _ {2} = - z _ {2 2} \\ u = \operatorname{fhan} \left(e _ {1}, c _ {2} e _ {2}, r _ {2}, h _ {2}\right) - z _ {2 3} \end{array} \right. \tag {6.4.19}
$$

这里有两个自抗扰控制器(ADRC)，其中第一个ADRC的可调参数为 $r_{1},c_{1},h_{1}$ 三个，第二个ADRC的可调参数为 $r_{2},c_{2},h_{2}$ 三个，共六个.

当采样步长 $h = 0.01$ 确定时，扩张状态观测器参数便被确定，是 $\beta_{01} = 100, \beta_{02} = 300, \beta_{03} = 1000.$ 为了让第二个输出 $y_{2}$ 更好的跟踪第一个ADRC的输出 $u_{1}$ ，需要使 $u_{1}$ 变化不要太激烈，为此对设定值 $v(t) = 1$ 安排过渡过程的参数 $r_0$ 不能太大，如 $0.1 \sim 10$ 的范围(如果要跟踪时变的设定轨线 $r_{0}$ 要取大一些,如30\~100范围),并且 $\beta_{03}=1000$ 可以取更小一些.

在对象(5.7.17)中取 $\gamma_{1} = 1.0, \gamma_{2} = 10, \omega_{1} = 0.3, \omega_{2} = 0.2$ 控制目标为常值 $v(t) = 1$ . 我们取两个 ARDC 参数分别取成 $r_{1} = 10, c_{1} = 0.3, h_{1} = 0.2$ 和 $r_{1} = 600, c_{1} = 0.5, h_{1} = 0.04$ . 步长 $h = 0.01$ 来进行控制仿真的结果示于图 6.4.9.

![](image/51073885e262a38c4df06076783bda4a1396cfdb58909af439b9d5e568f7bd04.jpg)

<details>
<summary>line</summary>

| x | y1 | y2 | y3 |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 5 | 1 | 0 | 0 |
| 10 | 2 | 0 | 0 |
| 15 | 3 | 0 | 0 |
| 20 | 4 | 0 | 0 |
| 25 | 5 | 0 | 0 |
| 30 | 6 | 0 | 0 |
| 35 | 7 | 0 | 0 |
| 40 | 8 | 0 | 0 |
</details>

图6.4.9
