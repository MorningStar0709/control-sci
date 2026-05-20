# EXAMPLE 2.2 Decrease of variance

Consider the case in which the model in Eq. (2.12) has only one parameter. Let $t$ be the number of observations. It follows from (ii) of Theorem 2.2 that the variance of the estimate is given by

$$\operatorname{cov} \hat {\theta} = \frac {\sigma^ {2}}{\sum_ {k = 1} ^ {t} \varphi^ {2} (k)}$$

Several different cases can now be considered, depending on the asymptotic behavior of $\varphi(k)$ for large k. Introduce the notation $a \sim b$ to indicate that a and b are proportional.

(a) Assume that $\varphi(k) \sim e^{-\alpha k} \cdot \alpha > 0$ . The sum in the denominator above then converges, and the variance goes to a constant.   
(b) Assume that $\varphi(k) \sim k^a, a > 0$ . Then

$$
\sum_ {k = 1} ^ {t} \varphi^ {2} (k) \sim \left\{ \begin{array}{l l} \text { const } & a > 0. 5 \\ \log t & a = 0. 5 \\ t ^ {1 - 2 a} & a <   0. 5 \end{array} \right.
$$

The variance goes to zero if $a \leq 0.5$ .

(c) Assume that $\varphi(k) \sim 1$ . The variance then goes to zero as $1/t$ .   
(d) Assume that $\varphi(k) \sim k^a, a > 0$ . The variance then goes to zero as $t^{-(1+2a)}$ .   
(e) Assume that $\varphi(k) \sim e^{\alpha k}, \alpha > 0$ . The variance then goes to zero as $e^{-2\alpha t}$ .

□

The example shows clearly how the precision of the estimate depends on the rate of growth of the regression vector. The variance does not go to zero with increasing number of observations if the regression variable decreases faster than $1/\sqrt{t}$ . In the normal situation, when the regressors are of the same order of magnitude, the variance decreases as 1/t. The variance decreases more rapidly if the regression variables increase with time.

When several parameters are estimated, the convergence rates may be different for different parameters. This is related to the structure of the matrix $(\Phi^{T}\Phi)^{-1}$ in Eq. (2.6).
