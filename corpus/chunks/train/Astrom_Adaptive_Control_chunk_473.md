To avoid the problem of shift in equilibria, the following modification has

also been suggested;

$$\frac {d \hat {\theta}}{d t} = \gamma \frac {\varphi e}{\alpha + \varphi^ {T} \varphi} + \alpha_ {1} | e | (\theta^ {0} - \hat {\theta}) \tag {6.85}$$

A third way to avoid the difficulty is to switch off the parameter estimation if the input signal is not appropriate. There are several ways to determine when the estimates should be switched off. A simple way is to update only when the error is large, that is, to introduce a dead zone in the estimator. Such an approach is discussed below. However, it is necessary to have prior knowledge to select the dead zone.

It has also been suggested that the width of the dead zone be varied adaptively. From the equilibrium analysis it appears more appropriate to use a criterion based on persistent excitation. An alternative to switching off the estimate is to introduce intentional perturbation signals so as to ensure a proper amount of excitation.
