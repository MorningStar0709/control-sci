# B.3 State Space Form for Discrete-Time Systems

A linear time-invariant (LTI), discrete-time, dynamical system is described by

$$\mathbf {x} (k + 1) = \mathbf {A x} (k) + \mathbf {B u} (k), \quad \text { state equation }\mathbf {y} (k) = \mathbf {C x} (k) + \mathbf {D u} (k), \quad \text { output equation } \tag {B.3.1}$$

with initial conditions $\mathbf{x}(k=k_{0})=\mathbf{x}(k_{0})$ . Here, $\mathbf{x}(k)$ is an n-dimensional state vector, $\mathbf{u}(k)$ is an r-dimensional control vector, and $\mathbf{y}(k)$ is a p-dimensional output vector and the various matrices A, B, ..., are matrices of appropriate dimensionality. The Z-transform (in terms of the complex variable z) is

$$z \mathbf {X} (z) - \mathbf {x} \left(k _ {0}\right) = \mathbf {A X} (z) + \mathbf {B U} (z)\mathbf {Y} (z) = \mathbf {C X} (z) + \mathbf {D U} (z) \tag {B.3.2}$$

which becomes

$$\mathbf {X} (z) = \left[ z \mathbf {I} - \mathbf {A} \right] ^ {- 1} \left[ \mathbf {x} \left(k _ {0}\right) + \mathbf {B U} (z) \right]\mathbf {Y} (z) = \mathbf {C} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} [ \mathbf {x} (k _ {0}) + \mathbf {B U} (z) ] + \mathbf {D U} (z). \tag {B.3.3}$$

In terms of the transfer function $\mathbf{G}(z)$ with zero initial conditions $\mathbf{x}(k_0) = 0$ , we have

$$\mathbf {G} (z) = \frac {\mathbf {Y} (z)}{\mathbf {U} (z)} = \mathbf {C} [ z \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {D}. \tag {B.3.4}$$

An LTV, discrete-time, dynamical system is described by

$$\mathbf {x} (k + 1) = \mathbf {A} (k) \mathbf {x} (k) + \mathbf {B} (k) \mathbf {u} (k), \quad \text { state equation }\mathbf {y} (k) = \mathbf {C} (k) \mathbf {x} (k) + \mathbf {D} (k) \mathbf {u} (k), \quad \text { output equation } \tag {B.3.5}$$

with initial conditions $\mathbf{x}(k = k_0) = \mathbf{x}(k_0)$ . The solution of the LTI discrete-time system (B.3.1) is given by

$$\mathbf {x} (k) = \boldsymbol {\Phi} (k, k _ {0}) \mathbf {x} (k _ {0}) + \sum_ {m = k _ {0}} ^ {k - 1} \boldsymbol {\Phi} (k, m + 1) \mathbf {B u} (m)\mathbf {y} (k) = \mathbf {C} \boldsymbol {\Phi} (k, k _ {0}) \mathbf {x} (k _ {0}) + \mathbf {C} \sum_ {m = k _ {0}} ^ {k - 1} \boldsymbol {\Phi} (k, m + 1) \mathbf {B u} (m) + \mathbf {D u} (k) \tag {B.3.6}$$

where, $\Phi(k, k_0)$ , called the state transition matrix of the discrete-time system (B.3.1), is given by

$$\boldsymbol {\Phi} (k, k _ {0}) = \mathbf {A} ^ {k} \tag {B.3.7}$$

having the properties
