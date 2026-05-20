# 4.3 李亚普诺夫第二方法的主要定理

约在一个世纪以前，俄国学者李亚普诺夫在其1892年发表的《运动稳定性的一般问题》论文中，首先建立了运动稳定性的一般理论。在这篇文献中，李亚普诺夫把分析由常微分方程组所描述的动力学系统的稳定性的方法归纳为本质不同的两种方法，分别称为李亚普诺夫第一方法和第二方法。李亚普诺夫第一方法又称间接法，这种方法中先要由系统的运动方程（4.20）来找出其一次近似的线性化方程，再通过对线性化方程的稳定性的分析而给出原非线性系统在小范围内稳定性的有关信息。李亚普诺夫第二方法也称为直接法，其特点是不需要引入线性近似，而直接由系统的运动方程（4.20）出发，通过构造一个类似于“能量”的李亚普诺夫函数，并分析它和其一次导数的定号性，而获得系统稳定性的有关信息。李亚普诺夫第二方法概念直观，方法具有一般性，物理含义清晰。因此，当李亚普诺夫第二方法在1960年前后被系统地引入到系统与控制理论中后，就很快得到了广泛的应用，不管是理论上还是在应用上都显示出了它的重要性。本节中，我们要在上一节的关于运动稳定性的基本概念的基础上，来介绍李亚普诺夫第二方法的主要结论。

大范围渐近稳定的判别定理 考察连续时间的非线性时变自由系统

$$\dot {\boldsymbol {x}} = \boldsymbol {f} (\boldsymbol {x}, t), \quad t \geqslant t _ {0} \tag {4.31}$$

其中，对一切 $t$ 成立 $f(0, t) = 0$ ，即状态空间的原点为系统的平衡状态。下面，给出原

点平衡状态为大范渐近稳定的判别定理，通常称其为李亚普诺夫主稳定性定理。

结论1[大范围一致渐近稳定判别定理] 对系统(4.31)，如果存在一个对 $\pmb{x}$ 和 $t$ 具有连续一阶偏导数的标量函数 $V(\pmb{x}, t)$ ， $V(0, t) = 0$ ，且满足如下的条件：

(i) $V(\pmb{x}, t)$ 正定且有界，即存在两个连续的非减标量函数 $\alpha (\| \pmb{x}\|)$ 和 $\beta (\| \pmb{x}\|)$ ，其中 $\alpha(0) = 0$ 和 $\beta(0) = 0$ ，使对一切 $t \geqslant t_0$ 和一切 $\pmb{x} \neq \pmb{0}$ 成立

$$\beta (\| \boldsymbol {x} \|) \geqslant V (\boldsymbol {x}, t) \geqslant \alpha (\| \boldsymbol {x} \|) > 0 \tag {4.32}$$

(ii) $V(x, t)$ 对时间 $t$ 的导数 $\dot{V}(x, t)$ 负定且有界，即存在一个连续的非减标量函数 $\gamma(\|x\|)$ ，其中 $\gamma(0) = 0$ ，使对一切 $t \geqslant t_0$ 和一切 $x \neq 0$ 成立

$$\dot {V} (\boldsymbol {x}, t) \leqslant - \gamma (\| \boldsymbol {x} \|) < 0 \tag {4.33}$$

(iii) 当 $\| x\| \to \infty$ 时，有 $a(\| x\|)\rightarrow \infty$ 即 $V(x,t)\rightarrow \infty$ 。

则系统原点平衡状态为大范围一致渐近稳定。

证 分成三点来进行证明。

① 证明原点平衡状态 $x = 0$ 是一致稳定的。为此，画出定理的条件 (i) 的几何描述，如图4.4所示。由图可以看出，由于 $\beta (\| x\|)$ 为连续非减且有 $\beta (0) = 0$ ，故对任给实数 $\varepsilon > 0$ 必存在对应的实数 $\delta (\varepsilon) > 0$ ，使成立 $\beta (\delta) \leqslant \alpha (\varepsilon)$ 。再知 $\dot{V} (x, t)$ 为负定，因此对一切 $t \geqslant t_0$ 必成立

$$V \left(\phi \left(t; x _ {0}, t _ {0}\right), t\right) - V \left(x _ {0}, t _ {0}\right) = \int_ {t _ {0}} ^ {t} \dot {V} \left(\left(\tau ; x _ {0}, t _ {0}\right), \tau\right) d \tau \leqslant 0 \tag {4.34}$$

由此，对任意 $t_0$ 和满足 $\| x_0\| \leqslant \delta (\varepsilon)$ 的任意 $x_0$ ，对一切 $t\geqslant t_0$ 均有

$$\alpha (\varepsilon) \geqslant \beta (\delta) \geqslant V (x _ {0}, t _ {0}) \geqslant V (\phi (t; x _ {0}, t _ {0}), t) \geqslant \alpha (\| \phi (t; x _ {0}, t _ {0}) \|) \tag {4.35}$$

据（4.32）

据 (4.32)
