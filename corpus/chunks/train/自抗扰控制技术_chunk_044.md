![](image/7f843bfff768cbd8d67d59dea05c8e7bde7eeab6190bda1330bb79936400e59e.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 1 | -1.0 |
| 2 | 0.8 |
| 3 | -0.8 |
| 4 | 0.6 |
| 5 | -0.6 |
| 6 | 0.4 |
| 7 | -0.4 |
| 8 | 0.2 |
| 9 | -0.2 |
| 10 | 0.0 |
| 11 | 0.2 |
| 12 | -0.2 |
| 13 | 0.4 |
| 14 | -0.4 |
| 15 | 0.6 |
| 16 | -0.6 |
| 17 | 0.8 |
| 18 | -0.8 |
| 19 | 1.0 |
| 20 | -1.0 |
</details>

图1.4.8

三阶对象．先取过渡过程的加加速度函数：

$$
v _ {4} (t) = \left\{ \begin{array}{l l} 3 2 \frac {v _ {0}}{T _ {0} ^ {\mathrm{a}}}, & t \leqslant \frac {T _ {0}}{4} \\ - 3 2 \frac {v _ {0}}{T _ {0} ^ {\mathrm{a}}}, & \frac {T _ {0}}{4} <   t \leqslant 3 \frac {T _ {0}}{4} \\ 3 2 \frac {v _ {0}}{T _ {0} ^ {\mathrm{a}}}, & 3 \frac {T _ {0}}{4} <   t \leqslant T _ {0} \\ 0, & T _ {0} <   t \end{array} \right.
$$

积分此加加速度函数得加速度函数：

$$
v _ {3} (t) = \int_ {0} ^ {t} v _ {4} (\tau) \mathrm{d} \tau =
\left\{ \begin{array}{l l} 3 2 \frac {v _ {0}}{T _ {0} ^ {2}} t, & t \leqslant \frac {T _ {0}}{4} \\ 8 \frac {v _ {0}}{T _ {0} ^ {2}} \left(1 - \frac {4}{T _ {0}} \left(t - \frac {T _ {0}}{4}\right)\right), & \frac {T _ {0}}{4} <   t \leqslant 3 \frac {T _ {0}}{4} \\ - 8 \frac {v _ {0}}{T _ {0} ^ {2}} \left(1 - \frac {4}{T _ {0}} \left(t - 3 \frac {T _ {0}}{4}\right)\right), & 3 \frac {T _ {0}}{4} <   t \leqslant T _ {0} \\ 0, & T _ {0} <   t \end{array} \right.
$$

安排的过渡过程 $v_{1}(t)$ 是由加速度函数 $v_{3}(t)$ 的两次积分所得. 从 $v_{4}(t)$ 依次积分得到 $v_{1}(t)$ 的过程表示为图1.4.9.

![](image/72f4908707fbbcac1845bac67d5f7ab234e1bcb054108b3a72d73c385cb7458b.jpg)

<details>
<summary>line</summary>

| x | v₄ | v₁/2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | 1.0 | -0.8 |
| 10 | 0.0 | 0.0 |
| 15 | 1.0 | 0.8 |
| 20 | 0.0 | 1.0 |
</details>

图1.4.9

构造 $v_{3}(t)$ 的一般办法如下:把区间 $[0,T_{0}]$ 分成:前部,中间,后部三段.然后构造函数,使前后两段取正值,中间段取负值;两个正部分的面积各相等,而正部分的面积之和是与中间负部分的面积相等.

对各阶对象安排过渡过程的一般方法可按如下公式给出:这里设定的过渡过程时间为 $T_{0}$ ，记

$$
s (t, T _ {0}) = \left\{ \begin{array}{l l} \operatorname{sign} (t), & t \leqslant T _ {0} \\ 0, & t > T _ {0} \end{array} \right.
$$

则函数

$$u _ {1} = s \left(t, T _ {0}\right), u _ {2} = - s \left(t - \frac {T _ {0}}{2}, \frac {T _ {0}}{2}\right),u _ {3} = s \left(t - \frac {T _ {0}}{4}, T _ {0}\right) s \left(t - \frac {3 T _ {0}}{4}, \frac {T _ {0}}{4}\right)u _ {4} = - s \left(t - \frac {2 - \sqrt {2}}{4} T _ {0}, T _ {0}\right) s \left(t - \frac {2}{4} T _ {0}, \frac {T _ {0}}{2}\right) s \left(t - \frac {2 + \sqrt {2}}{4} T _ {0}, T _ {0}\right),$$

是一组方波函数,其图像如图1.4.10所示.实际上,这些方波函数分别是一,二,三,四阶积分器串联对象,在控制输入受限制 $|u|\leqslant1$ 时,从静止初态移动到另一位置停下来的最速控制规律.
