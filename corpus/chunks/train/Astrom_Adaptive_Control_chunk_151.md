# Causality Conditions

To obtain a controller that is causal in the discrete-time case or proper in the continuous-time case, we must impose the conditions

$$\deg S \leq \deg R \tag {3.13}\deg T \leq \deg R$$

The Diophantine equation (3.4) has many solutions because if $R^{0}$ and $S^{0}$ are solutions, then so are

$$R = R ^ {0} + Q B \tag {3.14}S = S ^ {0} - Q A$$

where Q is an arbitrary polynomial. Since there are many solutions, we may select the solution that gives a controller of lowest degree. We call this the minimum-degree solution. Since $\deg A > \deg B$ , the term of highest order on the left-hand side of Eq. (3.4) is AR. Hence

$$\deg R = \deg A _ {c} - \deg A$$

Because of Eqs. (3.14) there is always a solution such that $\deg S < \deg A = n$ . We can thus always find a solution in which the degree of S is at most $\deg A - 1$ . This is called the minimum-degree solution to the Diophantine equation. The condition $\deg S \leq \deg R$ thus implies that

$$\deg A _ {c} \geq 2 \deg A - 1$$

It follows from Eq. (3.12) that the condition $\deg T \leq \deg R$ implies that

$$\deg A _ {m} - \deg B _ {m} ^ {\prime} \geq \deg A - \deg B ^ {+}$$

Adding $\deg B^{-}$ to both sides, we find that this is equivalent to $\deg A_{m} - \deg B_{m} \geq d_{0}$ . This means that in the discrete-time case the time delay of the model must be at least as large as the time delay of the process, which is a very natural condition. Summarizing, we find that the causality conditions (3.13) can be written as

$$\deg A _ {c} \geq 2 \deg A - 1\deg A _ {c} \geq 2 \deg B - 1 \tag {3.15}$$

It is natural to choose a solution in which the controller has the lowest possible degree. In the discrete-time case it is also reasonable to require that there be no extra delay in the controller. This implies that polynomials R, S, and T should have the same degrees. The following design procedure is then obtained.
