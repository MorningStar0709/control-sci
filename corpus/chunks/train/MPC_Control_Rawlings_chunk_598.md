# 5.3.2 State Estimator

To estimate the state a simple Luenberger observer is employed

$$\hat {x} ^ {+} = A \hat {x} + B u + L (y - \hat {y})\hat {y} = C \hat {x} \tag {5.11}$$

where $\hat { x } \in \mathbb { R } ^ { n }$ is the current observer state (state estimate), $u \in \mathbb { R } ^ { m }$ is the current control action, ${ \hat { x } } ^ { + }$ is the successor state of the observer system, $\hat { \boldsymbol { y } } \in \mathbb { R } ^ { p }$ is the current observer output, and $\ b { L } \in \mathbb { R } ^ { n \times p }$ . The output injection matrix L is chosen to satisfy $\rho ( A _ { L } ) < 1$ where $A _ { L } : =$ $A - L C$ .

The estimated state $\hat { x }$ therefore satisfies the following uncertain difference equation

$$\hat {x} ^ {+} = A \hat {x} + B u + L (C \tilde {x} + \nu)$$

where the state estimation error $\tilde { x }$ is defined by $\tilde { x } : = x - \hat { x }$ so that $x = { \hat { x } } + { \widetilde { x } }$ . Since $x ^ { + } \ = \ A x + B u + w$ , the state estimation error $\tilde { x }$ satisfies

$$\tilde {x} ^ {+} = A _ {L} \tilde {x} + \tilde {w} \quad \tilde {w} := w - L v \tag {5.12}$$

Because w and ν are bounded, so is $\tilde { { w } }$ ; in fact, $\tilde { { w } }$ takes values in the C-set $\tilde { \mathbb { W } }$ defined by

$$\tilde {\mathbb {W}} := \mathbb {W} \oplus (- L \mathbb {N})$$

We recall the following standard definitions (Blanchini, 1999):

Definition 5.1 (Positive invariance; robust positive invariance). A set $\Omega \subseteq \mathbb { R } ^ { n }$ is positive invariant for the system $x ^ { + } = f ( x )$ and the constraint set X if $\Omega \subseteq \mathbb { X }$ and $f ( x ) \in \Omega , \forall x \in \Omega$ .

A set $\Omega \subseteq \mathbb { R } ^ { n }$ is robust positive invariant for the system $x ^ { + } = f ( x , w )$ and the constraint set (X, W) if $\Omega \subseteq \mathbb X$ and $f ( x , w ) \in \Omega , \ \forall w \in \mathbb { W }$ , $\forall x \in \Omega$ .

Since $\rho ( A _ { L } ) < 1$ and $\tilde { \mathbb { W } }$ is compact, there exists, as shown in Kolmanovsky and Gilbert (1998), Theorem 4.1, a robust positive invariant set $\mathbb { Z } \subseteq \mathbb { R } ^ { n }$ , satisfying

$$A _ {L} \Sigma \oplus \tilde {\mathbb {W}} = \Sigma \tag {5.13}$$
