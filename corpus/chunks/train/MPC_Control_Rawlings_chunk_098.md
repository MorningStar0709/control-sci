# 1.4.6 Convergence of the State Estimator

Next we consider the question of convergence of the estimates of several of the estimators we have considered. The simplest convergence question to ask is the following. Given an initial estimate error, and zero state and measurement noises, does the state estimate converge to the state as time increases and more measurements become available? If the answer to this question is yes, we say the estimates converge; sometimes we say the estimator converges. As with the regulator, optimality of an estimator does not ensure its stability. Consider the case $A = I , C = 0$ . The optimal estimate is ${ \hat { x } } ( k ) = { \overline { { x } } } ( 0 )$ , which does not converge to the true state unless we have luckily chosen ${ \overline { { x } } } ( 0 ) = x ( 0 )$ .7 Obviously the lack of stability is caused by our choosing an unobservable (undetectable) system.

We treat first the Kalman filtering or full least squares problem. Recall that this estimator optimizes over the entire state trajectory $\mathbf { x } ( T ) : = \{ x ( 0 ) , \ldots , x ( T ) \}$ based on all measurements $\mathbf { y } ( T ) : = \{ y ( 0 )$ , $\ldots , y ( T ) \}$ . In order to establish convergence, the following result on the optimal estimator cost function proves useful.

Lemma 1.5 (Convergence of estimator cost). Given noise-free measurements $\mathbf { y } ( T ) ~ = ~ \left\{ C x ( 0 ) , C A x ( 0 ) , \ldots , C A ^ { T } x ( 0 ) \right\}$ , the optimal estimator cost $V _ { T } ^ { 0 } ( \mathbf { y } ( T ) )$ converges as $T \to \infty$ .

Proof. Denote the optimal state sequence at time T given measurement $\mathbf { y } ( T )$ by

$$\{\hat {x} (0 | T), \hat {x} (1 | T), \dots , \hat {x} (T | T) \}$$

We wish to compare the optimal costs at time T and $T - 1$ . Therefore, consider using the first T − 1 elements of the solution at time T as decision variables in the state estimation problem at time $T - 1$ . The cost for those decision variables at time $T - 1$ is given by

$$V _ {T} ^ {0} - \frac {1}{2} \left(| \hat {x} (T | T) - A \hat {x} (T - 1 | T) | _ {Q ^ {- 1}} ^ {2} + | y (T) - C \hat {x} (T | T) | _ {R ^ {- 1}} ^ {2}\right)$$

In other words, we have the full cost at time T and we deduct the cost of the last stage, which is not present at $T - 1$ . Now this choice of decision variables is not necessarily optimal at time $T - 1$ , so we have the inequality

$$V _ {T - 1} ^ {0} \leq V _ {T} ^ {0} - \frac {1}{2} \left(| \hat {x} (T | T) - A \hat {x} (T - 1 | T) | _ {Q ^ {- 1}} ^ {2} + | y (T) - C \hat {x} (T | T) | _ {R ^ {- 1}} ^ {2}\right)$$
