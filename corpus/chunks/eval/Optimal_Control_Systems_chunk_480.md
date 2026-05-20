# B.1 State Space Form for Continuous-Time Systems

A linear time-invariant (LTI), continuous-time, dynamical system is described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t), \quad \text { state equation }\mathbf {y} (t) = \mathbf {C x} (t) + \mathbf {D u} (t), \quad \text { output equation } \tag {B.1.1}$$

with initial conditions $\mathbf{x}(t=t_{0})=\mathbf{x}(t_{0})$ . Here, $\mathbf{x}(t)$ is an n-dimensional state vector, $\mathbf{u}(t)$ is an r dimensional control vector, and $\mathbf{y}(t)$ is a p dimensional output vector and the various matrices A,B,..., are of appropriate dimensionality. The Laplace transform (in terms of the Laplace variable s) of the preceding set of equations (B.1.1) is

$$s \mathbf {X} (s) - \mathbf {x} (t _ {0}) = \mathbf {A X} (s) + \mathbf {B U} (s)\mathbf {Y} (s) = \mathbf {C X} (s) + \mathbf {D U} (s) \tag {B.1.2}$$

which becomes

$$\mathbf {X} (s) = [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} [ \mathbf {x} (t _ {0}) + \mathbf {B U} (s) ]\mathbf {Y} (s) = \mathbf {C} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} [ \mathbf {x} (t _ {0}) + \mathbf {B U} (s) ] + \mathbf {D U} (s) \tag {B.1.3}$$

where, $\mathbf{X}(s) =$ Laplace transform of $\mathbf{x}(t)$ , etc. In terms of the transfer function $\mathbf{G}(s)$ with zero initial conditions $\mathbf{x}(t_0) = 0$ , we have

$$\mathbf {G} (s) = \frac {\mathbf {Y} (s)}{\mathbf {U} (s)} = \mathbf {C} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} + \mathbf {D}. \tag {B.1.4}$$

A linear time-varying (LTV), continuous-time, dynamical system is described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t), \quad \text { state equation }\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) + \mathbf {D} (t) \mathbf {u} (t), \quad \text { output equation } \tag {B.1.5}$$

with initial conditions $\mathbf{x}(t = t_0) = \mathbf{x}(t_0)$ . The solution of the continuous-time LTI system (B.1.1) is given by

$$\mathbf {x} (t) = \boldsymbol {\Phi} (t, t _ {0}) \mathbf {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} \boldsymbol {\Phi} (t, \tau) \mathbf {B u} (\tau) d \tau\mathbf {y} (t) = \mathbf {C} \boldsymbol {\Phi} (t, t _ {0}) \mathbf {x} (t _ {0}) + \mathbf {C} \int_ {t _ {0}} ^ {t} \boldsymbol {\Phi} (t, \tau) \mathbf {B u} (\tau) d \tau + \mathbf {D u} (t) \tag {B.1.6}$$

where, $\Phi(t, t_0)$ , called the state transition matrix of the system (B.1.1), is given by
