$$u _ {N - 1} ^ {0} (x) = K (N - 1) xx _ {N} ^ {0} (x) = (A + B K (N - 1)) xV _ {N - 1} ^ {0} (x) = (1 / 2) x ^ {\prime} \Pi (N - 1) x\Pi (N - 1) = Q + A ^ {\prime} P _ {f} A +K (N - 1) ^ {\prime} \left(B ^ {\prime} P _ {f} B + R\right) K (N - 1) + 2 K (N - 1) ^ {\prime} B ^ {\prime} P _ {f} A$$

We can rewrite Π(N − 1) using the result

$$
\begin{array}{l} K (N - 1) ^ {\prime} \left(B ^ {\prime} P _ {f} B + R\right) K (N - 1) + 2 K (N - 1) ^ {\prime} B ^ {\prime} P _ {f} A = \\ - A ^ {\prime} P _ {f} B (B ^ {\prime} P _ {f} B + R) ^ {- 1} B ^ {\prime} P _ {f} A \\ \end{array}
$$

which is obtained by substituting (1.10) for K into the equation for Π(N − 1) and simplifying. Substituting this result into the previous equation gives

$$\Pi (N - 1) = Q + A ^ {\prime} P _ {f} A - A ^ {\prime} P _ {f} B (B ^ {\prime} P _ {f} B + R) ^ {- 1} B ^ {\prime} P _ {f} A$$

The function $V _ { N - 1 } ^ { 0 } ( x )$ defines the optimal cost to go from state x for the last stage under the optimal control law $u _ { N - 1 } ^ { 0 } ( x )$ . Having this function allows us to move to the next stage of the DP recursion. For the next stage we solve the optimization

$$\min _ {u (N - 2), x (N - 1)} \ell (x (N - 2), u (N - 2)) + V _ {N - 1} ^ {0} (x (N - 1))$$

subject to

$$x (N - 1) = A x (N - 2) + B u (N - 2)$$

Notice that this problem is identical in structure to the stage we just solved, (1.9), and we can write out the solution by simply renaming variables

$$
\begin{array}{l} u _ {N - 2} ^ {0} (x) = K (N - 2) x \\ x _ {N - 1} ^ {0} (x) = (A + B K (N - 2)) x \\ V _ {N - 2} ^ {0} (x) = (1 / 2) x ^ {\prime} \Pi (N - 2) x \\ K (N - 2) = - (B ^ {\prime} \Pi (N - 1) B + R) ^ {- 1} B ^ {\prime} \Pi (N - 1) A \\ \Pi (N - 2) = Q + A ^ {\prime} \Pi (N - 1) A - \\ A ^ {\prime} \Pi (N - 1) B (B ^ {\prime} \Pi (N - 1) B + R) ^ {- 1} B ^ {\prime} \Pi (N - 1) A \\ \end{array}
$$

The recursion from Π(N −1) to Π(N −2) is known as a backward Riccati iteration. To summarize, the backward Riccati iteration is defined as follows

$$
\begin{array}{l} \Pi (k - 1) = Q + A ^ {\prime} \Pi (k) A - A ^ {\prime} \Pi (k) B \left(B ^ {\prime} \Pi (k) B + R\right) ^ {- 1} B ^ {\prime} \Pi (k) A \\ k = N, N - 1, \dots , 1 \tag {1.11} \\ \end{array}
$$

with terminal condition

$$\Pi (N) = P _ {f} \tag {1.12}$$

The terminal condition replaces the typical initial condition because the iteration is running backward. The optimal control policy at each stage is

$$u _ {k} ^ {0} (x) = K (k) x \quad k = N - 1, N - 2, \dots , 0 \tag {1.13}$$

The optimal gain at time k is computed from the Riccati matrix at time $k + 1$

$$K (k) = - \left(B ^ {\prime} \Pi (k + 1) B + R\right) ^ {- 1} B ^ {\prime} \Pi (k + 1) A \quad k = N - 1, N - 2, \dots , 0 \tag {1.14}$$

and the optimal cost to go from time k to time N is

$$V _ {k} ^ {0} (x) = (1 / 2) x ^ {\prime} \Pi (k) x \quad k = N, N - 1, \dots , 0 \tag {1.15}$$
