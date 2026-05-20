# Exercise 1.6: Continuous to discrete time conversion for nonlinear models

Consider the autonomous nonlinear differential equation model

$$\frac {d x}{d t} = f (x, u)x (0) = x _ {0} \tag {1.52}$$

Given a zero-order hold on the input, let ${ } s ( t , u , x _ { 0 } ) , 0 \leq t \leq \Delta$ , be the solution to (1.52) given initial condition $x _ { 0 }$ at time $t = 0$ , and constant input u is applied for t in the interval $0 \leq t \leq \Delta$ . Consider also the nonlinear discrete time model

$$x (k + 1) = F (x (k), u (k))$$

(a) What is the relationship between F and s so that the solution of the discrete time model agrees at the sample times with the continuous time model with a zero-order hold?

(b) Assume $f$ is linear and apply this result to check the result of Exercise 1.5.
