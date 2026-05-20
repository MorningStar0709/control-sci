# 1.3.3 Dynamic Programming Solution

After this brief introduction to DP, we apply it to solve the LQ control problem. We first rewrite (1.6) in the following form to see the structure clearly

$$V (x (0), \mathbf {u}) = \sum_ {k = 0} ^ {N - 1} \ell (x (k), u (k)) + \ell_ {N} (x (N)) \quad \text { s . t . } x ^ {+} = A x + B u$$

in which the stage cost $\ell ( x , u ) = ( 1 / 2 ) ( x ^ { \prime } Q x + u ^ { \prime } R u ) , k = 0 , \dots , N - 1$ and the terminal stage cost $\ell _ { N } ( x ) = ( 1 / 2 ) x ^ { \prime } P _ { f } x$ . Since x(0) is known, we choose backward DP as the convenient method to solve this problem. We first rearrange the overall objective function so we can optimize over input $u ( N - 1 )$ and state x(N)

$$
\begin{array}{l} \min _ {u (0), x (1), \dots u (N - 2), x (N - 1)} \ell (x (0), u (0)) + \ell (x (1), u (1)) + \dots + \\ \min _ {u (N - 1), x (N)} \ell (x (N - 1), u (N - 1)) + \ell_ {N} (x (N)) \\ \end{array}
$$

subject to

$$x (k + 1) = A x (k) + B u (k) \quad k = 0, \dots N - 1$$

The problem to be solved at the last stage is

$$\min _ {u (N - 1), x (N)} \ell (x (N - 1), u (N - 1)) + \ell_ {N} (x (N)) \tag {1.9}$$

subject to

$$x (N) = A x (N - 1) + B u (N - 1)$$

in which $x ( N - 1 )$ appears in this stage as a parameter. We denote the optimal cost by $V _ { N - 1 } ^ { 0 } ( x ( N - 1 ) )$ and the optimal decision variables by $u _ { N - 1 } ^ { 0 } ( x ( N - 1 ) )$ ) and $x _ { N } ^ { 0 } ( x ( N - 1 ) )$ . The optimal cost and decisions at the last stage are parameterized by the state at the previous stage as we expect in backward DP. We next solve this optimization. First we substitute the state equation for $x ( N )$ and combine the two quadratic terms using (1.8)

$$
\begin{array}{l} \ell (x (N - 1), u (N - 1)) + \ell_ {N} (x (N)) \\ = (1 / 2) \left(| x (N - 1) | _ {Q} ^ {2} + | u (N - 1) | _ {R} ^ {2} + | A x (N - 1) + B u (N - 1) | _ {P _ {f}} ^ {2}\right) \\ = (1 / 2) \left(| x (N - 1) | _ {Q} ^ {2} + | (u (N - 1) - v) | _ {H} ^ {2}\right) + d \\ \end{array}
$$

in which

$$H = R + B ^ {\prime} P _ {f} B\nu = K (N - 1) x (N - 1)d = (1 / 2) x (N - 1) ^ {\prime} \left(K (N - 1) ^ {\prime} R K (N - 1) + \right.\left. (A + B K (N - 1)) ^ {\prime} P _ {f} (A + B K (N - 1))\right) x (N - 1)K (N - 1) = - (B ^ {\prime} P _ {f} B + R) ^ {- 1} B ^ {\prime} P _ {f} A \tag {1.10}$$

Given this form of the cost function, we see by inspection that the optimal input for $u ( N - 1 )$ is v defining the optimal control law at stage $N - 1$ to be a linear function of the state $x ( N - 1 )$ . Then using the model equation, the optimal final state is also a linear function of state $x ( N - 1 )$ . The optimal cost is $^ { d , }$ which makes the optimal cost a quadratic function of $x ( N - 1 )$ . Summarizing, for all x
