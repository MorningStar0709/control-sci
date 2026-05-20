$$c (t) = 1 - \cos \omega_ {n} t, \quad \text { for } t \geq 0 \tag {5-13}$$

Thus, from Equation (5–13), we see that $\omega _ { n }$ represents the undamped natural frequency of the system. That is, $\omega _ { n }$ is that frequency at which the system output would oscillate if the damping were decreased to zero. If the linear system has any amount of damping, the undamped natural frequency cannot be observed experimentally. The frequency that may be observed is the damped natural frequency $\omega _ { d }$ , which is equal to $\omega _ { n } \bigvee 1 - \zeta ^ { 2 }$ . This frequency is always lower than the undamped natural frequency. An increase in $\zeta$ would reduce the damped natural frequency $\omega _ { d }$ . If $\zeta$ is increased beyond unity, the response becomes overdamped and will not oscillate.

(2) Critically damped case $( \zeta = 1 )$ : If the two poles of $C ( s ) / R ( s )$ are equal, the system is said to be a critically damped one.

For a unit-step input, $R ( s ) = 1 / s$ and $C ( s )$ can be written

$$C (s) = \frac {\omega_ {n} ^ {2}}{(s + \omega_ {n}) ^ {2} s} \tag {5-14}$$

The inverse Laplace transform of Equation (5–14) may be found as

$$c (t) = 1 - e ^ {- \omega_ {n} t} \left(1 + \omega_ {n} t\right), \quad \text { for } t \geq 0 \tag {5-15}$$

This result can also be obtained by letting $\zeta$ approach unity in Equation (5–12) and by using the following limit:

$$\lim _ {\zeta \rightarrow 1} \frac {\sin \omega_ {d} t}{\sqrt {1 - \zeta^ {2}}} = \lim _ {\zeta \rightarrow 1} \frac {\sin \omega_ {n} \sqrt {1 - \zeta^ {2}} t}{\sqrt {1 - \zeta^ {2}}} = \omega_ {n} t$$

(3) Overdamped case $( \zeta > 1 )$ : In this case, the two poles of $C ( s ) / R ( s )$ are negative real and unequal. For a unit-step input, $R ( s ) = 1 / s$ and $C ( s )$ can be written

$$C (s) = \frac {\omega_ {n} ^ {2}}{(s + \zeta \omega_ {n} + \omega_ {n} \sqrt {\zeta^ {2} - 1}) (s + \zeta \omega_ {n} - \omega_ {n} \sqrt {\zeta^ {2} - 1}) s} \tag {5-16}$$

The inverse Laplace transform of Equation (5–16) is

$$
\begin{array}{l} c (t) = 1 + \frac {1}{2 \sqrt {\zeta^ {2} - 1} (\zeta + \sqrt {\zeta^ {2} - 1})} e ^ {- (\zeta + \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} \\ - \frac {1}{2 \sqrt {\zeta^ {2} - 1} (\zeta - \sqrt {\zeta^ {2} - 1})} e ^ {- (\zeta - \sqrt {\zeta^ {2} - 1}) \omega_ {n} t} \\ = 1 + \frac {\omega_ {n}}{2 \sqrt {\zeta^ {2} - 1}} \left(\frac {e ^ {- s _ {1} t}}{s _ {1}} - \frac {e ^ {- s _ {2} t}}{s _ {2}}\right), \quad \text { for } t \geq 0 \tag {5-17} \\ \end{array}
$$
