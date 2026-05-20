$$V (\boldsymbol {x}) = \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} \tag {9.60}\dot {V} (\boldsymbol {x}) = \dot {\boldsymbol {x}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} + \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {x}} \tag {9.61}= (\boldsymbol {A} \boldsymbol {x} + \boldsymbol {g} (\boldsymbol {x}) ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} + \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} (\boldsymbol {A} \boldsymbol {x} + \boldsymbol {g} (\boldsymbol {x})) \tag {9.62}= \boldsymbol {x} ^ {\mathrm{T}} \left(\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}\right) \boldsymbol {x} + 2 \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P g} (\boldsymbol {x}) \tag {9.63}$$

由此得到一个基本的矩阵结果，就是著名的李雅普诺夫方程：

$$\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} = - Q \tag {9.64}$$

他证明了如果 A 是一个稳定矩阵，即 A 的所有特征值都在左半平面，那么对任意正定矩阵 Q，上述方程的解 P 也是正定的。接下来的问题就是选择 Q 和解出 P。那么，如果 A 的所有特征值都在左半平面，则 P 将是正定的，所以 $V(x)$ 是一个可能的李雅普诺夫函数，并且

$$\dot {V} (\boldsymbol {x}) = - \boldsymbol {x} ^ {\mathrm{T}} Q \boldsymbol {x} + 2 \boldsymbol {x} ^ {\mathrm{T}} P \boldsymbol {g} \tag {9.65}$$

这个论证的最后一部分指出：由式(9.59)可知，如果 $x$ 足够小，那么式(9.65)的第一项将占主导地位，第四个条件得以满足，于是 $V(x)$ 是一个李雅普诺夫函数，这就证明了系统是稳定的。注意 $x$ 足够小的要求只保证了在原点的一个邻域内系统是稳定的。想要证明随着 $\| x\|$ 趋于 $+\infty$ （先前不要求此条件），由 $V(x)$ 定义的“碗”朝着各个方向趋于 $+\infty$ ，以至于对于任意状态，稳定性均成立且是大范围稳定的，还需要更多条件。

还有一个不稳定性定理：如果 A 的任意一个特征值在右半平面，那么原点将是不稳定的。如果 A 除了几个极点在虚轴上，其余全在左半平面，那么系统的稳定性依赖于 $g(x)$ 非线性项的性质。有了这些结论，李雅普诺夫第一法或间接法可描述如下：

(1) 找到线性近似，计算出 A 的特征值。

(2) 如果所有特征值在左半平面，那么存在一个原点邻域的稳定区域。

（3）如果至少有一个特征值在右半平面，那么原点将是不稳定的。

（4）如果有几个特征值在虚轴上，其余全在左半平面，那么基于此方法不能得到任何关于稳定性的结论。
