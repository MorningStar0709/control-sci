# 6–7 LAG COMPENSATION

Electronic Lag Compensator Using Operational Amplifiers. The configuration of the electronic lag compensator using operational amplifiers is the same as that for the lead compensator shown in Figure 6–36. If we choose $R _ { 2 } C _ { 2 } > R _ { 1 } C _ { 1 }$ in the circuit shown in Figure 6–36, it becomes a lag compensator. Referring to Figure 6–36, the transfer function of the lag compensator is given by

$$\frac {E _ {o} (s)}{E _ {i} (s)} = \hat {K} _ {c} \beta \frac {T s + 1}{\beta T s + 1} = \hat {K} _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}}$$

where

$$T = R _ {1} C _ {1}, \quad \beta T = R _ {2} C _ {2}, \quad \beta = \frac {R _ {2} C _ {2}}{R _ {1} C _ {1}} > 1, \quad \hat {K} _ {c} = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}}$$

Note that we use $\beta$ instead of a in the above expressions. [In the lead compensator we used a to indicate the ratio $R _ { 2 } C _ { 2 } / { \left( R _ { 1 } C _ { 1 } \right) }$ which was less than 1, or, $0 < \alpha < 1 . ]$ In this book we always assume that $0 < \alpha < 1$ and $\beta > 1$ .

Lag Compensation Techniques Based on the Root-Locus Approach. Consider the problem of finding a suitable compensation network for the case where the system exhibits satisfactory transient-response characteristics but unsatisfactory steady-state characteristics. Compensation in this case essentially consists of increasing the openloop gain without appreciably changing the transient-response characteristics.This means that the root locus in the neighborhood of the dominant closed-loop poles should not be changed appreciably, but the open-loop gain should be increased as much as needed. This can be accomplished if a lag compensator is put in cascade with the given feedforward transfer function.

To avoid an appreciable change in the root loci, the angle contribution of the lag network should be limited to a small amount, say less than 5°. To assure this, we place the pole and zero of the lag network relatively close together and near the origin of the s plane.Then the closed-loop poles of the compensated system will be shifted only slightly from their original locations. Hence, the transient-response characteristics will be changed only slightly.

Consider a lag compensator $G _ { c } ( s )$ where,

$$G _ {c} (s) = \hat {K} _ {c} \beta \frac {T s + 1}{\beta T s + 1} = \hat {K} _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}} \tag {6-19}$$
