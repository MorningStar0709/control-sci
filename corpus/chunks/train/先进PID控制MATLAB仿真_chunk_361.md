# 7.3.4 仿真实例

一个典型的双关节刚性机械手示意图如图 7-5 所示。

![](image/071276efeb19f9137e841f461c367fbf8b1c2513281cc94d44f9a7772d2ff5b4.jpg)

<details>
<summary>text_image</summary>

m₂
l₂
q₂
m₁
l₁
q₁
g
</details>

图 7-5 双关节刚性机械手示意图

取二关节机械手系统，不考虑摩擦力和干扰，其动力学模型为

$$
D (q) \ddot {q} + C (q, \dot {q}) \dot {q} + G (q) = \tau
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} p _ {1} + p _ {2} + 2 p _ {3} \cos q _ {2} & p _ {2} + p _ {3} \cos q _ {2} \\ p _ {2} + p _ {3} \cos q _ {2} & p _ {2} \end{array} \right]

\boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - p _ {3} \dot {q} _ {2} \sin q _ {2} & - p _ {3} (\dot {q} _ {1} + \dot {q} _ {2}) \sin q _ {2} \\ p _ {3} \dot {q} _ {1} \sin q _ {2} & 0 \end{array} \right]

\boldsymbol {G} (\boldsymbol {q}) = \left[ \begin{array}{l} p _ {4} g \cos q _ {1} + p _ {5} g \cos (q _ {1} + q _ {2}) \\ p _ {5} g \cos (q _ {1} + q _ {2}) \end{array} \right]
$$

取 $p=\left[2.90\quad0.76\quad0.87\quad3.04\quad0.87\right]^{T}$ 。

被控对象初值为 $q_{0}=\left[0.09\quad-0.09\right]^{T}$ ， $\dot{q}_{0}=\left[0.0\quad0.0\right]^{T}$ 。仿真中，取位置指令为 $q_{d1}=0.5\sin(\pi t)$ ， $q_{d2}=\sin(\pi t)$ 。取控制器参数为 $K_{p}=\begin{bmatrix}100&0\\ 0&100\end{bmatrix}$ ， $K_{i}=\begin{bmatrix}100&0\\ 0&100\end{bmatrix}$ ， $K_{r}=15,\quad A=\begin{bmatrix}5.0&0\\ 0&5.0\end{bmatrix}$ 。控制律取式（7.13），采用 Simulink 和 S 函数进行控制系统的设计，仿真结果如图 7-6 和图 7-7 所示。

![](image/4d17d91d79c2fb973714dc1810939c1e920b602be876ca0f515131ec6eefff95.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position signal tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.5 | 0.5 |
| 2 | 0.0 | 0.0 |
| 3 | -0.5 | -0.5 |
| 4 | 0.0 | 0.0 |
| 5 | 0.5 | 0.5 |
| 6 | 0.0 | 0.0 |
| 7 | -0.5 | -0.5 |
| 8 | 0.0 | 0.0 |
| 9 | 0.5 | 0.5 |
| 10 | 0.0 | 0.0 |
</details>

![](image/bfbc09bee78c4d62f5154e0babc875e384d14e31491ccb29102d8e6a7054f287.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal speed signal | Speed signal tracking |
| --- | --- | --- |
| 0 | 1.5 | 1.5 |
| 1 | -1.5 | -1.5 |
| 2 | 1.5 | 1.5 |
| 3 | -1.5 | -1.5 |
| 4 | 1.5 | 1.5 |
| 5 | -1.5 | -1.5 |
| 6 | 1.5 | 1.5 |
| 7 | -1.5 | -1.5 |
| 8 | 1.5 | 1.5 |
| 9 | -1.5 | -1.5 |
| 10 | 1.5 | 1.5 |
</details>

图 7-6 关节 1 的位置速度跟踪

![](image/0fbb7448da2090a70e7d032f8963736d0c3d29496b6a4102722b1305eec762a8.jpg)

<details>
<summary>line</summary>
