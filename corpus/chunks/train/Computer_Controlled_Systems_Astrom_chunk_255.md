# More Realistic Disturbance Models

The controller based on a state feedback and an observer is interesting but it is still not very useful in practice. The reason is that the assumption about the disturbances made in Sec. 4.3 has been too simplistic. To generalize the problem it is therefore assumed that the system is described by

$$
\begin{array}{l} \frac {d x}{d t} = A x + B u + v \\ y = C x \\ \end{array}
$$

where v is a disturbance acting on the process. The disturbance v, which typically has much energy at low frequencies, is modeled as

$$
\begin{array}{l} \frac {d w}{d t} = A _ {w} w \\ v = C _ {w} w \\ \end{array}
$$

The matrix $A_{w}$ typically has eigenvalues at the origin or on the imaginary axis. We now introduce the augmented state vector

$$z = \binom{x}{w}$$

The augmented system can be described by

$$
\frac {d}{d t} \binom{x}{w} = \left( \begin{array}{l l} A & C _ {w} \\ 0 & A _ {w} \end{array} \right) \binom{x}{w} + \binom{B}{0} u \tag {4.39}

y = \left( \begin{array}{l l} C & 0 \end{array} \right) \binom{x}{w}
$$

Compare with (4.20). Sampling this system gives the following discrete-time system:

$$
\binom{x (k + 1)}{w (k + 1)} = \left( \begin{array}{c c} \Phi & \Phi_ {x w} \\ 0 & \Phi_ {w} \end{array} \right) \binom{x (k)}{w (k)} + \binom{\Gamma}{0} u (k)

y = \left( \begin{array}{l l} C & 0 \end{array} \right) \binom{x (k)}{w (k)}
$$

The disturbance states w are not reachable from the control signal but the complete state is observable from the output if the system (4.33) is observable. The control law is a linear feedback from all state variables, that is,

$$u (k) = - L \hat {x} (k) - L _ {w} \hat {w} (k) \tag {4.40}$$

where $\hat{x}$ and $\hat{w}$ are obtained from the observer

$$
\binom {\hat {x} (k + 1)} {\hat {w} (k + 1)} = \left( \begin{array}{c c} \Phi & \Phi_ {x w} \\ 0 & \Phi_ {w} \end{array} \right) \binom {\hat {x} (k)} {\hat {w} (k)} + \binom {\Gamma} {0} u (k) + \binom {K} {K _ {w}} \varepsilon (k) \tag {4.41}
$$

and

$$\varepsilon (k) = y (k) - C \hat {x} (k) \tag {4.42}$$

Notice that the state of the observer is composed of estimates of the states of the process and the disturbances and that the control signal contains a feedback from the estimated disturbance state $\hat{w}$ .

The closed-loop system is described by
