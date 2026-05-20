$$\dot {\tilde {\boldsymbol {\eta}}} = \tilde {\mathbf {A}} \tilde {\boldsymbol {\eta}} + \tilde {\mathbf {B}} y \tag {10-106}u = \widetilde {\mathbf {C}} \widetilde {\boldsymbol {\eta}} + \widetilde {D} y \tag {10-107}$$

Equations (10–106) and (10–107) define the minimum-order observer-based controller. By considering u as the output and –y as the input, $U ( s )$ can be written as

$$U (s) = \left[ \widetilde {\mathbf {C}} \left(s \mathbf {I} - \widetilde {\mathbf {A}}\right) ^ {- 1} \widetilde {\mathbf {B}} + \widetilde {D} \right] Y (s)= - \left[ \widetilde {\mathbf {C}} (s \mathbf {I} - \widetilde {\mathbf {A}}) ^ {- 1} \widetilde {\mathbf {B}} + \widetilde {D} \right] [ - Y (s) ]$$

Since the input to the observer controller is $- Y ( s )$ , rather than $Y ( s )$ , the transfer function of the observer controller is

$$\frac {U (s)}{- Y (s)} = \frac {\text { num }}{\text { den }} = - \left[ \widetilde {\mathbf {C}} (s \mathbf {I} - \widetilde {\mathbf {A}}) ^ {- 1} \widetilde {\mathbf {B}} + \widetilde {D} \right] \tag {10-108}$$

This transfer function can be easily obtained by using the following MATLAB statement:

$$[ \text { num,den } ] = \text { ss2tf } (\text { Atilde }, \text { Btilde }, - \text { Ctilde }, - \text { Dtilde }) \tag {10-109}$$

In this section we shall consider a problem of designing regulator systems by using the pole-placement-with-observer approach.

Consider the regulator system shown in Figure 10–19. (The reference input is zero.) The plant transfer function is

$$G (s) = \frac {1 0 (s + 2)}{s (s + 4) (s + 6)}$$

Using the pole-placement approach, design a controller such that when the system is subjected to the following initial condition:

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right], \qquad \mathbf {e} (0) = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right]
$$

where x is the state vector for the plant and e is the observer error vector, the maximum undershoot of $y ( t )$ is 25 to 35% and the settling time is about 4 sec. Assume that we use the minimum-order observer. (We assume that only the output y is measurable.)

We shall use the following design procedure:
