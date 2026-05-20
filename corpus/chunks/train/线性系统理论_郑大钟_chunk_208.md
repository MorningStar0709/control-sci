$$\dot {\boldsymbol {x}} ^ {*} (t) = A \boldsymbol {x} ^ {*} (t) + B \boldsymbol {u} ^ {*} (t), \quad \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0} \tag {5.243}$$

而最优性能值为:

$$J ^ {*} = \boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0}, \quad \forall \boldsymbol {x} _ {0} \neq 0 \tag {5.244}$$

其中，P 为下述矩阵黎卡提代数方程的正定对称解阵：

$$P A + A ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {5.245}$$

结论 2 对于定常的无限时间 LQ 调节问题 (5.210) 和 (5.211)，其最优调节系统是一个状态反馈系统，且保持定常性，同时状态反馈增益阵 $K^{*} = R^{-1}BP$ 是唯一的，且为常量矩阵。最优调节系统的动态方程为：

$$\dot {\boldsymbol {x}} ^ {*} = \left[ A - B R ^ {- 1} B ^ {T} P \right] \boldsymbol {x} ^ {*}, \quad \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0}, t \geqslant 0 \tag {5.246}$$

稳定性和指定衰减度 继续讨论定常的无限时间 LQ 调节问题，其中假定 $\{A, B\}$ 为能控，R > 0, Q > 0 或 $Q \geqslant 0$ 且 $\{A, H\}$ 为能观测，其中 $Q = H^{T}H$ 。并且，相应的最优调节系统由式 (5.246) 所给出。现首先讨论此系统的稳定性问题。

结论 1 最优调节系统 (5.246) 必是大范围渐近稳定的。

证 分成两类情况来加以证明。

第一种情况： $Q > 0$ 。此时，如前面所证得的， $P > 0$ 。故取李亚普诺夫函数 $V(\pmb {x}) = \pmb{x}^{T}\pmb {P}\pmb{x}$ 为正定。而利用(5.246）有

$$
\begin{array}{l} \dot {V} (\boldsymbol {x}) = \frac {d V (\boldsymbol {x})}{d t} = \dot {\boldsymbol {x}} ^ {T} P \boldsymbol {x} + \boldsymbol {x} ^ {T} P \dot {\boldsymbol {x}} \\ = \boldsymbol {x} ^ {T} \left(A ^ {T} P - P B R ^ {- 1} B ^ {T} P\right) \boldsymbol {x} + \boldsymbol {x} ^ {T} \left(P A - P B R ^ {- 1} B ^ {T} P\right) \boldsymbol {x} \\ = x ^ {T} \left[ \left(P A + A ^ {T} P - P B R ^ {- 1} B ^ {T} P\right) - P B R ^ {- 1} B ^ {T} P \right] x \\ = - \boldsymbol {x} ^ {T} (Q + P B R ^ {- 1} B ^ {T} P) \boldsymbol {x} \tag {5.247} \\ \end{array}
$$

由 $Q > 0$ 和 $R > 0$ ，故知 $\dot{V}(\pmb{x})$ 为负定。此外易知，当 $\| \pmb{x} \| \to \infty$ 时有 $V(\pmb{x}) \to \infty$ 。于是，由李亚普诺夫主稳定性定理即知，闭环系统（5.246）为大范围渐近稳定。

第二种情况： $Q \geqslant 0$ 且 $(A, H)$ 为能观测。如前已证得，此种情况下同样有 $P > 0$ 。因此，取 $V(x) = x^T P x$ 为正定；且由(5.247)有

$$\dot {V} (\boldsymbol {x}) = - \boldsymbol {x} ^ {T} (Q + P B R ^ {- 1} B ^ {T} P) \boldsymbol {x} \tag {5.248}$$

故由 $Q \geqslant 0$ 和 $R > 0$ 可知 $\dot{V}(\pmb{x})$ 为负半定。下面，来证明对一切 $\pmb{x}_0 \neq \pmb{0}$ 的运动解 $\pmb{x}(t)$ 有 $\dot{V}(\pmb{x}(t)) \neq 0$ 。现采用反证法来证明这一点。反设对某个 $\pmb{x}_0 \neq \pmb{0}$ 的相应解 $\pmb{x}(t)$ 有 $\dot{V}(\pmb{x}(t)) \equiv 0$ ，于是利用 (5.248) 就可进而导出

$$\boldsymbol {x} ^ {T} (t) Q \boldsymbol {x} (t) \equiv 0, \quad \boldsymbol {x} ^ {T} (t) P B R ^ {- 1} B ^ {T} P \boldsymbol {x} (t) \equiv 0 \tag {5.249}$$

上式中，后一个恒等式意味着

$$0 \equiv (R ^ {- 1} B ^ {T} P x (t)) ^ {T} R (R ^ {- 1} B ^ {T} P x (t)) = u ^ {* T} (t) R u ^ {*} (t) \tag {5.250}$$

也即有 $\pmb{u}^{*}(t) = 0$ ；而前一个恒等式表示
