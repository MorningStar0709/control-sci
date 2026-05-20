# 6.9.3 Gravity feedforward

Input voltage is proportional to force and gravity is a constant force, so a constant voltage feedforward can compensate for gravity. We’ll model gravity as an acceleration disturbance −g. To compensate for it, we want to find a voltage that is equal and opposite to it. The bottom row of the continuous elevator model contains the acceleration terms.

$$B u _ {f f} = - (\text { unmodeled dynamics })$$

where B is the motor acceleration term from B and $u _ { f f }$ is the voltage feedforward.

$$B u _ {f f} = - (- g)B u _ {f f} = g\frac {G K _ {t}}{R r m} u _ {f f} = gu _ {f f} = \frac {R r m g}{G K _ {t}}$$
