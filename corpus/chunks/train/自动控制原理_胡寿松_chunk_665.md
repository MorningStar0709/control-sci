# (2) 对偶原理

在研究系统的可控性和可观测性时，利用对偶原理常常带来许多方便。

设系统为 $\Sigma_{1}(A,B,C)$ ，则系统 $\Sigma_{2}(A^{T},C^{T},B^{T})$ 为系统 $\Sigma_{1}$ 的对偶系统。其动态方程分别为

$$\Sigma_ {1}: \quad \dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {B} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {C} \boldsymbol {x} \tag {9-186}\Sigma_ {2}: \quad \dot {\pmb {z}} = \pmb {A} ^ {\mathrm{T}} \pmb {z} + \pmb {C} ^ {\mathrm{T}} \pmb {v}, \quad \pmb {w} = \pmb {B} ^ {\mathrm{T}} \pmb {z} \tag {9-187}$$

式中，x,z 均为 n 维状态向量；u,w 均为 p 维向量；y,v 均为 q 维向量。注意到系统与对偶系统之间，其输入、输出向量的维数是相交换的，当 $\Sigma_{2}$ 为 $\Sigma_{1}$ 的对偶系统时， $\Sigma_{1}$ 也是 $\Sigma_{2}$ 的对偶系统。

不难验证, 系统 $\Sigma_{1}$ 的可控性判别矩阵 $[BAB\cdots A^{n-1}B]$ 与对偶系统 $\Sigma_{2}$ 的可观测性矩阵 $[(B^{\mathrm{T}})^{\mathrm{T}}(A^{\mathrm{T}})^{\mathrm{T}}(B^{\mathrm{T}})^{\mathrm{T}}\cdots((A^{\mathrm{T}})^{\mathrm{T}})^{n-1}(B^{\mathrm{T}})^{\mathrm{T}}]$ 完全相同; 系统 $\Sigma_{1}$ 的可观测性矩阵 $[C^{\mathrm{T}}A^{\mathrm{T}}C^{\mathrm{T}}\cdots(A^{\mathrm{T}})^{n-1}C^{\mathrm{T}}]$ 与对偶系统 $\Sigma_{2}$ 的可控性判别矩阵 $[C^{\mathrm{T}}A^{\mathrm{T}}C^{\mathrm{T}}\cdots(A^{\mathrm{T}})^{n-1}C^{\mathrm{T}}]$ 完全相同。

应用对偶原理,能把可观测的单输入-单输出系统化为可观测标准型的问题转化为将其对偶系统化为可控标准型的问题。设单输入-单输出系统动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {c} \boldsymbol {x} \tag {9-188}$$

系统可观测，但 A, c 不是可观测标准型。其对偶系统动态方程为

$$\dot {\boldsymbol {z}} = \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {z} + \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {v}, \quad \boldsymbol {w} = \boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {z} \tag {9-189}$$

对偶系统一定可控,但不是可控标准型。可利用已知的化为可控标准型的原理和步骤,先将对偶系统化为可控标准型,再一次使用对偶原理,便可获得原系统的可观测标准型。下面仅给出其计算步骤:

1) 列出对偶系统的可控性矩阵(即原系统的可观测性矩阵 $V_{1}$ )

$$
\bar {\boldsymbol {S}} _ {2} = \boldsymbol {V} _ {1} = \left[ \begin{array}{l l l l} \boldsymbol {c} ^ {\mathrm{T}} & \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {c} ^ {\mathrm{T}} & \dots & (\boldsymbol {A} ^ {\mathrm{T}}) ^ {n - 1} \boldsymbol {c} ^ {\mathrm{T}} \end{array} \right]
$$

2) 求 $V_{1}$ 的逆阵 $V_{1}^{-1}$ ，且记为行向量组

$$
\boldsymbol {V} _ {1} ^ {- 1} = \left[ \begin{array}{c} \boldsymbol {v} _ {1} ^ {\mathrm{T}} \\ \boldsymbol {v} _ {2} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {v} _ {n} ^ {\mathrm{T}} \end{array} \right]
$$
