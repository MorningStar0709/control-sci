The control engineer may be tempted to simply add one (or more) integrators to the controller in order to reduce (or eliminate) the steady-state error. However, adding integrators in the forward path adds lag to the closed-loop system, thus slowing down the response. In some cases, adding integrators can cause stability problems.

A final note is in order regarding Table 10.3: the tabulated steady-state errors are for unit input functions r(t) such as the unit step, unit ramp, and unit parabola. Hence, the corresponding Laplace transforms of these unit inputs are $R ( s ) = 1 / s , 1 / s ^ { 2 }$ , and $1 / s ^ { 3 }$ , respectively. Because R(s) has a unity numerator for a unit input function, the steady-state error equation (10.30) shows that the finite errors (the diagonal values in Table 10.3) all have unity numerators. However, if r(t) is a non-unit input, then the numerator of the finite value in Table 10.3 will match the coefficient of the input function. For example, if the input is a ramp function $r ( t ) = 0 . 2 t$ , then steady-state error of a type 1 system is $e ( \infty ) = 0 . 2 / K _ { \mathrm { s v } }$ .

Table 10.3 Steady-State Errors for Closed-Loop Control Systems with Unity Feedback

<table><tr><td>System Type, N</td><td>Unit-Step Input  $r(t) = 1$ </td><td>Unit-Ramp Input  $r(t) = t$ </td><td>Unit-Parabola Input  $r(t) = t^{2}/2$ </td></tr><tr><td>0</td><td> $\frac{1}{1 + K_{\text{sp}}}$ </td><td> $\infty$ </td><td> $\infty$ </td></tr><tr><td>1</td><td>0</td><td> $\frac{1}{K_{\text{sv}}}$ </td><td> $\infty$ </td></tr><tr><td>2</td><td>0</td><td>0</td><td> $\frac{1}{K_{\text{sa}}}$ </td></tr></table>

Static position error constant: $K _ { \mathrm { s p } } = \operatorname* { l i m } _ { s  0 } G ( s )$   
Static velocity error constant: $K _ { \mathrm { s v } } = \operatorname* { l i m } _ { s  0 } s G ( s )$ .   
Static acceleration error constant: $K _ { \mathrm { s a } } = \operatorname* { l i m } _ { s \to 0 } s ^ { 2 } G ( s )$ .
