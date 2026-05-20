# PROBLEMS

7.1 Discuss possible difficulties of extending the problem given in Section 7.3 to the case in which the system in Eq. (7.1) has an additional time delay.   
7.2 Show that the cautious controller of Eq. (7.15) minimizes the loss function of Eq. (7.14) and that the minimum value of the loss function is Eq. (7.16).   
7.3 Consider the process in Example 7.2, but with a constant but unknown gain $b$ . Calculate and compare the minimum values of the loss function when   
(a) the parameter $b$ is known (i.e., the minimum-variance controller),   
(b) the certainty equivalence controller is used,   
(c) the cautious controller is used.   
7.4 Compute the suboptimal control law that minimizes the loss function of Eq. (7.21). (Hint: See Goodwin and Payne (1977), p. 296.)   
7.5 Compute the suboptimal control law that minimizes the loss function of Eq. (7.22). (Hint: See Milito et al. (1982).)   
7.6 Assume that the process is described by one of the known models

$$y (t) = \varphi (t) \theta_ {i} + e (t) \quad i = 1, \dots , m$$

but it is not known which is the correct one. Let the initial information be described by the probabilities $p_{i} = \mathrm{P}(\theta = \theta_{i})$ . Formulate the dual control problem and discuss the computational difficulties associated with the solution.

7.7 Discuss the consequences of formulating the dual control problem for the model

$$x (t + 1) = \Phi (t) x (t) + \Gamma (t) u (t)y (t) = C (t) x (t) + e (t)$$

where $\Phi, \Gamma$ , and $C$ contain some unknown parameters. For simplicity, consider the case in which the system is given in controllable canonical form, that is,

$$
\Phi (t) = \left( \begin{array}{c c c c} - a _ {1} (t) & - a _ {2} (t) & \dots & - a _ {n} (t) \\ 1 & 0 & \dots & 0 \\ \vdots & \ddots & & \vdots \\ 0 & \dots & 1 & 0 \end{array} \right)

\Gamma^ {T} (t) = \left( \begin{array}{c c c} b _ {0} (t) & \dots & b _ {n - 1} (t) \end{array} \right)

C (t) = \left( \begin{array}{l l l l} 1 & 0 & \dots & 0 \end{array} \right)
$$
