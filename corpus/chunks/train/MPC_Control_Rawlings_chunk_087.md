$$
\left[ \begin{array}{c} x (0) \\ w (0) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \hat {x} (0) \\ 0 \end{array} \right], \left[ \begin{array}{c c} P (0) & 0 \\ 0 & Q \end{array} \right]\right)
$$

We then use the conditional version of the linear transformation of a normal (1.25) to obtain

$$p _ {x (1) \mid y (0)} (x (1) \mid y (0)) = n (x (1), \hat {x} ^ {-} (1), P ^ {-} (1))$$

in which the mean and variance are

$$\hat {x} ^ {-} (1) = A \hat {x} (0) \quad P ^ {-} (1) = A P (0) A ^ {\prime} + Q$$

We see that forecasting forward one time step may increase or decrease the conditional variance of the state. If the eigenvalues of A are less than unity, for example, the term $A P ( 0 ) A ^ { \prime }$ may be smaller than $P ( 0 )$ , but the process noise Q adds a positive contribution. If the system is unstable, $A P ( 0 ) A ^ { \prime }$ may be larger than $P ( 0 )$ , and then the conditional variance definitely increases upon forecasting. See also Exercise 1.27 for further discussion of this point.

Given that $p _ { x ( 1 ) | y ( 0 ) }$ is also a normal, we are situated to add measurement $y ( 1 )$ and continue the process of adding measurements followed by forecasting forward one time step until we have processed all the available data. Because this process is recursive, the storage requirements are small. We need to store only the current state estimate and variance, and can discard the measurements as they are processed. The required online calculation is minor. These features make the optimal linear estimator an ideal candidate for rapid online application. We next summarize the state estimation recursion.

Summary. Denote the measurement trajectory by

$$\mathbf {y} (k) := \left\{\mathcal {Y} (0), \mathcal {Y} (1), \dots \mathcal {Y} (k) \right\}$$

At time k the conditional density with data $\mathbf { y } ( k - 1 )$ is normal

$$p _ {x (k) | \mathbf {y} (k - 1)} (x (k) | \mathbf {y} (k - 1)) = n (x (k), \hat {x} ^ {-} (k), P ^ {-} (k))$$

and we denote the mean and variance with a superscript minus to indicate these are the statistics before measurement $y ( k )$ . $\mathrm { A t } \ k = 0$ , the recursion starts with $\hat { x } ^ { - } ( 0 ) = \overline { { x } } ( 0 )$ and $P ^ { - } ( 0 ) = Q ( 0 )$ as discussed previously. We obtain measurement $y ( k )$ which satisfies

$$
\left[ \begin{array}{c} x (k) \\ y (k) \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ C & I \end{array} \right] \left[ \begin{array}{c} x (k) \\ v (k) \end{array} \right]
$$
