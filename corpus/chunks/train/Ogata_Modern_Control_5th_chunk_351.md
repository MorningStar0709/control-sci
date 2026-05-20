The phase-lag portion of the compensator can be designed as follows: First the value of $\beta$ is determined to satisfy the requirement on the static velocity error constant:

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} s K _ {c} \frac {\beta}{\gamma} G (s) \\ = \lim _ {s \rightarrow 0} s (6. 2 6) \frac {\beta}{1 0 . 0 4} \frac {4}{s (s + 0 . 5)} = 4. 9 8 8 \beta = 8 0 \\ \end{array}
$$

Hence, $\beta$ is determined as

$$\beta = 1 6. 0 4$$

Finally, we choose the value $T _ { 2 }$ such that the following two conditions are satisfied:

$$\left| \frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{1 6 . 0 4 T _ {2}}} \right| _ {s = - 2. 5 + j 4. 3 3} \div 1, \quad - 5 ^ {\circ} < \left| \frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{1 6 . 0 4 T _ {2}}} \right| _ {s = - 2. 5 + j 4. 3 3} < 0 ^ {\circ}$$

We may choose several values for $T _ { 2 }$ and check if the magnitude and angle conditions are satisfied. After simple calculations we find for $T _ { 2 } = 5$

$$1 > \text { magnitude } > 0. 9 8, \quad - 2. 1 0 ^ {\circ} < \text { angle } < 0 ^ {\circ}$$

Since $T _ { 2 } = 5$ satisfies the two conditions, we may choose

$$T _ {2} = 5$$

Now the transfer function of the designed lag–lead compensator is given by

$$
\begin{array}{l} G _ {c} (s) = (6. 2 6) \left(\frac {s + \frac {1}{2}}{s + \frac {1 0 . 0 4}{2}}\right) \left(\frac {s + \frac {1}{5}}{s + \frac {1}{1 6 . 0 4 \times 5}}\right) \\ = 6. 2 6 \left(\frac {s + 0 . 5}{s + 5 . 0 2}\right) \left(\frac {s + 0 . 2}{s + 0 . 0 1 2 4 7}\right) \\ = \frac {1 0 (2 s + 1) (5 s + 1)}{(0 . 1 9 9 2 s + 1) (8 0 . 1 9 s + 1)} \\ \end{array}
$$

The compensated system will have the open-loop transfer function

$$G _ {c} (s) G (s) = \frac {2 5 . 0 4 (s + 0 . 2)}{s (s + 5 . 0 2) (s + 0 . 0 1 2 4 7)}$$
