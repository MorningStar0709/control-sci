# 6.4.2 The Spherical Hit Equation

From the discussion of Sections 6.2 and 6.3, we note that there are many trajectories that can be formed from the equation of an ellipse (e.g., (6.2)). It is now necessary to determine which of the many possible trajectories will actually impact at some predetermined target. Specifically, we will develop the equation for the velocity required to impact a target, and the hit equation, which is an equation that expresses the relation among the burnout parameters ri, Vi, and $\gamma _ { i }$ . Let us now return to (6.9a) and (6.9b):

$$\frac {d ^ {2} r}{d t ^ {2}} - \left(\frac {d \theta}{d t}\right) ^ {2} r = - \mu / r ^ {2}, \tag {6.9a}$$

![](image/811cbd27376e5b6a566eccfa217d243693db995672b5e9121f44fe3bfbe2c3d6.jpg)

<details>
<summary>text_image</summary>

Ballistic (or free fall)
trajectory
Local vertical
V_V
V_R
γ
V_H
h
R
T
θ
r_i = r_e + h
r_e
φ
r_t
0
Center of mass
of the Earth
</details>

Fig. 6.11. Planar geometry for a typical ballistic trajectory.

$$\left(\frac {d}{d t}\right) \left[ r ^ {2} \left(\frac {d \theta}{d t}\right) \right] = 0. \tag {6.9b}$$

As stated in Section 6.2, equation (6.9b) expresses the conservation of angular momentum h for the motion of the vehicle in a central force field. Now, integrating (6.9b), we obtain (6.25), that is,

$$r ^ {2} \left(\frac {d \theta}{d t}\right) = h = r _ {i} V _ {i} \sin \gamma_ {i}. \tag {6.25}$$

Note that here in (6.25) we use sin γ instead of cos γ because the flight path angle γ has been defined differently; that is, here we measure γ from the local vertical instead of from the horizontal.

The geometry used to describe the elliptical free flight path of the vehicle is shown in Figure 6.11. Here note that r and θ are the in-plane polar coordinates, γ the burnout flight path angle, $\phi$ the in-plane range angle, $r _ { e }$ the equatorial radius of the Earth (we assume here a spherical Earth), V the in-plane burnout velocity of the vehicle, R the great circle linear range, $r _ { t }$ the distance from the center of the mass of the Earth to the target, and h the burnout altitude of the vehicle. Then, the burnout radius is $r _ { i } = r _ { e } + h$ (note that here h is the height above the Earth, and should not be confused with the definition of the angular momentum).

The angular momentum integral given by (6.25) allows us, as before, to express time derivatives in terms of θ derivatives. Thus,
