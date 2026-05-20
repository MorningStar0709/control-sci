# 6.6 习题

6.1 如图 6.7 所示, 验证扇形区域 $\left[K_{1}, K_{2}\right]$ 内的函数可通过输入前馈及输出反馈转换为扇形区域 $[0, \infty]$ 内的函数。

6.2 考虑系统 $a\dot{x} = -x + \frac{1}{k} h(x) + u, \quad y = h(x)$

其中 a 和 k 是正常数, $h \in [0, k]$ 。证明系统是无源的, 其存储函数为 $V(x) = a \int_{0}^{x} h(\sigma) d\sigma$ 。

6.3 考虑系统 $\dot{x}_{1}=x_{2},\quad\dot{x}_{2}=-h(x_{1})-ax_{2}+u,\quad y=\alpha x_{1}+x_{2}$

其中 $0 < \alpha < a, h \in (0, \infty]$ 。证明系统是严格无源的。

提示:用例 4.5 中的 $V(x)$ 作为存储函数。

6.4 考虑系统 $\dot{x}_{1}=x_{2},\quad\dot{x}_{2}=-h(x_{1})-ax_{2}+u,\quad y=kx_{2}+u$

其中 $a > 0, k > 0, h \in [\alpha_1, \infty], \alpha_1 > 0$ 。设 $V(x) = k \int_{0}^{x_1} h(s) ds + x^{\mathrm{T}}Px$ ，其中 $p_{11} = ap_{12}$ ， $p_{22} = k/2, 0 < p_{12} < \min\{2\alpha_1, ak/2\}$ 。以 $V(x)$ 作为存储函数，证明系统是严格无源的。

6.5 考虑如方框图 6.15 所示的系统, 其中 $u, y \in R^{p}, M$ 和 K 是正定对称矩阵, $h \in [0, K]$ , 且对于所有 x, 有 $\int_{0}^{x} h^{\mathrm{T}}(\sigma) M d\sigma \geqslant 0$ 。证明系统是严格输出无源的。

![](image/4f6fc2f2245364b8a64f67bd8961067d443edb5d6a6e83cc22b63c24f151f63c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u"] --> B["(Ms + K)^-1"]
    B --> C["x"]
    C --> D["h(·)"]
    D --> E["y"]
```
</details>

图6.15 习题6.5

6.6 证明两个无源(分别为严格输入无源的,严格输出无源的,严格无源的)动力学系统的并联连接仍是无源的(分别为严格输入无源的,严格输出无源的,严格无源的)。

6.7 证明传递函数 $(b_{0}s+b_{1})/(s_{2}+a_{1}s+a_{2})$ 是严格正实的,当仅且当所有系数都为正,且 $b_{1}<a_{1}b_{0}$ 。

6.8 考虑方程(6.14)到方程(6.16)，并假设 $D+D^{T}$ 是非奇异阵。证明P满足Riccati方程

$$P A _ {0} + A _ {0} ^ {\mathrm{T}} P - P B _ {0} P + C _ {0} = 0$$

其中 $A_0 = -(\epsilon / 2)I - A + B(D + D^{\mathrm{T}})^{-1}C, B_0 = B(D + D^{\mathrm{T}})^{-1}B^{\mathrm{T}}$ 和 $C_0 = -C^{\mathrm{T}}(D + D^{\mathrm{T}})^{-1}C$ 。

6.9 证明如果系统是严格输入无源的, $\varphi(u)=\epsilon u$ ,且是有限增益 $L_{2}$ 稳定的,则存在一个存储函数V及正常数 $\epsilon_{1}$ 和 $\delta_{1}$ ,使得

$$u ^ {\mathrm{T}} y \geqslant \dot {V} + \epsilon_ {1} u ^ {\mathrm{T}} u + \delta_ {1} y ^ {\mathrm{T}} y$$

6.10 考虑 $m$ 连杆机器人的运动方程, 如习题 1.4 所述。假设 $P(q)$ 是 $q$ 的正定函数, 且 $g(q) = 0$ 在 $q = 0$ 处有孤立解。

(a) 用总能量 $V=\frac{1}{2}\dot{q}^{\mathrm{T}}M(q)\dot{q}+P(q)$ 作为存储函数, 证明从 u 到 $\dot{q}$ 的映射是无源的。

(b) $u = -K_{d}\dot{q} + v, K_{d}$ 是正对角常数阵。证明从 v 到 $\dot{q}$ 的映射是严格输出无源的。

(c) 证明 $u = -K_{d}\dot{q}$ , 使原点 $(q = 0, \dot{q} = 0)$ 是渐近稳定的, 其中 $K_{d}$ 是正对角常数阵。在什么附加条件下系统是全局渐近稳定的?

6.11 （见文献[151]）旋转刚性航天器的欧拉方程为
