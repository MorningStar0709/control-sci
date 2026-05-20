To ensure uniform Lyapunov stability, we add requirements to suboptimal MPC beyond obtaining only a cost decrease. Here we impose the constraint

$$| \mathbf {u} | \leq d | x | \quad x \in r \mathcal {B}$$

in which $d , r > 0$ . This type of constraint was first introduced in (2.43) of Chapter 2. In that arrangement of suboptimal MPC it was simplest to switch to local controller $u = \kappa _ { f } ( x )$ when the state entered $\mathbb { X } _ { f }$ to automatically enforce this constraint. In this chapter we instead include the constraint explicitly in the distributed MPC optimization problem and do not switch to a local controller. Both alternatives provide (uniform) Lyapunov stability of the solution $x ( k ) = 0$ for all k. The following lemma summarizes the conditions we use later in the chapter for establishing exponential stability of distributed MPC. A similar lemma establishing asymptotic stability of suboptimal MPC was given by Scokaert, Mayne, and Rawlings (1999) (Theorem 1).

Definition 6.3 (Exponential stability). Let X be positive invariant for $x ^ { + } = f ( x )$ . Then the origin is exponentially stable for $x ^ { + } = f ( x )$ with a region of attraction X if there exists $c > 0$ and $\gamma < 1$ such that

$$\left| \phi (i; x) \right| \leq c | x | \gamma^ {i}$$

for all $i \ge 0 , x \in \mathbb { X }$ .

Consider next the suboptimal MPC controller. Let the system satisfy $( x ^ { + } , \mathbf { u } ^ { + } ) = ( f ( x , \mathbf { u } ) , g ( x , \mathbf { u } ) )$ with initial sequence u $( 0 ) = { \bf h } ( x ( 0 ) )$ . The controller constraints are $\boldsymbol { x } ( i ) \in \mathbb { X } \subseteq \mathbb { R } ^ { n }$ for all $i \in \mathbb { I } _ { 0 : N }$ and u $( i ) \in \mathbb { U } \subseteq$ $\mathbb { R } ^ { m }$ for all $i \in \mathbb { I } _ { 0 : N - 1 }$ . Let $x _ { N }$ denote the set of states for which the MPC controller is feasible. The suboptimal MPC system satisfies the following. Given $r > 0$ , there exist $a , b , c > 0$ such that

$$
\begin{array}{l} a \left| (x, \mathbf {u}) \right| ^ {2} \leq V (x, \mathbf {u}) \leq b \left| (x, \mathbf {u}) \right| ^ {2} \quad x \in \mathcal {X} _ {N} \quad \mathbf {u} \in \mathbb {U} ^ {N} \\ V (x ^ {+}, \mathbf {u} ^ {+}) - V (x, \mathbf {u}) \leq - c | (x, u (0)) | ^ {2} \quad x \in \mathcal {X} _ {N} \quad \mathbf {u} \in \mathbb {U} ^ {N} \\ | \mathbf {u} | \leq d | x | \quad x \in r \mathcal {B} \\ \end{array}
$$
