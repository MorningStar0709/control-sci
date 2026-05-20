Fig. 7.17. Terrain correlation concept. Originally published in the Proceedings of the IEEE NAECON, 1978, article by M. D. Mobley, “Air launched Cruise Missile (ALCM) Navigation System Development Integration Test,” pages 1248–1254. Reprinted with permission.

For a MAD processor, $C _ { j k }$ is given by the following expression:

$$C _ {j k} = (1 / N) \sum_ {i = 1} ^ {N} | S _ {i j} - R _ {i k} |,$$

where

$$S _ {j} = j \text { th measured profile, }R _ {k} = k \text { th reference profile. }$$

Evaluation of the ambiguity expression may be implemented on a computer. Also, computation of the ambiguity between two profiles requires a model of the measured error distribution.

The terrain correlation (TC) system is required to update the position of the cruise missile inertial navigation system (see also Section 7.4.7). Crosstrack errors in the inertial navigation system (INS) can cause the missile to cross the map at a slightly skewed angle (or to sample data too slow or fast for downtrack velocity errors). This phenomenon increases the noise in the system and therefore reduces its accuracy and correlation probability. The vertical accuracy of the TC update is primarily a function of the bias accuracy of the radar altimeter. For altitude update, the mean of the sensed altitude data is differenced with that of the stored column at the elevation point. Any difference in the column “means” is ascribed as an absolute error in the vertical channel. The TC system combines airborne and ground software, and airborne and ground hardware. It extends from the original gathering of terrain elevation data, say by the DMA (Defense Mapping Agency), to the in-flight updating of the INS by the correlator. Correlation of terrain overflown with stored map data provides navigational updates that support system accuracy. The terrain correlation concept is illustrated in Figure 7.17.
