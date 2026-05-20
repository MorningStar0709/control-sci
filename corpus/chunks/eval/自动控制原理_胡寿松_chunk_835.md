$$\boldsymbol {u} ^ {*} (t) = - r ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \bar {\boldsymbol {P}} \boldsymbol {x} (t) = - 2 x _ {1} (t) - 2 x _ {2} (t)J ^ {*} = \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} (0) \overline {{{\boldsymbol {P}}}} \boldsymbol {x} (0) = 1$$

检验闭环系统的稳定性：

$$
\dot {\boldsymbol {x}} (t) = (\boldsymbol {A} - \boldsymbol {b r} ^ {- 1} \boldsymbol {b} ^ {\mathrm{T}} \overline {{\boldsymbol {P}}}) \boldsymbol {x} (t) = \left[ \begin{array}{c c} - 2 & - 2 \\ 1 & 0 \end{array} \right] \boldsymbol {x} (t) = \overline {{\boldsymbol {A}}} \boldsymbol {x} (t)
$$

其特征方程为

$$
\det (\lambda \boldsymbol {I} - \bar {\boldsymbol {A}}) = \det \left[ \begin{array}{c c} \lambda + 2 & 2 \\ - 1 & \lambda \end{array} \right]
= \lambda^ {2} + 2 \lambda + 2 = 0
$$

求出特征值为 $\lambda_{1}=-1+j,\lambda_{2}=-1-j$ 。由特征值判据知，闭环系统渐近稳定。
