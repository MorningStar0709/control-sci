The two other closed-loop poles for the compensated system are found as follows:

$$s _ {3} = - 2. 3 2 6, \quad s _ {4} = - 0. 0 5 4 9$$

The addition of the lag compensator increases the order of the system from 3 to 4, adding one additional closed-loop pole close to the zero of the lag compensator. (The added closed-loop pole at $s = - 0 . 0 5 4 9$ is close to the zero at $s = - 0 . 0 5 . )$ Such a pair of a zero and pole creates a long tail of small amplitude in the transient response, as we will see later in the unit-step response. Since the pole at $s = - 2 . 3 2 6$ is very far from the jv axis compared with the dominant closed-loop poles, the effect of this pole on the transient response is also small. Therefore, we may consider the closed-loop poles at $s = - 0 . 3 1 \pm j 0 . 5 5$ to be the dominant closed-loop poles.

The undamped natural frequency of the dominant closed-loop poles of the compensated system is 0.631 radsec.This value is about 6% less than the original value, 0.673 radsec.This implies that the transient response of the compensated system is slower than that of the original system. The response will take a longer time to settle down.The maximum overshoot in the step response will increase in the compensated system. If such adverse effects can be tolerated, the lag compensation as discussed here presents a satisfactory solution to the given design problem.

Next, we shall compare the unit-ramp responses of the compensated system against the uncompensated system and verify that the steady-state performance is much better in the compensated system than the uncompensated system.

To obtain the unit-ramp response with MATLAB, we use the step command for the system $C ( s ) / { \big [ } s R ( s ) { \big ] } ^ { * }$ SinceD . $C ( s ) / [ s R ( s ) ]$ for the compensated system is

$$
\begin{array}{l} \frac {C (s)}{s R (s)} = \frac {1 . 0 2 3 5 (s + 0 . 0 5)}{s [ s (s + 0 . 0 0 5) (s + 1) (s + 2) + 1 . 0 2 3 5 (s + 0 . 0 5) ]} \\ = \frac {1 . 0 2 3 5 s + 0 . 0 5 1 2}{s ^ {5} + 3 . 0 0 5 s ^ {4} + 2 . 0 1 5 s ^ {3} + 1 . 0 3 3 5 s ^ {2} + 0 . 0 5 1 2 s} \\ \end{array}
$$

we have

$$\mathrm{numc} = [ 1. 0 2 3 5 0. 0 5 1 2 ]\mathrm{denc} = [ 1 \quad 3. 0 0 5 \quad 2. 0 1 5 \quad 1. 0 3 3 5 \quad 0. 0 5 1 2 \quad 0 ]$$

Also, for the uncompensated system isC(s)CsR(s)D

$$
\begin{array}{l} \frac {C (s)}{s R (s)} = \frac {1 . 0 6}{s [ s (s + 1) (s + 2) + 1 . 0 6 ]} \\ = \frac {1 . 0 6}{s ^ {4} + 3 s ^ {3} + 2 s ^ {2} + 1 . 0 6 s} \\ \end{array}
$$

Hence,

$$\mathrm{num} = [ 1. 0 6 ]\mathrm{den} = [ 1 \quad 3 \quad 2 \quad 1. 0 6 \quad 0 ]$$
