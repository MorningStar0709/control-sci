# 2.2 LEAST SQUARES AND REGRESSION MODELS

Karl Friedrich Gauss formulated the principle of least squares at the end of the eighteenth century and used it to determine the orbits of planets and asteroids. Gauss stated that, according to this principle, the unknown parameters of a mathematical model should be chosen in such a way that

the sum of the squares of the differences between the actually observed and the computed values, multiplied by numbers that measure the degree of precision, is a minimum.

The least-squares method can be applied to a large variety of problems. It is particularly simple for a mathematical model that can be written in the form

$$y (i) = \varphi_ {1} (i) \theta_ {1} ^ {0} + \varphi_ {2} (i) \theta_ {2} ^ {0} + \dots - \varphi_ {n} (i) \theta_ {n} ^ {0} = \varphi^ {T} (i) \theta^ {0} \tag {2.1}$$

where $y$ is the observed variable, $\theta_1^0, \theta_2^0, \ldots, \theta_n^0$ are parameters of the model to be determined, and $\varphi_1, \varphi_2, \ldots, \varphi_n$ are known functions that may depend on other known variables. The vectors

$$
\varphi^ {T} (i) = \left( \begin{array}{c c c c} \varphi_ {1} (i) & \varphi_ {2} (i) & \dots & \varphi_ {n} (i) \end{array} \right)

\boldsymbol {\theta} ^ {0} = \left( \begin{array}{c c c c} \theta_ {1} ^ {0} & \theta_ {2} ^ {0} & \dots & \theta_ {n} ^ {0} \end{array} \right) ^ {T}
$$

have also been introduced. The model is indexed by the variable i, which often denotes time. It will be assumed initially that the index set is a discrete set. The variables $\varphi_{i}$ are called the regression variables or the regressors, and the model in Eq. (2.1) is also called a regression model. Pairs of observations and regressors $\{(y(i),\varphi(i)),i=1,2,\ldots,t\}$ are obtained from an experiment. The problem is to determine the parameters in such a way that the outputs computed from the model in Eq. (2.1) agree as closely as possible with the measured variables $y(i)$ in the sense of least squares. That is, the parameter $\theta$ should be chosen to minimize the least-squares loss function

$$V (\theta , t) = \frac {1}{2} \sum_ {i = 1} ^ {t} (y (i) - \varphi^ {T} (i) \theta) ^ {2} \tag {2.2}$$

Since the measured variable y is linear in parameters $\theta^{0}$ and the least-squares criterion is quadratic, the problem admits an analytical solution. Introduce the notations

$$
Y (t) = \left( \begin{array}{c c c c} y (1) & y (2) & \dots & y (t) \end{array} \right) ^ {T}
