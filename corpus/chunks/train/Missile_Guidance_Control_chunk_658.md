$$
[ T _ {b} ] = \left[ \begin{array}{c c c} X _ {x} & X _ {y} & X _ {z} \\ Y _ {x} & Y _ {y} & Y _ {z} \\ Z _ {x} & Z _ {y} & Z _ {z} \end{array} \right],
$$

and the resultant vector in ECI coordinates is

$$
\mathbf {F} _ {E C I} = [ T _ {b} ] \times \left[ \begin{array}{c} F _ {x} \\ F _ {y} \\ F _ {z} \end{array} \right],
$$

where

$$
\begin{array}{c} F _ {E C I} = \text { resultant   vector   in } E C I \\ \text { coordinates }, \end{array}

\begin{array}{c} \mathbf {F} _ {n} = \text { original   vector   in   body - axis } \\ n \text { th   direction. } \end{array}
$$

For the special case where the missile’s velocity components are zero, the rotations are performed using the missile position angles of latitude and longitude, and the orientation angles of azimuth and pitch. The missile is first rotated from its body-axis frame to the ENU frame by a positive rotation about the y-axis of $9 0 ^ { \circ }$ pitch (θ ), and then a negative rotation about the z-axis of $9 0 ^ { \circ }$ azimuth $( \psi )$ . Next, the missile is rotated from the ENU frame to the ECI frame by a negative rotation about the x-axis of $9 0 ^ { \circ }$ latitude (ϕ), and then a negative rotation about the z-axis of $9 0 ^ { \circ }$ longitude (λ). The transformation matrix for performing the pitch rotation about the y-axis is as follows [9]:

$$
\left[ T _ {p} \right] = \left[ \begin{array}{c c c} \sin \theta & 0 & - \cos \theta \\ 0 & 1 & 0 \\ \cos \theta & 0 & \sin \theta \end{array} \right]. \tag {6.250a}
$$

Next, the transformation matrix for performing the azimuth rotation about the z-axis is given by

$$
\left[ T _ {a} \right] = \left[ \begin{array}{c c c} \sin \psi & - \cos \psi & 0 \\ \cos \psi & \sin \psi & 0 \\ 0 & 0 & 1 \end{array} \right]. \tag {6.250b}
$$

The transformation matrix for performing the latitude rotation about the x-axis is given as follows:

$$
\left[ T _ {l a} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \sin \varphi & - \cos \varphi \\ 0 & \cos \varphi & \sin \varphi \end{array} \right]. \tag {6.250c}
$$

Finally, the transformation matrix for performing the longitude rotation about the z-axis is given by

$$
\left[ T _ {l o} \right] = \left[ \begin{array}{c c c} \sin \lambda & - \cos \lambda & 0 \\ \cos \lambda & \sin \lambda & 0 \\ 0 & 0 & 1 \end{array} \right]. \tag {6.250d}
$$

(Note that all angles are given in units of radians.) Using these transformation matrices, the vector is then rotated from the missile body-axis frame to the ECI frame according to the transformation
