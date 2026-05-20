# EXAMPLE 5.16 Adaptive feedback linearization

Consider the system

$$\frac {d x _ {1}}{d t} = x _ {2} + \theta f (x _ {1})\frac {d x _ {2}}{d t} = u$$

where $\theta$ is an unknown parameter and f is a known differentiable function. Applying the certainty equivalence principle gives the following control law:

$$u = - a _ {2} x _ {1} - \left(a _ {1} + \hat {\theta} f ^ {\prime} (x _ {1})\right) \left(x _ {2} + \hat {\theta} f (x _ {1})\right) + v \tag {5.88}$$

Introducing this into the system equations gives an error equation that is nonlinear in the parameter error. This makes it very difficult to find a parameter adjustment law that gives a stable system. Therefore it is necessary to use another approach.

Proceeding as in Example 5.15 and introducing the new coordinates

$$\xi_ {1} = x _ {1}\xi_ {2} = x _ {2} + \hat {\theta} f (x _ {1})$$

where $\hat{\theta}$ is an estimate of $\theta$ , we have

$$\frac {d \xi_ {1}}{d t} = \frac {d x _ {1}}{d t} = x _ {2} + \theta f (x _ {1}) = \xi_ {2} + (\theta - \hat {\theta}) f (\xi_ {1})\frac {d \xi_ {2}}{d t} = \frac {d \hat {\theta}}{d t} f (x _ {1}) + \hat {\theta} (x _ {2} + \theta f (x _ {1})) f ^ {\prime} (x _ {1}) + u$$

Choosing the control law to be

$$u = - a _ {2} \xi_ {1} - a _ {1} \xi_ {2} - \hat {\theta} (x _ {2} + \hat {\theta} f (x _ {1})) f ^ {\prime} (x _ {1}) - f (x _ {1}) \frac {d \hat {\theta}}{d t} + v \tag {5.89}$$

we get

$$
\frac {d \xi}{d t} = \left( \begin{array}{c c} 0 & 1 \\ - a _ {2} & - a _ {1} \end{array} \right) \xi + \binom{f (\xi_ {1})}{\hat {\theta} f (\xi_ {1}) f ^ {\prime} (\xi_ {1})} \tilde {\theta} + \binom{0}{1} v
$$

A comparison with the certainty equivalence control law given by Eq. (5.88) shows that the major difference is the presence of the term $d\hat{\theta}/dt$ in Eq. (5.89).

In analogy with the model-reference adaptive system, let us assume that it is desired to have a system in which the transfer function from command signal to output has the transfer function

$$G (s) = \frac {a _ {2}}{s ^ {2} + a _ {1} s + a _ {2}}$$

Introduce the following realization of the transfer function:

$$
\frac {d x _ {m}}{d t} = \left( \begin{array}{c c} 0 & 1 \\ - a _ {2} & - a _ {1} \end{array} \right) x _ {m} + \binom{0}{a _ {2}} u _ {m}
$$

and let $e = \xi - x_{m}$ be the error vector. If we choose

$$v = a _ {2} u _ {m} \tag {5.90}$$

we find that the error equation becomes
