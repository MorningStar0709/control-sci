# 7.4.6 TERCOM System Error Sources

TERCOM system errors arise from two basic sources, according to the manner in which they influence the fix accuracy: (1) vertical measurement errors that give erroneous altitude measurements, and (2) horizontal errors that induce vertical errors by causing measurements of terrain elevation to be horizontally displaced from desired location.

The vertical errors are due to [6]:

• Inaccuracies in source data   
• Radar altimeter measurement errors   
• Barometric pressure measurement errors.

The horizontal errors are due to:

Horizontal velocity and skew errors   
• Vertical altitude errors   
• Horizontal quantization (i.e., cell size).

(These sources of degradation can be reduced by (1) choosing suitable terrain for fix taking, and (2) increasing the match length.)

Source data errors arise from digitization errors caused during map generation and loss of double precision in going from 32-bit to 16-bit programming. Foliage and aerial photographs are also error sources. Radar altimeter errors result from signalto-noise ratio (SNR) effects, that is, the error in clearance measurement due to radar altimeter noise and the fluctuating character of the ground return. Typical values for radar altimeter noise effects are less than ±5 ft for state-of-the-art altimeters. Barometric altimeter errors result from sensitivity to angle of attack, dynamic lag in the pressure transducer, and hysteresis errors in the sensing diaphragm. These are reduced by mixing the vertical channel of the INS in a second- or third-order loop. The mixing allows the fast response of the inertial system to give an accurate measure of the vehicle’s short-term altitude changes with the long-term stability of the baro-altimeter used to dampen the inherent long-term stability of the INS’s vertical channel. Quantization is the error associated with quantization of the radar altimeter, barometric altimeter, and map elevations. Quantization can also be defined as the error induced by storing a discrete rather than continuous version of terrain, that is, quantization of the horizontal plane into cells of dimension d (see Figures 7.13 and 7.14 in Section 7.4.3).
