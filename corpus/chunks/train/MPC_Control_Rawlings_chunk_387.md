If A is stable, then, as shown in Kolmanovsky and Gilbert (1998), $\textstyle S ( \infty ) : = \sum _ { j = 0 } ^ { \infty } A ^ { j } \mathbb { W }$ exists and is positive invariant for $x ^ { + } = A x + w , \mathrm { i . e . }$ , $x \in S ( \infty )$ implies that $A x + w \in S ( \infty )$ for all $w \in \mathbb { W } ;$ also $S ( i ) \to S ( \infty )$ in the Hausdorff metric as $i  \infty$ . The set $S ( \infty )$ is known to be the minimal robust positive invariant set5 for $x ^ { + } = A x + w , w \in \mathbb { W }$ . Also $S ( i ) \subseteq S ( i + 1 ) \subseteq S ( \infty )$ for all $i \in \mathbb { I } _ { \geq 0 }$ so that the tube $\hat { \mathbf { X } } ( x , \mathbf { u } )$ defined by

$$\hat {\mathbf {X}} (x, \mathbf {u}) := \{\hat {X} (0), \hat {X} (1; x, \mathbf {u}), \dots , \hat {X} (N; x, \mathbf {u}) \}$$

in which

$$\hat {X} (0) = \{x \} \quad \hat {X} (i; x, \mathbf {u}) = \{z (i) \} \oplus S$$

in which $S ~ = ~ S ( \infty )$ is an outer-bounding tube with constant “crosssection” S for the exact tube ${ \mathbf { X } } ( x , { \mathbf { u } } ) ~ ( X ( i ; x , { \mathbf { u } } ) ~ \subseteq ~ \hat { X } ( i ; x , { \mathbf { u } } )$ for all $i \in \mathbb { I } _ { \geq 0 } )$ . It is sometimes more convenient to use the “constant crosssection” outer-bounding tube $\hat { \mathbf { X } } ( x , \mathbf { u } )$ in place of the exact tube $\mathbf { X } ( x , \mathbf { u } )$ .

If we restrict attention to the interval [0, N] as we do in computing the MPC action, then setting $S = S ( N )$ yields a less conservative, constrained cross-section, outer-bounding tube for this interval.

While the exact tube $\mathbf { X } ( x , \mathbf { u } )$ , and the outer-bounding tube $\hat { \mathbf { X } } ( x , { \mathbf { u } } )$ , are easily obtained, their use may be limited for reasons discussed earlier—the sets S(i) may be unnecessarily large simply because an open-loop control sequence rather than a feedback policy was employed to generate the tube. For example, if $\mathbb { W } = [ - 1 , 1 ]$ and $x ^ { + } = x + u + w$ , then $S ( i ) = ( i + 1 ) \mathbb { W }$ increases without bound as time i increases. We must introduce feedback to contain the size of S(i), but wish to do so in a simple way because optimizing over arbitrary policies is prohibitive. The feedback policy we propose is

$$u = v + K (x - z)$$

in which x is the current state of the system $x ^ { + } = A x + B u + w , z$ is the current state of a nominal system defined below, and v is the current input to the nominal system. With this feedback policy, the state x satisfies the difference equation

$$x ^ {+} = A x + B v + B K e + w$$
