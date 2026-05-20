$$
\left\{ \begin{array}{l} \dot {\boldsymbol {x}} = \left[ A _ {1} - B _ {1} \left(I + E _ {1}\right) ^ {- 1} C _ {1} \right] \boldsymbol {x} + B _ {1} \left(I + E _ {1}\right) ^ {- 1} \boldsymbol {u} \\ \boldsymbol {y} = \left(I + E _ {1}\right) ^ {- 1} C _ {1} \boldsymbol {x} + \left(I + E _ {1}\right) ^ {- 1} E _ {1} \boldsymbol {u} \end{array} \right. \tag {11.65}
$$

而且，由于 $S_{1}$ 为能控和能观测，可知 $S_{YF}$ 也为能控和能观测。因此，对于直接输出反馈系统 $S_{YF}$ ，其渐定稳定等价于BIBO稳定，而稳定条件为矩阵 $[A_1 - B_1(I + E_1)^{-1}C_1]$ 的特征值均具有负实部。进一步，可以导出

$$
\begin{array}{l} \det \left[ s I - A _ {1} + B _ {1} \left(I + E _ {1}\right) ^ {- 1} C _ {1} \right] \\ = \det \left\{\left(s I - A _ {1}\right) \left[ I + \left(s I - A _ {1}\right) ^ {- 1} B _ {1} \left(I + E _ {1}\right) ^ {- 1} C _ {1} \right] \right\} \\ = \det (s I - A _ {1}) \det [ I + (s I - A _ {1}) ^ {- 1} B _ {1} (I + E _ {1}) ^ {- 1} \cdot C _ {1} ] \tag {11.66} \\ \end{array}
$$

而且，若令

$$\hat {G} _ {1} (s) = \left(s I - A _ {1}\right) ^ {- 1} B _ {1} \left(I + E _ {1}\right) ^ {- 1}, \hat {G} _ {2} (s) = C _ {1} \tag {11.67}$$

那么因 $\operatorname{det}[I + \hat{G}_1(s)\hat{G}_2(s)] = \operatorname{det}[I + \hat{G}_2(s)\hat{G}_1(s)]$ ，故可将(11.66)进而表为：

$$
\begin{array}{l} \det \left[ s I - A _ {1} + B _ {1} \left(I + E _ {1}\right) ^ {- 1} C _ {1} \right] \\ = \det (s I - A _ {1}) \det [ I + C _ {1} (s I - A _ {1}) ^ {- 1} B _ {1} (I + E _ {1}) ^ {- 1} ] \\ = \det (s I - A _ {1}) \det \left\{\left[ I + E _ {1} + C _ {1} (s I - A _ {1}) ^ {- 1} B _ {1} \right] \left(I + E _ {1}\right) ^ {- 1} \right\} \\ = \det (s I - A _ {1}) \det [ I + G _ {1} (s) ] \det (I + E _ {1}) ^ {- 1} \tag {11.68} \\ \end{array}
$$

此外，因 $\operatorname{det}(I + E_1) = \operatorname{det}[I + G_1(\infty)] \neq 0$ ，故若令 $\beta_2 = \operatorname{det}(I - E_1)^{-1}$ 并注意到(11.63)，则由(11.68)还可导出：

$$\det \left[ s I - A _ {1} + B _ {1} (I + E _ {1}) ^ {- 1} C _ {1} \right] = \frac {\beta_ {2}}{\beta_ {1}} \Delta_ {1} (s) \det \left[ I + G _ {1} (s) \right] \tag {11.69}$$

这表明， $S_{YP}$ 的稳定条件可等价地化为

$$\Delta_ {1} (s) \det [ I + G _ {1} (s) ] = 0 \tag {11.70}$$

的根均具有负实部。于是，论断（i）证得。

(2) 再来证明论断 (ii)。已知 $G_{1}(s) = N_{1}(s)D_{1}^{-1}(s)$ ，可导出 $S_{YF}$ 的传递函数矩阵 $G_{F}(s)$ 为：

$$
\begin{array}{l} G _ {F} (s) = G _ {1} (s) \left[ I + G _ {1} (s) \right] ^ {- 1} = N _ {1} (s) D _ {1} ^ {- 1} (s) \left[ I + N _ {1} (s) D _ {1} ^ {- 1} (s) \right] ^ {- 1} \\ = N _ {1} (s) \left[ D _ {1} (s) + N _ {1} (s) \right] ^ {- 1} \tag {11.71} \\ \end{array}
$$

但已知 $\{D_1(s), N_1(s)\}$ 为右互质，故由互质性的贝佐特等式判据可知，存在多项式矩阵 $X(s)$ 和 $Y(s)$ 使成立

$$X (s) D _ {1} (s) + Y (s) N _ {1} (s) = I \tag {11.72}$$

进而，可把上式改写为
