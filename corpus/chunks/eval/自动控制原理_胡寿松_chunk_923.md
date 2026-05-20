在 MATLAB 中运行 M 文件 example9 后, 结果如下:

1) 由于对称矩阵 $P=\begin{bmatrix}0.5&-0.7778&0.5\\ -0.7778&3.6944&-2.1111\\ 0.5&-2.1111&1.5\end{bmatrix}$ 正定，可知系统稳定。当然 M 文件 example9 的第 2～5 行命令完全可以替换成如下命令：

$$\mathrm{e} = \text { eig(A) }$$

%计算系统的特征根

得结果为 $\lambda_{1}=\lambda_{2}=-1,\lambda_{3}=-2$ ，全部为负，也可得出系统稳定的结论。

2）系统的传递函数

$$\Phi (s) = \frac {s ^ {2} + s}{s ^ {3} + 4 s ^ {2} + 5 s + 2}$$

系统零输入响应的状态曲线和输出曲线分别如图 B-21 和图 B-22 所示。

![](image/d78e44c1d19fd505ebc3f7d082c2811447458406ed1147a0d1aa97d6015f7cf6.jpg)

<details>
<summary>line</summary>

| Time/sec | x(t) Upper Curve | x(t) Lower Curve |
| --- | --- | --- |
| 0 | 3.0 | -2.0 |
| 1 | 5.5 | -2.8 |
| 2 | 3.0 | -2.0 |
| 3 | 1.5 | -1.0 |
| 4 | 0.5 | -0.5 |
| 5 | 0.0 | -0.2 |
| 6 | 0.0 | -0.1 |
| 7 | 0.0 | 0.0 |
</details>

图 B-21 零输入状态响应曲线

![](image/5948cd1a77161b11314cf58e7c09de57cafdbf5e75956dcf0d63a2984654bc96.jpg)

<details>
<summary>line</summary>

| Time/sec | y(t) |
| --- | --- |
| 0 | 4.0 |
| 1 | 2.5 |
| 2 | 1.0 |
| 3 | 0.5 |
| 4 | 0.2 |
| 5 | 0.1 |
| 6 | 0.05 |
| 7 | 0.01 |
</details>

图 B-22 零输入输出响应曲线

3) 由于可控性矩阵满秩, 所以系统完全可控。利用变换矩阵 T 得系统的可控标准型为

$$
\dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 2 & - 5 & - 4 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] \boldsymbol {u} (t), y (t) = \left[ \begin{array}{l l l} 0 & 1 & 1 \end{array} \right] \boldsymbol {x} (t)
$$

4) 由于可观测性矩阵的秩为 2, 非满秩, 系统状态不完全可观测。观测性分解结果为

$$
\begin{array}{l} \dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c c} - 1 & - 4. 2 4 2 6 & 2 \\ 0 & - 2 & 0 \\ 0 & - 1. 4 1 4 2 & - 1 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{c} - 0. 7 0 7 1 \\ - 1 \\ - 0. 7 0 7 1 \end{array} \right] \boldsymbol {u} (t) \\ y (t) = [ 0 \quad 0 \quad - 1. 4 1 4 2 ] x (t) \\ \end{array}
$$

系统最小实现为

$$
\dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c} - 1 & - 1. 4 1 4 \\ 0 & - 2 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{c} - 0. 7 0 7 1 \\ - 1 \end{array} \right] \boldsymbol {u} (t), \quad y (t) = [ - 1. 4 1 4 \quad 0 ] \boldsymbol {x} (t)
$$

例 B-10 设线性定常系统的状态方程为

$$
\begin{array}{l} \dot {\boldsymbol {x}} (t) = \left[ \begin{array}{c c c} - 2 & - 2. 5 & - 0. 5 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \boldsymbol {x} (t) + \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] \boldsymbol {u} (t), y (t) = \left[ \begin{array}{l l l} 1 & 4 & 3. 5 \end{array} \right] \boldsymbol {x} (t), \\ \boldsymbol {x} (0) = \left[ \begin{array}{c} 1 \\ - 0. 7 5 \\ 0. 4 \end{array} \right] \\ \end{array}
$$

试问：
