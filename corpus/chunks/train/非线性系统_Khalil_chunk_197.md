证明: 设 $V_{1}(x_{1})$ 和 $V_{2}(x_{2})$ 分别是 $H_{1}$ 和 $H_{2}$ 的存储函数, 如果任一分支是无记忆函数, 取 $V_{i}=0$ , 则 $e_{i}^{T}y_{i}\geqslant\dot{V}_{i}$

由图 6.11 所示的反馈连接可知

$$e _ {1} ^ {\mathrm{T}} y _ {1} + e _ {2} ^ {\mathrm{T}} y _ {2} = \left(u _ {1} - y _ {2}\right) ^ {\mathrm{T}} y _ {1} + \left(u _ {2} + y _ {1}\right) ^ {\mathrm{T}} y _ {2} = u _ {1} ^ {\mathrm{T}} y _ {1} + u _ {2} ^ {\mathrm{T}} y _ {2}$$

因此 $u^{\mathrm{T}}y = u_{1}^{\mathrm{T}}y_{1} + u_{2}^{\mathrm{T}}y_{2}\geqslant \dot{V}_{1} + \dot{V}_{2}$

取 $V(x)=V_{1}(x_{1})+V_{2}(x_{2})$ 为反馈连接的存储函数, 得

$$u ^ {\mathrm{T}} y \geqslant \dot {V}$$

利用定理 6.1 和上一节里关于无源系统的稳定性性质, 我们可以直接得出反馈连接稳定性的结论。首先讨论 $L_{2}$ 稳定性, 下一个引理是引理 6.5 的一个直接结果。

引理 6.8 两个严格输出无源系统, 满足

$$e _ {i} ^ {\mathrm{T}} y _ {i} \geqslant \dot {V} _ {i} + \delta_ {i} y _ {i} ^ {\mathrm{T}} y _ {i}, \quad \delta_ {i} > 0$$

其反馈连接是有限增益 $L_{2}$ 稳定的，且 $L_{2}$ 增益小于或等于 $1/\min\left\{\delta_{1},\delta_{2}\right\}$ 。

证明: 取 $V = V_{1} + V_{2}, \delta = \min\left\{\delta_{1}, \delta_{2}\right\}$ ，有

$$
\begin{array}{l} u ^ {T} y = e _ {1} ^ {T} y _ {1} + e _ {2} ^ {T} y _ {2} \geqslant \dot {V} _ {1} + \delta_ {1} y _ {1} ^ {T} y _ {1} + \dot {V} _ {2} + \delta_ {2} y _ {2} ^ {T} y _ {2} \\ \geqslant \dot {V} + \delta \left(y _ {1} ^ {\mathrm{T}} y _ {1} + y _ {2} ^ {\mathrm{T}} y _ {2}\right) = \dot {V} + \delta y ^ {\mathrm{T}} y \\ \end{array}
$$

引理6.5的证明说明,利用不等式

$$u ^ {T} y \geqslant \dot {V} + \delta y ^ {T} y \tag {6.32}$$

得出不等式 $\dot{V}\leqslant\frac{1}{2\delta}u^{T}u-\frac{\delta}{2}y^{T}y$ (6.33)

然后用其证明有限增益 $L_{2}$ 稳定性。在引理6.8中，为反馈连接建立了不等式(6.32)，进而推导出不等式(6.33)。然而，即使不等式(6.32)对于反馈连接不成立，仍可得出形如不等式(6.33)的不等式。这一思想用于下一个定理，以证明更具有普遍意义的结果，引理6.8为一个特例。□

定理 6.2 考虑图 6.11 所示的反馈连接。假设对于某个存储函数 $V_{i}(x_{i})$ ，各反馈分支满足不

等式 $e_i^{\mathrm{T}}y_i\geqslant \dot{V}_i + \varepsilon_i e_i^{\mathrm{T}}e_i + \delta_i y_i^{\mathrm{T}}y_i,\quad i = 1,2$ (6.34)

若 $\varepsilon_{1}+\delta_{2}>0,\quad\varepsilon_{2}+\delta_{1}>0$ (6.35)

则从 u 到 y 的闭环映射是有限增益 $L_{2}$ 稳定的。

证明: 当 i=1,2 时, 将不等式(6.34)相加, 并利用

$$
\begin{array}{l} e _ {1} ^ {\mathrm{T}} y _ {1} + e _ {2} ^ {\mathrm{T}} y _ {2} = u _ {1} ^ {\mathrm{T}} y _ {1} + u _ {2} ^ {\mathrm{T}} y _ {2} \\ e _ {1} ^ {\mathrm{T}} e _ {1} = u _ {1} ^ {\mathrm{T}} u _ {1} - 2 u _ {1} ^ {\mathrm{T}} y _ {2} + y _ {2} ^ {\mathrm{T}} y _ {2} \\ e _ {2} ^ {\mathrm{T}} e _ {2} = u _ {2} ^ {\mathrm{T}} u _ {2} + 2 u _ {2} ^ {\mathrm{T}} y _ {1} + y _ {1} ^ {\mathrm{T}} y _ {1} \\ \end{array}
$$
