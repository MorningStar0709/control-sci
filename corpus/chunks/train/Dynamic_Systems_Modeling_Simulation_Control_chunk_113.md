$$I _ {C} = I _ {\mathrm{in}} (t) - \frac {e _ {C}}{R} - I _ {L} \tag {3.38}$$

In addition, we can substitute for inductor voltage $( e _ { L } = e _ { C } )$ in Eq. (3.33). Substituting Eq. (3.38) for $I _ { C }$ in Eq. (3.32) and capacitor voltage for $e _ { L }$ in Eq. (3.33) yields

$$C \dot {e} _ {C} + \frac {1}{R} e _ {C} + I _ {L} = I _ {\text { in }} (t) \tag {3.39}L \dot {I} _ {L} - e _ {C} = 0 \tag {3.40}$$

Equations (3.39) and (3.40) are the mathematical modeling equations for the parallel RLC circuit. The complete system is linear and second order as it consists of two first-order, linear, coupled ODEs.

We can express the electrical model as a single second-order ODE in terms of capacitor voltage $e _ { C }$ by taking a time derivative of Eq. (3.39)

$$C \ddot {e} _ {C} + \frac {1}{R} \dot {e} _ {C} + \dot {I} _ {L} = \dot {I} _ {\text { in }} (t) \tag {3.41}$$

Next, solve Eq. (3.40) for the time-rate of inductor current, $\dot { I } _ { L } = e _ { C } / L$ , and substitute this result into Eq. (3.41) to yield

$$C \ddot {e} _ {C} + \frac {1}{R} \dot {e} _ {C} + \frac {1}{L} e _ {C} = \dot {I} _ {\text { in }} (t) \tag {3.42}$$

Equation (3.42) is the mathematical model of the parallel RLC circuit, and it is equivalent to the model represented by the two, coupled first-order equations (3.39) and (3.40).
