# 14.1.3 仿真实例

针对被控对象式（14.1），选二关节机械手系统（不考虑重力、摩擦力和干扰），其动力学模型为

$$D (q) \ddot {q} + C (q, \dot {q}) \dot {q} = \tau$$

其中

$$
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} p _ {1} + p _ {2} + 2 p _ {3} \cos q _ {2} & p _ {2} + p _ {3} \cos q _ {2} \\ p _ {2} + p _ {3} \cos q _ {2} & p _ {2} \end{array} \right]

\boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - p _ {3} \dot {q} _ {2} \sin q _ {2} & - p _ {3} (\dot {q} _ {1} + \dot {q} _ {2}) \sin q _ {2} \\ p _ {3} \dot {q} _ {1} \sin q _ {2} & 0 \end{array} \right]
$$

取 $p=\left[2.90\quad0.76\quad0.87\quad3.04\quad0.87\right]^{T}$ ， $q_{0}=\left[0.0\quad0.0\right]^{T}$ ， $\dot{q}_{0}=\left[0.0\quad0.0\right]^{T}$ 。

位置指令为 $q_{\mathrm{d}}(0) = [1.0 \quad 1.0]^{\mathrm{T}}$ ，在控制器式（14.2）中，取 $K_{\mathrm{p}} = \begin{bmatrix} 100 & 0 \\ 0 & 100 \end{bmatrix}$ ， $K_{\mathrm{d}} = \begin{bmatrix} 100 & 0 \\ 0 & 100 \end{bmatrix}$ ，仿真结果见图14-1和图14-2所示。

![](image/2c9c5f1286448efc4c7dff8899d48fd11b6b0ea8f99631e2be7d2c07e6a8be60.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking of link 1 |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 0.8 |
| 3 | 0.9 |
| 4 | 0.95 |
| 5 | 0.98 |
| 6 | 0.99 |
| 7 | 0.995 |
| 8 | 0.998 |
| 9 | 0.999 |
| 10 | 1 |
</details>

![](image/21df547f9d352d5364178e3f3bb6b0458e64f76c33605da4d7ca70104ece5d76.jpg)

<details>
<summary>line</summary>

| time(s) | position tracking of link 2 |
| --- | --- |
| 0 | 0 |
| 1 | 0.6 |
| 2 | 0.8 |
| 3 | 0.9 |
| 4 | 0.95 |
| 5 | 0.98 |
| 6 | 0.99 |
| 7 | 0.995 |
| 8 | 0.998 |
| 9 | 0.999 |
| 10 | 1 |
</details>

图 14-1 双力臂的阶跃响应

![](image/fd643660ba229ea35b2ddc144cef3a30aaab55224083abac261d6dfd2b692772.jpg)

<details>
<summary>line</summary>

| time(s) | to/1 |
| --- | --- |
| 0 | 30 |
| 1 | -5 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/50affcfa6c2be7b8b94ca7b75a3421fca099035f6a83fabf32e87be43fa640c1.jpg)

<details>
<summary>line</summary>

| time(s) | tol2 |
| --- | --- |
| 0 | 10 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

图 14-2 独立 PD 控制的控制输入

仿真中，当改变参数 $K_{p}$ 、 $K_{d}$ 时，只要满足 $K_{d} > 0$ 、 $K_{p} > 0$ ，都能获得比较好的仿真结果。完全不受外力没有任何干扰的机械手系统是不存在的，独立的 PD 控制只能作为基础来考虑分析，但对它的分析是有重要意义的。
