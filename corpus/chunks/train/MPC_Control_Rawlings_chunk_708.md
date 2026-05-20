Centralized target problem. We can solve the target problem at the plantwide level or as a distributed target problem at the subunit controller level. Consider first the centralized target problem with the disturbance model discussed in Chapter 1, (1.46)

$$\min _ {x _ {s}, u _ {s}} \frac {1}{2} \left| u _ {s} - u _ {\mathrm{sp}} \right| _ {R _ {s}} ^ {2} + \frac {1}{2} \left| C x _ {s} + C _ {d} \hat {d} (k) - y _ {\mathrm{sp}} \right| _ {Q _ {s}} ^ {2}$$

subject to:

$$
\left[ \begin{array}{c c} I - A & - B \\ H C & 0 \end{array} \right] \left[ \begin{array}{c} x _ {s} \\ u _ {s} \end{array} \right] = \left[ \begin{array}{c} B _ {d} \hat {d} (k) \\ r _ {\mathrm{sp}} - H C _ {d} \hat {d} (k) \end{array} \right]
E u _ {s} \leq e
$$

in which we have removed the state inequality constraints to be consistent with the regulator problem. We denote the solution to this problem $( x _ { s } ( k ) , u _ { s } ( k ) )$ . Notice first that the solution of the target problem depends only on the disturbance estimate, $\hat { d } ( k )$ , and not the solution of the control problem. So we can analyze the behavior of the target by considering only the exponential convergence of the estimator. We restrict the plant disturbance d so that the target problem is feasible, and denote the solution to the target problem for the plant disturbance, $\hat { d } ( k ) = d , \mathrm { a s } ( x _ { s } ^ { * } , u _ { s } ^ { * } )$ . Because the estimator is exponentially stable, we know that $\hat { d } ( k ) \to$ d as $k \to \infty$ . Because the target problem is a positive definite QP, we know the solution is Lipschitz continuous on bounded sets in the term $\hat { d } ( k )$ , which appears linearly in the objective function and the right-hand side of the equality constraint. Therefore, if we also restrict the initial disturbance estimate error so that the target problem remains feasible for all time, we know $( x _ { s } ( k ) , u _ { s } ( k ) ) \to ( x _ { s } ^ { * } , u _ { s } ^ { * } )$ and the rate of convergence is exponential.

Distributed target problem. Consider next the cooperative approach, in which we assume the input inequality constraints are uncoupled. In the constrained case, we try to set things up so each player solves a local target problem
