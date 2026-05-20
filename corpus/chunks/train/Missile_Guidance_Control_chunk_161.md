and radiates it isotropically, so that the power density at the receiving antenna (which for simplicity is assumed to be collocated with the transmitting antenna) is [10]

$$\text { Power density } = P _ {t} G _ {t} \sigma / (4 \pi) ^ {2} R ^ {4} [ \mathrm{watts} / \mathrm{m} ^ {2} ]. \tag {3.93}$$

The power received by the radar antenna is simply the power density at the antenna, multiplied by the effective capture area $A _ { c }$ of the antenna, but it is usually more convenient to work with antenna gain, where the gain and capture area are given by

$$A _ {c} = G _ {r} \lambda^ {2} / (4 \pi) [ \mathrm{m} ^ {2} ], \tag {3.94}$$

where λ is the signal wavelength in meters.

Finally, if we assume that the same antenna is used for both transmission and reception, so that $G _ { t } = G _ { r } = G$ , then the received power $P _ { r }$ is [10]

$$P _ {r} = (P _ {t} G ^ {2} \lambda^ {2} \sigma) / (4 \pi) ^ {3} R ^ {4} \quad [ \text { watts } ], \tag {3.95}$$

where all the symbols have been defined. This is the simplest, most basic, radar equation. However, this equation ignores a number of effects that can be critical in detailed radar performance analysis. Nevertheless, it is invaluable for rough performance calculations. Equation (3.95) is sometimes presented in decibel form as follows:

$$\mathrm{dBP} _ {r} = 1 0 \log_ {1 0} P _ {r} [ \mathrm{dBw} ].$$

For detection range estimates, it is convenient to rewrite the radar equation in a slightly different form. Specifically, in the simple case of detection of a target in receiver noise, a required minimum SNR can be defined based on required detection probability, target statistics, and radar characteristics. However, because receiver noise can be considered to be a constant, the minimum SNR defines the maximum detection range by defining a minimum level of received signal, $P _ { m i n }$ , that can be tolerated. Therefore, the maximum detection range is given by

$$R _ {m a x} = \left[ P _ {t} G ^ {2} \lambda^ {2} \sigma / (4 \pi) ^ {3} P _ {\min} \right] ^ {1 / 4} [ \mathrm{m} ]. \tag {3.96}$$

The target radar cross-section (σ ) coordinate system is commonly site oriented with zero azimuth defined at the tail of an aircraft (the target) and $1 8 0 ^ { \circ }$ at the nose. Next, we note that in many systems, $G _ { t } = G _ { r }$ , since the same antenna is used for both transmitting and receiving. Equation (3.91) is sometimes presented in decibel form as follows:

$$\mathrm{dBS} = 1 0 \log_ {1 0} S [ \mathrm{dBw} ].$$
