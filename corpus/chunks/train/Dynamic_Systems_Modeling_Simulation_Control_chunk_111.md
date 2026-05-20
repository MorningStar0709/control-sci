Equation (3.28) is an integro-differential equation as it involves both the derivative and integral of current $I _ { L }$ . We can take the time derivative of Eq. (3.28) to eliminate the integral term (in addition, move the input variable $e _ { \mathrm { i n } } ( t )$ to the right-hand side)

$$L \ddot {I} _ {L} + R \dot {I} _ {L} + \frac {1}{C} I _ {L} = \dot {e} _ {\text { in }} (t) \tag {3.29}$$

Equation (3.29) is the mathematical model of the RLC circuit. It consists of a single linear second-order ODE with dynamic variable $I _ { L }$ and input variable $e _ { \mathrm { i n } } ( t )$ . The reader should note that the single second-order modeling equation (3.29) is equivalent to the two first-order modeling equations (3.25) and (3.26). To show this, we can take the time derivative of Eq. (3.26)

$$L \ddot {I} _ {L} + R \dot {I} _ {L} + \dot {e} _ {C} = \dot {e} _ {\text { in }} (t) \tag {3.30}$$

Next, we substitute Eq. (3.25) for the time derivative of capacitor voltage $( \dot { e } _ { C } = I _ { L } / C )$ to yield

$$L \ddot {I} _ {L} + R \dot {I} _ {L} + \frac {1}{C} I _ {L} = \dot {e} _ {\text { in }} (t) \tag {3.31}$$

which is equivalent to the second-order model (3.29).

In summary, we may use either mathematical model to represent the dynamics of the RLC circuit. If we choose the two first-order equations (3.25) and (3.26), our solution will be in terms of dynamic variables $e _ { C }$ and $I _ { L }$ . If we use the single second-order ODE (3.29), our single dynamic variable is $I _ { L }$ and the input is the time derivative of the source voltage $e _ { \mathrm { i n } } ( t )$ .
