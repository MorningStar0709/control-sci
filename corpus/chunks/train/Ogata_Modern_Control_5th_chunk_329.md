3. Assume the lead compensator $G _ { c } ( s )$ to be

$$G _ {c} (s) = K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}}, \quad (0 < \alpha < 1)$$

where a and T are determined from the angle deficiency. $K _ { c }$ is determined from the requirement of the open-loop gain.

4. If static error constants are not specified, determine the location of the pole and zero of the lead compensator so that the lead compensator will contribute the necessary angle $\phi .$ If no other requirements are imposed on the system, try to make the value of a as large as possible. A larger value of a generally results in a larger value of $K _ { v } ,$ , which is desirable. Note that

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = K _ {c} \alpha \lim _ {s \rightarrow 0} s G _ {c} (s)$$

5. Determine the value of $K _ { c }$ of the lead compensator from the magnitude condition.

Once a compensator has been designed, check to see whether all performance specifications have been met. If the compensated system does not meet the performance specifications, then repeat the design procedure by adjusting the compensator pole and zero until all such specifications are met. If a large static error constant is required, cascade a lag network or alter the lead compensator to a lag–lead compensator.

Note that if the selected dominant closed-loop poles are not really dominant, or if the selected dominant closed-loop poles do not yield the desired result, it will be necessary to modify the location of the pair of such selected dominant closed-loop poles. (The closed-loop poles other than dominant ones modify the response obtained from the dominant closed-loop poles alone.The amount of modification depends on the location of these remaining closed-loop poles.) Also, the closed-loop zeros affect the response if they are located near the origin.

EXAMPLE 6–6 Consider the position control system shown in Figure 6–39(a). The feedforward transfer function is

$$G (s) = \frac {1 0}{s (s + 1)}$$

The root-locus plot for this system is shown in Figure 6–39(b). The closed-loop transfer function for the system is

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {1 0}{s ^ {2} + s + 1 0} \\ = \frac {1 0}{(s + 0 . 5 + j 3 . 1 2 2 5) (s + 0 . 5 - j 3 . 1 2 2 5)} \\ \end{array}
$$

Figure 6–39

(a) Control system; (b) root-locus plot.

![](image/26c7abe3e4f40a140372ddc96de5fb4879e2eea5992b962e5c6106c651a393e9.jpg)

<details>
<summary>flowchart</summary>
