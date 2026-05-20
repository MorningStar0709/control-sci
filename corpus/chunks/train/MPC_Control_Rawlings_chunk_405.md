# 3.5 Tube-Based MPC of Linear Systems with Parametric Uncertainty

Introduction. Section 3.4 shows how it is possible to construct bounding tubes and, consequently, tube-based model predictive controllers when the uncertainty in the system takes the form of a bounded additive disturbance w. For this kind of uncertainty, the tube has a constant cross-section S or a cross-section $S _ { k }$ that increases with time k and converges to S.

Here we consider a different form of uncertainty, parametric uncertainty in linear constrained systems. More specifically, we consider here robust control of the system

$$x ^ {+} = A x + B u$$

in which the parameter $p : = ( A , B )$ can, at any time, take any value in the convex set $\mathcal { P }$ defined by

$$\mathcal {P} := \operatorname{co} \left\{\left(A _ {j}, B _ {j}\right) \mid j \in \mathcal {J} \right\}$$

in which $\mathcal { I } : = \{ 1 , 2 , \ldots , J \}$ . We make the following assumption.

Assumption 3.18 (Quadratic stabilizability). The system $x ^ { + } = A x + B u$ is quadratically stabilizable, i.e., there exists a positive definite function $V _ { f } : x \mapsto ( 1 / 2 ) x ^ { \prime } P _ { f } x$ , a feedback control law $u = K x$ , and a positive constant ε such that

$$V _ {f} ((A + B K) x) - V _ {f} (x) \leq - \varepsilon | x | ^ {2} \tag {3.45}$$

for all $x \in \mathbb { R } ^ { n }$ and all $p ~ = ~ ( A , B ) ~ \in ~ \{ ( A _ { j } , B _ { j } ) ~ | ~ j ~ \in ~ \mathcal { I } \}$ . The origin is globally exponentially stable for $x ^ { + } \ = \ A _ { K } x \ : = \ ( A + B K ) x$ for all $( A , B ) \in \{ ( A _ { j } , B _ { j } ) \mid j \in \mathcal { I } \}$ .

The feedback matrix K and the positive definite matrix $P _ { f }$ may be determined using linear matrix inequalities. Because P is convex and $V _ { f } ( \cdot )$ is strictly convex, (3.45) is satisfied for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ and all $( A , B ) \in$ P. The system is subject to the same constraints as before

$$x \in \mathbb {X} \quad u \in \mathbb {U}$$

in which X and U are assumed, for simplicity, to be compact and polytopic; each set contains the origin in its interior. We define the nominal system to be

$$z ^ {+} = \bar {A} z + \bar {B} v$$

in which

$$\bar {A} := (1 / J) \sum_ {j = 1} ^ {J} A _ {j} \quad \bar {B} := (1 / J) \sum_ {j = 1} ^ {J} B _ {j}$$

The origin is globally exponentially stable for $x ^ { + } = \bar { A } _ { K } x : = ( \bar { A } + \bar { B } K ) x$ . The difference equation $x ^ { + } = A x + B u$ of the system being controlled may be expressed in the form

$$x ^ {+} = \bar {A} x + \bar {B} u + w$$
