# 9.9 Unscented Kalman filter

In this book, we have covered the Kalman filter, which is the optimal unbiased estimator for linear systems. One method for extending it to nonlinear systems is the unscented Kalman filter.

The unscented Kalman filter (UKF) propagates carefully chosen points called sigma points through the nonlinear state and measurement models to obtain estimates of the true covariances (as opposed to linearized versions of them). Read Kalman and Bayesian Filters in Python by Roger Labbe[7] or the original paper[8] for more on UKFs.

Here’s an interview about the origin of the UKF with its creator.[9]
