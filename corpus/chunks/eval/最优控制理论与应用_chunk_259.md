# 12.3.1 导弹运动状态方程的建立

导弹与目标的运动关系是非线性的,如果把导弹与目标的运动方程相对于理想弹道线性化,可得导弹运动的线性状态方程。假设导弹和目标在同一平面内运动,如图 12-6 所示。选 $oxy$ 为固定坐标。导弹速度向量 $\vec{V}_M$ 与 $oy$ 轴成 $\theta$ 角,目标速度向量为 $\vec{V}_T$ 与 $oy$ 轴成 $\theta_T$ 角。导弹与目标的连线 $MT$ 与 $oy$ 轴成 $q$ 角。假定导弹以尾追的方式攻击目标。坐标轴 $ox$ 和 $oy$ 的方向可以任意选择,使 $\theta, \theta_T$ 和 $q$ 都比较小。再假定导弹和目标均匀速飞行,也就是说 $V_M$ 和 $V_T$ 均为恒值。使用相对坐标状态变量,设 $x$ 为导弹与目标在 $ox$ 轴方向上的距离偏差, $y$ 为导弹与目标在 $oy$ 轴方向上的距离偏差,即

$$
\left\{ \begin{array}{l} \boldsymbol {x} = \boldsymbol {x} _ {T} - \boldsymbol {x} _ {M} \\ \boldsymbol {y} = \boldsymbol {y} _ {T} - \boldsymbol {y} _ {M} \end{array} \right. \tag {12-2}
$$

![](image/6172251be462b18acdaa94ab776209d558e8c2fce435748166e04b6daae93514.jpg)

<details>
<summary>text_image</summary>

x
x_T
x_M
O
y_M
y
R
M
q
θ
V_M
H
T
V_T
θ_T
y_T
</details>

图12-6 导弹和目标运动几何关系图

将上式对 t 求导, 并根据导弹和目标的关系(如图 12-6 所示)可得

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = \dot {\boldsymbol {x}} _ {T} - \dot {\boldsymbol {x}} _ {M} = \boldsymbol {V} _ {T} \sin \boldsymbol {\theta} _ {T} - \boldsymbol {V} _ {M} \sin \boldsymbol {\theta} \\ \dot {\boldsymbol {y}} = \dot {\boldsymbol {y}} _ {T} - \dot {\boldsymbol {y}} _ {M} = \boldsymbol {V} _ {T} \cos \boldsymbol {\theta} _ {T} - \boldsymbol {V} _ {M} \cos \boldsymbol {\theta} \end{array} \right. \tag {12-3}
$$

假定 $\pmb{\theta}$ 和 $\pmb{\theta}_T$ 比较小，因此 $\sin \pmb{\theta}_T \approx \pmb{\theta}_T, \sin \pmb{\theta} \approx \pmb{\theta}, \cos \pmb{\theta}_T \approx 1, \cos \pmb{\theta} \approx 1$ ，则

$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = \dot {\boldsymbol {x}} _ {T} - \dot {\boldsymbol {x}} _ {M} = \boldsymbol {V} _ {T} \boldsymbol {\theta} _ {T} - \boldsymbol {V} _ {M} \boldsymbol {\theta} \\ \dot {\boldsymbol {y}} = \dot {\boldsymbol {y}} _ {T} - \dot {\boldsymbol {y}} _ {M} = \boldsymbol {V} _ {T} - \boldsymbol {V} _ {M} \end{array} \right. \tag {12-4}
$$

以 $x_{1}$ 表示 $\pmb{x},\pmb{x}_2$ 表示 $\dot{\pmb{x}}$ （即 $\dot{\pmb{x}}_1$ ），则

$$\dot {\pmb {x}} _ {1} = \pmb {x} _ {2} \tag {12-5}\dot {\boldsymbol {x}} _ {2} = \ddot {\boldsymbol {x}} = \boldsymbol {V} _ {T} \dot {\boldsymbol {\theta}} _ {T} - \boldsymbol {V} _ {M} \dot {\boldsymbol {\theta}} \tag {12-6}$$

式中 $V_{T}\dot{\theta}_{T}$ 表示目标的横向加速度， $V_{M}\dot{\theta}$ 表示导弹横向加速度，分别

以 $a_{T}$ 和 $a_{M}$ 表示,那么

$$\dot {\boldsymbol {x}} _ {2} = \boldsymbol {a} _ {T} - \boldsymbol {a} _ {M} \tag {12-7}$$
