# 11.4 线性定常系统的 $H_{\infty}$ 最优控制问题

为了更好地理解 $H_{\infty}$ 最优控制的设计思想, 首先考察线性系统中的最优控制问题。

假设单输入线性系统状态方程如下：

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u} \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {11-19}$$

其中， $\boldsymbol{x}(t)\in\mathbf{R}^{n}$ 为状态变量， $u\in\mathbf{R}$ 为控制输入， $A\in\mathbf{R}^{n\times n},B\in\mathbf{R}^{n}$ 为定常矩阵。

对于被控对象,设计状态反馈控制器:

$$u \in K x \quad K \in \mathbf {R} ^ {1 \times n}$$

使给定的二次型性能指标

$$J = \int_ {0} ^ {\infty} \left\{\boldsymbol {x} ^ {\mathrm{T}} (t) \boldsymbol {Q} \boldsymbol {x} (t) + r u ^ {2} (t) \right\} \mathrm{d} t$$

达到最小,同时,使闭环系统渐进稳定,其中 $Q \geqslant 0$ 为加权矩阵,r > 0 为加权系数。

最优控制理论的结果表明,通过解适当的代数 Riccati 方程,可以得到使 J 为最小的控制器 K。但是在这个设计问题中,并没有考虑干扰的影响,即性能指标的最优性只有在被控对象完全可以由式(11-19)精确描述时才能得到实现。由于实际系统中存在干扰等不确定性,使得这种最优设计的结果在实际应用中效果不好。

为了克服这一点,在被控对象的模型中,加入干扰项,并考虑干扰对系统响应特性的影响。下面将分别讨论线性定常系统的 $H_{\infty}$ 最优控制和次优控制问题。
