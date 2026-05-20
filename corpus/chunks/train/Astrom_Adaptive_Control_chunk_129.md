# EXAMPLE 2.17 Prior information in continuous time

Consider the continuous-time system with the transfer function

$$G (s) = \frac {\theta_ {3}}{(1 + \theta_ {1} s) (1 + \theta_ {2} s)}$$

The parameter $\theta_{1}$ is assumed to be known; $\theta_{2}$ and $\theta_{3}$ are unknown. If we introduce the filtered signal $\tilde{u}$ defined by

$$\bar {u} = \frac {1}{1 + \theta_ {1} p} u$$

the input-output relation may be written as

$$y + \theta_ {2} \frac {d y}{d t} = \theta_ {3} \bar {u} \tag {2.55}$$

The estimation problem thus reduces to estimation of parameters $\theta_{3}$ and $\theta_{2}$ of the first-order system given by Eq. (2.55). ☐

The example thus shows that it is straightforward to handle prior information for the continuous-time model. The next example illustrates some complications that occur when the model is sampled.
