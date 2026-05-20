# (2) 具有饱和特性的非线性控制系统

设具有饱和特性的非线性控制系统如图 8-30 所示。图中 T=1, K=4, $e_{0}=M_{0}=0.2$ ，系统初始状态为零。

![](image/2dd56f9299efb21bc78716f3bc502afa3721c09343c469423a68e9709a9d7c2b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> + --> e --> M0
    e --> M0
    M0 --> m --> K/(s(Ts+1))
    K --> c
    c --> - --> +
    + --> o((o))
    o --> e
```
</details>

图 8-30 具有饱和特性的非线性控制系统

取状态变量为 $e(t)$ 和 $\dot{e}(t)$ ，按饱和特性可列写以下三个线性微分方程：

$$T \ddot {e} + \dot {e} - K M _ {0} = T \ddot {r} + \dot {r}, \quad e \leqslant - e _ {0}T \ddot {e} + \dot {e} + K \frac {M _ {0}}{e _ {0}} e = T \ddot {r} + \dot {r}, \quad | e | < e _ {0} \tag {8-43}T \ddot {e} + \dot {e} + K M _ {0} = T \ddot {r} + \dot {r}, \quad e \geqslant e _ {0}$$

可知开关线 $e = -e_0$ 和 $e = e_0$ 将相平面分为负饱和区、线性区和正饱和区。下面分别研究系统在 $r(t) = R \cdot 1(t)$ 和 $r(t) = V_0t$ 作用下的相轨迹。

1) $r(t) = R \cdot 1(t)$ 。整理式(8-43)得

$$T \ddot {e} + \dot {e} - K M _ {0} = 0, \quad e \leqslant - e _ {0}T \ddot {e} + \dot {e} + K e = 0, \quad | e | < e _ {0} \tag {8-44}T \ddot {e} + \dot {e} + K M _ {0} = 0, \quad e \geqslant e _ {0}$$

这里涉及在饱和区需要确定形如

$$T \ddot {e} + \dot {e} + A = 0, \quad A \text {为常数} \tag {8-45}$$

的相轨迹。由上式得相轨迹微分方程

$$\frac {\mathrm{d} \dot {e}}{\mathrm{d} e} = \frac {- \dot {e} - A}{T \dot {e}} \neq \frac {0}{0}$$

相轨迹无奇点，而等倾线方程

$$\dot {e} = \frac {- A}{1 + \alpha T}$$

为一簇平行于横轴的直线，其斜率 $k$ 均为零。令 $\alpha = 0$ 得 $\dot{e} = -A$ ，即为特殊的等倾线 $(k = \alpha = 0)$ 。代入给定参数求得线性区的奇点为原点，且为实奇点，其特征根为 $s_{1,2} = -0.5 \pm j1.94$ ，所以奇点为稳定焦点。由零初始条件和输入 $r(t) = R \cdot 1(t)$ 得， $e(0) = R, \dot{e}(0) = 0$ 。取 $R = 2$ 绘制系统的相轨迹如图8-31所示。由图可见，相轨迹在 $e < -e_0$ 区域渐近趋近于 $\dot{e} = KM_0$ 的等倾线；在 $e > e_0$ 区域，渐近趋近于 $\dot{e} = -KM_0$ 的等倾线。相轨迹最终趋于坐标原点，系统稳定。

2) $r(t) = V_{0}t$ 。由 $\dot{r}(t) = V_{0}, \ddot{r}(t) = 0$ ，可分区间得下述三个线性微分方程：

$$T \ddot {e} + \dot {e} - \left(K M _ {0} + V _ {0}\right) = 0, \quad e \leqslant - e _ {0}T \left(e - \frac {V _ {0}}{K}\right) ^ {\prime \prime} + \left(e - \frac {V _ {0}}{K}\right) ^ {\prime} + K \left(e - \frac {V _ {0}}{K}\right) = 0, \quad | e | < e _ {0} \tag {8-46}T \ddot {e} + \dot {e} + \left(K M _ {0} - V _ {0}\right) = 0, \quad e \geqslant e _ {0}$$
