则式(9-8)的向量-矩阵形式的动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} u, \quad y = \boldsymbol {c x} + d u \tag {9-11}$$

式中

$$
\boldsymbol {A} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {0} & - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} \end{array} \right], \quad \boldsymbol {b} = \left[ \begin{array}{l} h _ {1} \\ h _ {2} \\ \vdots \\ h _ {n - 1} \\ h _ {n} \end{array} \right]

\boldsymbol {c} = \left[ \begin{array}{l l l l} 1 & 0 & \dots & 0 \end{array} \right], \quad d = h _ {0}
$$

式(9-8)的状态变量图见图9-6。若输入量中仅含 $m$ 次导数且 $m < n$ ，可将高于 $m$ 次导数项的系数置零，仍可应用上述所得公式。

![](image/e1617390b733c3a0e6c492b824ce3d01effa8a407aec3236d67b2ce5cb5bb16f.jpg)

<details>
<summary>flowchart</summary>
