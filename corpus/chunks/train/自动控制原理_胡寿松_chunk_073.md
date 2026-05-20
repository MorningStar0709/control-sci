$$\Delta y = \left(\frac {\partial f}{\partial x _ {1}}\right) _ {x _ {1 0}, x _ {2 0}} \Delta x _ {1} + \left(\frac {\partial f}{\partial x _ {2}}\right) _ {x _ {1 0}, x _ {2 0}} \Delta x _ {2} = K _ {1} \Delta x _ {1} + K _ {2} \Delta x _ {2}$$

式中， $K_{1}=(\partial f/\partial x_{1})_{x_{10},x_{20}}$ ； $K_{2}=(\partial f/\partial x_{2})_{x_{10},x_{20}}$ 。

这种小偏差线性化方法对于控制系统大多数工作状态是可行的。事实上，自动控制系统在正常情况下都处于一个稳定的工作状态，即平衡状态，这时被控量与期望值保持一致，控制系统也不进行控制动作。一旦被控量偏离期望值产生偏差时，控制系统便开始控制动作，以便减小或消除这个偏差，因此，控制系统中被控量的偏差一般不会很大，只是“小偏差”。在建立控制系统的数学模型时，通常是将系统的稳定工作状态作为起始状态，仅仅研究小偏差的运动情况，也就是只研究相对于平衡状态下，系统输入量和输出量的运动特性，这正是增量线性化方程所描述的系统特性。

例 2-7 设铁心线圈电路如图 2-7(a) 所示, 其磁通 $\phi$ 与线圈中电流 i 之间关系如图 2-7(b) 所示。试列写以 $u_{r}$ 为输入量, i 为输出量的电路微分方程。

![](image/95a1e5fb28a277144c49d37ce78cdd58c59352be9411297a0497ef161e698072.jpg)

<details>
<summary>text_image</summary>

R
i
uᵣ
(a)
φ
φ₀
Δi
Δφ
K
(b)
</details>

图 2-7 铁心线圈电路及其特性

解 设铁心线圈磁通变化时产生的感应电势为

$$u _ {\phi} = K _ {1} \frac {\mathrm{d} \phi (i)}{\mathrm{d} t}$$

根据基尔霍夫定律写出电路微分方程

$$
\begin{array}{l} u _ {r} = K _ {1} \frac {\mathrm{d} \phi (i)}{\mathrm{d} t} + R i \\ = K _ {1} \frac {\mathrm{d} \phi (i)}{\mathrm{d} i} \frac {\mathrm{d} i}{\mathrm{d} t} + R i \tag {2-33} \\ \end{array}
$$

式中 $\mathrm{d}\phi (i) / \mathrm{d}i$ 是线圈中电流 $i$ 的非线性函数，因

此，式(2-33)是一个非线性微分方程。

在工程应用中, 如果电路的电压和电流只在某平衡点 $(u_0, i_0)$ 附近作微小变化, 则可设 $u_r$ 相对于 $u_0$ 的增量是 $\Delta u_r$ , $i$ 相对于 $i_0$ 的增量是 $\Delta i$ , 并设 $\phi(i)$ 在 $i_0$ 的邻域内连续可导, 这样可将 $\phi(i)$ 在 $i_0$ 附近用泰勒级数展开为

$$\phi (i) = \phi (i _ {0}) + \left(\frac {\mathrm{d} \phi (i)}{\mathrm{d} i}\right) _ {i _ {0}} \Delta i + \frac {1}{2 !} \left(\frac {\mathrm{d} ^ {2} \phi (i)}{\mathrm{d} i ^ {2}}\right) _ {i _ {0}} (\Delta i) ^ {2} + \dots$$

当 $\Delta i$ 足够小时，略去高阶导数项，可得

$$\phi (i) - \phi (i _ {0}) = \left(\frac {\mathrm{d} \phi (i)}{\mathrm{d} i}\right) _ {i _ {0}} \Delta i = K \Delta i$$

式中 $K = (\mathrm{d}\phi (i) / \mathrm{d}i)_{i_0}$ 。令 $\Delta \phi = \phi (i) - \phi (i_0)$ ，并略去增量符号 $\Delta$ ，便得到磁通 $\phi$ 与电流 $i$ 之间的增量线性化方程为

$$\phi (i) = K i \tag {2-34}$$

由式(2-34)可求得 $\mathrm{d}\phi (i) / \mathrm{d}i = K$ ，代入式(2-33)，有

$$K _ {1} K \frac {\mathrm{d} i}{\mathrm{d} t} + R i = u _ {r} \tag {2-35}$$

式(2-35)便是铁心线圈电路在平衡点 $(u_{0},i_{0})$ 的增量线性化微分方程,若平衡点变动时,K值亦相应改变。
