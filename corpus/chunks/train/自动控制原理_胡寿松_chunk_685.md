系统加入状态反馈后可能改变其可观测性意味着有可能使得

$$\operatorname{rank} \bar {\mathbf {V}} _ {o} \neq \operatorname{rank} \bar {\mathbf {V}} _ {o H} \tag {9-221}$$

因为 $\bar{V}_{o}$ 也是系统 $\Sigma_{0}$ 的可控性判别阵， $\bar{V}_{oH}$ 又是系统 $\Sigma_{H}$ 的可控性判别阵，式(9-221)表明，输出至状态微分的反馈可能改变系统的可控性。证毕。

定理 9-3 对于系统(9-208)，输出至参考输入反馈的引入能同时不改变系统的可控性和可观测性，即输出反馈系统 $\Sigma_{F}$ 为可控（可观测）的充分必要条件是被控系统 $\Sigma_{0}$ 为可控（可观测）。

证明 首先,由于对任一输出至参考输入的反馈系统都能找到一个等价的状态反馈系统,由定理9-1知状态反馈可保持可控性,因而输出至参考输入反馈的引入不改变系统的可控性。

由于 $\Sigma_0$ 和 $\Sigma_F$ 的可观测性判别阵分别为

$$
\boldsymbol {V} _ {o} = \left[ \begin{array}{c} \boldsymbol {C} \\ \boldsymbol {C A} \\ \vdots \\ \boldsymbol {C A} ^ {n - 1} \end{array} \right], \quad \boldsymbol {V} _ {a F} = \left[ \begin{array}{c} \boldsymbol {C} \\ \boldsymbol {C (A - B F C)} \\ \vdots \\ \boldsymbol {C (A - B F C) ^ {n - 1}} \end{array} \right]
$$

并且

$$
\boldsymbol {C} = \left[ \begin{array}{l} \boldsymbol {c} _ {1} \\ \boldsymbol {c} _ {2} \\ \vdots \\ \boldsymbol {c} _ {q} \end{array} \right], \quad \boldsymbol {C A} = \left[ \begin{array}{l} \boldsymbol {c} _ {1} \boldsymbol {A} \\ \boldsymbol {c} _ {2} \boldsymbol {A} \\ \vdots \\ \boldsymbol {c} _ {q} \boldsymbol {A} \end{array} \right], \quad \boldsymbol {C (A - B F C)} = \left[ \begin{array}{l} \boldsymbol {c} _ {1} (\boldsymbol {A} - \boldsymbol {B F C}) \\ \boldsymbol {c} _ {2} (\boldsymbol {A} - \boldsymbol {B F C}) \\ \vdots \\ \boldsymbol {c} _ {q} (\boldsymbol {A} - \boldsymbol {B F C}) \end{array} \right]
$$

式中， $c_{i}(i=1,2,\cdots,q)$ 为行向量，将 F 表为列向量组 $\{f_{j}\}$ ，即 $F=\left[f_{1}\quad f_{2}\quad\cdots\quad f_{q}\right]$ ，则

$$
\begin{array}{l} \boldsymbol {c} _ {i} (\boldsymbol {A} - \boldsymbol {B F C}) = \boldsymbol {c} _ {i} \boldsymbol {A} - \boldsymbol {c} _ {i} \boldsymbol {B} \left(\boldsymbol {f} _ {1} \boldsymbol {c} _ {1} + \boldsymbol {f} _ {2} \boldsymbol {c} _ {2} + \dots + \boldsymbol {f} _ {q} \boldsymbol {c} _ {q}\right) \\ = \boldsymbol {c} _ {i} \boldsymbol {A} - \left[ \left(\boldsymbol {c} _ {i} \boldsymbol {B} \boldsymbol {f} _ {1}\right) \boldsymbol {c} _ {1} + \left(\boldsymbol {c} _ {i} \boldsymbol {B} \boldsymbol {f} _ {2}\right) \boldsymbol {c} _ {2} + \dots + \left(\boldsymbol {c} _ {i} \boldsymbol {B} \boldsymbol {f} _ {q}\right) \boldsymbol {c} _ {q} \right] \\ \end{array}
$$

令式中 $c_{i}Bf_{j}=\alpha_{j},\alpha_{j}$ 为标量, $j=1,2,\cdots,q$ ,则有
