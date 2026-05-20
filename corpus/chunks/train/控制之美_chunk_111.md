# 6.1.2 稳定性的定义

6.1.1 节从直观上解释了稳定性的含义,下面将介绍严谨的数学定义。在 1892 年,俄国数学家亚历山大·李雅普诺夫(Aleksandr Lyapunov)在其博士论文《运动稳定性的一般问题》中提出了稳定性的科学概念。本书将选用这个概念来定义系统的稳定性,它是一个通用的概念,既可以运用在线性系统中,也可以运用到非线性的系统分析中。

首先介绍平衡点的定义,考虑一个无输入的状态空间方程表达式,即

$$\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = f (\boldsymbol {z} (t)) \tag {6.1.1}$$

式(6.1.1)中的 $f(z(t))$ 可以是线性的,也可以是非线性的,它是一个通用的表达式。其中, $z(t)$ 是系统的状态变量。定义 $z_{f}$ 是系统的平衡点,如果在 $t=t_{0}$ 时刻状态变量的初始值 $z(t_{0})=z_{f}$ ,那么

$$z (t) = z _ {\mathrm{f}}, \quad \forall t \geqslant t _ {0} \tag {6.1.2a}$$

其中， $\forall$ 代表“对于任意，或对所有 (for all)”。式(6.1.2a)说明当系统初始状态处于平衡点时，状态变量将不会随时间发生改变，例如图6.1.1中小球在初始状态时处于 $A, B, C$ 三个位置。同时，根据式(6.1.1)，有

$$
\begin{array}{l} z (t) = z _ {f} \\ \Rightarrow \frac {\mathrm{d} z (t)}{\mathrm{d} t} = 0 \\ \Rightarrow f (z _ {\mathrm{f}}) = 0, \quad \forall t \geqslant t _ {0} \tag {6.1.2b} \\ \end{array}
$$

在接下来的分析中,我们将假设系统的平衡点在 $z_{f}=[0]$ 位置,或者可以转换到零点位置,这个假设不会影响系统的一般性。定义两个重要的稳定性概念:

(1) 李雅普诺夫意义下的稳定性(Stability in the Sense of Lyapunov):

如果平衡点 $z_{f}=0$ 满足

$$\forall t _ {0}, \forall \varepsilon > 0, \exists \delta (t _ {0}, \Delta): \| z (t _ {0}) \| < \delta (t _ {0}, \varepsilon) \Rightarrow \forall t \geqslant t _ {0}, \quad \| z (t) \| < \varepsilon \tag {6.1.3}$$

则它被称为在李雅普诺夫意义下是稳定的。式(6.1.3)中， $\varepsilon$ 是一个任意给定的实数， $\exists$ 代表存在， $\| \cdot \|$ 代表欧几里得范数（2 范数），例如，对于一个 $n$ 维向量 $z(t) = [z_1(t), z_2(t), \dots, z_n(t)]^{\mathrm{T}}$ ，其欧几里得范数 $\| z(t) \| = \sqrt{z_1^2(t) + z_2^2(t) + \cdots + z_n^2(t)}$ 。
