$$\int_ {0} ^ {t} C e ^ {A (t - \tau)} B u (\tau) d \tau = \int_ {0} ^ {t} \overline {{C}} e ^ {\mathcal {K} (t - \tau)} \overline {{B}} u (\tau) d \tau \tag {9.8}$$

再考虑到上式中 $\pmb{u}$ 和 $t$ 的任意性，所以由此可进一步导出

$$C e ^ {A (t - \tau)} B = \bar {C} e ^ {\bar {A} (t - \tau)} \bar {B}, \forall t, \tau \tag {9.9}$$

现令 $\tau = 0$ ，且记

$$H (t) = C e ^ {A t} B \text {和} \overline {{H}} (t) = \overline {{C}} e ^ {A t} \overline {{B}}, t \geqslant 0 \tag {9.10}$$

它们分别代表系统 $(A, B, C)$ 和 $(\vec{A}, \vec{B}, \vec{C})$ 的脉冲响应阵。进而，由(9.10)可求出 $H(t)$ 的各阶导数为：

$$
\left\{ \begin{array}{l} H ^ {(1)} (t) = C A e ^ {A t} B = C e ^ {A t} A B \\ H ^ {(2)} (t) = C A e ^ {A t} A B = C A ^ {2} e ^ {A t} B = C e ^ {A t} A ^ {2} B \\ \dots \dots \\ H ^ {(n - 1)} (t) = C A ^ {n - 1} e ^ {A t} B = C e ^ {A t} A ^ {n - 1} B \\ \dots \dots \\ H ^ {(2 n - 2)} (t) = C A ^ {n - 1} e ^ {A t} A ^ {n - 1} B \end{array} \right. \tag {9.11}
$$

于是，就有

$$
\begin{array}{l} L (t) \triangleq \left[ \begin{array}{c c c c} H (t) & H ^ {(1)} (t) & \dots \dots & H ^ {(n - 1)} (t) \\ H ^ {(1)} (t) & H ^ {(2)} (t) & \dots \dots & H ^ {(n)} (t) \\ \vdots & \vdots & & \vdots \\ \vdots & \vdots & & \vdots \\ \vdots & \vdots & & \vdots \\ H ^ {(n - 1)} (t) & H ^ {(n)} (t) & \dots \dots & H ^ {(2 n - 2)} (t) \end{array} \right] \\ = \left[ \begin{array}{c c c c} C e ^ {A t} B & C e ^ {A t} A B & \dots \dots & C e ^ {A t} A ^ {n - 1} B \\ C A e ^ {A t} B & C A e ^ {A t} A B & \dots \dots & C A e ^ {A t} A ^ {n - 1} B \\ \vdots & \vdots & & \vdots \\ \vdots & \vdots & & \vdots \\ C A ^ {n - 1} e ^ {A t} B & C A ^ {n - 1} e ^ {A t} A B & \dots \dots & C A ^ {n - 1} e ^ {A t} A ^ {n - 1} B \end{array} \right] \\ = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] e ^ {A t} [ B \quad A B \dots A ^ {n - 1} B ] \\ = Q _ {o} e ^ {A t} Q _ {c}, t \geqslant 0 \tag {9.12} \\ \end{array}
$$

其中， $Q_{\bullet}$ 和 $Q_{\epsilon}$ 分别表示 $(A, B, C)$ 的能观测性和能控性判别阵。式(9.12)对一切 $t \geqslant 0$ 均成立，所以对 t = 0 当然也成立。由此，又可有

$$L (0) = Q _ {o} Q _ {c} \tag {9.13}$$

同理，相应地也可导出

$$\overline {{{L}}} (0) = \overline {{{Q}}} _ {o} \overline {{{Q}}} _ {c} \tag {9.14}$$

其中， $\overline{Q}$ 和 $\overline{Q}$ ，分别为（ $\overline{A}$ ， $\overline{B}$ ， $\overline{C}$ ）的能观测性和能控性判别阵。并且，由(9.9)可知 $H(t) = \overline{H}(t)$ ，所以又有 $L(t) = \overline{L}(t)$ ，从而由(9.13)和(9.14)可导出

$$Q _ {o} Q _ {c} = \bar {Q} _ {o} \bar {Q} _ {c} \tag {9.15}$$

但已知 $(A, B, C)$ 为能控和能观测，所以有

$$\operatorname{rank} Q _ {e} = n, \operatorname{rank} Q _ {c} = n, \operatorname{rank} Q _ {o} Q _ {c} = n \tag {9.16}$$

于是，由此就可得到

$$\min \left\{\text { rank } \bar {Q} _ {o}, \text { rank } \bar {Q} _ {c} \right\} \geqslant n \tag {9.17}$$

也即
