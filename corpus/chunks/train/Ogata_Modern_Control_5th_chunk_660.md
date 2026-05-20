$$
\begin{array}{l} e ^ {(\mathbf {A} + \mathbf {B}) t} = \mathbf {I} + (\mathbf {A} + \mathbf {B}) t + \frac {(\mathbf {A} + \mathbf {B}) ^ {2}}{2 !} t ^ {2} + \frac {(\mathbf {A} + \mathbf {B}) ^ {3}}{3 !} t ^ {3} + \dots \\ e ^ {\mathbf {A} t} e ^ {\mathbf {B} t} = \left(\mathbf {I} + \mathbf {A} t + \frac {\mathbf {A} ^ {2} t ^ {2}}{2 !} + \frac {\mathbf {A} ^ {3} t ^ {3}}{3 !} + \dots\right) \left(\mathbf {I} + \mathbf {B} t + \frac {\mathbf {B} ^ {2} t ^ {2}}{2 !} + \frac {\mathbf {B} ^ {3} t ^ {3}}{3 !} + \dots\right) \\ = \mathbf {I} + (\mathbf {A} + \mathbf {B}) t + \frac {\mathbf {A} ^ {2} t ^ {2}}{2 !} + \mathbf {A B} t ^ {2} + \frac {\mathbf {B} ^ {2} t ^ {2}}{2 !} + \frac {\mathbf {A} ^ {3} t ^ {3}}{3 !} \\ + \frac {\mathbf {A} ^ {2} \mathbf {B} t ^ {3}}{2 !} + \frac {\mathbf {A B} ^ {2} t ^ {3}}{2 !} + \frac {\mathbf {B} ^ {3} t ^ {3}}{3 !} + \dots \\ \end{array}
$$

Hence,

$$
\begin{array}{l} e ^ {(\mathbf {A} + \mathbf {B}) t} - e ^ {\mathbf {A} t} e ^ {\mathbf {B} t} = \frac {\mathbf {B A} - \mathbf {A B}}{2 !} t ^ {2} \\ + \frac {\mathbf {B A} ^ {2} + \mathbf {A B A} + \mathbf {B} ^ {2} \mathbf {A} + \mathbf {B A B} - 2 \mathbf {A} ^ {2} \mathbf {B} - 2 \mathbf {A B} ^ {2}}{3 !} t ^ {3} + \dots \\ \end{array}
$$

The difference between $e ^ { ( \mathbf { A } + \mathbf { B } ) t }$ and $e ^ { \mathbf { A } t } e ^ { \mathbf { B } t }$ vanishes if A and B commute.

Laplace Transform Approach to the Solution of Homogeneous State Equations. Let us first consider the scalar case:

$$\dot {x} = a x \tag {9-32}$$

Taking the Laplace transform of Equation (9–32), we obtain

$$s X (s) - x (0) = a X (s) \tag {9-33}$$

where $X ( s ) = { \mathcal { L } } [ x ]$ Solving Equation (9–33) for. $X ( s )$ gives

$$X (s) = \frac {x (0)}{s - a} = (s - a) ^ {- 1} x (0)$$

The inverse Laplace transform of this last equation gives the solution

$$x (t) = e ^ {a t} x (0)$$

The foregoing approach to the solution of the homogeneous scalar differential equation can be extended to the homogeneous state equation:

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) \tag {9-34}$$

Taking the Laplace transform of both sides of Equation (9–34), we obtain

$$s \mathbf {X} (s) - \mathbf {x} (0) = \mathbf {A X} (s)$$

where $\mathbf { X } ( s ) = { \mathcal { L } } [ \mathbf { x } ] .$ Hence,.

$$(s \mathbf {I} - \mathbf {A}) \mathbf {X} (s) = \mathbf {x} (0)$$

Premultiplying both sides of this last equation by $( s \mathbf { I } - \mathbf { A } ) ^ { - 1 }$ , we obtain

$$\mathbf {X} (s) = (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {x} (0)$$
