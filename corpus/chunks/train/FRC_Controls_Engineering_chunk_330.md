# 9.10 Multiple model adaptive estimation

Multiple model adaptive estimation (MMAE) runs multiple Kalman filters with different models on the same data. The Kalman filter with the lowest residual has the highest likelihood of accurately reflecting reality. This can be used to detect certain system states like an aircraft engine failing without needing to invest in costly sensors to determine this directly.

For example, say you have three Kalman filters: one for turning left, one for turning right, and one for going straight. If the control input is attempting to fly the plane straight and the Kalman filter for going left has the lowest residual, the aircraft’s left engine probably failed.

See Roger Labbe’s book Kalman and Bayesian Filters in Python for more on MMAE.[14]
