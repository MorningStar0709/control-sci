$$K (k) \left(R _ {2} + C P (k) C ^ {T}\right) = \Phi P (k) C ^ {T} + R _ {1 2}$$

for any $\alpha$ . If $CP(k)C^T + R_2$ is positive definite then

$$K (k) = \left(\Phi P (k) C ^ {T} + R _ {1 2}\right) \left(R _ {2} + C P (k) C ^ {T}\right) ^ {- 1} \tag {11.46}$$

This inserted into (11.45) or using (11.15) gives

$$
\begin{array}{l} \boldsymbol {P} (\boldsymbol {k} + \mathbf {1}) = \Phi \boldsymbol {P} (\boldsymbol {k}) \boldsymbol {\Phi} ^ {T} + R _ {1} \\ - \left(\Phi P (k) C ^ {T} + R _ {1 2}\right) \left(R _ {2} + C P (k) C ^ {T}\right) ^ {- 1} \left(C P (k) \Phi^ {T} + R _ {1 2} ^ {T}\right) \tag {11.47} \\ \end{array}
P (0) = R _ {0}
$$

The reconstruction defined by (11.43), (11.46), and (11.47) is called the Kalman filter. This is summarized in the following theorem.

THEOREM 11.5 THE KALMAN FILTER—PREDICTOR CASE Consider the process of (11.3). The reconstruction of the states using the model in (11.43) is optimal in the sense that the variance of the reconstruction error is minimized if the matrix $R_2 + CP(k)C^T$ is positive definite and if the gain matrix is chosen according to (11.46) and (11.47). The variance of the reconstructing error is given by (11.47).

Remark 1. The reconstruction problem has been solved as a parametric optimization problem by assuming the structure in (11.43) of the estimator. It is in fact true that the structure is optimal for Gaussian disturbances.

Remark 2. Better than the traditional notation for the variance $P(k)$ is $P(k \mid k - 1)$ . The latter notation indicates that measurements up to and including time $k - 1$ are used. The different terms in the variance equation of (11.47) can be interpreted in the following way: The term $\Phi P\Phi^T$ shows how the variance is changed due to the system dynamics, and $R_1$ represents the increase in the variance due to the noise $v$ [compare with (10.11)]. The last term shows how the variance is decreased due to the information obtained through the measurements. Notice that $P(k)$ does not depend on the observations. Thus the gain can be precomputed in forward time and stored in the computer.

Remark 3. The Kalman filter can also be interpreted as the conditional mean of the state at time $k + 1$ given $Y_{k}$ ; that is,

$$
\begin{array}{l} \hat {x} (k + 1 \mid k) = \mathrm{E} (x (k + 1) \mid Y _ {k}) \\ P (k + 1) = \mathrm{E} \left[ (x (k + 1) - \hat {x} (k + 1 | k)) (x (k + 1) - \hat {x} (k + 1 | k)) ^ {T} \mid Y _ {k} \right] \\ \end{array}
$$
