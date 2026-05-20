# Leakage

Another way to avoid estimator windup, called leakage, was discussed in Section 6.9. In continuous time the estimator was modified as shown in Eq. (6.84) by adding the term $\alpha(\theta^0 - \theta)$ . This means that the parameters will converge to $\theta^0$ when no useful information is obtained, that is, when $e = 0$ . A similar modification can also be made in discrete-time estimators. When a least-squares type of algorithm is used, it is also common to add a similar term to the $P$ equation to drive it toward a specified matrix.
