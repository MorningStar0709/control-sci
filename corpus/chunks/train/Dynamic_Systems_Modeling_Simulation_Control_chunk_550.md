$$U (s) = K _ {P} E (s) + K _ {I} \frac {E (s)}{s} + K _ {D} s E (s) \tag {10.12}$$

The PID controller transfer function $G _ { C } ( s ) = U ( s ) / E ( s )$ is

$$G _ {C} (s) = \frac {K _ {P} s + K _ {I} + K _ {D} s ^ {2}}{s} \tag {10.13}$$

Figure 10.14 shows a closed-loop control system with a PID controller represented as $G _ { C } ( s )$ . The reader should see that the PID controllers shown in Figs. 10.13 and 10.14 are equivalent. It is also important to note that inserting a PID controller adds two zeros and one pole to the forward transfer function (the zeros of the PID controller $G _ { C } ( s )$ are the values of s that cause $G _ { C } ( s ) = 0 )$ . Equation (10.13) shows that the two zeros of $G _ { C } ( s )$ are computed from $K _ { D } s ^ { 2 } + K _ { P } s + K _ { I } = 0$ and therefore depend on the three gains while the single pole is $s = 0$ .
