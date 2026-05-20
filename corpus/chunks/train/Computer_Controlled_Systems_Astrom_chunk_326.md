# Validation

After a controller is obtained it is important to investigate the closed-loop system obtained to determine if it satisfies all requirements. To do this we must investigate the response to command signals and disturbances and the sensitivity to modeling errors.

In the nominal case when the process model is correct it follows from Eq. (5.33) and (5.45) that the response of the closed-loop system obtained by Algorithm 5.3 is given by

$$x = \frac {B _ {m}}{A _ {m}} u _ {c} + \frac {B R _ {d} \bar {R}}{A ^ {+} A _ {c l}} v - \frac {B ^ {-} S _ {d} \bar {S}}{A _ {c l}} ey = \frac {B _ {m}}{A _ {m}} u _ {c} + \frac {B R _ {d} \bar {R}}{A ^ {+} \bar {A} _ {c l}} v + \frac {A ^ {-} R _ {d} \bar {R}}{\bar {A} _ {c l}} e \tag {5.51}u = \frac {A B _ {m}}{B A _ {m}} u _ {c} - \frac {B ^ {-} S _ {d} \bar {S}}{\bar {A} _ {c l}} v - \frac {A S _ {d} \bar {S}}{B ^ {+} \bar {A} _ {c l}} e$$

Notice that these responses are completely characterised by six pulse-transfer functions. The properties of the system can be illustrated by time or frequency responses. To get a proper assessment of the system it is important to investigate the responses of all signals to all inputs.

Consider, for example, the response to command signals. If there are no disturbances it follows from Eq. (5.51) that

$$u = \frac {H _ {m}}{H} u _ {c} \tag {5.52}$$

This equation gives the control signals for a desired command signal. Notice that the ratio $H_{m}/H$ also appeared in the robustness analysis. Compare this with Figure 5.6. The fact that very large control signals are required for a given command signal is thus a very good indication that the system is highly sensitive to modeling errors.

To judge the sensitivity to modeling errors it is useful to compute tha

loop-transfer function

$$L = \frac {B S}{A R} = \frac {B ^ {-} S _ {d} \bar {S}}{A ^ {-} R _ {d} \bar {R}} \tag {5.53}$$

and to evaluate amplitude and phase margins and crossover frequencies. It is also useful to investigate the sensitivity function

$$S = \frac {1}{1 + L} = \frac {A R}{A R + B S} = \frac {A ^ {-} R _ {d} \dot {R}}{\bar {A} _ {c l}} \tag {5.54}$$
