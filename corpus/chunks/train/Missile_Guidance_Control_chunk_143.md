Normally, the boresight error is assumed to be negligible as compared to other system errors. Also, there is a possible contribution of the refraction error to measurement noise, when the frequency of the received signal is varied in a pseudorandom manner in order to reduce the effect of a potential enemy jammer (for example, when the seeker is an active or semiactive radar). This noise can be treated as a contributor to range-independent noise. The various noises (to be discussed in Section 3.4.2) associated with the seeker must also be considered in the design of a missile. As discussed earlier, the LOS angle is the fundamental quantity measured by the seeker. These measurements will generally be corrupted by various types of noise, which can be categorized according to the dependency of their rms (root-mean-square) levels on the missile-to-target range. The actual noise levels and bandwidths are dependent on the exact form of the measurement signal processor, target configuration and characteristics, environmental conditions, and a number of other system effects. In block diagram form, the seeker can be represented as shown in Figure 3.28. It should be pointed out that here we consider a single channel; an actual seeker system will require the implementation of two or three channels in order to account for motion in three dimensions.

![](image/a1cb7e40c85449ad12d436847cd6386596e9e4237a6810b78ace018dc6d9d85e.jpg)

<details>
<summary>line</summary>

| Maximum launch range [ft × 1000] | Altitude [k ft] (R = 0.035) | Altitude [k ft] (R = 0.05) | Altitude [k ft] (R = 0.07) | Altitude [k ft] (R = 0.1) | Altitude [k ft] (R = 0.14) |
| --- | --- | --- | --- | --- | --- |
| 120 | 80 | 70 | 65 | 55 | 50 |
| 160 | 85 | 75 | 70 | 60 | 55 |
| 180 | 90 | 80 | 75 | 65 | 60 |
</details>

Fig. 3.27. Radome error slope (R) limitations on maximum launch range.

Commonly, the stabilization dynamics comprise the gimbal servo and rate gyro, mounted on the antenna. Typically, the stabilization dynamics have a very wide bandwidth, in excess of 100 rad/sec. Moreover, the track loop model can be represented by simple first-order dynamics, commanding a gimbal rate proportional to the measured boresight error. In essence, the loop attempts to drive the boresight error to zero, thereby causing the antenna to track the target [5].
