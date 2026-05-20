$$
\begin{array}{l} M = | G (\mathrm{j} \omega_ {0}) | = | G (s) | _ {s = \mathrm{j} \omega_ {0}} \\ = \sqrt {\left\{\operatorname{Re} \left[ G \left(\mathrm{j} \omega_ {0}\right) \right] \right\} ^ {2} + \left\{\operatorname{Im} \left[ G \left(\mathrm{j} \omega_ {0}\right) \right] \right\} ^ {2}} \tag {6.5} \\ \end{array}
\phi = \arctan \left[ \frac {\mathrm{Im} [ G (\mathrm{j} \omega_ {0}) ]}{\mathrm{Re} [ G (\mathrm{j} \omega_ {0}) ]} \right] = \angle G (\mathrm{j} \omega_ {0}) \tag {6.6}
$$

在极坐标形式下，有

$$G (\mathrm{j} \omega_ {0}) = M \mathrm{e} ^ {\mathrm{j} \phi} \tag {6.7}$$

式(6.4)表明，具有传递函数 $G(s)$ 的稳定系统，被幅值为 1、频率为 $\omega_{0}$ 的正弦曲线激励后，当其响应达到稳态之后，得到一个正弦输出，该正弦输出在频率 $\omega_0$ 处的幅值为 $M(\omega_0)$ ，相位为 $\phi (\omega_0)$ 。事实上，输出 $y$ 和输入 $u$ 是具有相同频率的正弦曲线，且输出的幅值比 $M$ 和相位 $\phi$ 与输入幅值 $A$ 无关，这一结果是由于 $G(s)$ 是线性定常系统造成的。如果被激励的系统是非线性或者时变系统，那么输出可能包含输入频率以外的频率，并且输出输入比可能与输入幅值有关。

更一般地，幅值 $M$ 由 $\left|G(\mathrm{j}\omega)\right|$ 给出，且相位 $\phi$ 由 $\angle G(\mathrm{j}\omega)$ 给出；复数量 $G(s)$ 的幅值与角度是由 $s$ 沿着虚轴 $(s = \mathrm{j}\omega)$ 取值计算的。系统的频率响应由这些关于频率的函数组成，这反映出系统对于一个任意频率的正弦输入的响应。我们对分析系统的频率响应感兴趣，不仅仅是因为它可以帮助理解系统对于正弦输入是如何响应的，也是因为计算 $s$ 沿着 $\mathrm{j}\omega$ 轴取值时 $G(s)$ 的值被证实对确定闭环系统的稳定性是非常有用的。正如我们在第3章中所见， $\mathrm{j}\omega$ 轴是稳定与不稳定的边界；在6.4节中，我们将看到，通过计算 $G(\mathrm{j}\omega)$ 所提供的信息，我们可以根据开环的 $G(s)$ 确定闭环稳定性。
