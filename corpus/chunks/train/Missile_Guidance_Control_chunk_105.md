\left[ \begin{array}{l} \dot {u} \\ \dot {v} \\ \dot {w} \end{array} \right] = \left[ \begin{array}{l} X / m \\ Y / m \\ Z / m \end{array} \right] - \left[ \begin{array}{c c c} 0 & - R & Q \\ R & 0 & - P \\ - Q & P & 0 \end{array} \right] \left[ \begin{array}{l} u \\ v \\ w \end{array} \right], \tag {3}

\left[ \begin{array}{l} \dot {P} \\ \dot {Q} \\ \dot {R} \end{array} \right] = [ I ] ^ {- 1} \left[ \left[ \begin{array}{c} L \\ M \\ N \end{array} \right] - \left[ \begin{array}{c c c} 0 & - R & Q \\ R & 0 & - P \\ - Q & P & 0 \end{array} \right] [ I ] \left[ \begin{array}{c} P \\ Q \\ R \end{array} \right] \right], \tag {4}
$$

where

$$
c = \cos ,s = \sin ,t = \tan ,m = \text { mass of the missile },L = \text { rolling moment },M = \text { pitching moment, }N = \text { yawing moment },P = \text { roll rate },Q = \text { pitch rate },R = \text { yaw rate },\phi = \text { roll angle },\theta = \text { pitch angle },\psi = \text { yaw angle },
\begin{array}{c} u, v, w = \text { components   of   velocity   of   the   center   of   mass } \\ \text { relative   to   the   atmosphere. } \end{array}
$$

The total applied force is composed of the weight W and body aerodynamic force A terms. The weight portion of the external loads is given by

$$
\left[ \begin{array}{l} X _ {W} \\ Y _ {W} \\ Z _ {W} \end{array} \right] = m g \left[ \begin{array}{l} - s _ {\theta} \\ s _ {\phi} c _ {\theta} \\ c _ {\phi} c _ {\theta} \end{array} \right], \tag {5}
$$

where g is the gravitational acceleration. The aerodynamic force contribution is given by

$$
\left[ \begin{array}{c} X _ {A} \\ Y _ {A} \\ Z _ {A} \end{array} \right] = - q _ {\alpha} \left[ \begin{array}{c} C _ {X O} + (\alpha^ {2} + \beta^ {2}) \\ C _ {N A} \beta \\ C _ {N A} \alpha \end{array} \right], \tag {6}
$$

where

$$\alpha = \tan^ {- 1} (w / v), - \pi \leq \alpha \leq \pi , \tag {7a}\beta = \tan^ {- 1} (v / u), - \pi \leq \alpha \leq \pi , \tag {7b}q _ {a} = \frac {1}{8} \rho (u ^ {2} + v ^ {2} + w ^ {2}) \pi D ^ {2}, \tag {8}$$
