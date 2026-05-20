# A Few Comments on Lag Compensation.

1. Lag compensators are essentially low-pass filters. Therefore, lag compensation permits a high gain at low frequencies (which improves the steady-state performance) and reduces gain in the higher critical range of frequencies so as to improve the phase margin. Note that in lag compensation we utilize the attenuation characteristic of the lag compensator at high frequencies rather than the phaselag characteristic. (The phase-lag characteristic is of no use for compensation purposes.)

2. Suppose that the zero and pole of a lag compensator are located at $s = - z$ and $s = - p ,$ , respectively. Then the exact locations of the zero and pole are not critical provided that they are close to the origin and the ratio $z / p$ is equal to the required multiplication factor of the static velocity error constant.

It should be noted, however, that the zero and pole of the lag compensator should not be located unnecessarily close to the origin, because the lag compensator will create an additional closed-loop pole in the same region as the zero and pole of the lag compensator.

The closed-loop pole located near the origin gives a very slowly decaying transient response, although its magnitude will become very small because the zero of the lag compensator will almost cancel the effect of this pole. However, the transient response (decay) due to this pole is so slow that the settling time will be adversely affected.

It is also noted that in the system compensated by a lag compensator the transfer function between the plant disturbance and the system error may not involve a zero that is near this pole. Therefore, the transient response to the disturbance input may last very long.

3. The attenuation due to the lag compensator will shift the gain crossover frequency to a lower frequency point where the phase margin is acceptable. Thus, the lag compensator will reduce the bandwidth of the system and will result in slower transient response. [The phase angle curve of $G _ { c } ( j \omega ) G ( j \omega )$ is relatively unchanged near and above the new gain crossover frequency.]
