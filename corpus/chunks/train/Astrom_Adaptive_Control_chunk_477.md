# THEOREM 6.8 Conditional updating

Consider the plant (6.86) where $v$ is a disturbance that is bounded by

$$\sup _ {t} \left| \frac {R}{A _ {o} A _ {m} B} v \right| \leq C _ {1}$$

where R is the polynomial in the feedback law and $C_{1}$ is a constant. Assume that the direct adaptive algorithm defined by Eqs. (6.41) and (6.42) is used, with the modification that the parameters are updated only when the estimation error is such that

$$| e | \geq \frac {2 C _ {1}}{2 - \max (b _ {0} / r _ {0} , 1)}$$

Let Assumptions A1-A3 hold, and assume in addition that $0 < b_{0} < 2r_{0}$ . Then the inputs and outputs of the closed-loop system are bounded. ☐

Proofs of this theorem can be found in Egardt (1979) and Goodwin and Sin (1984). The modification of the algorithm is referred to as conditional updating or introduction of a dead zone in the estimator.

Of course, the result is of limited practical value because it requires an upper bound on the disturbance, which is not known a priori. The bound also depends on the ratio $b_{0}/r_{0} = b_{0}/\hat{b}_{0}$ , where $b_{0}$ is the instantaneous gain. The estimate of this gain is thus essential. If $b_{0}/r_{0} = 1$ and $A_{v} = A_{m} = 1$ , it follows that R = B, and the condition for updating becomes

$$| e (t) | \geq 2 \sup | v (t) |$$

This means that the estimate will be updated when the estimation error is twice as large as the maximum noise amplitude.

Another modification of the algorithm also leads to bounded signals. The modification consists of using the updating law of Eqs. (6.41) if the magnitude of the estimates is less than a given bound and to project into a bounded set if Eqs. (6.41) give estimates outside the bounds. We refer to Theorem 4.4 of Egardt (1979) for details. This method will, of course, require that the bounds on the parameters be known a priori.
