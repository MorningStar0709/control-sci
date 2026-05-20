# Exercise A.29: Observability in continuous time

Consider the linear time-invariant continuous time system

$$\frac {d x}{d t} = A xx (0) = x _ {0} \tag {A.42}y = C x$$

and let $y ( t ; x _ { 0 } )$ represent the solution to (A.42) as a function of time t given starting state value $x _ { 0 }$ at time zero. Consider the output from two different initial conditions $\begin{array} { r l } { { \boldsymbol { y } } ( t ; { \boldsymbol { w } } ) , \quad { \boldsymbol { y } } ( t ; { \boldsymbol { z } } ) } \end{array}$ on the time interval $0 \leq t \leq t _ { 1 }$ with $t _ { 1 } > 0$ .

The system in (A.42) is observable if

$$y (t; w) = y (t; z), \quad 0 \leq t \leq t _ {1} \Rightarrow w = z$$

In other words, if two output measurement trajectories agree, the initial conditions that generated the output trajectories must agree, and hence, the initial condition is unique. This uniqueness of the initial condition allows us to consider building a state estimator to reconstruct $x ( 0 )$ from $y ( t ; x _ { 0 } )$ . After we have found the unique $x ( 0 )$ , solving the model provides the rest of the state trajectory $x ( t )$ . We will see later that this procedure is not the preferred way to build a state estimator; it simply shows that if the system is observable, the goal of state estimation is reasonable.

Show that the system in (A.42) is observable if and only if

$$\operatorname{rank} (\mathcal {O}) = n$$

in which O is, again, the same observability matrix that was defined for discrete time systems 1.37

$$
\mathcal {O} = \left[ \begin{array}{c} C \\ C A \\ \vdots \\ C A ^ {n - 1} \end{array} \right]
$$

Hint: what happens if you differentiate $\gamma ( t ; w ) - \gamma ( t ; z )$ with respect to time? How many times is this function differentiable?
