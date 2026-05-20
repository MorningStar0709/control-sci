# 7.3 Model Reduction by Balanced Truncation

Consider a stable system $G \in \mathcal { R } \mathcal { H } _ { \infty }$ and suppose $G = \left[ { \frac { A \left. B \right. } { C \left. D \right. } } \right]$ is a balanced realization $( { \mathrm { i . e . } }$ , its controllability and observability Gramians are equal and diagonal). Denote the balanced Gramians by $\Sigma ;$ then

$$A \Sigma + \Sigma A ^ {*} + B B ^ {*} = 0 \tag {7.5}A ^ {*} \Sigma + \Sigma A + C ^ {*} C = 0. \tag {7.6}$$

Now partition the balanced Gramian as $\Sigma = \left[ \begin{array} { c c } { { \Sigma _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { \Sigma _ { 2 } } } \end{array} \right]$ and partition the system accordingly as

$$
G = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & D \end{array} \right].
$$

The following theorem characterizes the properties of these subsystems.

Theorem 7.9 Assume that $\Sigma _ { 1 }$ and $\Sigma _ { 2 }$ have no diagonal entries in common. Then both subsystems $( A _ { i i } , B _ { i } , C _ { i } ) , i = 1 , 2$ are asymptotically stable.

Proof. It is clearly sufficient to show that $A _ { 1 1 }$ is asymptotically stable. The proof for the stability of $A _ { 2 2 }$ is similar. Note that equations (7.5) and (7.6) can be written in terms of their partitioned matrices as

$$A _ {1 1} \Sigma_ {1} + \Sigma_ {1} A _ {1 1} ^ {*} + B _ {1} B _ {1} ^ {*} = 0 \tag {7.7}\Sigma_ {1} A _ {1 1} + A _ {1 1} ^ {*} \Sigma_ {1} + C _ {1} ^ {*} C _ {1} = 0 \tag {7.8}A _ {2 1} \Sigma_ {1} + \Sigma_ {2} A _ {1 2} ^ {*} + B _ {2} B _ {1} ^ {*} = 0 \tag {7.9}\Sigma_ {2} A _ {2 1} + A _ {1 2} ^ {*} \Sigma_ {1} + C _ {2} ^ {*} C _ {1} = 0 \tag {7.10}A _ {2 2} \Sigma_ {2} + \Sigma_ {2} A _ {2 2} ^ {*} + B _ {2} B _ {2} ^ {*} = 0 \tag {7.11}\Sigma_ {2} A _ {2 2} + A _ {2 2} ^ {*} \Sigma_ {2} + C _ {2} ^ {*} C _ {2} = 0. \tag {7.12}$$

By Lemma 7.3 or Lemma $7 . 4 , \Sigma _ { 1 }$ can be assumed to be positive definite without loss of generality. Then it is obvious that $\mathrm { R e } \lambda _ { i } ( A _ { 1 1 } ) \leq 0$ by Lemma 7.2. Assume that $A _ { 1 1 }$ is not asymptotically stable; then there exists an eigenvalue at $j \omega$ for some ω. Let $V$ be a basis matrix for $\operatorname { K e r } ( A _ { 1 1 } - j \omega I )$ . Then we have

$$(A _ {1 1} - j \omega I) V = 0, \tag {7.13}$$

which gives

$$V ^ {*} (A _ {1 1} ^ {*} + j \omega I) = 0.$$

Equations (7.7) and (7.8) can be rewritten as
