(4) 按照极点配置方法求向量 $a \in \mathbb{R}^n, v \in \mathbb{R}^{\nu_0 - 1}$ , 使得矩阵

$$
\left[ \begin{array}{c c} \boldsymbol {A _ {1}} & \boldsymbol {b h ^ {\mathrm{T}}} \\ \boldsymbol {g a ^ {\mathrm{T}}} & \boldsymbol {E + g v ^ {\mathrm{T}}} \end{array} \right]
$$

有预先指定的 $n + \nu_0 - 1$ 个复特征值；

(5) 计算向量 $e^{T}$ 和 $\overline{c}_{i}^{T}, i = 0, 1, \cdots, \nu_{0} - 2,$ 使得

$$\boldsymbol {a} ^ {\mathrm{T}} - \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {C} \boldsymbol {A} _ {1} ^ {\nu_ {0} - 1} = \overline {{\boldsymbol {e}}} _ {0} ^ {\mathrm{T}} \boldsymbol {C} + \overline {{\boldsymbol {e}}} _ {1} ^ {\mathrm{T}} \boldsymbol {C} \boldsymbol {A} _ {1} + \dots + \overline {{\boldsymbol {e}}} _ {\nu_ {0} - 2} ^ {\mathrm{T}} \boldsymbol {C} \boldsymbol {A} _ {1} ^ {\nu_ {0} - 2};$$

然后，取

$$\boldsymbol {d} ^ {\mathrm{T}} = \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {C},$$

请注意，其解不唯一；

(6) 计算向量 $e_{i}^{T}, i = 0, 1, \cdots, \nu_{0} - 2.$ 使得

$$\boldsymbol {a} ^ {\mathrm{T}} - \boldsymbol {e} ^ {\mathrm{T}} \boldsymbol {C} (\boldsymbol {A} _ {1} + \boldsymbol {b d} ^ {\mathrm{T}}) ^ {\nu_ {0} - 1} = \boldsymbol {e} _ {0} ^ {\mathrm{T}} \boldsymbol {C} + \boldsymbol {e} _ {1} ^ {\mathrm{T}} \boldsymbol {C} (\boldsymbol {A} _ {1} + \boldsymbol {b d} ^ {\mathrm{T}}) + \dots + \boldsymbol {e} _ {\nu_ {0} - 2} ^ {\mathrm{T}} \boldsymbol {C} (\boldsymbol {A} _ {1} + \boldsymbol {b d} ^ {\mathrm{T}}) ^ {\nu_ {0} - 2};$$

(7) 令 $\pmb{T} = \pmb{E} + \pmb{g}\pmb{v}^{\mathrm{T}}$ , 并求出它的特征多项式

$$f (\lambda) = \lambda^ {\nu_ {0} - 1} - \theta_ {\nu_ {0} - 2} \lambda^ {\nu_ {0} - 2} - \dots - \theta_ {1} \lambda - \theta_ {0};$$

(8) 计算 $a_{i}$ 和 $r_{i}, i = 0, 1, \cdots, \nu_{0} - 2,$

$$\boldsymbol {a} _ {\nu_ {0} - i - 2} ^ {\mathrm{T}} = \boldsymbol {e} _ {i} ^ {\mathrm{T}} + \theta_ {i} \boldsymbol {e} ^ {\mathrm{T}} + \theta_ {i + 1} \boldsymbol {a} _ {0} ^ {\mathrm{T}} + \dots + \theta_ {\nu_ {0} - 2} \boldsymbol {a} _ {\nu_ {0} - i - 2} ^ {\mathrm{T}}, \quad i = 0, 1, \dots , \nu_ {0} - 2,\boldsymbol {r} _ {0} ^ {\mathrm{T}} = \boldsymbol {e} ^ {\mathrm{T}} C,\boldsymbol {r} _ {i + 1} ^ {\mathrm{T}} = \boldsymbol {r} _ {i} ^ {\mathrm{T}} \left(\boldsymbol {A} _ {1} + \boldsymbol {b d} ^ {\mathrm{T}}\right) + \boldsymbol {a} _ {i} ^ {\mathrm{T}} \boldsymbol {C}, \quad i = 0, 1, \dots , \nu_ {0} - 2;$$

(9) 计算
