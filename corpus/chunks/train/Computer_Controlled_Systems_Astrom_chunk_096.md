# 2.3 Sampling a Continuous-Time State-Space System

A fundamental problem is how to describe a continuous-time system connected to a computer via A-D and D-A converters. Consider the system shown in Fig. 2.1. The signals in the computer are the sequences $\{u(t_k)\}$ and $\{y(t_k)\}$ . The key problem is to find the relationship between these sequences. To find the discrete-time equivalent of a continuous-time system is called sampling a continuous-time system. The model obtained is also called a stroboscopic model because it gives a relationship between the system variables at the sampling instants only. To obtain the desired descriptions, it is necessary to describe the converters and the system. Assume that the continuous-time system is given in the following state-space form:

$$\frac {d x}{d t} = A x (t) + B u (t) \tag {2.1}y (t) = C x (t) + D u (t)$$

The system has r inputs, p outputs, and is of order n.
