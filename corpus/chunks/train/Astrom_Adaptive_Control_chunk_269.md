# 5.2 THE MIT RULE

The MIT rule is the original approach to model-reference adaptive control. The name is derived from the fact that it was developed at the Instrumentation Laboratory (now the Draper Laboratory) at MIT.

To present the MIT rule, we will consider a closed-loop system in which the controller has one adjustable parameter $\theta$ . The desired closed-loop response is specified by a model whose output is $y_{m}$ . Let e be the error between the output y of the closed-loop system and the output $y_{m}$ of the model. One possibility is to adjust parameters in such a way that the loss function

$$J (\theta) - \frac {1}{2} e ^ {2} \tag {5.1}$$

is minimized. To make J small, it is reasonable to change the parameters in the direction of the negative gradient of J, that is,

$$\frac {d \theta}{d t} = - \gamma \frac {\partial J}{\partial \theta} = - \gamma e \frac {\partial e}{\partial \theta} \tag {5.2}$$

This is the celebrated MIT rule. The partial derivative $\partial e/\partial\theta$ , which is called the sensitivity derivative of the system, tells how the error is influenced by the adjustable parameter. If it is assumed that the parameter changes are slower than the other variables in the system, then the derivative $\partial e/\partial\theta$ can be evaluated under the assumption that $\theta$ is constant.

There are many alternatives to the loss function given by Eq. (5.1). If it is chosen to be

$$J (\theta) = | e | \tag {5.3}$$

the gradient method gives

$$\frac {d \theta}{d t} = - \gamma \frac {\partial e}{\partial \theta} \text { sign } e \tag {5.4}$$

The first MRAS that was implemented was based on this formula. There are, however, many other possibilities, for example,

$$\frac {d \theta}{d t} = - \gamma \operatorname{sign} \left(\frac {\partial e}{\partial \theta}\right) \operatorname{sign} (e)$$

This is called the sign-sign algorithm. A discrete-time version of this algorithm is used in telecommunications, in which simple implementation and fast computations are required. (See Section 13.2.)

Adjusting many parameters Equation (5.2) also applies when there are many parameters to adjust. The symbol $\theta$ should then be interpreted as a vector and $\partial e/\partial\theta$ as the gradient of the error with respect to the parameters.
