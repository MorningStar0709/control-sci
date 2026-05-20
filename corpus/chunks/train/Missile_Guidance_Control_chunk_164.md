1. Noise jamming, which is assumed to be continuous in time (CW ).   
2. Track break jamming, a responsive technique that denies acquisition.   
3. Deceptive countermeasures (DECM), which cause errors in range or angle measurement.

All three types of these jamming models are characterized by the effective radiated power and jammer bandwidth.

Since the effective radiated power includes the jammer’s antenna gain, it is input as a function of the aspect angles (i.e., azimuth and elevation) of the target.

One of the most important parameters affecting the effectiveness of noise jamming is the jam-to-signal or (J /S) ratio. This is the ratio of the power of the noise J to the power of the echo S. Thus, for a jammer with an output power $P _ { j }$ and an antenna gain $G _ { j }$ , the power received by a radar with antenna gain G is given by

$$J = (P _ {j} G _ {j} G \lambda^ {2}) / (4 \pi) ^ {2} R ^ {2} \quad [ \text { watts } ]. \tag {3.100}$$

The skin return is simply given by the radar equation, (3.95); therefore,

$$J / S = (4 \pi P _ {j} G _ {j} R ^ {2}) / P _ {t} G \sigma . \tag {3.101}$$

This equation is sometimes written in the form

$$J / S = [ P _ {j} G _ {j} / P _ {t} G ] [ 4 \pi / \sigma ] [ R ^ {2} ].$$

As with $P _ { r }$ , J can also be written in decibel form as follows:

$$d B J = 1 0 \log_ {1 0} J [ \mathrm{dBw} ].$$

At this point, let us examine the radar range-tracking loop. Typically, tracking radars are closed-loop systems that attempt to keep the selected target centered within the beam scan pattern and provide tracking data to a fire-control system. The primary output of most radar tracking systems is the target location determined by the pointing angles of the antenna beam and the positions of the range-tracking gates [10]. The tracking data is used by a fire-control computer to predict the future position of the target so as to achieve an intercept. In pulsed systems, target range is determined by measuring the time delay between transmission of an RF pulse and the reception of the pulse echo from the target. Range tracking provides an important means of multiple-target discrimination by eliminating signal returns other than those of the intended target. This is accomplished by receiver gating. That is, the receiver-input channel is opened for an interval when a pulse return is expected, and closed the remainder of the time. The range-tracking circuitry is used to keep an open gate centered on the desired target return.
