# 9.8 Extended Kalman filter

In this book, we have covered the Kalman filter, which is the optimal unbiased estimator for linear systems. One method for extending it to nonlinear systems is the extended Kalman filter.

The extended Kalman filter (EKF) linearizes the dynamical and measurement models during the prediction and correction steps respectively. Then, the linear Kalman filter equations are used to compute the error covariance matrix P and Kalman gain matrix K.

Theorem 9.8.1 shows the predict and update steps for an extended Kalman filter at the $k ^ { t h }$ timestep.
