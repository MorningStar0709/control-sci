# Recursion in the Number of Observations

Recursive equations can be derived for the case when the observations are obtained sequentially. The procedure is often referred to as recursive identification. The solution in (13.5) to the least-squares problem can be rewritten to give recursive equations. Let $\theta(N)$ denote the least-squares estimate based on N measurements. To derive the equations, N is introduced as a formal parameter in the functions, that is,

$$
\Phi (N) = \left( \begin{array}{c} {\varphi^ {T} (1)} \\ {\vdots} \\ {\varphi^ {T} (N)} \end{array} \right) \qquad y (N) = \left( \begin{array}{c} {y _ {1}} \\ {\vdots} \\ {y _ {N}} \end{array} \right)
$$

It is assumed that the matrix $\Phi^{T}\Phi$ is nonsingular for all N. The least-squares estimate $\hat{\theta}(N)$ is then given by Eq. (13.5):

$$\hat {\theta} (N) = \left(\Phi^ {T} (N) \Phi (N)\right) ^ {- 1} \Phi^ {T} (N) y (N)$$

When an additional measurement is obtained, a row is added to the matrix $\Phi$ and an element is added to the vector y. Hence

$$\Phi (N + 1) = \binom{\Phi (N)}{\varphi^ {T} (N + 1)} \quad y (N + 1) = \binom{y (N)}{y _ {N - 1}}$$

The estimate $\hat{\theta}(N + 1)$ given by (13.5) can then be written as

$$
\begin{array}{l} \hat {\theta} (N + 1) = \left(\Phi^ {T} (N + 1) \Phi (N + 1)\right) ^ {- 1} \Phi^ {T} (N + 1) y (N + 1) \\ = \left(\Phi^ {T} (N) \Phi (N) + \varphi (N + 1) \varphi^ {T} (N + 1)\right) ^ {- 1} \tag {13.9} \\ \times \left(\Phi^ {T} (N) y (N) + \varphi (N + 1) y _ {N + 1}\right) \\ \end{array}
$$

The solution is given by the following theorem.

THEOREM 13.3 RECURSIVE LEAST-SQUARES ESTIMATION Assume that the matrix $\Phi^T (N)\Phi (N)$ is positive definite. The least-squares estimate $\hat{\theta}$ then satisfies the recursive equation

$$
\hat {\theta} (N + 1) = \hat {\theta} (N) - K (N) \left(y _ {N + 1} - \varphi^ {T} (N + 1) \hat {\theta} (N)\right) \tag {13.10}
\begin{array}{l} K (N) = P (N + 1) \varphi (N + 1) \\ = P (N) \varphi (N + 1) \left(1 + \varphi^ {T} (N + 1) P (N) \varphi (N + 1)\right) ^ {- 1} \tag {13.11} \\ \end{array}
P (N + 1) = \Big (I - K (N) \varphi^ {T} (N + 1) \Big) P (N) \tag {13.12}
$$

Proof. To simplify the notation in the manipulations that follow, the argument N of $\Phi(N)$ and $y(N)$ and the argument $N+1$ of $\varphi^{T}(N+1)$ will be suppressed. Equation (13.9) can then be written as
