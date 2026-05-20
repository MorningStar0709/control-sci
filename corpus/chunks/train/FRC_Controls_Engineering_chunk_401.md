# 14.2 1-DOF mechanism state-space model

$$\dot {x} = \alpha x + \beta u + \gamma \operatorname{sgn} (x)\dot {x} = \text { acceleration } \quad x = \text { velocity } \quad u = \text { voltage }$$

We can determine $\alpha , \beta ,$ , and $\gamma$ by applying ordinary least squares (OLS) to vectors of recorded input voltage, velocity, and acceleration data from quasistatic velocity tests and acceleration tests, where acceleration is the dependent variable. If acceleration isn’t directly available, it can be computed numerically from the velocity data and filtered.

Solving this model for u gives the following feedforward model.

$$u = - \frac {\gamma}{\beta} \operatorname{sgn} (x) - \frac {\alpha}{\beta} x + \frac {1}{\beta} \dot {x}$$

Let $\begin{array} { r } { K _ { s } = - \frac { \gamma } { \beta } , K _ { v } = - \frac { \alpha } { \beta } } \end{array}$ , and $\begin{array} { r } { K _ { a } = \frac { 1 } { \beta } } \end{array}$

$$u = K _ {s} \operatorname{sgn} (x) + K _ {v} x + K _ {a} \dot {x} \tag {14.2}$$

$K _ { s }$ is a constant that describes how much voltage is required to overcome friction and start moving.

$K _ { v }$ is a proportional constant that describes how much voltage is required to maintain a given constant velocity by offsetting the electromagnetic resistance of the motor and any friction that increases linearly with speed (viscous drag). The relationship between speed and voltage (for a given initial acceleration) is linear for permanent-magnet DC motors in the FRC operating regime.

$K _ { a }$ is a proportional constant that describes how much voltage is required to induce a given acceleration in the motor shaft. As with $K _ { v } .$ , the relationship between voltage and acceleration (for a given initial velocity) is linear.

Convert equation (14.2) to state-space form by solving for ${ \dot { x } } .$

$$\dot {x} = - \frac {K _ {v}}{K _ {a}} x + \frac {1}{K _ {a}} u - \frac {K _ {s}}{K _ {a}} \mathrm{sgn} (x)$$

By inspection, $\begin{array} { r } { { \bf A } = - \frac { K _ { v } } { K _ { a } } , { \bf B } = \frac { 1 } { K _ { a } } } \end{array}$ K , and $\begin{array} { r } { \mathbf { c } = - \frac { K _ { s } } { K _ { a } } \mathrm { s g n } ( \mathbf { x } ) } \end{array}$ K in the state-space model $\dot { \mathbf { x } } = \mathbf { A } \mathbf { x } + \mathbf { B } \mathbf { u } + \mathbf { c }$ a a a. A model with position and velocity states would be

Theorem 14.2.1 — 1-DOF mechanism position model.
