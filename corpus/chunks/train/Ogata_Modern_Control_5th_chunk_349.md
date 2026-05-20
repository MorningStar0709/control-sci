$$G _ {c} (s) = K _ {c} \frac {\left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right)}{\left(\frac {T _ {1}}{\beta} s + 1\right) \left(\beta T _ {2} s + 1\right)} = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\beta}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)} \tag {6-24}$$

where $\beta > 1$ . The open-loop transfer function of the compensated system is $G _ { c } ( s ) G ( s )$ . If the static velocity error constant $K _ { v }$ is specified, determine the value of constant $K _ { c }$ from the following equation:

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s K _ {c} G (s) \\ \end{array}
$$

3. To have the dominant closed-loop poles at the desired location, calculate the angle contribution $\phi$ needed from the phase-lead portion of the lag–lead compensator.

4. For the lag–lead compensator, we later choose $T _ { 2 }$ sufficiently large so that

$$
\left| \begin{array}{c} s _ {1} + \frac {1}{T _ {2}} \\ \hline s _ {1} + \frac {1}{\beta T _ {2}} \end{array} \right|
$$

is approximately unity, where $s = s _ { 1 }$ is one of the dominant closed-loop poles. Determine the values of $T _ { 1 }$ and $\beta$ from the magnitude and angle conditions:

$$\left| K _ {c} \left(\frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\beta}{T _ {1}}}\right) G (s _ {1}) \right| = 1\left\lfloor \frac {s _ {1} + \frac {1}{T _ {1}}}{s _ {1} + \frac {\beta}{T _ {1}}} = \phi \right.$$

5. Using the value of $\beta$ just determined, choose $T _ { 2 }$ so that

$$\left| \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} \right| \div 1- 5 ^ {\circ} < \left\lfloor \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} < 0 ^ {\circ} \right.$$

The value of $\beta T _ { 2 }$ the largest time constant of the lag–lead compensator, should not be, too large to be physically realized. (An example of the design of the lag–lead compensator when $\gamma = \beta$ is given in Example 6–9.)

$$G (s) = \frac {4}{s (s + 0 . 5)}$$

This system has closed-loop poles at

$$s = - 0. 2 5 0 0 \pm j 1. 9 8 4 3$$

The damping ratio is 0.125, the undamped natural frequency is 2 rad/sec, and the static velocity error constant is 8 sec–1.
