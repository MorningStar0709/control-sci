If (i) $(A, B)$ is stabilizable and (ii) $A_{w}$ and $A_{y}$ have only stable eigenvalues, then the system of Equation 7.46 is stabilizable. To see this, it is sufficient to notice that $A - BK_{x}$ can be made stable by proper choice of $K_{x}$ . If that is the case, then the design of the gain matrix $\left[K_{x} \quad K_{w} \quad K_{y}\right]$ can be made by the LQ technique. To summarize:

1. Calculate the dc steady-state input to yield the desired constant output. (More generally, do this for nondecreasing complex exponential signals.)   
2. Append the state equations that describe those parts of the disturbance of set-point inputs corresponding to decreasing exponentials.   
3. Solve the LQ control problem for the gain matrix.
