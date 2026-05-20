# LQR 调节器的鲁棒性能

已经证明用 LQR 设计的奈奎斯特图绕过了以 -1 点为圆心的单位圆（安德森（Anderson）和摩尔（Moore）于 1990 年提出），如图 7.23 所示。这就产生了特别的相位和增益裕度特性。可以看出（见习题 7.33）回差必须满足

$$\left| 1 + \boldsymbol {K} (\mathrm{j} \omega \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} \right| \geqslant 1 \tag {7.124}$$

下面将回路增益改写为它的实部和虚部之和的形式：

$$L (\mathrm{j} \omega) = K (\mathrm{j} \omega I - A) ^ {- 1} B = \operatorname{Re} (L (\mathrm{j} \omega)) + \mathrm{jIm} (L (\mathrm{j} \omega)) \tag {7.125}$$

由式(7.124)意味着，有

$$\left(\left[ \mathrm{Re} (L (\mathrm{j} \omega) \right] + 1\right) ^ {2} + \left[ \mathrm{Im} (L (\mathrm{j} \omega) \right] ^ {2} \geqslant 1 \tag {7.126}$$

这说明奈奎斯特图的确绕过了以-1为圆心的单位圆。这暗示着 $\frac{1}{2} < GM < +\infty$ ，也即增益裕度的上限为 $\mathrm{GM} = +\infty$ ，增益裕度的下限为 $\mathrm{GM} = \frac{1}{2}$ （见第6章习题6.24）。因此LQR增益矩阵 $K$ 可以乘上一个大的标量系数或是除以2都可以保证闭环系统的稳定性。相位裕度PM至少为 $\pm 60^{\circ}$ 。这些裕度都是很大的，而在实际中，由于模型误差的存在以及缺少传感器，因此设想它们能够达到是不现实的！
