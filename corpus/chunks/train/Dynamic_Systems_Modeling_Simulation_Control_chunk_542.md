# Example 10.3

Repeat Examples 10.1 and 10.2 for the case where coil inductance is neglected and compare the results from the simplified model with the full DC motor model from Examples 10.1 and 10.2.

If we set inductance $L = 0$ in the DC motor block diagram (see Fig. 10.5), we see that motor current I changes instantaneously according to Ohm’s law:

$$I = \frac {e _ {\mathrm{in}} (t) - e _ {b}}{R}$$

where $e _ { b }$ is the back emf. Consequently, the forward transfer function becomes

$$G (s) = \frac {K _ {m}}{R (J s + b)}$$

and the closed-loop transfer function is

$$T (s) = \frac {G (s)}{1 + G (s) H (s)} = \frac {\frac {K _ {m}}{R (J s + b)}}{1 + \frac {K _ {m} K _ {b}}{R (J s + b)}}$$

or, simplifying

$$T (s) = \frac {K _ {m}}{R (J s + b) + K _ {m} K _ {b}} \tag {10.7}$$

The reduced-order closed-loop system (10.7) is equivalent to the full (second-order) closed-loop system (10.6) with inductance $L = 0$ . Note that Eq. (10.7) is a first-order system because the RL circuit dynamics have been removed. Using the numerical parameters for the DC motor, the reduced-order closed-loop transfer function is

$$T (s) = \frac {0 . 0 5}{1 . 2 5 (1 0 ^ {- 4}) s + 0 . 0 0 2 5 5} = \frac {4 0 0}{s + 2 0 . 4} \tag {10.8}$$

Note that the DC gain is $4 0 0 / 2 0 . 4 = 1 9 . 6 0 8$ , which matches the DC gain from the second-order closed-loop system where inductance was included. The single time constant for the reduced-order closed-loop system (10.8)

is $\tau = 1 / 2 0 . 4 = 0 . 0 4 9 \mathrm { ~ s ~ }$ , which shows a very close match with the slowest time constant from the second-order model in Example 10.2. Hence, this reduced-order closed-loop DC motor model reaches steady state in the settling time $\begin{array} { r } { 4 \tau = 0 . 1 9 6 \mathrm { ~ s ~ } } \end{array}$ , which is very similar to the second-order model.

As a final note, we see that while inductance L can be neglected without too much loss of accuracy, we cannot neglect the back-emf constant $K _ { b } .$ . Recall that the steady-state angular velocity for an 8-V step source voltage input is $\omega _ { \mathrm { s s } } = 1 5 6 . 8 6 \mathrm { r a d / s }$ . The steady-state back-emf voltage for this speed is $e _ { b } = K _ { b } \omega _ { \mathrm { s s } } = 7 . 8 4 \ : \mathrm { V } ,$ which is nearly as large as the source voltage.
