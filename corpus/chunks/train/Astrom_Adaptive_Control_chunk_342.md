# 5.8 OUTPUT FEEDBACK

We now derive an MRAS for adjusting the parameters of a controller based on output feedback in a fairly general case. A process with one input and one output is considered. It is assumed that the dynamics are linear and that the control problem is formulated as model-following. The key assumption is that the controller can be parameterized in such a way that the error is linear in the controller parameters. The derivation of the MRAS is described as follows:

Step 1: Find a controller structure that admits perfect output tracking.

Step 2: Derive an error model of the form

$$\varepsilon = G _ {1} (p) \left\{\varphi^ {T} (t) (\theta^ {0} - \theta) \right\} \tag {5.61}$$

where $G_{1}$ is a strictly positive real transfer function, $\theta^{0}$ is the process parameters, and $\theta$ is the controller parameters. The right-hand side should be expressed in computable quantities.

Step 3: Use the parameter adjustment law

$$\frac {d \theta}{d t} = \gamma \varphi \varepsilon \tag {5.62}$$

or the normalized law

$$\frac {d \theta}{d t} = \gamma \frac {\varphi \varepsilon}{\alpha + \varphi^ {T} \varphi} \tag {5.63}$$

Notice that the error $\varepsilon$ in Eq. (5.61) is linear in the parameters, a condition that imposes restrictions on the models and controllers that can be dealt with. A model of the form (5.61) is typically obtained by algebraic manipulations, filtering, and error augmentation.

We now show one way to apply the design procedure.
