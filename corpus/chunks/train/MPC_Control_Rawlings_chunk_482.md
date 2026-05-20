# 4.5 Unscented Kalman Filtering

The linearization of the nonlinear model at the current state estimate may not accurately represent the dynamics of the nonlinear system behavior even for one sample time. In the EKF prediction step, the mean propagates through the full nonlinear model, but the covariance propagates through the linearization. The resulting error is sufficient to throw off the correction step and the filter can diverge even with a perfect model. The unscented Kalman filter (UKF) avoids this linearization at a single point by sampling the nonlinear response at several points. The points are called sigma points, and their locations and weights are chosen to satisfy the given starting mean and covariance (Julier and Uhlmann, 2004a,b).5 Given $\hat { x }$ and P, choose sample points, $z ^ { i }$ , and weights, $\boldsymbol { w ^ { i } }$ , such that

$$\hat {x} = \sum_ {i} w ^ {i} z ^ {i} \qquad P = \sum_ {i} w ^ {i} (z ^ {i} - \hat {x}) (z ^ {i} - \hat {x}) ^ {\prime}$$

Similarly, given $w \sim N ( 0 , Q )$ and $\nu \sim N ( 0 , R )$ , choose sample points $n ^ { i }$ for w and $m ^ { i }$ for v. Each of the sigma points is propagated forward at each sample time using the nonlinear system model. The locations and weights of the transformed points then update the mean and covariance

$$z ^ {i} (k + 1) = f \left(z ^ {i} (k), n ^ {i} (k)\right)\eta^ {i} = h (z ^ {i}) + m ^ {i} \quad \mathrm{all} i$$

From these we compute the forecast step

$$
\begin{array}{l} \hat {x} ^ {-} = \sum_ {i} w ^ {i} z ^ {i} \quad \hat {y} ^ {-} = \sum_ {i} w ^ {i} \eta^ {i} \\ P ^ {-} = \sum_ {i} w ^ {i} (z ^ {i} - \hat {x} ^ {-}) (z ^ {i} - \hat {x} ^ {-}) ^ {\prime} \\ \end{array}
$$

After measurement, the EKF correction step is applied after first expressing this step in terms of the covariances of the innovation and state prediction. The output error is given as $\tilde { \mathcal { y } } : = \mathcal { y } - \hat { \mathcal { y } }$ −. We next rewrite the Kalman filter update as

$$
\begin{array}{l} \hat {x} = \hat {x} ^ {-} + L (y - \hat {y} ^ {-}) \\ L = \underbrace {\mathcal {E} ((x - \hat {x} ^ {-}) \tilde {\mathcal {Y}} ^ {\prime})} _ {P ^ {-} C ^ {\prime}} \underbrace {\mathcal {E} (\tilde {\mathcal {Y}} \tilde {\mathcal {Y}} ^ {\prime}) ^ {- 1}} _ {(R + C P ^ {-} C ^ {\prime}) ^ {- 1}} \\ P = P ^ {-} - L \underbrace {\mathcal {E} ((x - \hat {x} ^ {-}) \tilde {y} ^ {\prime}) ^ {\prime}} _ {C P ^ {-}} \\ \end{array}
$$

in which we approximate the two expectations with the sigma point samples
