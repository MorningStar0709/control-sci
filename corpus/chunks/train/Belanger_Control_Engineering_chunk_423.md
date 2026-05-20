# 7.6.2 A Naive Observer

We begin with the LTI system:

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}. \tag {7.54}$$

We might think of estimating the state $\mathbf{x}(t)$ by running a model in parallel with the system, driven by the system input. Let this be represented by

$$\widehat {\mathbf {x}} = A \widehat {\mathbf {x}} + B \mathbf {u}. \tag {7.55}$$

Here, $\widehat{\mathbf{x}}(t)$ (read "x hat") is presumed to track $\mathbf{x}(t)$ .

Define the estimation error $\widetilde{\mathbf{x}}$ (read "x tilde") to be

$$\widetilde {\mathbf {x}} (t) = \mathbf {x} (t) - \widehat {\mathbf {x}} (t). \tag {7.56}$$

Differentiation yields

$$
\begin{array}{l} \dot {\tilde {\mathbf {x}}} = \dot {\mathbf {x}} - \dot {\hat {\mathbf {x}}} \\ = A \mathbf {x} + B \mathbf {u} - A \widehat {\mathbf {x}} - B \mathbf {u} \\ = A (\mathbf {x} - \widehat {\mathbf {x}}) \\ \end{array}
$$

or

$$\widetilde {\mathbf {x}} = A \widetilde {\mathbf {x}}. \tag {7.57}$$

The solution to Equation 7.57 is

$$\widetilde {\mathbf {x}} (t) = e ^ {A t} \widetilde {\mathbf {x}} (0). \tag {7.58}$$

If the system is stable, $\widetilde{\mathbf{x}}(t) \to 0$ and the estimate $\widehat{\mathbf{x}}(t)$ will asymptotically track the state $\mathbf{x}(t)$ . If the system is unstable, the error $\widetilde{\mathbf{x}}(t)$ will not go to zero—unless we are so fortunate as to have an initial error $\widetilde{\mathbf{x}}(0)$ that excites only stable modes. Even if the system is stable,

Even if the system is stable, this observer leaves much to be desired; for one thing, we have no control of the error dynamics, because we do not choose $A$ . Furthermore, if $A$ and $B$ are not precisely known, the system state $\mathbf{x}$ and the estimate $\widetilde{\mathbf{x}}$ will not track each other.
