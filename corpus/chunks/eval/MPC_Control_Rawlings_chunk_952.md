# B.5 Control-Lyapunov Functions

A control-Lyapunov function is a useful generalization, due to Sontag (1998a, pp.218–233), of a Lyapunov function; while a Lyapunov function is relevant for a system $x ^ { + } = f ( x )$ and provides conditions for the (asymptotic) stability of a set for this system, a control-Lyapunov function is relevant for a control system $x ^ { + } = f ( x , u )$ and provides conditions for the existence of a controller $u = \kappa ( x )$ that ensures (asymptotic) stability of a set for the controlled system $x ^ { + } = f ( x , \kappa ( x ) )$ ). Consider the control system

$$x ^ {+} = f (x, u)$$

where the control u is subject to the constraint

$$u \in \mathbb {U}$$

Our standing assumptions in this section are that $f ( \cdot )$ is continuous and U is compact.

Definition B.24 (Global control-Lyapunov function (CLF)). A function $V : \mathbb { R } ^ { n } \to \mathbb { R } _ { \geq 0 }$ is a global control-Lyapunov function for the system $x ^ { + } = f ( x , u )$ and set A if there exist $\mathcal { K } _ { \infty }$ -functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ and a PD-function $\alpha _ { 3 } ( \cdot )$ satisfying for all $x \in \mathbb { R } ^ { n }$ :

$$V (x) \geq \alpha_ {1} (| x | _ {\mathcal {A}})V (x) \leq \alpha_ {2} (| x | _ {\mathcal {A}})\inf _ {u \in \mathbb {U}} V (f (x, u)) \leq V (x) - \alpha_ {3} (| x | _ {\mathcal {A}})$$

Definition B.25 (Global stabilizability). Let A be compact. The set A is globally stabilizable for the system $x ^ { + } = f ( x , u )$ if there exists a statefeedback function $\kappa : \mathbb { R } ^ { n }  \mathbb { U }$ such that A is globally asymptotically stable for $x ^ { + } = f ( x , \kappa ( x ) )$ ).

In a similar fashion one can extend the concept of control-Lyapunov functions to the case when the system is subject to disturbances. Consider the system

$$x ^ {+} = f (x, u, w)$$

where the control u is constrained to lie in U and the disturbance takes values in the set W. We assume that $f ( \cdot )$ is continuous and that U and W are compact. The system may be equivalently defined by

$$x ^ {+} \in F (x, u)$$

where the set-valued function F(·) is defined by

$$F (x, u) := \{f (x, u, w) \mid w \in \mathbb {W} \}$$

We can now make the obvious generalizations of the definitions in Section B.4.2.
