# 10.6 最优线性原理和贝尔曼-依萨克斯方程

贝尔曼在动态规划中提出了最优控制原理；对于微分对策，依萨克斯也提出了类似的最优性原理，即最优微分对策过程的任何最后一段都是最优的，而不管此段的初始状态是什么，达到此初始状态的对策是什么。

在动态规划中,得到了哈密顿-雅克比-贝尔曼方程式(6-25),把它重写于下:

$$- \frac {\partial J (\boldsymbol {x} , t)}{\partial t} = \min _ {\boldsymbol {u} \in \Omega} \left\{\boldsymbol {F} (\boldsymbol {x}, \boldsymbol {u}, t) + \left(\frac {\partial J}{\partial \boldsymbol {x}}\right) ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t) \right\}$$

在微分对策中,依萨克斯也得出了与上式相似的公式,称为贝尔曼-依萨克斯方程,有时又称为哈密顿-雅克比-依萨克斯方程(简称HJI方程)。下面为了简洁起见,直接给出此公式。

设对策双方的状态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}), \quad x (t _ {0}) = \boldsymbol {x} _ {0}$$

性能指标为

$$J (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}) = \Phi [ \boldsymbol {x} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \boldsymbol {F} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) \mathrm{d} t$$

则最优性能指标满足下面的贝尔曼－依萨克斯方程

$$\frac {\partial J (\boldsymbol {x} , t)}{\partial t} + \min _ {\boldsymbol {v}} \max _ {\boldsymbol {u}} \left[ \boldsymbol {F} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}, t) + \left(\frac {\partial J (\boldsymbol {x} , t)}{\partial \boldsymbol {x}}\right) ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, \boldsymbol {v}) \right] = 0J (\boldsymbol {x} (t _ {\mathrm{f}}), t _ {\mathrm{f}}) = \Phi [ \boldsymbol {x} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ]$$
