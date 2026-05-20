# 5.6.4 仿真实例

针对双关节刚性机械手,其动力学方程为式(5.67),具体表达为

$$
\left[ \begin{array}{c c} D _ {1 1} (q _ {2}) & D _ {1 2} (q _ {2}) \\ D _ {2 1} (q _ {2}) & D _ {2 2} (q _ {2}) \end{array} \right] \left[ \begin{array}{l} \ddot {q} _ {1} \\ \ddot {q} _ {2} \end{array} \right] + \left[ \begin{array}{c c} - C _ {1 2} (q _ {2}) \dot {q} _ {2} & - C _ {1 2} (q _ {2}) (\dot {q} _ {1} + \dot {q} _ {2}) \\ C _ {1 2} (q _ {2}) \dot {q} _ {1} & 0 \end{array} \right]
\binom {g _ {1} \left(q _ {1} + q _ {2}\right) g} {g _ {2} \left(q _ {1} + q _ {2}\right) g} + F (q, \dot {q}, \ddot {q}) = \binom {\tau_ {1}} {\tau_ {2}}
$$

其中

$$D _ {1 1} \left(q _ {2}\right) = \left(m _ {1} + m _ {2}\right) r _ {1} ^ {2} + m _ {2} r _ {2} ^ {2} + 2 m _ {2} r _ {1} r _ {2} \cos \left(q _ {2}\right)D _ {1 2} \left(q _ {2}\right) = D _ {2 1} \left(q _ {2}\right) = m _ {2} r _ {2} ^ {2} + m _ {2} r _ {1} r _ {2} \cos \left(q _ {2}\right)D _ {2 2} \left(q _ {2}\right) = m _ {2} r _ {2} ^ {2}C _ {1 2} \left(q _ {2}\right) = m _ {2} r _ {1} r _ {2} \sin \left(q _ {2}\right)\boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) = \boldsymbol {F} _ {\mathrm{r}} (\dot {\boldsymbol {q}}) + \tau_ {\mathrm{d}}$$

令 $y=[q_{1},q_{2}]^{T},\tau=[\tau_{1},\tau_{2}]^{T},x=[q_{1},\dot{q}_{1},q_{2},\dot{q}_{2}]^{T}$ 。取系统参数为 $r_{1}=1m,r_{2}=0.8m$ ， $m_{1}=1kg,m_{2}=1.5kg$ 。

控制目标是使双关节的输出 $q_{1}$ 、 $q_{2}$ 分别跟踪期望轨迹 $q_{d1}=0.3\sin t$ 和 $q_{d2}=0.3\sin t$ 。定义隶属函数为

$$\mu_ {A _ {i} ^ {l}} (x _ {i}) = \exp \left(- \left(\frac {x _ {i} - \overline {{x _ {i} ^ {l}}}}{\pi / 2 4}\right) ^ {2}\right)$$

式中， $\overline{x}_{i}^{l}$ 分别为 $-\pi/6, -\pi/12, 0, \pi/12$ 和 $\pi/6, i = 1, 2, 3, 4, 5, A_{i}$ 分别为 NB, NS, ZO, PS, PB。

针对带有摩擦的情况，采用基于摩擦模糊补偿的机械手控制，取控制器设计参数为 $\lambda_{1} = 10$ ， $\lambda_{2} = 10, K_{\mathrm{D}} = 20I, I$ 为 $2\times 2$ 单位阵， $\Gamma_{1} = \Gamma_{2} = 0.0001$ 。取系统初始状态为 $q_{1}(0) = q_{2}(0) = \dot{q}_{1}(0) = \dot{q}_{2}(0) = 0$ ，取摩擦项为 $F_{\mathrm{r}}(\dot{\pmb{q}}) = \begin{bmatrix} 15\dot{q}_1 + 6\mathrm{sign}(\dot{q}_1) \\ 15\dot{q}_2 + 6\mathrm{sign}(\dot{q}_2) \end{bmatrix}$ ，取干扰项为 $\pmb{\tau}_{\mathrm{d}} = \begin{bmatrix} 0.05\sin (20t) \\ 0.1\sin (20t) \end{bmatrix}$ 。在鲁棒控制律中，取 $\pmb{W} = \begin{bmatrix} 1.5 & 0 \\ 0 & 1.5 \end{bmatrix}$ 。

采用鲁棒控制律式(5.78)，自适应律取式(5.79)，仿真结果如图5-24至图5-26所示。

![](image/1e15f792428ada735f5ef52014ccd1e9bde848fa2784a113afb52ccf15264ee1.jpg)

<details>
<summary>line</summary>
