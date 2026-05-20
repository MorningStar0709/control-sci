# 9.6.8 Process noise and measurement noise covariance selection

Recall that the process noise covariance is Q and the measurement noise covariance is R. To tune the elements of these, it can be helpful to take a collection of measurements, then run the Kalman filter on them offline to evaluate its performance.

The diagonal elements of R are the variances of each measurement, which can be easily determined from the offline measurements. The diagonal elements of Q are the variances of each state. They represent how much each state is expected to deviate from the model.

Selecting Q is more difficult. If the data is trusted too much over the model, one risks overfitting the data. One should balance estimating any hidden states sufficiently with actually filtering out the noise.
