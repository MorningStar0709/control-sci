# Coefficient-Pole Sensitivity

Finite precision in the representation of the coefficients of the controller gives a distortion of the poles and zeros of the controller. The following analysis gives quantitative results for the sensitivity of the roots of a polynomial with respect to changes in the coefficients. Consider a linear filter with distinct poles in $p_{i}$ and the characteristic polynomial

$$A (z, a _ {i}) = z ^ {n} + a _ {1} z ^ {n - 1} + \dots + a _ {n} = (z - p _ {1}) \dots (z - p _ {n})$$

The characteristic polynomial A can be regarded as a function of z and $a_{i}$ . When the parameter $a_{i}$ is changed to $a_{i} + \delta a_{i}$ , the poles are changed from $p_{k}$ to $p_{k} + \delta p_{k}$ . Hence

$$0 = A (p _ {k} + \delta p _ {k}, a _ {i} + \delta a _ {i}) \approx A (p _ {k}, a _ {i}) + \left. \frac {\delta A}{\delta z} \right| _ {p _ {k}} \delta p _ {k} + \left. \frac {\delta A}{\delta a _ {i}} \right| _ {p _ {k}} \delta a _ {i} + \dots$$

The first term on the right-hand side is zero. If terms of second order and higher are neglected, it follows that

$$\delta p _ {k} \approx - \left. \frac {\delta A / \delta a _ {i}}{\delta A / \delta z} \right| _ {z = p _ {k}} \cdot \delta a _ {i}$$

Because

$$\frac {\delta A}{\delta a _ {i}} \Big | _ {z = p _ {k}} = p _ {k} ^ {n - i} \quad \text { and } \quad \frac {\delta A}{\delta z} \Big | _ {z = p _ {k}} = \prod_ {j \neq k} (p _ {k} - p _ {j})$$

the following estimate is obtained:

$$\delta p _ {k} \approx - \frac {p _ {k} ^ {n - i}}{\prod_ {j \neq k} (p _ {k} - p _ {j})} \delta a _ {i} \tag {9.17}$$

If the polynomial has a root $p_k$ with multiplicity $m$ , Eq. (9.17) becomes

$$\delta p _ {k} \approx - \frac {p _ {k} ^ {n - i}}{\prod_ {j \neq k} (p _ {k} - p _ {j})} (\delta a _ {i}) ^ {1 / m} \tag {9.18}$$

If the filter is stable, then $|p_{k}| < 1$ and the numerator of (9.17) has its largest magnitude for i = n. The coefficient $a_{n}$ is thus the most sensitive parameter. Furthermore, the denominator will be small if the poles are close, which then makes the system sensitive to changes in the coefficients. Equation (9.18) shows that the sensitivity is even higher if the polynomial has multiple roots. Equations (9.17) and (9.18) may be used to determine the conditioning numbers for the transformation from the diagonal form to the companion form. It follows from the equations that the computation of companion forms may be poorly conditioned.
