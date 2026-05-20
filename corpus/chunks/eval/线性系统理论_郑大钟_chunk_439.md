![](image/dff9bb085e6f4580479b1a033c593aef8a14fd9095c18c651df7f13e06980bd3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    v -->|+| Sum
    Sum --> C["C(s)"] --> Go["G₀(s)"] --> y
    y -->|-| Feedback
```
</details>

图 P11.2

11.9 对于图 $P$ 11.2 所示的单位输出反馈系统, 若受控系统的传递函数矩阵为

$$G _ {o} (s) = \left[ \frac {s + 2}{s (s - 2)} \quad \frac {1}{s ^ {2} - 4} \right]$$

试确定一个补偿器 $C(s)$ ，使得此单位输出反馈系统的极点为 $-1, -2 \pm i, -2$ 。

11.10 对于图 $P$ 11.2 所示的单位输出反馈系统, 若受控系统的传递函数矩阵为

$$
G _ {o} (s) = \left[ \begin{array}{l l} s & 0 \\ 0 & s ^ {2} \end{array} \right] ^ {- 1} \left[ \begin{array}{l l l} s & 1 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

试确定一个补偿器 $C(s)$ ，使得此单位输出反馈系统的分母矩阵为

$$
D _ {f} (s) = \left[ \begin{array}{c c} (s + 1) & 0 \\ 0 & (s + 1) ^ {2} \end{array} \right]
$$

11.11 考虑图 $P$ 11.2 所示的单位输出反馈系统, 令

$$G _ {o} (s) = N (s) D ^ {- 1} (s) = D _ {L} ^ {- 1} (s) N _ {L} (s)$$

为互质的 MFD，再设 $X(s)$ 和 $Y(s)$ 是使 $X(s)D(s) + Y(s)N(s) = I$ 成立的多项式矩阵。试证明：如果 $H(s)$ 为极点均具有负实部的任意有理分式阵，则如下形式的补偿器

$$C (s) = [ X (s) - H (s) N _ {L} (s) ] ^ {- 1} [ Y (s) + H (s) D _ {L} (s) ]$$

可使单位输出反馈系统为稳定。

11.12 给定受控系统的传递函数矩阵为:

$$
G _ {o} (s) = \left[ \begin{array}{l l} 1 & 1 \\ s & 1 \end{array} \right] \left[ \begin{array}{c c} 0 & s ^ {2} \\ s - 1 & s \end{array} \right] ^ {- 1}
$$

试设计一个观测器一控制器型的补偿器，使闭环系统的分母矩阵为

$$
D _ {f} (s) = \left[ \begin{array}{c c} (s + 1) ^ {3} & 0 \\ 0 & (s + 1) ^ {2} \end{array} \right]
$$

11.13 给定受控系统的传递函数矩阵为：

$$
G _ {o} (s) = \left[ \begin{array}{l l} s & 1 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c c c} s - 1 & s \\ 0 & s ^ {2} \end{array} \right] ^ {- 1}
$$

且采用图 P11.2 所示的控制方式, 试设计一个补偿器 $C(s)$ , 使闭环系统实现动态解耦, 同时满足如下要求:

(i) $C(s)$ 是严格真的；  
(ii) 闭环系统的传递函数矩阵 $G_{F}(s)$ 是严格真的；  
(iii) 解耦后， $g_{1}(s)$ 的期望极点均为 -2， $g_{2}(s)$ 的期望极点均为 -3。

11.14 考虑图 P11.3 的单位输出反馈系统, 其中 $G_{o}(s)$ 如上题所示, 试确定补偿器 $P(s)$ 和 $C(s)$ 使闭环系统相对于单位阶跃的参考输入 $v = 1(t)\begin{bmatrix}1\\ 1\end{bmatrix}$ 实现静态解耦, 同时规定闭环系统传递矩阵的极点即 $\det D_{F}(s) = 0$ 的根均为 -2。

11.15 考虑图 P11.4 的单位输出反馈系统, 其中 $G_{o}(s) = N_{r}(s)D_{r}^{-1}(s)$ 如题 11.12 所示, $D^{-1}(s)N(s)$ 为 $G_{o}(s)$ 的一左互质 MFD。再知参考输入和扰动为

$$
\boldsymbol {v} (t) = 1 (t) \left[ \begin{array}{l} 1 \\ 1 \end{array} \right], \quad \boldsymbol {w} (t) = e ^ {t} \left[ \begin{array}{l} 1 \\ 1 \end{array} \right]
$$

试确定一个补偿器 $C(s)$ ，使闭环系统实现无静差跟踪，同时使闭环极点即 $\det D_{f}(s) = 0$ 的根均为-2。

![](image/1632893fd1e5016338275aa2121ebb9965ce5e2bc5f637879de0a8d61203ddb9.jpg)

<details>
<summary>flowchart</summary>
