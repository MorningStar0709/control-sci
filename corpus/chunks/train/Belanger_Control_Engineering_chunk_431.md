# ◆ ◆ ◆ REMARKS

1. The result is independent of $\mathbf{k}$ , so the observer is optimal for all linear functions of the state, including individual state variables.

2. Since $\mathbf{w}_0$ is not usually given, we normally use expected averages of the terms $w_{0i}^2$ and $w_{0i}w_{0j}$ in $W$ .

3. Similarly, we use an average $v_0^2$ in $V$ . We can also include a vector measurement noise $\mathbf{v}$ , provided that matrix $V$ is positive definite. The dyad $\mathbf{v}_0\mathbf{v}_0^T$ is not, but its average often is. (For example, the average of the product of two independent signals $v_1$ and $v_2$ is zero, so the off-diagonal terms of $V$ can justifiably be made zero.)

4. The properties of the dual LQ solution apply to the observer. For example, A - GC is stable.

A relatively large V tends to make the observer gain small, exactly as a large R makes the state feedback gain small. This happens when the observation noise $\mathbf{v}(t)$ is expected to be large; since the correction term $y - C\widehat{x} = C\widetilde{x} + v$ is heavily noise-contaminated, it is weighted less heavily by the gain G than when v is expected to be generally small. As the observation noise increases, the gain decreases, and the observer “shuts down.”

Conversely, if the plant perturbations are expected to be heavy, a large W is used, making V small by comparison. The observer gain increases to reflect the fact that more updating must be done. As the plant noise increases, the observer "opens up."

This observer actually has its origin in the stochastic setting of the problem and is a special case of the celebrated Kalman filter [6, 7]. In the problem setup for the Kalman filter, the signals $\mathbf{w}(t)$ and $\mathbf{v}(t)$ are white-noise processes, and $W$ and $V$ are their respective covariances. The filter is an observer that minimizes the variance of all components of the estimation error. The general Kalman filter holds for time-varying systems with time-varying noise properties. The Kalman filter is a vital tool not only in control, but also in a great many estimation problems in such diverse fields as navigation, seismic signal processing, and speech processing.
