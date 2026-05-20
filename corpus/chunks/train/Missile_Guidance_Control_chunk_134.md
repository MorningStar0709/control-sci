# Sources of Miss Distance

(1) Initial heading error.   
(2) Acceleration bias.   
(3) Gyro drifts (if gyros are used in seeker stabilization).   
(4) Glint (scintillation noise).   
(5) Receiver noise.   
(6) Fading noise (except for monopulse).   
(7) Angle noise (due to varying refraction with frequency diversity).

Noise components of miss depend on guidance-system response and thus α/γ˙ and refraction slope R.

2. Preserve stability of the parasitic attitude loop (to be discussed in Section 3.5).

(In maneuvers, missile pitching affects seeker boresight-error measurement.)

3. Filtering.

(1) Limit power consumption and saturation of the actuators.   
(2) Prevent noise from excessive hitting of dynamic-range limits, such as autopilot g-limits.

A more detailed discussion of the above problems is in order. First, in order to maximize the single-shot kill probability, the main problem of the guidance designer is to minimize the miss distance enumerated above under problem 1. The seven sources of miss distance listed above are statistical in nature. Both the alpha over gamma dot of the airframe and the statistically varying radome-refraction slope R affect the speed of response of the guidance system and thereby affect the components of miss due to noise. Evaluation and partial optimization of total rss (root-sum-squares) miss distance can be performed rapidly and efficiently with a digital computer program.

The second major problem of the guidance designer is to preserve the stability of the parasitic attitude loop (for a discussion see Section 3.5). The third problem states that some filtering must be used to limit noise perturbations of the seeker and actuators, so that power consumption, saturation, g-limiting, etc., will not be excessive. A successful guidance design requires a compromise that meets all three major problems listed above.
