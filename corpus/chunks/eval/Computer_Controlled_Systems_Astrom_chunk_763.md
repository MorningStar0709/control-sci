# Disturbance Reduction

The return difference is

$$H _ {r d} = 1 + \mathcal {L} = 1 + \frac {B S}{A R} = \frac {A R + B S}{A R}$$

The inverse of the return difference is a measure of how effectively the closed-loop system eliminates disturbances.

Consider the model of (12.70). Without control the output is

$$y _ {o l} = \frac {C}{A} e$$

With the LQG-control law, the output becomes

$$y _ {l q g} = \frac {R}{P} e$$

Elimination of e between these equations gives

$$y _ {l q g} = \frac {A R}{P C} y _ {o l} = \frac {1}{\frac {P C}{A R}} y _ {o l} = \frac {1}{1 + \frac {B S}{A R}} y _ {o l} = \frac {1}{H _ {r d}} y _ {o l} = S y _ {o l}$$

The sensitivity function thus tells how much disturbances of different frequencies are attenuated.
