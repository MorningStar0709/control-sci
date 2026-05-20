$$
\left[ \begin{array}{c} \mathcal {Y} (T) \\ \mathcal {Y} (T + 1) \\ \vdots \\ \mathcal {Y} (T + n - 1) \end{array} \right] = \mathcal {O X} (T)
$$

Multiplying (1.40) by C and subtracting gives

$$
\left[ \begin{array}{c} y (T) - C \hat {x} (T | T + n - 1) \\ y (T + 1) - C \hat {x} (T + 1 | T + n - 1) \\ \vdots \\ y (T + n - 1) - C \hat {x} (T + n - 1 | T + n - 1) \end{array} \right] = \mathcal {O} \big (x (T) - \hat {x} (T | T + n - 1) \big) -

\left[ \begin{array}{c c c c} 0 & & & \\ C & 0 & & \\ \vdots & \vdots & \ddots & \\ C A ^ {n - 2} & C A ^ {n - 3} & \dots & C \end{array} \right] \left[ \begin{array}{c} \hat {w} _ {T} (0) \\ \hat {w} _ {T} (1) \\ \vdots \\ \hat {w} _ {T} (n - 2) \end{array} \right]
$$

Applying (1.39) to this equation, we conclude $\mathcal { O } ( x ( T ) - \hat { x } ( T | T + n -$ 1)) → 0 with increasing T . Because the observability matrix has independent columns, we conclude $x ( T ) - { \hat { x } } ( T | T + n - 1 ) \to 0$ as $T \to \infty$ . Thus we conclude that the smoothed estimate ${ \hat { x } } ( T | T + n - 1 )$ converges to the state $x ( T )$ . Because the $\hat { w } _ { T } ( j )$ terms go to zero with increasing $T ,$ the last line of (1.40) gives xˆ $( T + n - 1 | T + n - 1 ) \to A ^ { n - 1 } { \hat { x } } ( T | T + n - 1 )$ as $T \to \infty$ . From the system model $A ^ { n - 1 } x ( T ) = x ( T + n - 1 )$ and, therefore, after replacing $T + n - 1$ by T , we have

$$\hat {x} (T | T) \rightarrow x (T) \quad \text { as } T \rightarrow \infty$$

and asymptotic convergence of the estimator is established.

This convergence result also covers MHE with prior weighting set to the exact arrival cost because that is equivalent to Kalman filtering and full least squares. The simplest form of MHE, which discounts prior data completely, is also a convergent estimator, however, as discussed in Exercise 1.28.

The estimator convergence result in Lemma 1.6 is the simplest to establish, but, as in the case of the LQ regulator, we can enlarge the class of systems and weighting matrices (variances) for which estimator convergence is guaranteed. The system restriction can be weakened from observability to detectability, which is discussed in Exercises 1.31 and 1.32. The restriction on the process disturbance weight (variance) Q can be weakened from $Q > 0 \mathrm { t o } Q \geq 0$ and $( A , Q )$ stabilizable, which is discussed in Exercise 1.33. The restriction $R > 0$ remains to ensure uniqueness of the estimator.
