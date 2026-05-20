# (1) 线性定常连续系统渐近稳定性的判别

设线性定常系统状态方程为 $\dot{\pmb{x}} = \pmb{A}\pmb{x},\pmb{x}(0) = \pmb{x}_0,t\geqslant 0,\pmb{A}$ 为非奇异矩阵，故原点是唯一平衡状态。设取正定二次型函数 $V(x) = x^{\mathrm{T}}Px$ 作为可能的李雅普诺夫函数，考虑到系统状态方程，则有

$$\dot {V} (\boldsymbol {x}) = \dot {\boldsymbol {x}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {x} + \boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {x}} = \boldsymbol {x} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P} \boldsymbol {A}) \boldsymbol {x} \tag {9-263}$$

令 $A^{T}P + PA = -Q$ (9-264)

于是有 $\dot{V} (\pmb {x}) = -\pmb{x}^{\mathrm{T}}\pmb {Q}\pmb {x}$ (9-265)

根据定常系统大范围渐近稳定判别定理1, 只要 $Q$ 正定(即 $\dot{V}(x)$ 负定), 则系统是大范围渐近稳定的。于是线性定常连续系统渐近稳定的充分必要条件可表示为: 给定一正定矩阵 $P$ , 存在着满足式(9-264)的正定矩阵 $Q$ , 而 $x^{\mathrm{T}}Px$ 是该系统的一个李雅普诺夫函数, 式(9-264)称为李雅普诺

夫矩阵代数方程。

但是，按上述先给定 $P$ 、再验证 $Q$ 是否正定的步骤去分析系统稳定性时，若 $P$ 选取不当，往往会导致 $Q$ 非正定，需反复多次选取 $P$ 阵来检验 $Q$ 是否正定，使用中很不方便。因而在应用时，往往是先选取 $Q$ 为正定实对称矩阵，再求解式(9-264)，若所求得的 $P$ 阵为正定实对称矩阵，则可判定系统是渐近稳定的。由于使用中常选取 $Q$ 阵为单位阵或对角线阵，比起先选 $P$ 阵再检验 $Q$ 阵要方便得多，所以在判定系统的稳定性时常利用下述定理：

定理9-13 线性定常系统 $\dot{x} = Ax, x(0) = x_0, t \geqslant 0$ 的原点平衡状态 $x_e = 0$ 为渐近稳定的充分必要条件是，对于任意给定的一个正定对称矩阵 $Q$ ，有唯一的正定对称矩阵 $P$ 使式(9-264)成立。

需要说明的是,在利用上述定理判断线性定常系统的渐近稳定性时,对Q的唯一限制是其应为对称正定阵。显然,满足这种限制的Q阵可能有无穷多个,但判断的结果即系统是否为渐近稳定,则和Q阵的不同选择无关。上述定理的实质是给出了矩阵A的所有特征值均具有负实部的充分必要条件。

根据定常系统大范围渐近稳定判别定理2可以推知，若系统任意的状态轨迹在非零状态不存在 $\dot{V} (x)$ 恒为零时， $Q$ 阵可选择为正半定的，即允许 $Q$ 取半正定对角阵时主对角线上部分元素为零，而解得的 $P$ 阵仍应正定。

由于利用上述定理判断线性定常系统是否渐近稳定时需要求解李雅普诺夫方程(9-264)，但一般地说求解李雅普诺夫方程并非易事，因而这种方法往往不用来判定系统的渐近稳定性，而是用来构造线性定常连续渐近稳定系统。

例9-25 已知线性定常连续系统状态方程为

$$\dot {x} _ {1} = x _ {2}, \quad \dot {x} _ {2} = 2 x _ {1} - x _ {2}$$

试用李雅普诺夫方程判定系统的渐近稳定性。

解 为便于对比,先用特征值判据判断。系统状态方程为

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c} 0 & 1 \\ 2 & - 1 \end{array} \right] \boldsymbol {x}, \quad \boldsymbol {A} = \left[ \begin{array}{c c} 0 & 1 \\ 2 & - 1 \end{array} \right]

| \lambda I - A | = \left| \begin{array}{c c} \lambda & - 1 \\ - 2 & \lambda + 1 \end{array} \right| = \lambda^ {2} + \lambda - 2 = (\lambda - 1) (\lambda + 2)
$$

特征值为-2,1，故系统不稳定。令

$$
\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A} = - Q = - I
\boldsymbol {P} = \boldsymbol {P} ^ {\mathrm{T}} = \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right]
$$
