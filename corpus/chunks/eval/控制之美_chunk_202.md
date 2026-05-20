这是由系统本身的物理限制决定的, 虽然原系统是能控的, 状态变量 $z_{2}(t)$ 可以达到任意值, 但并不意味着它可以被稳定在任意值。本例中的 $z_{2}(t)$ 代表了角速度, 如果它不为 0 , 连杆小球就一定还在运动过程当中, 自然无法稳定。

但是 $z_{1}(t)$ 不一样，它的平衡点的位置是可以通过输入 $u(t)$ 改变的。令 $\pmb{u}(t) = \pmb{F}\pmb{z}_{\mathrm{d}} + \pmb{K}_{\mathrm{e}}\pmb{e}(t)$ ，其中 $\pmb{F}\pmb{z}_{\mathrm{d}}$ 部分称为前馈(Feedforward)，用来将平衡点 $z_{1\mathrm{f}}$ 移动到 $z_{1\mathrm{d}}$ 。 $\pmb{K}_{\mathrm{e}}\pmb{e}(t)$ 项用来配置极点，使得系统稳定，其中 $\pmb{K}_{\mathrm{e}} = [k_{\mathrm{e}1}, k_{\mathrm{e}2}]$ 。

根据上述分析,平衡点位置为 $\left[z_{1d},0\right]^{T}$ 。令

$$
\boldsymbol {u} (t) = \boldsymbol {F} \boldsymbol {z} _ {\mathrm{d}} + \boldsymbol {K} _ {\mathrm{e}} \boldsymbol {e} (t) = \left[ - \frac {g}{d} 0 \right] \left[ \begin{array}{c} z _ {1 \mathrm{d}} \\ 0 \end{array} \right] + \boldsymbol {K} _ {\mathrm{e}} \boldsymbol {e} (t) \tag {10.3.23}
$$

将其代入式(10.3.21)，得到

$$
\begin{array}{l} \frac {\mathrm{d} \boldsymbol {e} (t)}{\mathrm{d} t} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] - \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{l} z _ {1 d} \\ 0 \end{array} \right] - \\ \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \left(\left[ \begin{array}{c c} - \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{c} z _ {1 d} \\ 0 \end{array} \right] + \left[ \begin{array}{c c} k _ {\mathrm{e} 1} & k _ {\mathrm{e} 2} \end{array} \right] \left[ \begin{array}{c} e _ {1} (t) \\ e _ {2} (t) \end{array} \right]\right) \\ \end{array}
$$

$$
\begin{array}{l} = \left[ \begin{array}{l l} 0 & 1 \\ \frac {g}{d} & 0 \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] - \left[ \begin{array}{c c} 0 & 0 \\ k _ {\mathrm{e} 1} & k _ {\mathrm{e} 2} \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] \\ = \left[ \begin{array}{c c} 0 & 1 \\ \frac {g}{d} - k _ {\mathrm{e} 1} & - k _ {\mathrm{e} 2} \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] \tag {10.3.24} \\ \end{array}
$$

此时，误差状态变量的平衡点为 $e_{f}=[0,0]^{T}$ 。
