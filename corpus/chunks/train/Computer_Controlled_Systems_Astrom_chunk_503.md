# Example 8.4 Modification of a state-feedback controller

The system in Example A.1 is the double integrator; that is, the system is defined by the matrices

$$
A = \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) \quad B = \left( \begin{array}{l} 0 \\ 1 \end{array} \right) \quad \text { and } \quad C = \left( \begin{array}{l l} 1 & 0 \end{array} \right)
$$

Let the continuous-time controller be

$$
u (t) = u _ {c} (t) - \left( \begin{array}{l l} 1 & 1 \end{array} \right) x (t) \tag {8.18}
$$

Figure 8.7 shows the behavior when the sampled controller

$$
u (k h) = u _ {c} (k h) - \left( \begin{array}{l l} 1 & 1 \end{array} \right) x (k h) \tag {8.19}
$$

is used when $h = 0.5$ . Using the modifications in (8.16) and (8.17), we get

$$
\tilde {L} = \left( \begin{array}{l l} 1 - 0. 5 h & 1 \end{array} \right) \tag {8.20}
\tilde {M} = 1 - 0. 5 h
$$

![](image/fb9184fe51e03cd035a1e05928a99f9e0e149b9c70995c10ba7ec337ae321c21.jpg)  
Figure 8.8 Control of the double integrator using the modified controller in (8.20) when h = 0.5 (solid). The continuous-time response when using (8.18) is also shown (dashed).

Figure 8.8 shows the behavior when the modified controller is used for h = 0.5; there is an improvement compared with the unmodified controller. However, the sampling period cannot be increased much further before the closed-loop behavior starts to deteriorate, even when the modified controller is used. The example shows that a simple modification can have a large influence on the performance.
