# D.1 Linear system zero-order hold

Starting with the continuous model

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t)$$

by premultiplying the model by $e ^ { - \mathbf { A } t }$ , we get

$$e ^ {- \mathbf {A} t} \dot {\mathbf {x}} (t) = e ^ {- \mathbf {A} t} \mathbf {A x} (t) + e ^ {- \mathbf {A} t} \mathbf {B u} (t)e ^ {- \mathbf {A} t} \dot {\mathbf {x}} (t) - e ^ {- \mathbf {A} t} \mathbf {A x} (t) = e ^ {- \mathbf {A} t} \mathbf {B u} (t)$$

The derivative of the matrix exponential is

$$\frac {d}{d t} e ^ {\mathbf {A} t} = \mathbf {A} e ^ {\mathbf {A} t} = e ^ {\mathbf {A} t} \mathbf {A}$$

so we recognize the previous equation as

$$\frac {d}{d t} \left(e ^ {- \mathbf {A} t} \mathbf {x} (t)\right) = e ^ {- \mathbf {A} t} \mathbf {B u} (t)$$

By integrating this equation, we get

$$e ^ {- \mathbf {A} t} \mathbf {x} (t) - e ^ {0} \mathbf {x} (0) = \int_ {0} ^ {t} e ^ {- \mathbf {A} \tau} \mathbf {B u} (\tau) d \tau\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau$$

which is an analytical solution to the continuous model. Now we want to discretize it.

$$
\begin{array}{l} \mathbf {x} _ {k} \stackrel {d e f} {=} \mathbf {x} (k T) \\ \mathbf {x} _ {k} = e ^ {\mathbf {A} k T} \mathbf {x} (0) + \int_ {0} ^ {k T} e ^ {\mathbf {A} (k T - \tau)} \mathbf {B u} (\tau) d \tau \\ \mathbf {x} _ {k + 1} = e ^ {\mathbf {A} (k + 1) T} \mathbf {x} (0) + \int_ {0} ^ {(k + 1) T} e ^ {\mathbf {A} ((k + 1) T - \tau)} \mathbf {B u} (\tau) d \tau \\ \mathbf {x} _ {k + 1} = e ^ {\mathbf {A} (k + 1) T} \mathbf {x} (0) + \int_ {0} ^ {k T} e ^ {\mathbf {A} ((k + 1) T - \tau)} \mathbf {B u} (\tau) d \tau \\ + \int_ {k T} ^ {(k + 1) T} e ^ {\mathbf {A} ((k + 1) T - \tau)} \mathbf {B u} (\tau) d \tau \\ \mathbf {x} _ {k + 1} = e ^ {\mathbf {A} (k + 1) T} \mathbf {x} (0) + \int_ {0} ^ {k T} e ^ {\mathbf {A} ((k + 1) T - \tau)} \mathbf {B u} (\tau) d \tau \\ + \int_ {k T} ^ {(k + 1) T} e ^ {\mathbf {A} (k T + T - \tau)} \mathbf {B u} (\tau) d \tau \\ \mathbf {x} _ {k + 1} = e ^ {\mathbf {A} T} \underbrace {\left(e ^ {\mathbf {A} k T} \mathbf {x} (0) + \int_ {0} ^ {k T} e ^ {\mathbf {A} (k T - \tau)} \mathbf {B u} (\tau) d \tau\right)} _ {\mathbf {x} _ {k}} \\ + \int_ {k T} ^ {(k + 1) T} e ^ {\mathbf {A} (k T + T - \tau)} \mathbf {B u} (\tau) d \tau \\ \end{array}
$$

We assume that u is constant during each timestep, so it can be pulled out of the integral.

$$\mathbf {x} _ {k + 1} = e ^ {\mathbf {A} T} \mathbf {x} _ {k} + \left(\int_ {k T} ^ {(k + 1) T} e ^ {\mathbf {A} (k T + T - \tau)} d \tau\right) \mathbf {B u} _ {k}$$
