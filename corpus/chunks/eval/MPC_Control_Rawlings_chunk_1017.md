where $V ( \cdot )$ is the cost function, assumed to be Lipschitz continuous on bounded sets, and $\kappa ( \cdot )$ , the optimal control law, satisfies $\kappa ( { \boldsymbol { x } } ) \in$ $U ( x ) \subset \mathbb { U }$ and $\kappa ( \boldsymbol { x } ^ { \prime } ) \in U ( \boldsymbol { x } ^ { \prime } ) \subset \mathbb { U }$ . It follows from Corollary C.32 that there exists a $K > 0$ such that for all $x , x ^ { \prime } \in \mathcal { X }$ , there exists a $u ^ { \prime } \in U ( x ^ { \prime } ) \subset \mathbb { U }$ such that $| u ^ { \prime } - \kappa ( x ) | \ \leq \ K | x ^ { \prime } - x |$ . Since $\kappa ( x )$ is optimal for the problem $\mathbb { P } ( x )$ , and since $( x , \kappa ( x ) )$ and $( x ^ { \prime } , u ^ { \prime } )$ both lie in $R = S \times \mathbb { U }$ , there exists a constant $L _ { R }$ such that

$$
\begin{array}{l} V ^ {0} (x ^ {\prime}) - V ^ {0} (x) \leq V (x ^ {\prime}, u ^ {\prime}) - V (x, \kappa (x)) \\ \leq L _ {R} \left(\left| \left(x ^ {\prime}, u ^ {\prime}\right) - (x, \kappa (x)) \right|\right) \\ \leq L _ {R} \left| x ^ {\prime} - x \right| + L _ {R} K \left| x ^ {\prime} - x \right| \\ \leq M _ {S} | x ^ {\prime} - x |, \quad M _ {S} := L _ {R} (1 + K) \\ \end{array}
$$

Reversing the role of x and $x ^ { \prime }$ we obtain the existence of a $u \in \mathcal { U } ( x )$ such that $| u - \kappa ( x ^ { \prime } ) | \le K | x - x ^ { \prime } |$ ; it follows from the optimality of $\kappa ( \boldsymbol { x } ^ { \prime } )$ that

$$
\begin{array}{l} V ^ {0} (x) - V ^ {0} \left(x ^ {\prime}\right) \leq V (x, u) - V \left(x ^ {\prime}, \kappa \left(x ^ {\prime}\right)\right) \\ \leq M _ {S} \left| x - x ^ {\prime} \right| \\ \end{array}
$$

where, now, $u \in U ( x )$ and $\kappa ( \boldsymbol { x } ^ { \prime } ) \in U ( \boldsymbol { x } ^ { \prime } )$ . Hence $| V ^ { 0 } ( x ^ { \prime } ) - V ^ { 0 } ( x ) | \le$ $M _ { S } | x - x ^ { \prime } |$ for all $x , x ^ { \prime }$ in S. Since S is an arbitrary bounded set in $x$ , $V ^ { 0 } ( \cdot )$ is Lipschitz continuous on bounded sets.
