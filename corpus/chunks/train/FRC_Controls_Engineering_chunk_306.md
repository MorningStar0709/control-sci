# 9.6.2 Predict and update equations

Now that we’ve derived all the pieces we need, we can finally write all the equations for a Kalman filter. Theorem 9.6.3 shows the predict and update steps for a Kalman filter at the $k ^ { t h }$ timestep.

Intuitively, the predict step projects the error covariance forward in an increasing parabolic shape because you become less certain in your state estimate as you go longer since a measurement. In your state-space (think like 3D space but each state is an axis), the error ellipsoid grows over time.

The correct step decreases the error covariance again by injecting new information. The input has no effect on this because it has no noise associated with it. In fact, input cancels out in the Kalman filter expectation and covariance update equation derivations.

A Kalman filter chooses the Kalman gain ${ \bf K } _ { k + 1 }$ in the correct equation $\hat { \mathbf { x } } _ { k + 1 } ^ { + } = \hat { \mathbf { x } } _ { k + 1 } ^ { - } +$ $\mathbf { K } _ { k + 1 } \big ( \mathbf { y } _ { k + 1 } - \hat { \mathbf { y } } _ { k + 1 } \big )$ such that the eigenvalues of P are minimized. This minimizes the error variances and thus the dimensions of the uncertainty ellipsoid over time.

If the update period is constant, the predict and correct steps are run in a loop as opposed to sporadically skipping correct steps, and the (A, C) pair is detectable, the error covariance matrix P will approach a steady-state. This steady-state P results in a steady-state Kalman gain that can be used instead of the error covariance update equations to conserve computational resources.
