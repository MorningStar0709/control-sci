# (a) Continuous-Time Kalman Filtering

We begin with a brief discussion of filtering theory as applied to the design of optimal homing missile guidance systems. In particular, we will develop the covariance equations that are used in the design of these homing guidance systems. The principal advantage of the covariance technique is that it circumvents Monte Carlo simulations, thereby achieving substantial savings in computer running time. Furthermore, this application of filtering theory yields a simple method for determining the smallest possible rms miss distance that can be obtained with the “optimal missile” for an arbitrary specification of noise and target statistics, and parameters such as nominal closing velocity, initial range, and initial errors at the launch time of the missile. Knowledge of the best theoretically possible performance is always important in determining whether further improvement can be obtained in a guidance system that has been designed via another, perhaps trial and error, design method. It also helps in estimating the performance shortfall (with respect to ideal) while using a heuristic and/or suboptimal scheme.

Consider now the dynamics of a stable, nth-order, time-invariant, linear, continuous stochastic system that can be represented by a first-order vector–matrix differential equation of the form [25]

$$\frac {d \mathbf {x} (t)}{d t} = F (t) \mathbf {x} (t) + G (t) \mathbf {u} (t), \tag {4.100}$$

where

$$\mathbf {x} (t) = \text { state vector of dimension } n \times 1,F (t) = \text { a matrix that describes the system dynamics }(n \times n),G (t) = \text { noise gain matrix } (n \times r),\mathbf {u} (t) = \text { zero - mean white Gaussian noise } (r \times 1).$$

The continuous available measurements are modeled by a process defined by

$$\mathbf {z} (t) = H (t) \mathbf {x} (t) + \mathbf {v} (t), \tag {4.101}$$

where

$$\mathbf {z} (t) = \text { measurement (or observation) vector } (m \times 1),H (t) = \text { observation matrix } (m \times n),\mathbf {v} (t) = \text { zero - mean white Gaussian noise } (m \times 1).$$

The system prior statistics can be represented by
