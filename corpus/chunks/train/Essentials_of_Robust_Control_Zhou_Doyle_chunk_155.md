# 6.4 Bode’s Gain and Phase Relation

One important problem that arises frequently is concerned with the level of performance that can be achieved in feedback design. It has been shown in Section 6.1 that the feedback design goals are inherently conflicting, and a tradeoff must be performed among different design objectives. It is also known that the fundamental requirements, such as stability and robustness, impose inherent limitations on the feedback properties irrespective of design methods, and the design limitations become more severe in the presence of right-half plane zeros and poles in the open-loop transfer function.

In the classical feedback theory, Bode’s gain-phase integral relation (see Bode [1945]) has been used as an important tool to express design constraints in scalar systems. This integral relation says that the phase of a stable and minimum phase transfer function is determined uniquely by the magnitude of the transfer function. More precisely, let $L ( s )$ be a stable and minimum phase transfer function: then

$$\angle L (j \omega_ {0}) = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {d \ln | L |}{d \nu} \ln \coth \frac {| \nu |}{2} d \nu \tag {6.11}$$

where $\nu : = \ln ( \omega / \omega _ { 0 } )$ . The function ln coth ${ \frac { | \nu | } { 2 } } = \ln { \frac { e ^ { | \nu | / 2 } + e ^ { - | \nu | / 2 } } { e ^ { | \nu | / 2 } - e ^ { - | \nu | / 2 } } }$ is plotted in Figure 6.9.

Note that ln coth $\frac { | \nu | } { 2 }$ decreases rapidly as ω deviates from $\omega _ { 0 }$ and hence the integral depends mostly on the behavior of $\frac { d \ln | L ( j \omega ) | } { d \nu }$ dν near the frequency $\omega _ { 0 }$ . This is clear from the following integration:

$$
\frac {1}{\pi} \int_ {- \alpha} ^ {\alpha} \ln \coth \frac {| \nu |}{2} d \nu = \left\{ \begin{array}{l l} 1. 1 4 0 6 (\mathrm{rad}), & \alpha = \ln 3 \\ 1. 3 1 4 6 (\mathrm{rad}), & \alpha = \ln 5 \\ 1. 4 4 3 (\mathrm{rad}), & \alpha = \ln 1 0 \end{array} \right. = \left\{ \begin{array}{l l} 6 5. 3 ^ {\circ}, & \alpha = \ln 3 \\ 7 5. 3 ^ {\circ}, & \alpha = \ln 5 \\ 8 2. 7 ^ {\circ}, & \alpha = \ln 1 0. \end{array} \right.
$$

![](image/35ee0cc0ab0200576e7dd5e08b4d64e83a1654dc1df8355fbe929b6bdf8c35df.jpg)  
Figure 6.9: The function ln coth $\frac { | \nu | } { 2 }$ vs ν
