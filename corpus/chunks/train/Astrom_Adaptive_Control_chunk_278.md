# 5.3 DETERMINATION OF THE ADAPTATION GAIN

In Section 5.2 we found that it was straightforward to obtain an adaptive system by using the MIT rule. The adaptive control laws had one parameter, the adaptation gain $\gamma$ , which had to be chosen by the user. The simulation experiments indicated that the choice of the adaptation gain could be crucial. In this section we will discuss methods for determining the adaptation gain.

Consider the MRAS for adaptation of a feedforward gain in Example 5.1. We thus have a system with the transfer function $kG(s)$ , where $G(s)$ is known and k is an unknown constant. It is assumed that $G(s)$ is stable. We would like to find a feedforward control that gives the transfer function $k_{0}G(s)$ . The system is described by the following equations:

$$y = k G (p) uy _ {m} = k _ {0} G (p) u _ {c}u = \theta u _ {c}e = y - y _ {m}\frac {d \theta}{d t} = - \gamma y _ {m} e$$

where $u_{c}$ is the command signal, $y_{m}$ is the model output, y is the process output, O is the adjustable parameter, and p = d/dt is the differential operator. Elimination of the variables u and y in these equations gives

$$\frac {d \theta}{d t} + \gamma y _ {m} (k G (p) \theta u _ {c}) = \gamma y _ {m} ^ {2} \tag {5.11}$$

This equation is a compact description of the behavior of the parameters that we call the parameter equation. Notice that $y_{m}$ may be considered a known function of time. If $G(s)$ is a rational transfer function, Eq. (5.11) is a linear time-varying ordinary differential equation. Such equations may exhibit very complicated behavior. It is not possible to give a simple analytical characterization of the properties of the system, particularly how they are influenced by the parameter $\gamma$ .
