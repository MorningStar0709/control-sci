where $\{ w ( t ) \}$ and $\{ \nu ( t ) \}$ are sequences of zero mean normal independent random variables with variances $\Sigma _ { w }$ and $\Sigma _ { \nu }$ , respectively, and if the prior density $p ( 0 )$ of $x ( 0 )$ is normal with density n $( { \bar { x } } _ { 0 } , \Sigma _ { 0 } )$ then, as is well known, $p ( t )$ is the normal density $n ( { \hat { x } } ( t ) , \Sigma ( t ) )$ ) so that the hyperstate $p ( t )$ is finitely parameterized by $( \hat { x } ( t ) , \Sigma ( t ) )$ ; hence the evolution equation for $p ( t )$ is defined by the evolution equation for $( \hat { x } , \Sigma )$ , that is by:

$$\hat {x} (t + 1) = A \hat {x} (t) + B u + L (t) \psi (t) \tag {5.2}\Sigma (t + 1) = \Phi (\Sigma (t)) \tag {5.3}$$

in which

$$\Phi (\Sigma) := A \Sigma A ^ {\prime} - A \Sigma C ^ {\prime} \left(C ^ {\prime} \Sigma C + \Sigma_ {v}\right) ^ {- 1} C \Sigma A ^ {\prime} + \Sigma_ {w}\psi (t) := y (t) - C \hat {x} (t) = C \tilde {x} (t) + v (t)\tilde {x} (t) := x (t) - \hat {x} (t)$$

The initial conditions for (5.2) and (5.3) are

$$\hat {x} (0) = \bar {x} _ {0} \quad \Sigma (0) = \Sigma_ {0}$$

These are, of course, the celebrated Kalman filter equations derived in Chapter 1. The random variables $\tilde { x }$ and ψ have the following densities: $\tilde { { \boldsymbol { x } } } ( t ) \sim n ( 0 , { \boldsymbol { \Sigma } } ( t ) )$ and $\psi ( t ) \sim n ( 0 , \Sigma _ { \nu } + C ^ { \prime } \Sigma ( t ) C )$ . The finite dimensional equations (5.2) and (5.3) replace the difference equation (5.1) for the hyperstate p that is a conditional density and, therefore, infinite dimensional in general. The sequence $\{ \psi ( t ) \}$ is known as the innovation sequence; $\psi ( t )$ is the “new” information contained in $y ( t )$ .
