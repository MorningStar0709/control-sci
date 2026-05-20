# A Thought Experiment

To get some insight into the behavior of the system given by Eq. (5.11), we consider an experiment with the adaptive system such that the equation simplifies considerably. An understanding of the behavior of the system under such circumstances will give us some insight, but it will of course not give the full picture.

Consider the following experiment: Assume that the value of parameter $\theta$ is fixed, that the adaptation mechanism is disconnected, and that a constant input signal $u_{c}$ is applied. The adaptation mechanism is then connected when all signals have settled to steady-state values. The behavior of the parameter is then given by

$$\frac {d \theta}{d t} + \gamma y _ {m} ^ {o} u _ {c} ^ {o} (k G (p) \theta) = \gamma \left(y _ {m} ^ {o}\right) ^ {2} \tag {5.12}$$

which is a linear time-invariant system. This equation is linear with constant coefficients. Its stability is governed by the algebraic equation

$$s + \gamma y _ {m} ^ {o} u _ {c} ^ {o} k G (s) = 0 \tag {5.13}$$

We can immediately conclude that the behavior of the parameter is determined by the quantity

$$\mu = \gamma y _ {m} ^ {o} u _ {c} ^ {o} k \tag {5.14}$$

A picture of how the zeros of Eq. (5.13) vary with parameter $\mu$ is easily obtained by plotting the root locus with respect to the parameter. We can conclude that if Eq. (5.13) has zeros in the right half-plane, then the parameters will diverge even in the very special conditions of the experiment. Intuitively, we may also expect the analysis to approximately describe the case in which the command signal is changing slowly with respect to the dynamics of $G(s)$ .

Equation (5.13) can also be used to determine a suitable value of the adaptation gain, as is illustrated in Example 5.4.
