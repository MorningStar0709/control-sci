# 9.3节习题

9.8 考虑如图 9.61 所示的三阶系统。

![](image/b453e41fdca5deca780e4e091241cdb11fa96cf244a54e99dc84ef1ae4948293.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum -->|e| K
    K -->|u| Transfer["(s+1)²/s³"]
    Transfer --> O["Y"]
    O -->|-| Sum
```
</details>

图 9.61 习题 9.8 的控制系统

(a) 绘制该系统关于 K 的根轨迹图，写出渐近线的角度、分离角的计算过程，等等。  
(b) 利用绘图法，仔细确定该轨迹穿过虚轴的点。在该点 K 的值是多少？  
(c) 假设，由于某些未知机理，放大器的输出由下面的饱和非线性函数给定（而不是比例增益 K）：

$$
u = \left\{ \begin{array}{l l} e, & | e | \leqslant 1 \\ 1, & e > 1 \\ - 1, & e <   - 1 \end{array} \right.
$$

定性地描述你认为系统将对单位阶跃输入会有怎样的响应。

9.9 考虑具有如下传递函数的系统：

$$G (s) = \frac {1}{s ^ {2} + 1}$$

我们将使用如下形式的 PID 控制来控制系统。

$$D _ {c} (s) = 1 0 \left(1 + \frac {1}{2 s} + 2 s\right)$$

已知该系统的执行器是一个具有单位斜率的饱和非线性函数，且 $|u|\leqslant 10$ 。对于大小为

10 的阶跃输入，比较具有和不具有抗饱和电路的系统响应。用 Simulink 画出两者的阶跃响应和控制输入。定性地描述抗饱和电路的影响。
