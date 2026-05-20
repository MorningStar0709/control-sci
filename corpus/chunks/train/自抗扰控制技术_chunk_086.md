# 2.7 离散系统快速最优控制综合函数的推导

离散系统

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) + h u, \quad | u | \leqslant r \end{array} \right. \tag {2.7.1}
$$

的快速最优控制综合函数的推导过程如下.

先确定能用控制序列 $u(0), u(1), \cdots, u(k)$ 来达到原点的初始点 $[x_{1}(0) \quad x_{2}(0)]^{\mathrm{T}}$ 的表达式，然后想法用 $[x_{1}(0) \quad x_{2}(0)]^{\mathrm{T}}$ 来表示出初始时刻的控制量 $u(0)$ ，那么这个控制量就是初始点 $[x_{1}(0) \quad x_{2}(0)]^{\mathrm{T}}$ 的最优控制量，从而这个表达式成为最优控制综合函数.

从初值 $\left[x_{1}(0)\quad x_{2}(0)\right]^{T}$ 出发的系统(2.7.1)解的表达式为

$$
\begin{array}{l} \left[ \begin{array}{c} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] = \left[ \begin{array}{c c} 1 & k h \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \left[ \begin{array}{c c} 1 & (k - 1) h \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} 0 \\ h \end{array} \right] u (0) + \\ \dots + \left[ \begin{array}{l l} 1 & h \\ 0 & 1 \end{array} \right] \left[ \begin{array}{l} 0 \\ h \end{array} \right] u (k - 2) + \left[ \begin{array}{l} 0 \\ h \end{array} \right] u (k - 1) \tag {2.7.2} \\ \end{array}
$$

式中， $u(i)$ 为第 $i+1$ 步的控制量.

如果对给定的初始点 $\left[x_{1}(0)\quad x_{2}(0)\right]^{T}$ ，存在k个控制量 $u(0),u(1),\cdots,u(k-1)$ ，使式(2.7.2)的左边等于零，就能得到在k步内能到达原点的初始点表达式

$$
\left[ \begin{array}{l} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{l} k h ^ {2} \\ - h \end{array} \right] u (k - 1) + \left[ \begin{array}{c} (k - 1) h ^ {2} \\ - h \end{array} \right] u (k - 2) + \dots +

\left[ \begin{array}{l} 2 h ^ {2} \\ - h \end{array} \right] u (1) + \left[ \begin{array}{l} h ^ {2} \\ - h \end{array} \right] u (0) \tag {2.7.3}
$$

控制量 u 受限制 $\left|u\right|\leqslant r$ 的情况下，k 步内能到达原点的所有初始点 $[x_{1}\quad x_{2}]$ 的全体称为 k-等时区，记做 $G(k)$ 。在式(2.7.3)中，控制量 $u(i)$ 取满足 $\left|u(i)\right|\leqslant r$ 的所有可能的值，那么它就给出等时区 $G(k)$ 的表达式。由于这个表达式是向量 $\left[\frac{ih^{2}}{h}\right], i=1,2,\cdots,k$ 的线性组合（加权和），而其权因子又满足 $\left|u(i)\right|\leqslant r$ ，因此 $G(k)$ 是凸的 2k 边际 (k=1 时为一线段)。图 2.7.1 画出的是 k≤5 时的 $G(k)$ 。 $G(1)$ 是以 $a_{-1},a_{+1}$ 为顶点的线段； $G(2)$ 是以 $a_{-2},b_{-2},a_{+2},a_{+2}$ 为顶点的平行四边形； $G(3)$ 是一个六边形等。

![](image/b4eb1609cab21fa8ebe6d93430467f20cedc2a4e42539a1ed3dd30af508b227a.jpg)

<details>
<summary>line</summary>

| x | y=0 | y=-h/r |
| --- | --- | --- |
| -1.5 | 1.0 | - |
| -1.0 | 0.5 | - |
| -0.5 | 0.0 | - |
| 0.0 | -0.5 | - |
| 0.5 | -1.0 | - |
| 1.0 | -1.5 | - |
| 1.5 | -2.0 | - |
| 2.0 | -2.5 | - |
</details>

图2.7.1
