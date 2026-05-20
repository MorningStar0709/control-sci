$$\frac {d \gamma}{d t} = N \left(\frac {d \sigma}{d t}\right), \tag {7}$$

where N is the navigation constant between the LOS turning rate and the missile velocity vector turning rate. In this example N will be given by

$$N = N ^ {\prime} \left(\frac {d R _ {M T}}{d t}\right) / (V _ {m} \cos (\gamma - \sigma)), \tag {8}$$

where $N ^ { \prime }$ is the effective navigation ratio and may be chosen as required (see also (4.32)). Substituting (8) into (7) leads to the following navigational equation, the combined seeker and autopilot transfer function in the over-all guidance loop:

$$\frac {d \gamma}{d t} = N ^ {\prime} \{N \dot {R} _ {M T} \dot {\sigma} ^ {\prime} / (V _ {M} \cos (\gamma - \sigma)) \}. \tag {9}$$

The primary reason for using the ratio given in (8) is that with it, the dynamic response of the system remains constant no matter what the angle of approach between the missile and target velocity vectors.

The three equations required in closing the loop in Figure 4.27 are (5), representing the geometry; (6), representing the smoothing in the seeker; and (9), representing the navigation ratio. If (6) and (9) are substituted into (5), a closed-loop expression is obtained that expresses the lateral acceleration of the missile $( a _ { M } )$ as a function of the input disturbances $V _ { M } , V _ { T }$ , and $V _ { T } ( d \gamma _ { T } / d t )$ :

$$
\begin{array}{l} a _ {M} = V _ {M} \left(\frac {d \gamma_ {T}}{d t}\right) = \frac {N / (N - 2)}{\left[ \frac {t _ {g} t _ {s}}{N - 2} p ^ {2} + \frac {t _ {g} - 2 t _ {s}}{N - 2} p + 1 \right]} \bigg [ - \dot {V} _ {M} \tan (\gamma - \sigma) \\ \left. + \dot {V} _ {T} \frac {\sin (\sigma - \gamma_ {T})}{\cos (\gamma - \sigma)} + V _ {T} \dot {\theta} _ {T} \frac {\cos (\sigma - \gamma_ {r})}{\cos (\gamma - \sigma)} \right] \tag {10} \\ \end{array}
$$

where $t _ { g }$ (time-to-go until intercept) equals $R _ { M T } / ( d R _ { M T } / d t )$ , and s is the Laplace operator. Several qualitative statements can be made about (10):
