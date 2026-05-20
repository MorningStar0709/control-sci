It should be noted here that in military applications, GPS signal acquisition must be done quickly in a high-jamming environment, using the more precise, harder to jam GPS Y-code. Usually, military GPS receivers first acquire the less-precise CA-code, then search for the Y-signal. In an integrated GPS/INS system, the GPS will pass on position data to update the inertial navigation system. If the GPS is jammed, the navigation computer will rely solely on the INS. Other precisionguided weapons are fed inertial data before launch, then use GPS to update the INS in flight. The phase stability of the GPS receiver’s oscillator also must be high in order to acquire the satellites and accurately track the vehicle’s velocity. Finally, the goal for the use of an integrated GPS/INS system is to bring the price below \$1500.

We conclude this section by noting that the receiver clock drift $\delta _ { t }$ can be represented by the integration of an exponentially correlated random process $x _ { i }$ . Therefore, for the purposes of modeling clock drifts and uncertainties, the equations that describe the clock drifts are as follows [9]:

$$\frac {d x _ {t}}{d t} = - a x _ {t} + w _ {t},\frac {d \delta_ {t}}{d t} = x _ {t},$$

where $w _ { t }$ is a Gaussian white noise, $a = 1 / \tau ( \tau$ is the correlation time), and

$$E \{w (t) w (t + \tau) \} = (2 \sigma_ {x _ {t}} ^ {2} / \tau) \delta (\tau).$$
