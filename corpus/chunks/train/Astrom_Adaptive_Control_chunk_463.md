$$g (\bar {\theta}) = E \left\{\varphi^ {T} (t - d) \varphi (t - d) \right\}$$

and $\bar{R}$ is replaced by $\bar{r}$ in Eq. (6.81). These equations are called the associated ordinary differential equations to Eqs. (6.74) and (6.75). They are a special kind of averaged equations. First, the difference equations are replaced by differential equations; second, there is a time scaling compared with the original system. The time scaling can be interpreted as a logarithmic compression of the original time. That is, more and more steps of length $\gamma(t)$ are needed to get the step $\Delta\tau$ as the time progresses.

The arguments leading to Eqs. (6.81) and (6.82) have been heuristic. However, it can be rigorously shown that, provided that the estimates $\hat{\theta}(t)$ are “sufficiently often” in the domain of attraction of the associated differential equations, then

\- Only stable stationary points of Eqs. (6.81) and (6.82) are possible convergence points for the estimates.

\- The trajectories $\bar{\theta}(\tau)$ are the "asymptotic paths" of the estimates $\hat{\theta}(t)$ .

The associated ODE can be used to find possible convergence points of an adaptive algorithm, $\bar{\theta}^{0}$ and $\bar{R}^{0}$ . The equations can then be linearized around these stationary points. It is easily seen that the linearized equations are

$$
\frac {d}{d t} \left( \begin{array}{l} \bar {\theta} - \tilde {\theta} ^ {0} \\ \bar {R} - \bar {R} ^ {0} \end{array} \right) = \left( \begin{array}{c c} G (\bar {\theta}) ^ {- 1} \frac {\partial f (\bar {\theta})}{\partial \bar {\theta}} & 0 \\ X & - I \end{array} \right) _ {\bar {\theta} = \bar {\theta} ^ {0}} \binom{\bar {\theta} - \bar {\theta} ^ {0}}{\bar {R} - \bar {R} ^ {0}}
$$

where the element X is not important for the local stability. The stationary point is thus stable if the matrix

$$K = G (\bar {\theta}) ^ {- 1} \frac {\partial f (\bar {\theta})}{\partial \bar {\theta}} \Bigg | _ {\bar {\theta} = \bar {\theta} ^ {0}} \tag {6.83}$$

has all its eigenvalues in the left half-plane. The associated ODEs can thus be used in the following way:

1. Compute the expressions for $\varphi(t)$ and $\varepsilon(t) = y(t) - \varphi(t - d)^T\bar{\theta}$ for a fixed value of $\bar{\theta}$ .

2. Compute the expected values $G(\bar{\theta})$ and $f(\bar{\theta})$ .

3. Determine possible convergence points for Eqs. (6.81) and (6.82), and determine the local stability properties by using Eq. (6.83).

4. Simulate the equations.

Even if Eqs. (6.81) and (6.82) can be quite difficult to analyze in detail, it is usually easy to determine the possible stationary points. The equations can also be simulated to obtain a feel for the behavior of the convergence properties. The change in the time scale makes it more favorable to simulate the ODEs than the averaged difference equations.
