Proof. Since $\mathbf { u } \ \in \ \mathcal { U } ( x , 0 )$ , the control sequence $\mathbf { u } ^ { i } \in \mathcal { U } ( x ( i ) , i )$ . If $\mathbf { u } ^ { i } = \{ u ( i ) , u ( i + 1 ) , \ldots , u ( N - 1 ) \}$ is not optimal for $\mathbb { P } ( x ( i ) , i )$ , there exists a control $\mathrm { s e q u e n c e } \mathbf { u ^ { \prime } } = \{ u ^ { \prime } ( i ) , u ^ { \prime } ( i + 1 ) , \ldots , u ( N { - } 1 ) ^ { \prime } \} \in \mathcal { U } ( x ( i ) , i )$ such that $V ( x ( i ) , i , \mathbf { u } ^ { \prime } ) ~ < ~ V ( x ( i ) , \mathbf { u } )$ . Consider now the control sequence $\widetilde { \mathbf { u } } : = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( i - 1 ) , u ^ { \prime } ( i ) , u ^ { \prime } ( i + 1 ) , \ldots , u ( N - 1 ) ^ { \prime } \}$ . It follows that $\tilde { \mathbf { u } } \in \mathcal { U } ( x , 0 )$ and $V ( x , 0 , { \tilde { \mathbf { u } } } ) < V ( x , 0 , \mathbf { u } ) = V ^ { 0 } ( x , 0 )$ , a contradiction. Hence ${ \mathbf u } ( x ( i ) , i )$ is optimal for $\mathbb { P } ( x ( i ) , i )$ .

The most important feature of DP is the fact that the DP recursion yields the optimal value $V ^ { 0 } ( x , i )$ and the optimal control $\kappa ( x , i ) =$ arg min ${ \mathrm { i } } _ { u } \{ \ell ( x , u ) + V ^ { 0 } ( f ( x , u ) , i + 1 ) \mid ( x , u ) \in \mathbb { Z } , f ( x , u ) \in X ( i + 1 ) \}$ for each $( x , i ) \in X ( i ) \times \{ 0 , 1 , \ldots , N - 1 \}$ .

Theorem C.2 (Optimal value function and control law from DP). Suppose that the function $\Psi ~ : ~ \mathbb { R } ^ { n } \times \{ 0 , 1 , \ldots , N \} ~ \to ~ \mathbb { R }$ , satisfies, for all $i \in \{ 1 , 2 , \ldots , N - 1 \}$ , all $x \in X ( i )$ , the DP recursion

$$\Psi (x, i) = \min \{\ell (x, u) + \Psi (f (x, u), i + 1) \mid (x, u) \in \mathbb {Z}, f (x, u) \in X (i + 1) \}X (i) = \{x \in \mathbb {R} ^ {n} \mid \exists u \in \mathbb {R} ^ {m} \text { such that } (x, u) \in \mathbb {Z}, f (x, u) \in X (i + 1) \}$$

with boundary conditions

$$\Psi (x, N) = V _ {f} (x) \forall x \in \mathbb {X} _ {f}, X (N) = \mathbb {X} _ {f}$$

Then $\Psi ( x , i ) = V ^ { 0 } ( x , i )$ for all $( x , i ) \in X ( i ) \times \{ 0 , 1 , 2 , \ldots , N \}$ ; the DP recursion yields the optimal value function and the optimal control law.
