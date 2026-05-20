# State-Space Models

The concept of state has its roots in cause-and-effect relationships in classical mechanics. The motion of a system of particles is uniquely determined for all future times by the present positions and moments of the particles and the future forces. How the present positions and moments were achieved is not important. The state is an abstraction of this property; it is the minimal information about the history of a system required to predict its future motion.

For stochastic systems, it cannot be required that the future motion be determined exactly. A natural extension of the notion of state for stochastic systems is to require that the probability distribution of future states be uniquely given by the current state. Stochastic processes with this property are called Markov processes. Markov processes are thus the stochastic equivalents of state-space models. They are formally defined as follows.

DEFINITION 10.1 MARKOV PROCESS Let $t_t$ and $t$ be elements of the index set $T$ such that $t_1 < t_2 < \ldots < t_n < t$ . A stochastic process $\{x(t), t \in T\}$ is called a Markov process if

$$P \{x (t) \leq \xi | x (t _ {1}), \dots , x (t _ {n}) \} = P \{x (t) \leq \xi | x (t _ {n}) \}$$

where $P\{\cdot, x(t_1), \ldots, x(t_n)\}$ denotes the conditional probability given $x(t_1), \ldots, x(t_n)$ .

A Markov process is completely determined by the initial probability distribution

$$F (\xi ; t _ {0}) = P \{x (t _ {0}) \leq \xi \}$$

and the transition probability distribution

$$F (\xi_ {t}; t \mid \xi_ {s}; s) = P \{x (t) \leq \xi_ {t} \mid x (s) = \xi_ {s} \}$$

All finite-dimensional distributions can then be generated from these distributions using the multiplication rule for conditional probabilities.

The Markov process is the natural concept to use when extending the notion of state model to the stochastic case.

Linear stochastic-difference equations. Consider a discrete-time system where the sampling period is chosen as the time unit. Let the state at time k be given by $x(k)$ . The probability distribution of the state at time $k + 1$ is then a function of $x(k)$ . If the mean value is linear in $x(k)$ and the distribution around the mean is independent of $x(k)$ , then $x(k + 1)$ can be represented as

$$x (k + 1) = \Phi x (k) + v (k) \tag {10.7}$$
