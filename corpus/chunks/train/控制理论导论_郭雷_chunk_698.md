# 习题 9.4

9.4.1 设回归向量 $\{\phi_{k}\}$ 由下列状态方程所产生：

$$
\left\{ \begin{array}{l l} x _ {k} = A x _ {k \dots 1} + B \xi_ {k}, & E \| x _ {0} \| ^ {4} <   \infty , \\ \phi_ {k} = C x _ {k} + \zeta_ {k}, & k \geqslant 0, \end{array} \right.
$$

其中 $A \in \mathbb{R}^{n \times n}$ , $B \in \mathbb{R}^{n \times q}$ 及 $C \in \mathbb{R}^{d \times n}$ 是确定性矩阵. 假设

(i) $A$ 是稳定矩阵，且 $(A, B, C)$ 在下列意义下输出能控

$$\sum_ {i = 0} ^ {n - 1} C A ^ {i} B (C A ^ {i} B) ^ {\mathrm{T}} > 0;$$

(ii) $\{\xi_k, \zeta_k\}$ 是零均值独立序列，且存在 $\varepsilon > 0$ 及 $M > 0$ 使

$$E \xi_ {k} \xi_ {k} ^ {\mathrm{T}} \geqslant \varepsilon I, \quad E [ \| \xi_ {k} \| ^ {4} + \| \zeta_ {k} \| ^ {4} ] \leqslant M, \quad \forall k,$$

证明： $\{\phi_k\}$ 满足激励条件9.4.1.（提示：利用习题9.3.4或命题9.3.3.)

9.4.2 假设式 (9.4.1) 是一个时变自回归模型

$$y _ {t + 1} = a _ {1} (t) y _ {t} + \dots + a _ {p} (t) y _ {t - p + 1} + w _ {t + 1} \tag {9.4.53}\stackrel {\text { def }} {=} \theta_ {t} ^ {\mathrm{T}} \phi_ {t} + w _ {t + 1}, \tag {9.4.54}$$

其中 $\theta_{t}^{T}=[a_{1}(t)\cdots a_{p}(t)]$ , $\phi_{t}^{T}=[y_{t}\cdots y_{t-p+1}]$ , $\{w_{t}\}$ 是一个与 $\phi_{0}$ 独立的独立序列并满足

$$E w _ {k} = 0, \quad E w _ {k} ^ {2} \geqslant \sigma_ {w} ^ {2} > 0, \quad \sup _ {k} E | w _ {k} | ^ {9} < \infty .$$

显然，上述回归模型又可化为状态空间模型

$$\phi_ {t + 1} = A _ {t} \phi_ {t} + b w _ {t + 1},$$

其中

$$
A _ {t} = \left[ \begin{array}{c c c} a _ {1} (t) & \dots & a _ {p} (t) \\ 1 & 0 & \vdots \\ & \ddots & \\ 0 & 1 & 0 \end{array} \right] \quad b = [ 1, 0 \dots 0 ] ^ {\mathrm{T}}.
$$

证明在下述进一步的假设条件 A) 下， $\{\phi_{t}\}$ 满足激励条件 9.4.1:

A) $\{A_{t}\}$ 是与 $\{w_{t}\}$ 独立的独立序列，且存在 $\delta \in (0,1)$ 使

$$\left\| \prod_ {i = k p} ^ {(k + 1) p - 1} A _ {i} \right\| _ {L _ {4}} \leqslant \delta , \quad \forall k \geqslant 0, \quad \sup _ {k} \| A _ {k} \| _ {L _ {q}} < \infty ,$$

其中 $q = \max\{4, 2(p - 1)\}$ .

9.4.3 仍考虑上题中的时变自回归模型。证明：若上题中的条件 A) 换成下述 (非独立性) 条件 A)'，则 $\{\phi_t\}$ 仍满足激励条件 9.4.1。

A)' $\{A_{t},\mathcal{F}_{t}^{\prime}\}$ 是适应矩阵序列，且可分解为

$$A _ {t} = A + \overline {{{A}}} _ {t},$$

其中 $A$ 是稳定矩阵，而 $\{\overline{A}_t, \mathcal{F}_t'\}$ 被一个线性序列所控制

$$\| \overline {{{A}}} _ {t} \| \leqslant \beta_ {t}, \quad \beta_ {t} = \beta \beta_ {t - 1} + e _ {t}, \quad 0 \leqslant \beta < 1,$$

其中 $e_t \geqslant 0, e_t \in \mathcal{F}_t'$ , 且 $e_{t+1}$ 与 $\mathcal{F}_t'$ 独立. 进一步, 假设 $\mathcal{F}_{\infty}' \stackrel{\text{def}}{=} \sigma \{\cup_i \mathcal{F}_i'\}$ 与 $\{V_t\}$ 独立, 且存在适当大和适当小的正常数 $b$ 和 $\epsilon$ 使

$$\log \{E [ \exp (b e _ {t}) ] \} \leqslant \varepsilon , \quad \forall t \geqslant 0.$$

(提示：利用推论 9.3.2.)
