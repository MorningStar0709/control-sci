for all $\phi ( 0 ) \in ( \mathcal { Z } _ { N } \oplus \mathbb { S } ) \times \mathcal { Z } _ { N }$ . Since, for all $z ( 0 ) \in \mathcal { Z } _ { N } , z ( i ) \in \mathbb { Z }$ and $\nu ( i ) \in \mathbb { V }$ , it follows that $\hat { x } ( i ) \in \{ z ( i ) \} \oplus \mathbb { S } , x ( i ) \in \mathbb { X }$ , and $u ( i ) \in \mathbb { U }$ for all $i \in \mathbb { I } _ { \geq 0 }$ . Thus $\mathcal { A } : = \mathbb { S } \times \{ 0 \}$ is exponentially stable with a region of attraction $( \mathcal { Z } _ { N } \oplus \mathbb { S } ) \times \mathcal { Z } _ { N }$ for the composite system (5.25) and (5.26). 

It follows from Proposition 5.5 that x(i), which lies in the set $\{ z ( i ) \}$ ⊕ $\mathbb { T } , \mathbb { T } : = \mathbb { S } \oplus \mathbb { Z }$ , converges to the set Γ. In fact $x ( i )$ converges to a set that is, in general, smaller than Γ since Γ is a conservative bound on $\tilde { { \boldsymbol { x } } } ( i ) + e ( i )$ . We determine this smaller set as follows. Let $\phi : = ( \tilde { x } , e )$ and let $\psi : = ( w , \nu )$ ; φ is the state of the two error systems and ψ is a bounded disturbance lying in a C-set $\Psi : = \mathbb { W } \times \mathbb { N }$ . Then, from (5.12) and (5.18) the state φ evolves according to

$$\phi^ {+} = \tilde {A} \phi + \tilde {B} \psi \tag {5.27}$$

where

$$
\widetilde {A} := \left[ \begin{array}{c c} A _ {L} & 0 \\ L C & A _ {K} \end{array} \right] \qquad \widetilde {B} := \left[ \begin{array}{c c} I & - L \\ 0 & L \end{array} \right]
$$

Because $\rho ( A _ { L } ) \ < \ 1$ and $\rho ( A _ { K } ) \ < \ 1$ , it follows that $\rho ( \stackrel { \sim } { A } ) \ < \ 1$ . Since $\rho ( \tilde { \boldsymbol { A } } ) < 1$ and Ψ is compact, there exists a robust positive invariant set $\Phi \subseteq \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ for (5.27) satisfying

$$\tilde {A} \Phi \oplus \tilde {B} \Psi = \Phi$$

Hence $\phi ( i ) \in \Phi$ for all $i \in \mathbb { I } _ { \geq 0 }$ if $\phi ( 0 ) \in \Phi$ . Since $x ( i ) = z ( i ) + e ( i ) +$ $\tilde { x } ( i )$ , it follows that $x ( i ) \in \{ z ( i ) \} \oplus H \Phi , H : = { \Big | } I _ { n } \quad I _ { n } { \Big | }$ , for all $i \in$ $ { \mathbb { I } } _ { \geq 0 }$ provided that $x ( 0 ) , { \hat { x } } ( 0 )$ and $z ( 0 )$ satisfy $( \tilde { x } ( 0 ) , e ( 0 ) ) \in \Phi$ where $\tilde { { x } } ( 0 ) = { x } ( 0 ) - \hat { { x } } ( 0 )$ and $e ( 0 ) = { \hat { x } } ( 0 ) - z ( 0 )$ . If these initial conditions are satisfied, x(i) converges robustly and exponentially fast to the set H Φ.

The remaining robust controllers presented in Section 3.4 of Chapter 3 may be similarly modified to obtain a robust output model predictive controller.
