# 9.6.7 Error covariance selection

While one could assume no correlation between the state variables and set the error covariance matrix entries to zero, this may not reflect reality. The Kalman filter is still guaranteed to converge to the steady-state error covariance after a finite time, but it will take longer than otherwise.
