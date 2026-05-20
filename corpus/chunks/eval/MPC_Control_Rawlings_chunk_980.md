Proof. Let $( x , i ) \in X ( i ) \times \{ 0 , 1 , \ldots , N \}$ be arbitrary. Let $\mathbf { u } = \{ u ( i ) , u ( i +$ $1 ) , \ldots , u ( N - 1 ) \}$ be an arbitrary control sequence in $\mathcal { U } ( x , i )$ and let $\mathbf { x } = \{ x , x ( i { + } 1 ) , \ldots , x ( N ) \}$ denote the corresponding trajectory starting at $( x , i )$ so that for each $j \in \{ i , i + 1 , \dots , N \} , x ( j ) = \phi ( j ; x , i , \mathbf { u } )$ . For each $j \in \{ i , i + 1 , \ldots , N - 1 \} , \mathrm { l e t } { \bf u } ^ { j } : = \{ u ( j ) , u ( j + 1 ) , \ldots , u ( N - 1 ) \}$ ; clearly $\mathbf { u } ^ { j } \in \mathcal { U } ( x ( j ) , j )$ . The cost due to initial event $( x ( j ) , j )$ and control sequence $\mathbf { u } ^ { j }$ is $\Phi ( x ( j ) , j )$ defined by

$$\Phi (x (j), j) := V (x (j), j, \mathbf {u} ^ {j})$$

Showing that $\Psi ( x , i ) \leq \Phi ( x , i )$ proves that $\Psi ( x , i ) = V ^ { 0 } ( x , i )$ since u is an arbitrary sequence in $\mathcal { U } ( x , i )$ ; because $( x , i ) \in X ( i ) \times \{ 0 , 1 , \ldots , N \}$ is arbitrary, that fact that $\Psi ( x , i ) = V ^ { 0 } ( x , i )$ proves that DP yields the optimal value function.

To prove that $\Psi ( x , i ) \leq \Phi ( x , i )$ , we compare $\Psi ( x ( j ) , j )$ and $\Phi ( x ( j ) , j )$ for each $j \in \{ i , i + 1 , \ldots , N \}$ , i.e., we compare the costs yielded by the DP recursion and by the arbitrary control u along the corresponding trajectory x. By definition, $\Psi ( x ( j ) , j )$ satisfies for each j

$$
\begin{array}{l} \Psi (x (j), j) = \min _ {u} \left\{\ell (x (j), u) + \Psi (f (x (j), u), j + 1) \right| \\ (x (j), u) \in \mathbb {Z}, f (x (j), u) \in X (j + 1) \} \tag {C.11} \\ \end{array}
$$

To obtain Φ $\cdot ( x ( j ) , j )$ for each j we solve the following recursive equation

$$\Phi (x (j), j) = \ell (x (j), u (j)) + \Phi (f (x (j), u (j)), j + 1) \tag {C.12}$$

The boundary conditions are

$$\Psi (x (N), N) = \Phi (x (N), N) = V _ {f} (x (N)) \tag {C.13}$$

Since $u ( j )$ satisfies $( x ( j ) , u ( j ) ) \in \mathbb { Z }$ and $f ( x ( j ) , u ( j ) ) \in X ( j + 1 )$ but is not necessarily a minimizer in (C.11), we deduce that

$$\Psi (x (j), j) \leq \ell (x (j), u (j)) + \Psi (f (x (j), u (j)), j + 1) \tag {C.14}$$

For each j, let E(j) be defined by

$$E (j) := \Psi (x (j), j) - \Phi (x (j), j)$$

Subtracting (C.12) from (C.14) and replacing $f ( x ( j ) , u ( j ) ) \mathrm { b y } x ( j + 1 )$ yields

$$E (j) \leq E (j + 1) \forall j \in \{i, i + 1, \dots N \}$$

Since $E ( N ) = 0$ by virtue of (C.13), we deduce that $E ( j ) \leq 0$ for all $j \in \{ i , i + 1 , \ldots , N \}$ ; in particular, $E ( i ) \leq 0$ so that

$$\Psi (x, i) \leq \Phi (x, i) = V (x, i, \mathbf {u})$$

for all $\mathbf { u } \in \mathcal { U } ( x , i )$ . Hence $\Psi ( x , i ) = V ^ { 0 } ( x , i )$ for all $( x , i ) \in X ( i ) \times$ $\{ 0 , 1 , \ldots , N \}$ .
