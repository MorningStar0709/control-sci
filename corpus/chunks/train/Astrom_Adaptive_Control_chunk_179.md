Figure 3.11 Parameter estimates corresponding to the simulation shown in Fig. 3.10: $\hat{r}_{1}/\hat{r}_{0}$ (solid line), $\hat{t}_{0}/\hat{r}_{0}$ (dashed line), $\hat{s}_{0}/\hat{r}_{0}$ (dash-dot line), $\hat{s}_{1}/\hat{r}_{0}$ (dotted line).

Notice that the estimate of $r_{0}$ must be different from zero for the controller to be causal.

Figure 3.10 shows the process inputs and outputs in a simulation of the direct algorithm, and Fig. 3.11 shows the parameter estimates. The initial transient depends strongly on the initial conditions. At t = 100 the controller parameters are

$$
\begin{array}{l} \frac {\hat {r} _ {1} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = 0. 8 5 0 \quad (0. 8 4 6 7) \quad \frac {\hat {t} _ {0} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = 1. 6 5 \tag {1.6531} \\ \frac {\hat {s} _ {0} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = 2. 6 8 \quad (2. 6 8 5 2) \quad \frac {\hat {s} _ {1} (1 0 0)}{\hat {r} _ {0} (1 0 0)} = - 1. 0 3 \quad (- 1. 0 3 2 1) \\ \end{array}
$$

The controller parameters are divided by $\hat{r}_{0}$ to make a direct comparison with Examples 3.1 and 3.3. The correct values are given in parentheses. A comparison of Fig. 3.4 and Fig. 3.10 shows that the direct and indirect algorithms have very similar behavior. The limiting control law is the same in both cases. There is “ringing” in the control signal because of the cancellation of the process zero.

In a practical case the time delay and the order of the process that we would like to control are not known. It is therefore natural to consider these variables as design parameters that are chosen by the user. The parameter $d_{0}$ is of particular importance for a direct algorithm. In the next example we show that “ringing” can be avoided simply by increasing the value of $d_{0}$ .
