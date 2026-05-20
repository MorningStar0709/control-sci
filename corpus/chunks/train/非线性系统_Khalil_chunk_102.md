当忽略摩擦力时 $(b=0)$ ，系统是保守系统，也就是说系统没有能量损耗。因此，系统在运动过程中E为常数，即沿系统的轨线有dE/dt=0。因为当c较小时， $E(x)=c$ 表示一条绕x=0的闭等高线（周线），同样可得到x=0是稳定平衡点的结论。在考虑摩擦的情况下 $(b>0)$ ，系统在运动过程中有能量损耗，即沿系统的轨线有 $dE/dt\leqslant0$ 。由于摩擦力的作用，系统在运动中不可能始终保持能量 E 为常数, 而是逐渐减少, 最终为零。这表明轨线随着 t 趋于无穷而趋近 x=0, 因而有可能通过检验 E 沿系统轨线的导数确定平衡点的稳定性。1892 年, Lyapunov 证明了能够用某些其他函数代替能量以确定平衡点的稳定性。设 $V: D \rightarrow R$ 为定义在包含原点的 $D \subset R^{n}$ 上的连续可微函数, V 沿方程(4.1) 轨线的导数用 $\dot{V}(x)$ 表示, 有

$$
\begin{array}{l} \dot {V} (x) = \sum_ {i = 1} ^ {n} \frac {\partial V}{\partial x _ {i}} \dot {x} _ {i} = \sum_ {i = 1} ^ {n} \frac {\partial V}{\partial x _ {i}} f _ {i} (x) \\ = \left[ \begin{array}{l l l l} \frac {\partial V}{\partial x _ {1}}, & \frac {\partial V}{\partial x _ {2}}, & \dots , & \frac {\partial V}{\partial x _ {n}} \end{array} \right] \left[ \begin{array}{c} f _ {1} (x) \\ f _ {2} (x) \\ \vdots \\ f _ {n} (x) \end{array} \right] = \frac {\partial V}{\partial x} f (x) \\ \end{array}
$$

$V$ 沿系统轨线的导数与系统方程有关, 因而系统不同, $\dot{V}(x)$ 也不同。如果 $\phi(t;x)$ 是方程(4.1)在 $t=0$ 时刻始于初始状态 $x$ 的解, 那么

$$\dot {V} (x) = \left. \frac {d}{d t} V (\phi (t; x)) \right| _ {t = 0}$$

于是,如果 $\dot{V}(x)$ 为负,V 将沿系统(4.1)的解减少。下面是李雅普诺夫稳定性定理。

定理4.1 设 $x = 0$ 是方程(4.1)的一个平衡点, $D \subset R^n$ 是包含原点的定义域。设 $V: D \to R$ 是连续可微函数, 如果

$$V (0) = 0, \quad V (x) > 0 \quad \text {在} D - \{0 \} \text {内} \tag {4.2}\dot {V} (x) \leqslant 0 \quad \text {在} D \text {内} \tag {4.3}$$

那么，原点 $x = 0$ 是稳定的。此外，如果

$$\dot {V} (x) < 0 \quad \text { 在 } D - \{0 \} \text { 内 } \tag {4.4}$$

那么,原点 x=0 是渐近稳定的。

证明:给定 $\varepsilon > 0$ , 选择 $r \in (0, \varepsilon]$ , 满足

$$B _ {r} = \{x \in R ^ {n} \mid \| x \| \leqslant r \} \subset D$$

设 $\alpha = \min_{\|x\| = r} V(x)$ ，则由式(4.2)得 $\alpha > 0$ 。取 $\beta \in (0, \alpha)$ ，并设

$$\Omega_ {\beta} = \{x \in B _ {r} \mid V (x) \leqslant \beta \}$$

那么, $\Omega_{\beta}$ 在 $B_{r}$ 内①(见图4.1)。集合 $\Omega_{\beta}$ 具有下面的性质, 即当 $t \geqslant 0$ 时, 在 $t = 0$ 时刻始于 $\Omega_{\beta}$ 内的任何轨线都保持在 $\Omega_{\beta}$ 内, 这是由式(4.3)得到的, 因为

![](image/615018f5e93322d0f656a926b7b07cf45e17002cddf6dc7d1b57f2deb122f088.jpg)

<details>
<summary>text_image</summary>

D
B_r
B_δ
Ω_β
</details>

图4.1 证明定理4.1中各集合的几何表示

$$\dot {V} (x (t)) \leqslant 0 \Rightarrow V (x (t)) \leqslant V (x (0)) \leqslant \beta , \forall t \geqslant 0$$

由于 $\Omega_{\beta}$ 是紧集②, 所以由定理3.3可得出这样的结论: 只要 $x(0) \in \Omega_{\beta}$ , 则对于所有 $t \geqslant 0$ , 方

程(4.1)有唯一解。因为 $V(x)$ 连续且 $V(0)=0$ ，故存在 $\delta>0$ 满足
