# 9.9.3 仿真实例

选两关节机器人力臂系统,其动力学模型为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \boldsymbol {q}) \boldsymbol {q} + \boldsymbol {G} (\boldsymbol {q}) + F (\boldsymbol {q}) + \tau_ {\mathrm{d}} = \tau$$

其中

$$
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} p _ {1} + p _ {2} + 2 p _ {3} \cos q _ {2} & p _ {2} + p _ {3} \cos q _ {2} \\ p _ {2} + p _ {3} \cos q _ {2} & p _ {2} \end{array} \right], \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - p _ {3} \dot {q} _ {2} \sin q _ {2} & - p _ {3} (\dot {q} _ {1} + \dot {q} _ {2}) \sin q _ {2} \\ p _ {3} \dot {q} _ {1} \sin q _ {2} & 0 \end{array} \right]

\boldsymbol {G} (\boldsymbol {q}) = \left[ \begin{array}{c} p _ {4} g \cos q _ {1} + p _ {5} g \cos \left(q _ {1} + q _ {2}\right) \\ p _ {5} g \cos \left(q _ {1} + q _ {2}\right) \end{array} \right], \boldsymbol {F} (\dot {\boldsymbol {q}}) = 0. 2 \operatorname{sign} (\boldsymbol {q}), \boldsymbol {\tau} _ {\mathrm{d}} = \left[ \begin{array}{l l} 0. 1 \sin (t) & 0. 1 \sin (t) \end{array} \right] ^ {\mathrm{T}}
$$

取 $p = [p_{1}, p_{2}, p_{3}, p_{4}, p_{5}] = [2.9, 0.76, 0.87, 3.04, 0.87]$ 。RBF 网络高斯基函数参数的取值对神经网络控制的作用很重要，如果参数取值不合适，将使高斯基函数无法得到有效的映射，从而导致 RBF 网络无效。故按网络具体输入值的范围取值，取 b = 10，网络的初始权矩阵各元素值取 0 或 0.1，网络输入取 $z = [e \dot{e} q_{d} \dot{q}_{d} \ddot{q}_{d}]$ 。

系统的初始状态为[0.09 0 -0.09 0]，两个关节的位置指令分别为 $q_{1\mathrm{d}} = 0.1\sin t, q_{2\mathrm{d}} = 0.1\sin t$ ，控制参数取 $\mathbf{K}_{\mathrm{v}} = \mathrm{diag}\{20,20\}, \mathbf{F}_{\mathrm{W}}$ 取对角阵，其每个元素取值为 $15, \Lambda = \mathrm{diag}\{5,5\}$ ， $\mathrm{diag}\{\cdot\}$ 为Matlab对角阵表示， $\varepsilon_{\mathrm{N}} = 0.2, b_{\mathrm{d}} = 0.1$ 。

采用 Simulink 和 S 函数进行控制系统的仿真。首先采用针对 $f(x)$ 进行逼近的控制器子程序 chap9\_6ctrl.m，控制律取式(9.70)，自适应律取式(9.73)，仿真结果如图 9-31 至图 9-33 所示。

![](image/200072c4662e24c80170f7f6382401d10c50a0064ae92fd3a552d0a218c511d6.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking for link1 | position tracking for link2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | -0.1 | -0.1 |
| 10 | 0.1 | 0.1 |
| 15 | -0.1 | -0.1 |
| 20 | 0.1 | 0.1 |
| 25 | -0.1 | -0.1 |
| 30 | 0.1 | 0.1 |
| 35 | -0.1 | -0.1 |
| 40 | 0.1 | 0.1 |
</details>

图9-31 关节1及关节2的位置跟踪

基于模型整体逼近的机器人 RBF 网络自适应控制仿真实例程序包括:①Simulink 主程序, chap9\_7sim.mdl;②位置指令子程序,chap9\_7input.m;③控制器子程序,chap9\_7ctrl.m;④被控对象子程序,chap9\_7plant.m;⑤绘图子程序,chap9\_7plot.m。程序见本章附录。
