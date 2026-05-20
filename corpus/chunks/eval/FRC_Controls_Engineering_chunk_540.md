$$s \omega + \frac {K _ {t} K _ {d} s}{J R} \omega + \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t} K _ {p}}{J R} \omega = \frac {K _ {t} K _ {p}}{J R} \omega_ {\text {goal}} + \frac {K _ {t} K _ {d} s}{J R} \omega_ {\text {goal}}\left(s + \frac {K _ {t} K _ {d} s}{J R} + \frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}\right) \omega = \left(\frac {K _ {t} K _ {p}}{J R} + \frac {K _ {t} K _ {d} s}{J R}\right) \omega_ {g o a l}\left(s \left(1 + \frac {K _ {t} K _ {d}}{J R}\right) + \frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}\right) \omega = \frac {K _ {t}}{J R} \left(K _ {p} + K _ {d} s\right) \omega_ {g o a l}$$

Solve for $\frac { \omega } { \omega _ { g o a l } }$ .

$$\frac {\omega}{\omega_ {g o a l}} = \frac {\frac {K _ {t}}{J R} (K _ {p} + K _ {d} s)}{s (1 + \frac {K _ {t} K _ {d}}{J R}) + \frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}}$$

So, we added a zero at $- \frac { K _ { p } } { K _ { d } }$ and moved our pole to $- \frac { \frac { K _ { t } } { J R K _ { v } } + \frac { K _ { t } K _ { p } } { J R } } { 1 + \frac { K _ { t } K _ { d } } { J R } }$ . This isn’t progress. We’ve added more complexity to our system and, practically speaking, gotten nothing good in return. Zeroes should be avoided if at all possible because they amplify unwanted high frequency modes of the system and are noisier the faster the system is sampled. At least this is a stable zero, but it’s still undesirable.

In summary, derivative doesn’t help on an ideal flywheel. $K _ { d }$ may compensate for unmodeled dynamics such as accelerating projectiles slowing the flywheel down, but that effect may also increase recovery time; $K _ { d }$ drives the acceleration to zero in the undesired case of negative acceleration as well as well as the actually desired case of positive acceleration.

Subsection 6.7.2 covers a superior compensation method that avoids zeroes in the controller, doesn’t act against the desired control action, and facilitates better tracking.
