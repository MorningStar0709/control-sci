(ii) for each frequency ω

$$\kappa (W _ {1} ^ {- 1} W _ {d}) \overline {{\sigma}} (W _ {e} S _ {o} W _ {d}) + \overline {{\sigma}} (W _ {1} ^ {- 1} P W _ {1}) \overline {{\sigma}} (W _ {2} P ^ {- 1} W _ {2} ^ {- 1}) \overline {{\sigma}} (W _ {2} T _ {o} W _ {1}) \leq 1. \tag {8.10}$$

Remark 8.6 If the appropriate invertibility conditions are not satisfied, then an alternative sufficient condition for robust performance can be given by

$$\overline {{\sigma}} (W _ {d}) \overline {{\sigma}} (W _ {e} S _ {o}) + \overline {{\sigma}} (P W _ {1}) \overline {{\sigma}} (W _ {2} K S _ {o}) \leq 1.$$

Similar to the previous case, there are many different variations of sufficient conditions although equation (8.10) may be the most useful one. ✸

Remark 8.7 It is important to note that in this case, the robust stability condition is given in terms of $L _ { i } = K P$ while the nominal performance condition is given in terms of $L _ { o } = P K$ . These classes of problems are called skewed problems or problems with skewed specifications.2 Since, in general, $P K \neq K P$ , the robust stability margin or tolerances for uncertainties at the plant input and output are generally not the same.

✸

Remark 8.8 It is also noted that the robust performance condition is related to the condition number of the weighted nominal model. So, in general, if the weighted nominal model is ill-conditioned at the range of critical frequencies, then the robust performance condition may be far more restrictive than the robust stability condition and the nominal performance condition together. For simplicity, assume $W _ { 1 } = I , W _ { d } = I$ and $W _ { 2 } = w _ { t } I ,$ where $w _ { t } \in \mathcal { R } \mathcal { H } _ { \infty }$ is a scalar function. Further, P is assumed to be invertible. Then the robust performance condition (8.10) can be written as

$$\overline {{\sigma}} (W _ {e} S _ {o}) + \kappa (P) \overline {{\sigma}} (w _ {t} T _ {o}) \leq 1, \forall \omega .$$

Comparing these conditions with those obtained for nonskewed problems shows that the condition related to robust stability is scaled by the condition number of the plant.3 Since $\kappa ( P ) \geq 1$ , it is clear that the skewed specifications are much harder to satisfy if the plant is not well conditioned. This problem will be discussed in more detail in Section 10.3.3 of Chapter 10. ✸

Remark 8.9 Suppose K is invertible, then $\tilde { T } _ { e \tilde { d } }$ can be written as
