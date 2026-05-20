# Exercise 1.33: Estimator stability and semidefinite state noise penalty

We wish to show that the least squares estimator is stable for $( A , C )$ detectable and $Q \geq 0 , ( A , Q )$ stabilizable.

(a) Because $Q ^ { - 1 }$ is not defined in this problem, the objective function defined in (1.27) requires modification. Show that the objective function with semidefinite $Q \geq 0$ can be converted into the following form

$$
\begin{array}{l} V (x (0), \mathbf {w} (T)) = \frac {1}{2} \left(| x (0) - \overline {{{{x}}}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \right. \\ \sum_ {k = 0} ^ {T - 1} | w (k) | _ {\tilde {Q} ^ {- 1}} ^ {2} + \sum_ {k = 0} ^ {T} \left| y (k) - C x (k) \right| _ {R ^ {- 1}} ^ {2}\left. \right) \\ \end{array}
$$

in which

$$x ^ {+} = A x + G w \quad \tilde {Q} > 0$$

Find expressions for $\tilde { \boldsymbol { Q } }$ and G in terms of the original semidefinite $Q .$ How are the dimension of $\tilde { \boldsymbol { Q } }$ and G related to the rank of Q?

(b) What is the probabilistic interpretation of the state estimation problem with semidefinite Q?

(c) Show that $( A , Q )$ stabilizable implies $( A , G )$ stabilizable in the converted form.

(d) Show that this estimator is stable for $( A , C )$ detectable and $( A , G )$ stabilizable with $\tilde { Q } , R > 0$ .

(e) Discuss what happens to the estimator’s stability if Q is not positive semidefinite or $( A , Q )$ is not stabilizable.
