The diagonal elements of $P ( t )$ are the mean-square values of the state variables, while the off-diagonal elements represent the amount of correlation between the different state variables. Equation (4.104) provides a direct method for analyzing the statistical properties of ${ \bf x } ( t )$ . This is to be contrasted with the Monte Carlo method, where many sample trajectories of ${ \bf x } ( t )$ are calculated from computer-generated random noise, or random numbers in the case of a digital computer. In using the latter technique, m such trajectories are generated using (4.100), each denoted by ${ \bf x } _ { k } ( t )$ , $k = 1 , 2 , \ldots , m$ . Consequently, $P ( t )$ can be approximated by the expression

$$P (t) \cong \hat {P} (t) \triangleq (1 / m) \sum_ {k = 1} ^ {m} \mathbf {x} _ {k} (t) \mathbf {x} _ {k} ^ {T} (t). \tag {4.105}$$

Note that in the limit, as $m \to \infty$ , we have

$$\lim _ {m \to \infty} \hat {P} (t) = P (t). \tag {4.106}$$

Kalman and Bucy showed that the optimal filter (which is independent of the weightings given to each of the error components) is a linear dynamic system described by

$$\frac {d \hat {\mathbf {x}} (t)}{d t} = [ F (t) - R (t) H (t) ] \hat {\mathbf {x}} (t) + R (t) \mathbf {z} (t), \tag {4.107}$$

where $\hat { \mathbf { x } } ( t )$ is the best linear estimate of $\mathbf { x } ( t )$ . In other words, the form of the optimal filter is specified by the form of the message process. The time-varying gain matrix (also known as Kalman gain matrix) $K ( t )$ is of the form

$$K (t) = P (t) H ^ {T} (t) R ^ {- 1} (t). \tag {4.108}$$

By way of illustrating the error covariance matrix $P ( t )$ , let $y _ { M }$ be the missile displacement and $y _ { T }$ the target displacement. In particular, let $\hat { { \bf x } } _ { 1 } ( t )$ be the best linear estimate of the target displacement, $\hat { \mathbf { x } } _ { 2 } ( t )$ be the best linear estimate of the target velocity, and $\hat { \mathbf { x } } _ { 3 } ( t )$ the best linear estimate of target acceleration. The filter state variables can be formulated as follows:

$$\hat {\mathbf {x}} _ {1} (t) = \text { best linear estimate of } y _ {T} (t),\hat {\mathbf {x}} _ {2} (t) = \text { best linear estimate of } v _ {T} (t),\hat {\mathbf {x}} _ {3} (t) = \text { best linear estimate of } a _ {T} (t).$$

For the error in the estimate, that is, $\widetilde { \mathbf { x } } ( t ) = \mathbf { x } ( t ) - \hat { \mathbf { x } } ( t )$ , the error covariance matrix takes the form
