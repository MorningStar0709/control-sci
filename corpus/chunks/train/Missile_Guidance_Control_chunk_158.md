$$\boldsymbol {R a n g e} = \left(\left| \mathbf {R} _ {T S} \right| + \left| \mathbf {R} _ {T S P} \right| + \left| \mathbf {R} _ {S P S} \right|\right) / 2,$$

where ${ \pmb R } _ { T S }$ is the target-to-site vector, ${ \pmb R } _ { T S P }$ is the target-to-specular-point vector, and $\pmb { R } _ { S P S }$ is the specular-point-to-site vector. The diffuse multipath, which is a random scattering of the radar energy from rough surfaces, can be implemented using Monte Carlo techniques. Clutter, which is the radar energy return that has been backscattered from the terrain surrounding the target, provides a competition signal to the target return depending on the following: (a) general terrain type, (b) depression angle, (c) geometry, (d) surface roughness, and (e) radar characteristics. Specifically, the term clutter can be defined as any undesired radar echo, and is descriptive of the fact that such echoes can “clutter” the radar output and make detection of targets difficult. Reflectivity, a term associated with clutter, refers to the intensity of the reflection from clutter and is typically denoted by $\sigma _ { 0 }$ (also termed the incremental backscattering coefficient). It is the cross-section per unit area:

$$\sigma_ {0} = \sigma_ {c} / A _ {c},$$

where $\sigma _ { c }$ is the radar cross section (RCS) from the area $A _ { c }$ . Reflectivity $\sigma _ { 0 }$ varies with the angle of incidence, frequency, and polarization of the transmitted wave, electrical characteristics of the surface, and roughness of the terrain. It is commonly expressed in dB $( m ^ { 2 } / m ^ { 2 } )$ . The power received from a clutter patch with RCS $\sigma _ { c }$ is [10]

$$P _ {c} = P _ {t} G _ {t} ^ {2} \sigma_ {c} \lambda^ {2} F _ {c} ^ {4} / (4 \pi) ^ {3} R ^ {4} L _ {c},$$

where

$$P _ {t} = \text { transmitted power },G _ {t} = \text { antenna gain },R = \text { target slant range },F _ {c} ^ {4} = \text { clutter pattern propagation factor },L _ {c} = \text { clutter transmission and beamshape losses }.$$
