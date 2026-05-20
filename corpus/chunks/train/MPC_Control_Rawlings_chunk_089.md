# 1.4.3 Least Squares Estimation

We next consider the state estimation problem as a deterministic optimization problem rather than an exercise in maximizing conditional density. This viewpoint proves valuable in Chapter 4 when we wish to add constraints to the state estimator. Consider a time horizon with measurements $y ( k ) , k = 0 , 1 , \dotsc , T$ . We consider the prior information to be our best initial guess of the initial state x(0), denoted $\overline { { x } } ( 0 )$ , and weighting matrices $P ^ { - } ( 0 ) , Q$ , and R for the initial state, process disturbance, and measurement disturbance. A reasonably flexible choice for objective function is

$$
\begin{array}{l} V _ {T} (\mathbf {x} (T)) = \frac {1}{2} \left(| x (0) - \overline {{{{x}}}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \right. \\ \sum_ {k = 0} ^ {T - 1} | x (k + 1) - A x (k) | _ {Q ^ {- 1}} ^ {2} + \sum_ {k = 0} ^ {T} | y (k) - C x (k) | _ {R ^ {- 1}} ^ {2}) \tag {1.27} \\ \end{array}
$$

in which $\mathbf { x } ( T ) : = \{ x ( 0 ) , x ( 1 ) , \ldots , x ( T ) \}$ . We claim and then show that the following (deterministic) least squares optimization problem produces the same result as the conditional density function maximization of the Kalman filter

$$\min _ {\mathbf {x} (T)} V _ {T} (\mathbf {x} (T)) \tag {1.28}$$

Game plan. Using forward DP, we can decompose and solve recursively the least squares state estimation problem. To see clearly how the procedure works, first we write out the terms in the state estimation least squares problem (1.28)

$$
\begin{array}{l} \min _ {x (0), \dots , x (T)} \frac {1}{2} \left(| x (0) - \overline {{x}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + | y (0) - C x (0) | _ {R ^ {- 1}} ^ {2} + | x (1) - A x (0) | _ {Q ^ {- 1}} ^ {2} \right. \\ + \left| y (1) - C x (1) \right| _ {R ^ {- 1}} ^ {2} + | x (2) - A x (1) | _ {Q ^ {- 1}} ^ {2} + \dots + \\ \left. \left| x (T) - A x (T - 1) \right| _ {Q ^ {- 1}} ^ {2} + \left| y (T) - C x (T) \right| _ {R ^ {- 1}} ^ {2}\right) \tag {1.29} \\ \end{array}
$$

We decompose this T -stage optimization problem with forward DP. First we combine the prior and the measurement $y ( 0 )$ into the quadratic function $V _ { 0 } ( x ( 0 ) )$ as shown in the following equation
