Because the quadratic terms are nonnegative, the sequence of optimal estimator costs is nondecreasing with increasing T . We can establish that the optimal cost is bounded above as follows: at any time T we can choose the decision variables to be $\{ x ( 0 ) , A x ( 0 ) , \ldots , A ^ { T } x ( 0 ) \}$ , which achieves cost $| x ( 0 ) - \overline { { x } } ( 0 ) | _ { ( P ^ { - } ( 0 ) ) ^ { - 1 } } ^ { 2 }$ independent of T . The optimal cost sequence is nondecreasing and bounded above and, therefore, converges.

The optimal estimator cost converges regardless of system observability. But if we want the optimal estimate to converge to the state, we have to restrict the system further. The following lemma provides an example of what is required.

Lemma 1.6 (Estimator convergence). For $( A , C )$ observable, $Q , R > 0$ , and noise-free measurements $\mathbf { y } ( T ) ~ = ~ \left\{ C x ( 0 ) , C A x ( 0 ) , \ldots , C A ^ { T } x ( 0 ) \right\}$ , the optimal linear state estimate converges to the state

$$\hat {x} (T) \rightarrow x (T) \quad a s T \rightarrow \infty$$

Proof. To compress the notation somewhat, let $\hat { w } _ { T } ( j ) ~ = ~ \hat { x } ( T + j +$ $1 | T + n - 1 ) - A \hat { x } ( T + j | T + n - 1 )$ . Using the optimal solution at time $T + n - 1$ as decision variables at time $T - 1$ allows us to write the following inequality

$$V _ {T - 1} ^ {0} \leq V _ {T + n - 1} ^ {0} -\frac {1}{2} \left(\sum_ {j = - 1} ^ {n - 2} | \hat {w} _ {T} (j) | _ {Q ^ {- 1}} ^ {2} + \sum_ {j = 0} ^ {n - 1} | y (T + j) - C \hat {x} (T + j | T + n - 1) | _ {R ^ {- 1}} ^ {2}\right)$$

Because the sequence of optimal costs converges with increasing $T _ { : }$ , and $Q ^ { - 1 } , R ^ { - 1 } > 0$ , we have established that for increasing $T$

$$\hat {w} _ {T} (j) \rightarrow 0 \quad j = - 1, \dots , n - 2y (T + j) - C \hat {x} (T + j | T + n - 1) \rightarrow 0 \quad j = 0, \dots , n - 1 \tag {1.39}$$

From the system model we have the following relationship between the last n stages in the optimization problem at time $T + n - 1$ with data $\mathbf { y } ( T + n - 1 )$

$$
\left[ \begin{array}{c} \hat {x} (T | T + n - 1) \\ \hat {x} (T + 1 | T + n - 1) \\ \vdots \\ \hat {x} (T + n - 1 | T + n - 1) \end{array} \right] = \left[ \begin{array}{c} I \\ A \\ \vdots \\ A ^ {n - 1} \end{array} \right] \hat {x} (T | T + n - 1) +

\left[ \begin{array}{c c c c} 0 & & & \\ I & 0 & & \\ \vdots & \vdots & \ddots & \\ A ^ {n - 2} & A ^ {n - 3} & \dots & I \end{array} \right] \left[ \begin{array}{c} \hat {w} _ {T} (0) \\ \hat {w} _ {T} (1) \\ \vdots \\ \hat {w} _ {T} (n - 2) \end{array} \right] \tag {1.40}
$$

We note the measurements satisfy
