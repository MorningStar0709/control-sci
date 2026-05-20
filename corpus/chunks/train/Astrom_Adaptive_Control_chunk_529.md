The minimization can be done analytically for N = 1, giving

$$\mu_ {1} (\eta , \beta) = \arg \min \left(1 + \eta^ {2} (1 - \mu) ^ {2} + \frac {\mu^ {2} \eta^ {2}}{\beta^ {2}}\right) = \frac {\beta^ {2}}{1 + \beta^ {2}}$$

The original variables give

$$u (t) = - \frac {1}{\hat {b} (t + 1)} \cdot \frac {\hat {b} ^ {2} (t + 1)}{\hat {b} ^ {2} (t + 1) + P (t + 1)} y (t)$$

This control law is the one-step control, or myopic control, derived in Example 7.2.

For N > 1 the optimization can no longer be done analytically. Instead, we have to resort to numerical calculations. Figure 7.5 shows the dual control laws obtained for different time horizons N. The discontinuity of the control law corresponds to the situation in which a probing signal is introduced to improve the estimates.

The certainty equivalence controller

$$u (t) = - y (t) / \hat {b}$$

can be expressed as

$$\mu = 1$$

in normalized variables. Notice that all control laws are the same for large $\beta$ , that is, if the estimate is accurate. The optimal control law is close to the cautious control for large control errors. For estimates with poor precision and moderate control errors, the dual control gives larger control actions than the other control laws. The optimal dual controller has been computed on a Vax 11/780. The normalized variables $\eta$ and $\beta$ are discretized into 64 values each. The control table and the loss function table are thus of dimension $64 \times 64$ . One iteration of the Bellman equation takes about 6 hours of CPU time. ☐
