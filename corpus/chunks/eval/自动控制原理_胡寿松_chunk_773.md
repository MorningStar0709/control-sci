# (2) 末端时刻自由时的横截条件

![](image/745e828655014d7d0eb3d303e952de6c32e043fbac7216d95645f6a49c5e0a0b.jpg)

<details>
<summary>line</summary>

| t | x(t) | x*(t_f) |
| --- | --- | --- |
| t₀ | x(t₀) | x*(t_f) |
| t_f | δx(t_f) | δx*(t_f) |
| t_f+δt_f | c(t) | c(t) |
</details>

图 10-2 末端时刻自由时的变分问题

$t_{f}$ 自由且 $x(t_{f})$ 自由或受约束情况，属于变动端点情况。在变动端点问题中，可以证明：极值仅在欧拉方程的解 $x=x(t, c_{1}, c_{2})$ 上达到。其中，待定系数 $c_{1}$ 和 $c_{2}$ 由横截条件确定。因此，泛函极值由 $x(t, c_{1}, c_{2})$ 一类函数确定。

设 $t_f$ 自由，起点固定 $\pmb{x}(t_0) = \pmb{x}_0$ ，末端有约束 $\pmb{x}(t_f) = \pmb{c}(t_f)$ 的变分问题如图10-2所示。图中， $\pmb{x}^{*}(t)$ 为极值轨线； $\pmb{x}(t)$ 为 $\pmb{x}^{*}(t)$ 邻域内的任一条容许轨线； $(x_0,t_0)$

表示起点；点 $(\pmb{x}_f, t_f)$ 到点 $(\pmb{x}_f + \delta \pmb{x}_f, t_f + \delta t_f)$ 表示变动端； $\pmb{c}(t)$ 表示端点约束曲线，要求 $x(t_f) = c(t_f)$ ； $\delta t_f$ 为微变量，表示末端时刻的变分。例如，利用地空导弹截击按程序机构控制飞行轨迹的高空无人侦察机即属于这类问题。其中，导弹轨迹 $x(t)$ 和无人机轨迹 $c(t)$ 都随时间而变，但要求有 $x(t_f) = c(t_f)$ 。

由图 10-2 可见，在末端受约束时，存在如下近似关系式：

$$\delta \boldsymbol {x} (t _ {f}) = \delta \boldsymbol {x} _ {f} - \dot {\boldsymbol {x}} (t _ {f}) \delta t _ {f} \tag {10-26}\delta \boldsymbol {x} _ {f} = \dot {\boldsymbol {c}} (t _ {f}) \delta t _ {f} \tag {10-27}$$

如果末端 $x(t_f)$ 自由，由于约束曲线 $\pmb{c}(t)$ 不存在，故仅存在关系式(10-26)。

设性能指标泛函为下列连续泛函：

$$J [ \boldsymbol {x} ] = \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \dot {\boldsymbol {x}}, t) \mathrm{d} t \tag {10-28}$$

容许轨线 $x(t)$ 与极值轨线 $x^{*}(t)$ 之间有如下关系：

$$\boldsymbol {x} (t) = \boldsymbol {x} ^ {*} (t) + \delta \boldsymbol {x} (t), \quad \dot {\boldsymbol {x}} (t) = \dot {\boldsymbol {x}} ^ {*} (t) + \delta \dot {\boldsymbol {x}} (t) \tag {10-29}$$

当末端由 $(x_{f},t_{f})$ 位置移动到 $(x_{f} + \delta x_{f},t_{f} + \delta t_{f})$ 位置时，产生如下泛函增量：
