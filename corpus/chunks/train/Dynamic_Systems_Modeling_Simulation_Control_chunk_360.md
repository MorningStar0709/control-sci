# Step Response of a First-Order System

Next, we consider the response of a first-order system with a constant or step input with magnitude A; that is, $u ( t ) = A U ( t )$ . Therefore, our general first-order model Eq. (7.25) becomes

$$\tau \dot {y} + y = b A \tag {7.30}$$

The total response to the step input (that is, the step response) is

$$y (t) = y _ {H} (t) + y _ {P} (t) \tag {7.31}$$

where the homogeneous solution was found to be $y _ { H } ( t ) = c e ^ { - t / \tau }$ . The particular solution $y _ { P } ( t )$ must satisfy Eq. (7.30) with constant input $b A .$ , and we see that $y _ { P } ( t ) = b A$ is the solution. The step response Eq. (7.31) is rewritten as

$$y (t) = c e ^ {- t / \tau} + b A \tag {7.32}$$

Because the homogeneous solution $c e ^ { - t / \tau }$ goes to zero as $t \to \infty$ , the steady-state response is $y ( \infty ) = y _ { \mathrm { s s } } = b A$ , which depends on the coefficient b and the magnitude of the step input A. Finally, we solve for the coefficient c by applying the initial condition $y ( 0 ) = y _ { 0 }$ to Eq. (7.32), which yields

$$y (0) = c e ^ {0} + y _ {\mathrm{ss}} = y _ {0} \tag {7.33}$$

and hence $c = y _ { 0 } - y _ { \mathrm { s s } }$ . The step response is

$$y (t) = \left(y _ {0} - y _ {\mathrm{ss}}\right) e ^ {- t / \tau} + y _ {\mathrm{ss}} \tag {7.34}$$

We see that the first term of the step response is the transient response as it dies out over time, and that the second term is the steady-state response because it remains as $t \to \infty$ . We define $t _ { S }$ as the settling time, or the time it takes to reach steady state, and we can estimate settling time for a first-order system as four time constants, or $t _ { S } = 4 \tau$ .

In many instances, we may simply wish to sketch the step response of a first-order system. The following steps will lead to an accurate step-response sketch:

1. Rewrite the first-order model in the “standard form” of Eq. (7.25) and compute the time constant, ??.   
2. Estimate the settling time as four time constants, that is, $t _ { S } = 4 \tau$ .   
3. Compute the steady-state response for the step input $u ( t ) = A U ( t )$ , that is, $y _ { \mathrm { s s } } = b A$ .   
4. Sketch an exponential response from the known initial condition $y _ { 0 }$ to the steady-state value $y _ { \mathrm { s s } }$ . The response approximately reaches $y _ { \mathrm { s s } }$ at $t = t _ { S }$ . The total response will “decay down” to steady state if $y _ { 0 } > y _ { \mathrm { s s } }$ , or show an “exponential rise” to steady state if $y _ { \mathrm { s s } } > y _ { 0 }$ .
