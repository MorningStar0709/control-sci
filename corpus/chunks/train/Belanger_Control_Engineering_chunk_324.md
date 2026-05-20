# Solution

To adjust k for gain margin, we locate the frequency where the phase is $180^{\circ}$ , which corresponds to a crossing of the negative real axis on the Nyquist plot. From the phase curve of Figure 6.15, that frequency is $\omega = 1.73$ rad/s. The magnitude at that frequency is -2.4 db. For a gain margin of 6 db, the loop gain on a magnitude must be at most -6 db where the phase is $180^{\circ}$ . To achieve that, we must lower the gain curve by 3.6 db; therefore $k \leq -3.6$ db to satisfy the gain-margin condition.

To satisfy the phase-margin condition, we locate the frequency where the phase is $-180^{\circ} + \text{phase margin} = -180^{\circ} + 45^{\circ} = -135^{\circ}$ . That frequency is $\omega = 1.0 \, rad/s$ , from the phase curve. The phase margin will be $45^{\circ}$ if the magnitude is 0 db where the phase is $-135^{\circ}$ , i.e., at $\omega = 1.0 \, rad/s$ . The magnitude is 6.51 db at $\omega = 1.0 \, rad/s$ , so the gain curve must be lowered by 6.51 db, i.e., k = -6.51 db. If k < -6.51 db, the crossover frequency is less than 1.0 rad/s, and the phase margin ( $180^{\circ} + \text{phase at crossover}$ ) is greater than $45^{\circ}$ . Therefore, $k \leq -6.51 \, db$ will satisfy the phase margin specification.

To satisfy both stability margins, we need $k \leq -6.51$ db.
