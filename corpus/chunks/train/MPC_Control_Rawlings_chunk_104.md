Assumption 1.7 (a) ensures that the solution $( x _ { s } , u _ { s } )$ exists, and Assumption 1.7 (b) ensures that the solution is unique. If one chooses $n _ { c } = 0$ , then no controlled variables are required to be at setpoint, and the problem is feasible for any $( u _ { \mathrm { s p } } , y _ { \mathrm { s p } } )$ because $( x _ { s } , u _ { s } ) = ( 0 , 0 )$ is a feasible point. Exercises 1.56 and 1.57 explore the connection between feasibility of the equality constraints and the number of controlled variables relative to the number of inputs and outputs. One restriction is that the number of controlled variables chosen to be offset free must be less than or equal to the number of manipulated variables and the number of measurements, $n _ { c } \le m$ and $n _ { c } \le p$ .

Dynamic regulation problem. Given the steady-state solution, we define the following multistage objective function

$$V (\widetilde {x} (0), \widetilde {\mathbf {u}}) = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} | \widetilde {x} (k) | _ {Q} ^ {2} + | \widetilde {u} (k) | _ {R} ^ {2} \quad \text { s.t. } \widetilde {x} ^ {+} = A \widetilde {x} + B \widetilde {u}$$

in which $\smash { \widetilde { x } ( 0 ) = \hat { x } ( k ) - x _ { s } }$ , i.e., the initial condition for the regulation problem comes from the state estimate shifted by the steady-state $x _ { s }$ . The regulator solves the following dynamic, zero-state regulation problem

$$\min _ {\tilde {\mathbf {u}}} V (\tilde {x} (0), \tilde {\mathbf {u}})$$

subject to

$$E \tilde {u} \leq e - E u _ {s}F C \tilde {x} \leq f - F C x _ {s}$$

in which the constraints also are shifted by the steady state $( x _ { s } , u _ { s } )$ . The optimal cost and solution are $V ^ { 0 } ( \tilde { x } ( 0 ) )$ and $\tilde { \mathbf { u } } ^ { 0 } ( \tilde { \boldsymbol { x } } ( 0 ) )$ . The move e eing horizon control law uses the first move of this optimal sequence, $\tilde { \boldsymbol { u } } ^ { 0 } ( \tilde { \boldsymbol { x } } ( 0 ) ) = \tilde { \boldsymbol { \mathbf { u } } } ^ { 0 } ( 0 ; \tilde { \boldsymbol { x } } ( 0 ) )$ , so the controller output is $u ( k ) = \widetilde { u } ^ { 0 } ( \widetilde { x } ( 0 ) ) +$ $u _ { s }$ .
