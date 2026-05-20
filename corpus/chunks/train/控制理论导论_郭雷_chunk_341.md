$$
\begin{array}{l} E (u _ {k} + L _ {k} x _ {k}) ^ {*} M _ {k} (u _ {k} + L _ {k} x _ {k}) \\ = E \left[ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} \left(x _ {k} + \hat {x} _ {k}\right) \right] ^ {*} M _ {k} \left[ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} \left(x _ {k} - \hat {x} _ {k}\right) \right] \\ = \operatorname{tr} E [ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} (x _ {k} - \hat {x} _ {k}) ] [ u _ {k} + L _ {k} \hat {x} _ {k} + L _ {k} (x _ {k} - \hat {x} _ {k}) ] ^ {*} M _ {k} \\ = \operatorname{tr} E (u _ {k} + L _ {k} \hat {x} _ {k}) (u _ {k} + L _ {k} \hat {x} _ {k}) ^ {*} M _ {k} + \operatorname{tr} L _ {k} P _ {k} L _ {k} ^ {*} M _ {k} \\ = E \left(u _ {k} + L _ {k} \hat {x} _ {k}\right) ^ {*} M _ {k} \left(u _ {k} + L _ {k} \hat {x} _ {k}\right) + \operatorname{tr} L _ {k} P _ {k} L _ {k} ^ {*} M _ {k}. \\ \end{array}
$$

为固定起见，设 $x_{k}$ 为 $\pmb{n}$ 维的．设 $S_{k}$ 是由下述Riccati方程从 $N$ 递推地写出的 $n\times n$ 阵：

$$
\begin{array}{l} S _ {k} = \left(\Phi_ {k + 1, k} - B _ {k} L _ {k}\right) ^ {*} S _ {k + 1} \left(\Phi_ {k + 1, k} - B _ {k} L _ {k}\right) + L _ {k} ^ {*} Q _ {2} (k) L _ {k} + Q _ {1} (k) \\ (= \Phi_ {k + 1, k} ^ {*} S _ {k + 1} \Phi_ {k + 1, k} - \Phi_ {k + 1, k} ^ {*} S _ {k + 1} B _ {k} M _ {k} ^ {+} B _ {k} ^ {*} S _ {k + 1} \Phi_ {k + 1, k} + Q _ {1} (k)), \tag {4.4.44} \\ \end{array}
L _ {k} = M _ {k} ^ {+} B _ {k} ^ {*} S _ {k + 1} \Phi_ {k + 1, k}, \tag {4.4.45}M _ {k} = Q _ {2} (k) + B _ {k} ^ {*} S _ {k + 1} B _ {k}, \quad S _ {N} = Q _ {0}. \tag {4.4.46}
$$

$S_{k}$ 是非负定的 Hermite 阵， $k=0,1,\cdots,N.$

定理 4.4.3 对系统 (4.4.40), (4.4.41), 使 $EJ(u)(J(u)$ 由式 (4.4.43) 表达) 最小的最优随机控制为

$$u _ {k} ^ {0} = - L _ {k} \hat {x} _ {k} + (I - M _ {k} ^ {+} M _ {k}) u _ {k}, \quad k = 0, 1, \dots , N - 1, \tag {4.4.47}$$

这里 $u_{k}$ 为任一线性反馈控制，并且

$$E J (u ^ {0}) = E x _ {0} ^ {\mathrm{T}} S _ {0} E x _ {0} + \operatorname{tr} S _ {0} R + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} S _ {k + 1} D _ {k + 1} D _ {k + 1} ^ {*} + \sum_ {k = 0} ^ {N - 1} \operatorname{tr} L _ {k} P _ {k} L _ {k} ^ {*} M _ {k}. \tag {4.4.48}$$

证明 注意到

$$(M _ {k} ^ {+} M _ {k} - I) M _ {k} (M _ {k} ^ {+} M _ {k} - I) = 0,$$

所以

$$S _ {k + 1} B _ {k} \left[ M _ {k} ^ {+} M _ {k} - I \right] = 0,$$

或

$$S _ {k + 1} S _ {k} M _ {k} ^ {+} M _ {k} = S _ {k + 1} B _ {k}. \tag {4.4.49}$$

注意到

$$L _ {k} ^ {*} M _ {k} = \Phi_ {k + 1, k} ^ {*} S _ {k + 1} B _ {k},L _ {k} ^ {*} M _ {k} L _ {k} = \Phi_ {k + 1, k} ^ {*} S _ {k + 1} B _ {k} L _ {k} = L _ {k} ^ {*} B _ {k} ^ {*} S _ {k + 1} \Phi_ {k + 1, k},$$

可把 $J(u)$ 改写成
