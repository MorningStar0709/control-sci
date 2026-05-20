# 5.11 CONCLUSIONS

The fundamental ideas behind the MRAS have been covered in this chapter, including

- Gradient methods,   
• Lyapunov and passivity design, and   
- Augmented error.

In all cases the rule for updating the parameters is of the form

$$\frac {d \theta}{d t} = \gamma \varphi \varepsilon$$

or, in the normalized form,

$$\frac {d \theta}{d t} = \gamma \frac {\varphi \varepsilon}{\alpha + \varphi^ {T} \varphi}$$

In the gradient method the vector $\varphi$ is the negative gradient of the error with respect to the parameters. Estimation of parameters or approximations may be needed to obtain the gradient. In other cases, $\varphi$ is a regression vector, which is found by filtering inputs, outputs, and command signals. The quantity $\varepsilon$ is the augmented error, which also can be interpreted as the prediction error of the estimation problem. It is customary to use an augmented error that is linear in the parameters.

The gradient method is flexible and simple to apply to any system structure. The calculations required are the determination of the sensitivity derivative. Since the sensitivity derivative cannot be obtained for an unknown process, it is necessary to make several approximations. The initial values of the parameters must be such that the closed-loop system is stable. Empirical evidence indicates that the system is stable for small adaptation gains but that high gains lead to instability. It is difficult to find the bounds. In Chapter 6 we give more insight into the properties of the gradient method.

A general MRAS is derived in Section 5.8 on the basis of the model-following design in Chapter 3. This algorithm includes as special cases many of the MRAS designs given in the literature. The estimation of the parameters can be done in several ways other than those given in Eqs. (5.62) and (5.63). Various modifications are discussed in Chapter 6.
