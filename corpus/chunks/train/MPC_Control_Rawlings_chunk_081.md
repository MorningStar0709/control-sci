In fact we know more. From the previous sections, we know the optimal solution is found by iterating the Riccati equation, and the optimal infinite horizon control law and optimal cost are given by

$$u ^ {0} (x) = K x \quad V ^ {0} (x) = (1 / 2) x ^ {\prime} \Pi x$$

in which

$$
\begin{array}{l} K = - (B ^ {\prime} \Pi B + R) ^ {- 1} B ^ {\prime} \Pi A \\ \Pi = Q + A ^ {\prime} \Pi A - A ^ {\prime} \Pi B (B ^ {\prime} \Pi B + R) ^ {- 1} B ^ {\prime} \Pi A \tag {1.19} \\ \end{array}
$$

Proving Lemma 1.3 has shown also that for (A, B) controllable and $Q , R > 0$ , a positive definite solution to the discrete algebraic Riccati equation (DARE), (1.19), exists and the eigenvalues of $( A + B K )$ are asymptotically stable for the K corresponding to this solution (Bertsekas, 1987, pp.58–64).

This basic approach to establishing regulator stability will be generalized in Chapter 2 to handle constrained and nonlinear systems, so it is helpful for the new student to first become familiar with these ideas in the unconstrained, linear setting. For linear systems, asymptotic convergence is equivalent to asymptotic stability, and we delay the discussion of stability until Chapter 2. In Chapter 2 the optimal cost is shown to be a Lyapunov function for the closed-loop system. We also can strengthen the stability for linear systems from asymptotic stability to exponential stability based on the form of the Lyapunov function.

The LQR convergence result in Lemma 1.3 is the simplest to establish, but we can enlarge the class of systems and penalties for which closed-loop stability is guaranteed. The system restriction can be weakened from controllability to stabilizability, which is discussed in Exercises 1.19 and 1.20. The restriction on the allowable state penalty Q can be weakened from $Q > 0$ to $Q \geq 0$ and $( A , Q )$ detectable, which is also discussed in Exercise 1.20. The restriction $R > 0$ is retained to ensure uniqueness of the control law. In applications, if one cares little about the cost of the control, then R is chosen to be small, but positive definite.
