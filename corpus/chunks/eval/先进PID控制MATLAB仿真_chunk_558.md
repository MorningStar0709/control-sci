# 14.2.4 仿真实例

考虑平面两关节机械手，其动力学方程为

$$D (q) \ddot {q} + C (q, \dot {q}) \dot {q} + G (q) = \tau$$

其中

$$
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} m _ {1} + m _ {2} + 2 m _ {3} \cos q _ {2} & m _ {2} + m _ {3} \cos q _ {2} \\ m _ {2} + m _ {3} \cos q _ {2} & m _ {2} \end{array} \right]

\boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - m _ {3} \dot {q} _ {2} \sin q _ {2} & - m _ {3} (\dot {q} _ {1} + \dot {q} _ {2}) \sin q _ {2} \\ m _ {3} \dot {q} _ {1} \sin q _ {2} & 0. 0 \end{array} \right]

\boldsymbol {G} (\boldsymbol {q}) = \left[ \begin{array}{l} m _ {4} g \cos q _ {1} + m _ {5} g \cos (q _ {1} + q _ {2}) \\ m _ {5} g \cos (q _ {1} + q _ {2}) \end{array} \right]
$$

式中， $m_{i}$ 值由式 $\pmb {M} = \pmb {P} + p_l\pmb{L}$ 给出，有

$$
\begin{array}{l} \boldsymbol {M} = \left[ \begin{array}{l l l l l} m _ {1} & m _ {2} & m _ {3} & m _ {4} & m _ {5} \end{array} \right] ^ {\mathrm{T}} \\ \boldsymbol {P} = \left[ \begin{array}{l l l l l} p _ {1} & p _ {2} & p _ {3} & p _ {4} & p _ {5} \end{array} \right] ^ {\mathrm{T}} \\ \boldsymbol {L} = \left[ \begin{array}{l l l l l} l _ {1} ^ {2} & l _ {2} ^ {2} & l _ {1} l _ {2} & l _ {1} & l _ {2} \end{array} \right] ^ {\mathrm{T}} \\ \end{array}
$$

式中， $p_{l}$ 为负载； $l_{1}$ 和 $l_{2}$ 分别为关节 1 和关节 2 的长度；P 是机械手自身的参数向量。机械力臂实际参数为 $p_{l}=0.50$ ， $P=\left[1.66\quad0.42\quad0.63\quad3.75\quad1.25\right]^{T}$ ， $l_{1}=l_{2}=1$ 。

在笛卡尔空间中的理想跟踪轨迹取 $x_{d1} = \cos t$ ， $x_{d2} = \sin t$ ，该轨迹为一个半径为 1.0、圆心在 $(x_{1}, x_{2}) = (1.0, 1.0)$ m 的圆。初始条件为 $x(0) = [1.0 \quad 1.0]$ ， $\dot{x}(0) = [0.0 \quad 0.0]$ 。

由于跟踪轨迹为工作空间中的直角坐标，而不是关节空间中的角位置，应按式（14.5）和式（14.6）将工作空间中的关节末端直角坐标 $(x_{1},x_{2})$ 转为关节角位置 $(q_{1},q_{2})$ 。

仿真中，被控对象取式（14.10），控制器取式（14.11），控制器的增益选为 $K_{p}=\begin{bmatrix}30&0\\ 0&30\end{bmatrix},\quad K_{d}=\begin{bmatrix}30&0\\ 0&30\end{bmatrix}$ ，由式（14.9）可求 $\tau$ 。仿真结果如图14-4～图14-7所示。

![](image/1688a4e682e68b64f2637e5cd830e9152fa4442159bb96273c2ebdaa4c30bf54.jpg)  
图 14-4 末关节节点的位置跟踪

![](image/41e2962b7aee4e78517467f23494ef87294881eb0f6b04412f3272138aa2ef47.jpg)

<details>
<summary>line</summary>

| time(s) | ideal dx | practical dx |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | -0.8 | -0.8 |
| 2 | -1.0 | -1.0 |
| 3 | -0.5 | -0.5 |
| 4 | 0.5 | 0.5 |
| 5 | 1.0 | 1.0 |
| 6 | 0.5 | 0.5 |
| 7 | -0.5 | -0.5 |
| 8 | -1.0 | -1.0 |
| 9 | -0.5 | -0.5 |
| 10 | 0.5 | 0.5 |
</details>

![](image/cccdcdd9379d612cc155e2d7cefd755f3ad1ae100f1b1120bb5c450fa6e34c53.jpg)

<details>
<summary>line</summary>
