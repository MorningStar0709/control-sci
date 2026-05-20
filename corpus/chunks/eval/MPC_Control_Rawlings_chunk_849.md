# A.14 Differential Equations

Although difference equation models are employed extensively in this book, the systems being controlled are most often described by differential equations. Thus, if the system being controlled is described by the differential equation $\dot { x } = f _ { c } ( x , u )$ , as is often the case, and if it is decided to control the system using piecewise constant control with period $\Delta ,$ then, at sampling instants $k \Delta$ where $k \in \mathbb { I }$ , the system is described by the difference equation

$$x ^ {+} = f (x, u)$$

then $f ( \cdot )$ may be derived from $f _ { c } ( \cdot )$ as follows

$$f (x, u) = x + \int_ {0} ^ {\Delta} f _ {c} (\phi_ {c} (s; x, u), u) d s$$

where $\phi _ { c } ( s ; x , u )$ is the solution of $\dot { x } = f _ { c } ( x , u )$ at time s if its initial state at time 0 is x and the control has a constant value u in the interval $[ 0 , \Delta ]$ . Thus x in the difference equation is the state at time k, say, u is the control in the interval $[ 0 , \Delta ]$ , and $x ^ { + }$ is the state at time $k + 1$ .

Because the discrete time system is most often obtained by a continuous time system, we must be concerned with conditions which guarantee the existence and uniqueness of solutions of the differential equation describing the continuous time system. For excellent expositions of the theory of ordinary differential equations see the books by Hale (1980), McShane (1944), Hartman (1964), and Coddington and Levinson (1955).

Consider, first, the unforced system described by

$$(d / d t) x (t) = f (x (t), t) \text { or } \dot {x} = f (x, t) \tag {A.12}$$

with initial condition

$$x (t _ {0}) = x _ {0} \tag {A.13}$$

Suppose $f : D  \mathbb { R } ^ { n }$ , where D is an open set in $\mathbb { R } ^ { n } \times \mathbb { R }$ , is continuous. A function $x : T \to \mathbb { R } ^ { n }$ , where T is an interval in R, is said to be a (conventional) solution of (A.12) with initial condition (A.13) (or passing through $( x _ { 0 } , t _ { 0 } ) )$ if:

(a) x is continuously differentiable and x satisfies (A.12) on $T _ { \ast }$ ,

(b) $x ( t _ { 0 } ) = x _ { 0 }$ ,

and $( x ( t ) , t ) \in D$ for all t in T . It is easily shown, when $f$ is continuous, that x satisfies (A.12) and (A.13) if and only if:

$$x (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (x (s), s) d s \tag {A.14}$$
