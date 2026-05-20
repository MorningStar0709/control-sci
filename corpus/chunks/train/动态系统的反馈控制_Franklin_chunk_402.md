# 例 7.3 状态变量形式的桥接三通电路

确定如图 2.25 所示电路图的状态空间方程。

解答。为了写出状态变量形式的方程（也就是，一组同时成立的一阶微分方程式），选择电容电压 $v_{C1}$ 和 $v_{C2}$ 作为状态元素（即， $x=\left[v_{C1}\right.$ $v_{C2}\right]^{T}$ ），以及 $v_{i}$ 作为输入（即 $u=v_{i}$ ）。这里， $v_{C1}=v_{2}$ ， $v_{C2}=v_{1}-v_{3}$ ， $v_{1}=v_{i}$ 。因此， $v_{1}=v_{i}$ ， $v_{2}=v_{C1}$ ， $v_{3}=v_{i}-v_{C2}$ 作为输出（也就是 $y=v_{3}$ ）。依据 $v_{C1}$ 和 $v_{C2}$ ，式（2.34）为

$$\frac {v _ {\mathrm{C1}} - v _ {\mathrm{i}}}{R _ {1}} + \frac {v _ {\mathrm{C1}} - (v _ {\mathrm{i}} - v _ {\mathrm{C2}})}{R _ {2}} + C _ {1} \frac {\mathrm{d} v _ {\mathrm{C1}}}{\mathrm{d} t} = 0$$

将该方程转化为标准形，我们得到

![](image/0f89d9af7dadece806fe1a6d1d1d7ad3f4d61933432b1cc17545db22ebcfa9df.jpg)

<details>
<summary>line</summary>

| 时间/s | 速度 |
| --- | --- |
| 0 | 0 |
| 50 | 8.5 |
| 100 | 10 |
</details>

图 7.2 阶跃输入为 u 的汽车速度响应曲线

$$\frac {\mathrm{d} v _ {\mathrm{C1}}}{\mathrm{d} t} = - \frac {1}{C _ {1}} \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}}\right) v _ {\mathrm{C1}} - \frac {1}{C _ {1}} \left(\frac {1}{R _ {2}}\right) v _ {\mathrm{C2}} + \frac {1}{C _ {1}} \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}}\right) v _ {\mathrm{i}} \tag {7.6}$$

依据 $v_{C1}$ 和 $v_{C2}$ ，式(2.35)为

$$\frac {v _ {\mathrm{i}} - v _ {\mathrm{C2}} - v _ {\mathrm{C1}}}{R _ {2}} + C _ {2} \frac {\mathrm{d}}{\mathrm{d} t} (v _ {\mathrm{i}} - v _ {\mathrm{C2}} - v _ {\mathrm{i}}) = 0$$

写成标准形，上式为

$$\frac {\mathrm{d} v _ {\mathrm{C2}}}{\mathrm{d} t} = - \frac {v _ {\mathrm{C1}}}{C _ {2} R _ {2}} - \frac {v _ {\mathrm{C2}}}{C _ {2} R _ {2}} + \frac {v _ {\mathrm{i}}}{C _ {2} R _ {2}} \tag {7.7}$$

式(2.34)、式(2.35)完全等价于状态变量形式，式(7.6)、式(7.7)用来描述电路。标准矩阵定义为

$$
\mathbf {A} = \left[ \begin{array}{l l} - \frac {1}{C _ {1}} (\frac {1}{R _ {1}} + \frac {1}{R _ {2}}) & - \frac {1}{C _ {1}} (\frac {1}{R _ {2}}) \\ - \frac {1}{C _ {2} R _ {2}} & - \frac {1}{C _ {2} R _ {2}} \end{array} \right]

\boldsymbol {B} = \left[ \begin{array}{c} \frac {1}{C _ {1}} \left(\frac {1}{R _ {1}} + \frac {1}{R _ {2}}\right) \\ \frac {1}{C _ {2} R _ {2}} \end{array} \right]

\mathbf {C} = \left[ \begin{array}{c c} 0 & - 1 \end{array} \right], \quad D = 1
$$
