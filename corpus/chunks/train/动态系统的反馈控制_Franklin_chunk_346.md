# 6.6 闭环频率响应

在6.1节和图6.5中已经定义了闭环带宽。如图6.3所示，自然频率总是在二阶系统带宽的2倍范围内。在例6.14中，我们设计的补偿环节使穿越频率在期望带宽频率处，通过计算已经证明带宽频率等于穿越频率。通常情况下，穿越频率和带宽频率的匹配并不像例6.14中那样好。我们可以通过一些观察建立更准确的对应关系。考虑这样的系统，其 $|KG(j\omega)|$ 具有如下典型性质：

$$\text {当} \omega \ll \omega_ {\mathrm{c}} \text {时,} | K G (\mathrm{j} \omega) | \gg 1\mathrm{当} \omega \gg \omega_ {\mathrm{c}} \text {时,} | K G (\mathrm{j} \omega) | \ll 1$$

其中， $\omega_{\mathrm{c}}$ 是穿越频率。闭环频率响应的幅值近似为

$$
\left| \mathcal {T} (\mathrm{j} \omega) \right| = \left| \frac {K G (\mathrm{j} \omega)}{1 + K G (\mathrm{j} \omega)} \right| \approx \left\{ \begin{array}{l l} 1, & \omega \ll \omega_ {\mathrm{c}} \\ | K G |, & \omega \gg \omega_ {\mathrm{c}} \end{array} \right. \tag {6.36}
$$

在穿越频率附近，其 $|KG(j\omega)| = 1$ ， $|T(j\omega)|$ 在很大程度上依赖于相位裕度PM。PM=

$90^{\circ}$ 意味着 $\angle G(\mathrm{j}\omega_{c}) = -90^{\circ}$ ，则 $|\mathcal{T}(\mathrm{j}\omega_{c})| = 0.707$ 。另一方面， $\mathrm{PM} = 45^{\circ}$ 满足 $|\mathcal{T}(\mathrm{j}\omega_{c})| = 1.31$ 。

根据式(6.36)的准确估计，生成 $\left|T(j\omega)\right|$ 的曲线如图6.50所示。图中PM较小时的带宽频率明显比 $\omega_{c}$ 稍大一些，但通常小于 $2\omega_{c}$ ；因此， $\omega_{c}\leqslant\omega_{BW}\leqslant2\omega_{c}$ 。

![](image/0cfa517d989fb1296dbb5cf79ebdad36dc1f1324b32ec6ae5b96418216843fd6.jpg)  
图 6.50 不同 PM 对应的闭环带宽

另一个与闭环频率响应相关的性能指标是谐振峰值 $M_{r}$ ，其定义如图 6.5 所示。如图 6.3 和图 6.37 所示，对于线性系统， $M_{r}$ 通常与系统的阻尼比有关。在实际中， $M_{r}$ 很少被使用；大多设计者更喜欢使用 PM 来评估系统的阻尼比，因为使系统产生非线性或引起延时的不合理因素通常对相位的削减比对幅值的削减更明显。

正如上一例子所示，在设计中得到确定的误差特征也是很重要的，并且这些经常是作为输入函数或扰动频率的函数来评估的。在一些情况下，控制系统的主函数用于调节输出以得到一个有扰动存在的准确恒定输入。对于这些情况，设计中应注意的关键问题应该是带有扰动输入的误差的闭环频率响应。
