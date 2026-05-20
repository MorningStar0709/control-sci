# 1.4.5 Observability

We next explore the convergence properties of the state estimators. For this we require the concept of system observability. The basic idea of observability is that any two distinct states can be distinguished by applying some input and observing the two system outputs over some finite time interval (Sontag, 1998, p.262–263). We discuss this general definition in more detail when treating nonlinear systems in Chapter 4, but observability for linear systems is much simpler. First of all, the applied input is irrelevant and we can set it to zero. Therefore consider the linear time-invariant system (A, C) with zero input

$$x (k + 1) = A x (k)y (k) = C x (k)$$

The system is observable if there exists a finite N, such that for every $x ( 0 )$ , N measurements $\{ y ( 0 ) , y ( 1 ) , \ldots , y ( N - 1 ) \}$ distinguish uniquely the initial state $x ( 0 )$ . Similarly to the case of controllability, if we cannot determine the initial state using n measurements, we cannot determine it using $N > n$ measurements. Therefore we can develop a convenient test for observability as follows. For n measurements, the system model gives

$$
\left[ \begin{array}{c} y (0) \\ y (1) \\ \vdots \\ y (n - 1) \end{array} \right] = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] x (0) \tag {1.36}
$$

The question of observability is therefore a question of uniqueness of solutions to these linear equations. The matrix appearing in this equation is known as the observability matrix O

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right] \tag {1.37}
$$

From the fundamental theorem of linear algebra, we know the solution to (1.36) is unique if and only if the columns of the np ×n observability matrix are linearly independent.6 Therefore, we have that the system (A, C) is observable if and only if

$$\operatorname{rank} (\mathcal {O}) = n$$

The following result for checking observability also proves useful (Hautus, 1972).

Lemma 1.4 (Hautus Lemma for observability). A system is observable if and only if

$$
\operatorname{rank} \left[ \begin{array}{c} \lambda I - A \\ C \end{array} \right] = n \quad \text {for all} \lambda \in \mathbb {C} \tag {1.38}
$$

in which C is the set of complex numbers.

Notice that the first n rows of the matrix in (1.38) are linearly independent if λ ∉ eig(A), so (1.38) is equivalent to checking the rank at just the eigenvalues of A

$$
\operatorname{rank} \left[ \begin{array}{c} \lambda I - A \\ C \end{array} \right] = n \quad \text { for   all } \lambda \in \operatorname{eig} (A)
$$
