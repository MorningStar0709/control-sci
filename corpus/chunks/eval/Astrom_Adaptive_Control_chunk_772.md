# Adaptive Control

The adaptive controller was designed as an indirect adaptive pole placement algorithm.

Parameter Estimation. The dynamics can be expected to be of third order, representing the dynamics of the pressure loop and the dynamics of the filter introduced to filter the flow signal. This filter has a time constant of about 30 s. Experiments with system identification indicated, however, that data could be fitted adequately by

$$Q _ {f} (t) = a Q _ {f} (t - h) + b _ {1} p _ {c} (t - h) + b _ {2} p _ {c} (t - 2 h) \tag {12.6}$$

where $Q_{f}$ is the filtration flow and $p_{c}$ is the setpoint of the pressure loop. This model represents first-order dynamics with a time delay. A sampling interval of 5 s was found to be suitable. The parameter estimation was made on differences to avoid problems with a constant level in the signals.

The estimated steady-state gain is an important parameter. With a low estimated gain, the gain in the controller will be large. It is therefore advantageous to have the sum of the b parameters as one of the estimated parameters so that it is easy to set a lower limit to the estimated gain. This has been done in the FCM by using the regression vector

$$
\left( \begin{array}{c c c} Q _ {f} (t) & p _ {c} (t) & p _ {c} (t) - p _ {c} (t - h) \end{array} \right)
$$

instead of

$$
\left( \begin{array}{c c c} Q _ {f} (t) & p _ {c} (t) & p _ {c} (t - h) \end{array} \right)
$$

If the estimated gain becomes too small, the estimate is stopped at the limit.

A constant forgetting factor of 0.999 is used to track slowly time-varying parameters. To improve numerics, only the diagonal elements of the covariance matrix P are divided by this factor. It is well known that the equation for $P(t)$ may be sensitive to numerical precision when a forgetting factor is used. This is because the eigenvalues of the P-matrix may be widely separated. Several methods to handle this problem were described in Chapter 11 and in the discussion of the ABB adaptive controller and Firstloop in this chapter. In this case the problem was avoided by careful scaling, and an ordinary recursive least-squares method could be used.
