$$
\begin{array}{l} E \left\{\left[ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} \left(x _ {k} - \hat {x} _ {k}\right) \right] ^ {\mathrm{T}} M _ {k} \left[ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} \left(x _ {k} - \hat {x} _ {k}\right) \right] \mid y ^ {k} \right\} \\ = \left(u _ {k} + L _ {k} \hat {x} _ {k}\right) ^ {\mathrm{T}} M _ {k} \left(u _ {k} + L _ {k} \hat {x} _ {k}\right) + \operatorname{tr} L _ {k} P _ {k} L _ {k} ^ {\mathrm{T}} M _ {k}, \\ \end{array}
$$

再注意到 $w_{k + 1}$ 和 $(y^{k},x_{k})$ 独立，便知

$$
\begin{array}{l} E J (u) = E x _ {0} ^ {\mathrm{T}} S _ {0} x _ {0} + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} \left(D _ {k + 1} ^ {\mathrm{T}} S _ {k + 1} D _ {k + 1} + L _ {k} P _ {k} L _ {k} ^ {\mathrm{T}} M _ {k}\right) \\ + \sum_ {k = 0} ^ {N - 1} E (u _ {k} + L _ {k} \hat {x} _ {k}) ^ {\mathrm{T}} M _ {k} (u _ {k} + L _ {k} \hat {x} _ {k}). \tag {4.4.53} \\ \end{array}
$$

据定理 4.4.2 及条件 C1), 便知 $P_{k}$ 是不依赖控制的确定性阵, 所以使式 (4.4.53) 达极小的控制为

$$u _ {k} ^ {0} = - L _ {k} \hat {x} _ {k} + (I - M _ {k} ^ {+} M _ {k}) u _ {k}, \quad k = 0, \dots , N - 1,$$

$u_{k}$ 为任一属 U 的容许控制.
