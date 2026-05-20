# B.7 Output-to-State Stability and Detectability

We present some definitions and results that are discrete time versions of results due to Sontag and Wang (1997) and Krichman, Sontag, and Wang (2001). The output-to-state (OSS) property corresponds, informally, to the statement that “no matter what the initial state is, if the observed outputs are small, then the state must eventually be small”. It is therefore a natural candidate for the concept of nonlinear (zero-state) detectability. We consider first the autonomous system

$$x ^ {+} = f (x) \quad y = h (x) \tag {B.12}$$

where $f ( \cdot ) : \mathbb { X } \to \mathbb { X }$ is locally Lipschitz continuous and $h ( \cdot )$ is continuously differentiable where ${ \mathbb X } = { \mathbb R } ^ { n }$ for some n. We assume $x \ = \ 0$ is an equilibrium state, i.e., $f ( 0 ) = 0$ . We also assume $h ( 0 ) = 0$ . We use $\phi ( k ; x _ { 0 } )$ to denote the solution of (B.12) with initial state $x _ { 0 }$ , and $y ( k ; x _ { 0 } )$ to denote $h ( \phi ( k ; x _ { 0 } ) )$ . The function $y _ { x _ { 0 } } ( \cdot )$ is defined by

$$y _ {x _ {0}} (k) := y (k; x _ {0})$$

We use |·| and k·k to denote, respectively the Euclidean norm of a vector and the sup norm of a sequence; $\| \cdot \| _ { 0 : k }$ denotes the max norm of a sequence restricted to the interval [0, k]. For conciseness, u, y denote, respectively, the sequences $\{ u ( j ) \} , \{ y ( j ) \}$ .

Definition B.39 (Output-to-state stable (OSS)). The system (B.12) is outputto-state stable (OSS) if there exist functions $\beta ( \cdot ) \in \mathcal { K L }$ and $\gamma ( \cdot ) \in \mathcal { K }$ such that for all $\boldsymbol { x } _ { 0 } \in \mathbb { R } ^ { n }$ and all $k \geq 0$

$$\left| x (k; x _ {0}) \right| \leq \max \left\{\beta \left(\left| x _ {0} \right|, k\right), \gamma \left(\left\| \mathbf {y} \right\| _ {0: k}\right) \right\}$$

Definition B.40 (OSS-Lyapunov function). An OSS-Lyapunov function for system (B.12) is any function V (·) with the following properties (a) There exist $\mathcal { K } _ { \infty } \mathrm { { \cdot f u n c t i o n s \ : } } \alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that

$$\alpha_ {1} (x) \leq V (x) \leq \alpha_ {2} (x)$$

for all x in $\mathbb { R } ^ { n }$ .

(b) There exist K∞-functions α(·) and $\sigma ( \cdot )$ such that for all $x \in \mathbb { R } ^ { n }$ either

$$V (f (x)) - V (x) \leq - \alpha (| x |) + \sigma (| h (x) |)$$

or

$$V (x (k + 1; x _ {0})) \leq \rho V (x (k; x _ {0})) + \sigma (\left| y (k; x _ {0}) \right|) \tag {B.13}$$

for some $\rho \in ( 0 , 1 )$ .

Inequality (B.13) corresponds to an exponential-decay OSS-Lyapunov function.

Theorem B.41 (OSS and OSS-Lyapunov function). The following properties are equivalent for system (B.12):

(a) The system is OSS.

(b) The system admits an OSS-Lyapunov function.

(c) The system admits an exponential-decay OSS-Lyapunov function.
