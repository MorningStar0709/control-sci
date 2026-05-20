It is unfortunately the case, however, that due to state constraints, $U ( \cdot )$ is often not continuous in constrained optimal control problems. If $U ( \cdot )$ is constant, which is the case in optimal control problem if state or mixed control-state constraints are absent, then, from the above results, the value function $V ^ { 0 } ( \cdot )$ is continuous. Indeed, under slightly stronger assumptions, the value function is Lipschitz continuous.

Lipschitz continuity of the value function. If we assume that $V ( \cdot )$ is Lipschitz continuous and that $U ( x ) \equiv U$ , we can establish Lipschitz continuity of $V ^ { 0 } ( \cdot )$ . Interestingly the result does not require, nor does it imply, Lipschitz continuity of the minimizer $u ^ { 0 } ( \cdot )$ .

Theorem C.29 (Lipschitz continuity of value function). Suppose that $V : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to \mathbb { R }$ is Lipschitz continuous on bounded sets6 and that $U ( x ) \equiv U$ where U is a compact subset of $\mathbb { R } ^ { m }$ . Then $V ^ { 0 } ( \cdot )$ is Lipschitz continuous on bounded sets.

Proof. Let S be an arbitrary bounded set in X, the domain of the value function $V ^ { 0 } ( \cdot )$ , and let $R : = S \times \mathbb { U } ; R$ is a bounded subset of $z .$ Since R is bounded, there exists a Lipschitz constant $L _ { S }$ such that

$$\left| V (x ^ {\prime}, u) - V (x ^ {\prime \prime}, u) \right| \leq L _ {S} | x ^ {\prime} - x ^ {\prime \prime} |$$

for all $x ^ { \prime } , x ^ { \prime \prime } \in S$ , all $u \in U$ . Hence,

$$V ^ {0} (x ^ {\prime}) - V ^ {0} (x ^ {\prime \prime}) \leq V (x ^ {\prime}, u ^ {\prime \prime}) - V (x ^ {\prime \prime}, u ^ {\prime \prime}) \leq L _ {S} | x ^ {\prime} - x ^ {\prime \prime} |$$

for all $x ^ { \prime } , x ^ { \prime \prime } \in S$ , any $u ^ { \prime \prime } \in u ^ { 0 } ( x ^ { \prime \prime } )$ . Interchanging $x ^ { \prime }$ and $x ^ { \prime \prime }$ in the above derivation yields

$$V ^ {0} (x ^ {\prime \prime}) - V ^ {0} (x ^ {\prime}) \leq V (x ^ {\prime \prime}, u ^ {\prime}) - V (x ^ {\prime}, u ^ {\prime}) \leq L _ {S} | x ^ {\prime \prime} - x ^ {\prime} |$$

for all $x ^ { \prime } , x ^ { \prime \prime } \in S$ , any $u ^ { \prime } \in u ^ { 0 } ( x ^ { \prime } )$ . Hence $V ^ { 0 } ( \cdot )$ is Lipschitz continuous on bounded sets.
