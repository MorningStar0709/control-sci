$$
\left\{ \begin{array}{l} \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {R} = \boldsymbol {d} ^ {\mathrm{T}}, \quad \boldsymbol {T} \boldsymbol {R} = \boldsymbol {R} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {B} _ {\mathrm{c}} \boldsymbol {C} - \boldsymbol {g a} ^ {\mathrm{T}}, \\ \boldsymbol {A} _ {c} = \boldsymbol {T} - \boldsymbol {R b h} ^ {\mathrm{T}}, \quad \boldsymbol {T} = \boldsymbol {E} + \boldsymbol {g v} ^ {\mathrm{T}}. \end{array} \right. \tag {1.6.22}
$$

可见，如果能够从等式(1.6.22)中求出 $d^{T}$ ，R和 $B_{c}$ ，那么 $A_{c}$ 自然就确定了。

假设等式 (1.6.22) 有解，然后具体地把 $d^{\mathrm{T}}, R$ 和 $B_{c}$ 解出来，这样所得到的解一定满足要求。为此，在方程 (1.6.22) 第二个等式的两边左乘 $h^{\mathrm{T}}T^{i-1}, i=1,2,\cdots,\nu_{0}-2$ ，于是得出

$$\boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {R} \stackrel {\text { def }} {=} \boldsymbol {d} ^ {\mathrm{T}}, \tag {1.6.23}\boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {i} \boldsymbol {R} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {i - 1} \boldsymbol {R} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {i - 1} \boldsymbol {B} _ {c} \boldsymbol {C}, \quad i = 1, 2, \dots , \nu_ {0} - 2, (1. 6. 2 4)\boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 1} \boldsymbol {R} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \boldsymbol {R} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \boldsymbol {B} _ {c} \boldsymbol {C} - \boldsymbol {a} ^ {\mathrm{T}}. \tag {1.6.25}$$

将式 (1.6.23), (1.6.24) 代入式 (1.6.25), 并经简单计算得

$$
\begin{array}{l} \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 1} \boldsymbol {R} = \boldsymbol {d} ^ {\mathrm{T}} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) ^ {\nu_ {0} - 1} + \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {B} _ {c} \boldsymbol {C} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) ^ {\nu_ {0} - 2} \\ + \dots + h ^ {T} T ^ {\nu_ {0} - 3} B _ {c} C (A + b d ^ {T}) + h ^ {T} T ^ {\nu_ {0} - 2} B _ {c} C - a ^ {T}. \tag {1.6.26} \\ \end{array}
$$

另一方面，假设矩阵 $\pmb{T}$ 的特征多项式为

$$f (\lambda) = \lambda^ {\nu_ {0} - 1} - \theta_ {\nu_ {0} - 2} \lambda^ {\nu_ {0} - 2} - \dots - \theta_ {1} \lambda - \theta_ {0},$$

则有

$$\boldsymbol {T} ^ {\nu_ {0} - 1} = \theta_ {\nu_ {0} - 2} \boldsymbol {T} ^ {\nu_ {0} - 2} + \dots + \theta_ {1} \boldsymbol {T} + \theta_ {0} \boldsymbol {I} _ {\nu_ {0} - 1}.$$

于是
