If we express the $y ( k )$ in terms of $x ( 0 )$ and $u ( k )$ and collect terms we obtain

$$0 = x (0) ^ {\prime} \left[ \overline {{x}} (0) - C ^ {\prime} \overline {{u}} (1) - A ^ {\prime} C ^ {\prime} \overline {{u}} (2) - \dots - A ^ {N} \overline {{x}} (N) \right]+ u (0) ^ {\prime} \left[ \overline {{y}} (1) - D ^ {\prime} \overline {{u}} (1) - B ^ {\prime} C ^ {\prime} \overline {{u}} (2) - \dots - B ^ {\prime} A ^ {(N - 2)} C ^ {\prime} \overline {{u}} (N) - B ^ {\prime} A ^ {(N - 1)} \overline {{x}} (N) \right]+ \dots+ u (N - 2) ^ {\prime} \left[ \overline {{y}} (N - 1) - D ^ {\prime} \overline {{u}} (N - 1) - B ^ {\prime} C ^ {\prime} \overline {{u}} (N) - B ^ {\prime} A ^ {\prime} \overline {{x}} (N) \right]+ u (N - 1) ^ {\prime} \left[ \overline {{y}} (N) - D ^ {\prime} \overline {{u}} (N) - B ^ {\prime} \overline {{x}} (N) \right]$$

Since this equation must hold for all $( x ( 0 ) , u ( 0 ) , \ldots , u ( N - 1 ) )$ , each term in brackets must vanish. From the $u ( N - 1 )$ term we conclude

$$\overline {{y}} (N) = B ^ {\prime} \overline {{x}} (N) + D ^ {\prime} \overline {{u}} (N)$$

Using this result, the u(N − 2) term gives

$$B ^ {\prime} \left(\overline {{x}} (N - 1) - \left(A ^ {\prime} \overline {{x}} (N) + C ^ {\prime} \overline {{u}} (N)\right)\right) = 0$$

From which we find the state recursion for the dual system

$$\overline {{{x}}} (N - 1) = A ^ {\prime} \overline {{{x}}} (N) + C ^ {\prime} \overline {{{u}}} (N)$$

Passing through each term then yields the dual state space description of the adjoint operator $G ^ { * }$

$$\overline {{{x}}} (k - 1) = A ^ {\prime} \overline {{{x}}} (k) + C ^ {\prime} \overline {{{u}}} (k), \qquad k = N, \dots , 1\overline {{y}} (k) = B ^ {\prime} \overline {{x}} (k) + D ^ {\prime} \overline {{u}} (k)$$

So the primal and dual dynamic systems change matrices in the following way

$$(A, B, C, D) \longrightarrow (A ^ {\prime}, C ^ {\prime}, B ^ {\prime}, D ^ {\prime})$$

Notice this result produces the duality variables listed in Table A.1 if we first note that we have also renamed the regulator’s input matrix B to G in the estimation problem. We also note that time runs in the opposite directions in the dynamic system and the dual dynamic system, which corresponds to the fact that the Riccati equation iterations run in opposite directions in the regulation and estimation problems.
