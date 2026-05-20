试求可控子系统与不可控子系统的动态方程。

9-28 系统各矩阵同习题 9-27, 试求可观测子系统与不可观测子系统的动态方程。

9-29 设被控系统状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & - 1 & 1 \\ 0 & - 1 & 1 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c} 0 \\ 0 \\ 1 0 \end{array} \right] \boldsymbol {u}
$$

可否用状态反馈任意配置闭环极点？求状态反馈阵，使闭环极点位于 $-10, -1 \pm j\sqrt{3}$ ，并画出状态变量图。

9-30 设被控系统动态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \boldsymbol {u}, \quad y = [ 1 \quad 0 ] \boldsymbol {x}
$$

试设计全维状态观测器，使闭环极点位于- $r,-2r(r>0)$ ，并画出状态变量图。

9-31 设系统传递函数为

$$\frac {(s - 1) (s + 2)}{(s + 1) (s - 2) (s + 3)}$$

试问能否利用状态反馈将传递函数变成

$$\frac {s - 1}{(s + 2) (s + 3)}$$

若有可能,求出一个满足要求的状态反馈阵 K,并画出状态变量图。(提示:状态反馈不改变原传递函数零点。)

9-32 试用李雅普诺夫第二法判断下列线性系统平衡状态的稳定性：

$$\dot {x} _ {1} = - x _ {1} + x _ {2}, \quad \dot {x} _ {2} = 2 x _ {1} - 3 x _ {2}$$

9-33 已知系统状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} 2 & \frac {1}{2} & - 3 \\ 0 & - 1 & 0 \\ 0 & \frac {1}{2} & - 1 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{c c} 1 & 0 \\ 0 & 2 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right]
$$

当 Q = I 时，P = ? 若选 Q 为正半定矩阵，Q = ? 对应 P = ? 判断系统稳定性。

9-34 设线性定常离散系统状态方程为

$$
\pmb {x} (k + 1) = \left[ \begin{array}{l l l} 0 & 1 & 0 \\ 0 & 0 & 1 \\ \frac {\pmb {k}}{2} & 0 & 0 \end{array} \right] \pmb {x} (k), \quad k > 0
$$

试求使系统渐近稳定的 k 值范围。

9-35 设工业机器人如图 9-47 所示, 其中两相伺服电机转动肘关节之后, 通过小臂移动机器人的手腕。假定弹簧的弹性系数为 k, 阻尼系数为 f, 并选取系统的如下状态变量:

$$x _ {1} = \phi_ {1} - \phi_ {2}, \quad x _ {2} = \frac {\omega_ {1}}{\omega_ {0}}, \quad x _ {3} = \frac {\omega_ {2}}{\omega_ {0}}$$

其中 $\omega_{0}^{2}=\frac{k(J_{1}+J_{2})}{J_{1}J_{2}}$ 。试列写该机器人的状态方程。

![](image/9d19543b9839606a7db9876465223e7c9839a72093eea47c98e496751f606c5e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["i(t) 电流"] --> B["电机"]
    B --> C["肘关节 ω₁"]
    C --> D["φ₁ J₁"]
    D --> E["k, f"]
    E --> F["φ₂ J₂"]
    F --> G["手腕 ω₂"]
```
</details>

图 9-47 工业机器人

9-36 为了完成空间站装配、卫星捕获等空间操作，航天飞机的货舱内装备了一种可膨胀机械臂的遥操作系统，如图9-48(a)所示。柔性机械臂的模型如图9-48(b)所示，其中 $J$ 是驱动电机的转动惯量， $u$ 为电机驱动转矩， $\theta_{1}$ 和 $\theta_{2}$ 为柔性臂转角， $k$ 为柔性臂的弹性系数， $M$ 和 $I$ 分别为负载质量与转动惯量， $l$ 为机械臂在负载上的作用点到负载重心的距离。若选取状态变量为 $x_{1} = \theta_{1}, x_{2} = \dot{\theta}_{1}, x_{3} = \theta_{2}, x_{4} = \dot{\theta}_{2}$ ，试列写柔性机械臂系统的线性化状态方程。
