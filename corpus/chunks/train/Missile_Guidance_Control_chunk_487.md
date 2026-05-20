$$\phi = \text { longitude },\lambda = \text { latitude },\lambda_ {O A P} = \text { latitude of } O A P,\phi_ {O A P} = \text { longitude of } O A P,\lambda_ {A / C} = \text { latitude of aircraft from the INS or alternative navigation },\phi_ {A / C} = \text { longitude of aircraft from the INS or alternative navigation },\lambda R _ {A / C} = \text { modified latitude of aircraft },\phi R _ {A / C} = \text { modified longitude of aircraft },R _ {E} = \text { radius of the Earth. }$$

The current aircraft position ${ \bf P } _ { o }$ is computed using $\lambda R _ { A / C }$ and φ $R _ { A / C }$ during the bomb run. If a position update is taken, the tracking handle buffer is set to zero, and $\lambda _ { A / C }$ and $\phi _ { A / C }$ are updated in the autopilot, and as a result, $\Delta \lambda$ and $\Delta \phi$ are zero until the tracking is moved again. The target is used as the destination in the great circle equations.

The manner in which an update to the aircraft position vector ${ \bf P } _ { o }$ is accomplished during a bomb run depends on whether alternative navigation or inertial navigation is used. When using alternative navigation, the direction cosines of the aircraft position vector are

$$C _ {3 1} = \cos \phi \cos \lambda , \tag {5.65a}C _ {3 2} = \sin \phi \cos \lambda , \tag {5.65b}C _ {3 3} = \sin \lambda . \tag {5.65c}$$

These equations are updated relative to the target as follows:

$$C _ {3 1} ^ {\prime} = \cos (\phi - \Delta \phi) \cos (\lambda - \Delta \lambda), \tag {5.66a}C _ {3 2} ^ {\prime} = \sin (\phi - \Delta \phi) \cos (\lambda - \Delta \lambda), \tag {5.66b}C _ {3 3} ^ {\prime} = \sin (\lambda - \Delta \lambda), \tag {5.66c}$$

where $C _ { 3 1 } ^ { \prime } , C _ { 3 2 } ^ { \prime }$ , and $C _ { 3 3 } ^ { \prime }$ are the newer direction cosines that define the aircraft position relative to the target, and $\Delta \lambda$ and $\Delta \phi$ are the relative latitude and longitude increments resulting from a tracking handle correction. With inertial navigation, (5.65a)–(5.65c) are applied. Consequently, ${ \bf P } _ { o }$ is modified to account for radar updates by (5.67a)–(5.67c). Note that

$$\Delta \phi = \Delta E / R _ {E} \cos \lambda ,\Delta \lambda = \Delta N / R _ {E},$$

where

$$\Delta E = \text { easterly component of the update },\Delta N = \text { northerly component of the update. }$$

Then
