The main negative effect of the lag compensation is that the compensator zero that will be generated near the origin creates a closed-loop pole near the origin.This closedloop pole and compensator zero will generate a long tail of small amplitude in the step response, thus increasing the settling time.

Design Procedures for Lag Compensation by the Root-Locus Method. The procedure for designing lag compensators for the system shown in Figure 6–47 by the root-locus method may be stated as follows (we assume that the uncompensated system meets the transient-response specifications by simple gain adjustment; if this is not the case, refer to Section 6–8):

1. Draw the root-locus plot for the uncompensated system whose open-loop transfer function is $G ( s )$ . Based on the transient-response specifications, locate the dominant closed-loop poles on the root locus.   
2. Assume the transfer function of the lag compensator to be given by Equation (6–19):

$$G _ {c} (s) = \hat {K} _ {c} \beta \frac {T s + 1}{\beta T s + 1} = \hat {K} _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}}$$

Then the open-loop transfer function of the compensated system becomes $G _ { c } ( s ) G ( s )$ .

3. Evaluate the particular static error constant specified in the problem.   
4. Determine the amount of increase in the static error constant necessary to satisfy the specifications.   
5. Determine the pole and zero of the lag compensator that produce the necessary increase in the particular static error constant without appreciably altering the original root loci. (Note that the ratio of the value of gain required in the specifications and the gain found in the uncompensated system is the required ratio between the distance of the zero from the origin and that of the pole from the origin.)   
6. Draw a new root-locus plot for the compensated system. Locate the desired dominant closed-loop poles on the root locus. (If the angle contribution of the lag network is very small—that is, a few degrees—then the original and new root loci are almost identical. Otherwise, there will be a slight discrepancy between them.Then locate, on the new root locus, the desired dominant closed-loop poles based on the transient-response specifications.)   
7. Adjust gain $\hat { K } _ { c }$ of the compensator from the magnitude condition so that the dominant closed-loop poles lie at the desired location. $\left( \hat { K } _ { c } \right.$ will be approximately 1.B c
