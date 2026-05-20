# 8.6 RELAY OSCILLATIONS

Since limit cycling under relay feedback is a key idea of relay auto-tuning, it is important to understand why a linear system oscillates under relay feedback and when the oscillation is stable. It is also important to have methods for determining the period and the amplitude of the oscillations. Consider the system shown in Fig. 8.3. Introduce the following state space realization of the transfer function $G(s)$ :

$$\frac {d x}{d t} = A x + B u \tag {8.9}y = C x$$

The relay can be described by

$$
u = \left\{ \begin{array}{l l} d & \text { if } e > 0 \\ - d & \text { if } e <   0 \end{array} \right. \tag {8.10}
$$

where $e = u_{c} - y$ . We have the following result.
