# 3.4.3 Radar Target Tracking Signal

For missiles using radar as the target tracking sensor, the signal-to-noise ratio (SNR) and power requirements play an important role in the proper design of a guidance system. For example, in surface-to-air missiles (SAMs), the target’s radar return signal strength is used for three purposes: (1) unless the SNR is above a given threshold, the missile will not be fired by the SAM system; (2) if the SNR drops below a given threshold, the target track will be lost by the system; this will result in a cessation of missile guidance; and (3) in an electronic countermeasures (ECM) environment, the SNR will be compared to the jammer-to-signal ratio $( J / S )$ in simulations utilizing jammers to determine whether jamming is effective. Based on the discussion of Section 3.4.2, the radar sensor tracking errors of concern are the following:

(1) Target glint.   
(2) Instrumentation.   
(3) Thermal noise.   
(4) Ground clutter.   
(5) Multipath.

(6) Knife edge diffraction: In many low-angle tracking cases, there is a hill or tree line that masks the target at long range and that blocks the paths to the specular reflection point and to much of the diffuse glistening surface. Reflected multipath is then replaced by a diffraction component arriving from the top of the mask.

Each of these errors affects both the target elevation and target azimuth angle measurement channels. The instrumentation errors can be modeled as a fixed value nominally set at 0.5 mils and distributed about the true target elevation and azimuth angles with a Gaussian distribution standard deviation of 0.0005 mils.
