# Exercise 1.42: Least squares parameter estimation and Bayesian estimation

Consider a model linear in the parameters

$$y = X \theta + e \tag {1.65}$$

in which $\ b { y } \in \mathbb { R } ^ { p }$ is a vector of measurements, $\theta \in \mathbb { R } ^ { m }$ is a vector of parameters, $X \in \mathbb { R } ^ { p \times m }$ is a matrix of known constants, and $e \in \mathbb { R } ^ { p }$ is a random variable modeling the measurement error. The standard parameter estimation problem is to find the best estimate of $\theta$ given the measurements $_ y$ corrupted with measurement error e, which we assume is distributed as

$$e \sim N (0, R)$$

(a) Consider the case in which the errors in the measurements are independently and identically distributed with variance $\sigma ^ { 2 } , R = \sigma ^ { 2 } I$ . For this case, the classic least squares problem and solution are

$$\min _ {\theta} \left| y - X \theta \right| ^ {2} \qquad \hat {\theta} = \left(X ^ {\prime} X\right) ^ {- 1} X ^ {\prime} y$$
