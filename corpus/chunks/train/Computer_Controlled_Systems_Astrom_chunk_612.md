$$
x (k - n + 1) = W _ {o} ^ {- 1} \left( \begin{array}{l l l} y (k - n + 1) & \dots & y (k) \end{array} \right) ^ {T} \tag {10.2}
$$

where $W_{o}$ is the observability matrix given by Eq. (3.22). The following predictor gives the state m steps ahead:

$$
\hat {x} (k + m \mid k) = \Phi^ {m + n - 1} W _ {o} ^ {- 1} \left( \begin{array}{l l l} y (k - n + 1) & \dots & y (k) \end{array} \right) ^ {T} \tag {10.3}
$$

The predictor for the signal is thus obtained from a linear combination of n values of the measured signal. The predictor can be expressed as

$$\hat {y} (k + m \mid k) = P ^ {*} (q ^ {- 1}) y (k)$$

where P is a polynomial of degree n - 1.

The predictor can also be represented by the recursive equation

$$
\begin{array}{l} \hat {x} (k \mid k) = \Phi \hat {x} (k - 1 \mid k - 1) + K \left(y (k) - C \Phi \hat {x} (k - 1 \mid k - 1)\right) \\ \hat {x} (k + m \mid k) = \Phi^ {m} \hat {x} (k \mid k) \\ \end{array}
$$

where the matrix K is chosen so that all eigenvalues of the matrix $(I - KC)\Phi$ are equal to zero.

Simple calculations for an integrator and a double integrator give the same predictors as in Examples 10.1 and 10.2. This is a consequence of the fact that the important characteristics of the disturbances are captured by the dynamics of the systems that generate the disturbances. These dynamics determine the predictors uniquely; it does not matter if the systems are driven by a single pulse or by several pulses. The properties of the predictors are illustrated in Fig. 10.2.
