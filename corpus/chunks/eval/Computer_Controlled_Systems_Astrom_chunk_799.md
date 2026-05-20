# Time-Varying Systems

Using the loss function of $(13.3)$ , all data points are given the same weight. If the parameters are time-varying, it is necessary to eliminate the influence of old data. This can be done by using a loss function with exponential weighting, that is,

$$J (\theta) = \sum_ {k = 1} ^ {N} \lambda^ {N - k} (y (k) - \varphi^ {T} (k) \theta) ^ {2} \tag {13.14}$$

The forgetting factor, $\lambda$ , is less than one and is a measure of how fast old data are forgotten. The least-squares estimate when using the loss function of (13.14) is given by

$$\hat {\theta} (k + 1) = \hat {\theta} (k) + K (k) \left(y _ {k + 1} - \varphi^ {T} (k + 1) \hat {\theta} (k)\right)K (k) = P (k) \varphi (k + 1) \left(\lambda + \varphi^ {T} (k + 1) P (k) \varphi (k + 1)\right) ^ {- 1} \tag {13.15}P (k + 1) = \left(I - K (k) \varphi^ {T} (k + 1)\right) P (k) / \lambda$$

It is also possible to model the time-varying parameters by a Markov process,

$$\theta (k + 1) = \Phi \theta (k) + v (k)$$

and then use a Kalman filter to estimate $\theta$ . See Remark 2 of Theorem 13.3.
