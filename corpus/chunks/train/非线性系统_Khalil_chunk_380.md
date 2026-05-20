$$H (s) = \frac {N (s)}{Q (s) N (s) + R (s)} = \frac {\frac {1}{Q (s)}}{1 + \frac {1}{Q (s)} \frac {R (s)}{N (s)}}$$

这样 $H(s)$ 就可以表示为一个负反馈连接, $1/Q(s)$ 在正向通路, $R(s)/N(s)$ 在反馈通路(见图 13.1)。 $\rho$ 阶传递函数 $1/Q(s)$ 没有零点, 可由 $\rho$ 阶状态向量

$$
\xi = \left[ \begin{array}{l l l l} y, & \dot {y}, & \dots , & y ^ {(\rho - 1)} \end{array} \right] ^ {\mathrm{T}}
$$

实现,得到的状态模型为

$$\dot {\xi} = (A _ {c} + B _ {c} \lambda^ {\mathrm{T}}) \xi + B _ {c} b _ {m} ey = C _ {c} \xi$$

其中 $(A_{c},B_{c},C_{c})$ 是 $\rho$ 积分器链的标准形表达式,即

![](image/b96a7f48b47b0bb8bc7665325bc5c0e17b922ba8682ef217803d296a93f5b4c2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> +
    + --> e --> |1/Q(s)| y
    y --> w --> |R(s)/N(s)| w
    w --> - --> +
    + --> e
```
</details>

图 13.1 $H(s)$ 的反馈表示

$$
A _ {c} = \left[ \begin{array}{l l l l l} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & & \ddots & & \vdots \\ \vdots & & & 0 & 1 \\ 0 & \dots & \dots & 0 & 0 \end{array} \right], B _ {c} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], C _ {c} = \left[ \begin{array}{l l l l l} 1 & 0 & \dots & 0 & 0 \end{array} \right] \tag {13.10}
$$

且 $\lambda \in R^{\rho}$ 。设 $(A_0,B_0,C_0)$ 是传递函数 $R(s) / N(s)$ 的最小实现，即

$$\dot {\eta} = A _ {0} \eta + B _ {0} yw = C _ {0} \eta$$

$A_{0}$ 的特征值是多项式 $N(s)$ 的零点, 也是传递函数 $H(s)$ 的零点。从反馈连接可以看出, $H(s)$ 可由状态模型

$$\dot {\eta} = A _ {0} \eta + B _ {0} C _ {c} \xi \tag {13.11}\dot {\xi} = A _ {c} \xi + B _ {c} (\lambda^ {T} \xi - b _ {m} C _ {0} \eta + b _ {m} u) \tag {13.12}y = C _ {c} \xi \tag {13.13}$$

实现。利用 $(A_{c}, B_{c}, C_{c})$ 的特殊结构可直接验证

$$y ^ {(\rho)} = \lambda^ {\mathrm{T}} \xi - b _ {m} C _ {0} \eta + b _ {m} u$$

由(输入-输出线性化)状态反馈控制

$$u = \frac {1}{b _ {m}} [ - \lambda^ {\mathrm{T}} \xi + b _ {m} C _ {0} \eta + v ]$$

可得系统 $\dot{\eta} = A_{0}\eta + B_{0}C_{c}\xi$

$$\dot {\xi} = A _ {c} \xi + B _ {c} vy = C _ {c} \xi$$

其输入-输出映射是一个 $\rho$ 积分器链，且其状态子向量 $\eta$ 在输出 y 是不可观测的。假设希望把输出稳定为一个恒定参考信号 r，这就要求把 $\xi$ 稳定在 $\xi^{*} = (r, 0, \cdots, 0)^{\mathrm{T}}$ 处。通过变量代换 $\zeta = \xi - \xi^{*}$ ，把平衡点转移至原点，这样问题则简化为 $\zeta = A_{c}\zeta + B_{c}v$ 的稳定性问题。取 $v = -K\zeta = -K(\xi - \xi^{*})$ ，其中 $A_{c} - B_{c}K$ 是赫尔维茨矩阵，最后得控制律为

$$u = \frac {1}{b _ {m}} [ - \lambda^ {\mathrm{T}} \xi + b _ {m} C _ {0} \eta - K (\xi - \xi^ {*}) ]$$

相应的闭环系统为 $\dot{\eta} = A_{0}\eta + B_{0}C_{c}(\xi^{*} + \zeta)$

$$\dot {\zeta} = (A _ {c} - B _ {c} K) \zeta$$
