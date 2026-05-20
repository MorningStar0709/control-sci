If we designate the DC motor dynamics as the plant transfer function $G _ { P } ( s )$ ), the closed-loop transfer function for any controller is

$$T (s) = \frac {G (s)}{1 + G (s)} = \frac {G _ {C} (s) G _ {P} (s)}{1 + G _ {C} (s) G _ {P} (s)} \tag {10.14}$$

(again, note that we have unity feedback so $H ( s ) = 1 )$ ). First, we consider a proportional (P) controller, and therefore the controller transfer function is simply a constant gain. Substituting $G _ { C } ( s ) = K _ { P }$ for the controller and $G _ { P } ( s ) =$ $4 0 0 / ( s + 2 0 . 4 )$ for the plant, the closed-loop transfer function (10.14) becomes

$$T (s) = \frac {K _ {P} \frac {4 0 0}{s + 2 0 . 4}}{1 + K _ {P} \frac {4 0 0}{s + 2 0 . 4}} = \frac {4 0 0 K _ {P}}{s + 2 0 . 4 + 4 0 0 K _ {P}} \tag {10.15}$$

Equation (10.15) relates the closed-loop speed response of the motor (??) to the speed command $( \omega _ { \mathrm { r e f } } )$ ). If the speed command $\omega _ { \mathrm { r e f } }$ is a constant (step) input, then the steady-state motor speed can be determined from the DC gain:

$$\text { DC gain: } \quad T (s = 0) = \frac {4 0 0 K _ {P}}{2 0 . 4 + 4 0 0 K _ {P}} \tag {10.16}$$

For a step speed command, the steady-state motor speed is

$$\omega_ {\mathrm{ss}} = \frac {4 0 0 K _ {P}}{2 0 . 4 + 4 0 0 K _ {P}} \omega_ {\mathrm{ref}}$$

Hence, for a P-gain, $K _ { P } = 0 . 5 \mathrm { V } \mathrm { - s } / \mathrm { r a d }$ , the DC gain is $2 0 0 / 2 2 0 . 4 = 0 . 9 0 7 4$ , and therefore the steady-state motor speed $\omega _ { \mathrm { s s } }$ is 90.74% of the commanded reference speed $\omega _ { \mathrm { r e f } } .$ . Clearly, the steady-state motor speed exhibits better tracking (i.e., smaller velocity error) as the P-gain is increased. However, the P-controller cannot provide perfect steady-state tracking because a zero velocity error would produce a zero armature voltage $( \mathrm { i . e . , } e _ { \mathrm { i n } } ( t ) = K _ { P } \omega _ { e } )$ and the motor cannot maintain a constant angular velocity without an input torque (or, input voltage) to offset the friction torque.

Equation (10.15) shows that the time constant of the first-order closed-loop system is

$$\tau = \frac {1}{2 0 . 4 + 4 0 0 K _ {P}}$$
