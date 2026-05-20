$$\frac {\partial}{\partial t} \phi_ {\alpha} = \frac {\partial g}{\partial z} (\phi (t; z, \alpha), \alpha) \phi_ {\alpha} + \frac {\partial g}{\partial \alpha} (\phi (t; z, \alpha), \alpha), \quad \phi_ {\alpha} (0; z, \alpha) = 0$$

由此可得

$$
\begin{array}{l} \| \phi_ {\alpha} (t; z, \alpha) \| _ {2} \leqslant \int_ {0} ^ {t} L _ {1} \| \phi_ {\alpha} (\tau ; z, \alpha) \| _ {2} d \tau + \int_ {0} ^ {t} L _ {2} \| \phi (\tau ; z, \alpha) \| _ {2} d \tau \\ \leqslant \int_ {0} ^ {t} L _ {1} \| \phi_ {\alpha} (\tau ; z, \alpha) \| _ {2} d \tau + \int_ {0} ^ {t} L _ {2} k e ^ {- \gamma \tau} d \tau \| z \| _ {2} \\ \leqslant \int_ {0} ^ {t} L _ {1} \| \phi_ {\alpha} (\tau ; z, \alpha) \| _ {2} d \tau + \frac {L _ {2} k}{\gamma} \| z \| _ {2} \\ \end{array}
$$

运用 Gronwall-Bellman 不等式,有

$$\left\| \phi_ {\alpha} (t; z, \alpha) \right\| _ {2} \leqslant \frac {L _ {2} k}{\gamma} \| z \| _ {2} e ^ {L _ {1} t}$$

因此 $\left\| \frac{\partial V}{\partial\alpha}\right\| _2 = \left\| \int_0^T 2\phi^\mathrm{T}(t;z,\alpha)\phi_\alpha (t;z,\alpha)dt\right\| _2$

$$\leqslant \int_ {0} ^ {T} 2 k e ^ {- \gamma t} \| z \| _ {2} \left(\frac {L _ {2} k}{\gamma}\right) e ^ {L _ {1} t} \| z \| _ {2} d t\leqslant \frac {2 k ^ {2} L _ {2}}{\gamma (\gamma - L _ {1})} \left[ 1 - e ^ {- (\gamma - L _ {1}) T} \right] \| z \| _ {2} ^ {2} \stackrel {\text { def }} {=} c _ {5} \| z \| _ {2} ^ {2}$$

即完成了引理的证明。

![](image/507b87af60373769f1f488f0dfe4b6fb01e73bc3e2bc2b1eb60d47d26c0fd614.jpg)

当冻结系统(9.40)是线性系统时,满足式(9.41)至式(9.44)的李雅普诺夫函数可以通过解参数李雅普诺夫方程确定,这一点在下一引理中说明。

引理9.9 考虑系统 $z = A(\alpha)z$ ，其中 $\alpha \in \Gamma$ 和 $A(\alpha)$ 是连续可微的。假设 $A$ 的元素及其对于 $\alpha$ 的一阶偏导数一致有界，即

$$\| A (\alpha) \| _ {2} \leqslant c, \quad \left\| \frac {\partial}{\partial \alpha_ {i}} A (\alpha) \right\| _ {2} \leqslant b _ {i}, \forall \alpha \in \Gamma , \forall 1 \leqslant i \leqslant m$$

进一步假设 $A(\alpha)$ 是关于 $\alpha$ 一致赫尔维茨的，即

$$\operatorname{Re} [ \lambda (A (\alpha)) ] \leqslant - \sigma < 0, \quad \forall \alpha \in \Gamma$$

则李雅普诺夫方程 $PA(\alpha)+A^{\mathrm{T}}(\alpha)P=-I$ (9.48)

对于每个 $\alpha \in \Gamma$ 有唯一正定解 $P(\alpha)$ , 而且 $P(\alpha)$ 是连续可微的, 对于所有 $(z, a) \in R^n \times \Gamma$ 满足

$$c _ {1} z ^ {\mathrm{T}} z \leqslant z ^ {\mathrm{T}} P (\alpha) z \leqslant c _ {2} z ^ {\mathrm{T}} z\left\| \frac {\partial}{\partial \alpha_ {i}} P (\alpha) \right\| _ {2} \leqslant \mu_ {i}, \forall 1 \leqslant i \leqslant m$$
