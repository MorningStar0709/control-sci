# 1.4.2 Optimal Control Theory

The linear quadratic control problem has its origins in the celebrated work of N. Wiener on mean-square filtering for weapon fire control during World War II (1940-45) [144, 145]. Wiener solved the problem of designing filters that minimize a mean-square-error criterion (performance measure) of the form

$$J = E \{e ^ {2} (t) \} \tag {1.4.1}$$

where, $e(t)$ is the error, and $E\{x\}$ represents the expected value of the random variable x. For a deterministic case, the above error criterion is generalized as an integral quadratic term as

$$J = \int_ {0} ^ {\infty} \mathbf {e} ^ {\prime} (t) \mathbf {Q e} (t) d t \tag {1.4.2}$$

where, Q is some positive definite matrix. R. Bellman in 1957 [12] introduced the technique of dynamic programming to solve discrete-time optimal control problems. But, the most important contribution to optimal control systems was made in 1956 [25] by L. S. Pontryagin (formerly of the United Soviet Socialistic Republic (USSR)) and his associates, in development of his celebrated maximum principle described in detail in their book [109]. Also, see a very interesting article on the “discovery of the Maximum Principle” by R. V. Gamkrelidze [52], one of the authors of the original book [109]. At this time in the United States, R. E. Kalman in 1960 [70] provided linear quadratic regulator (LQR) and linear quadratic Gaussian (LQG) theory to design optimal feedback controls. He went on to present optimal filtering and estimation theory leading to his famous discrete Kalman filter [71] and the continuous Kalman filter with Bucy [76]. Kalman had a profound effect on optimal control theory and the Kalman filter is one of the most widely used technique in applications of control theory to real world problems in a variety of fields.

At this point we have to mention the matrix Riccati equation that appears in all the Kalman filtering techniques and many other fields. C. J. Riccati [114, 22] published his result in 1724 on the solution for some types of nonlinear differential equations, without ever knowing that the Riccati equation would become so famous after more than two centuries!
