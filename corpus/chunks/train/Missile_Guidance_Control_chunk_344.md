The missile lead angle and target aspect angle define the orientation of the respective missile and target velocity vectors relative to the original LOS. The heading error $\theta _ { h e }$ is the angular error in the collision-course triangle defined at the initiation of the terminal phase. For a given target aspect angle, the collision-course missile lead angle is given by

$$\theta_ {l c} = \sin^ {- 1} [ (v _ {T} / v _ {M}) \sin \theta_ {a} ], \tag {4.147}$$

where $\theta _ { h e } = \theta _ { l c } - \theta _ { l }$ . From (4.147) we note that if the orientation and magnitude of the velocity vectors were to remain fixed for the remainder of the terminal phase, the two vehicles would collide. However, it should be pointed out that it is not possible to achieve the collision-course lead angle. For missile systems having a midcourse guidance phase preceding the terminal phase, the heading error tends to be small (i.e., having an rms (root mean square) value of a few degrees or less).

Before we develop the optimal guidance law, certain relationships will be defined. Referring to Figure 4.33, we note first of all that the LOS angle λ is given by

$$\lambda = \tan^ {- 1} (y _ {d} / x _ {T M}), \tag {4.148}$$

![](image/5e4b76ce11f628294cc7a53239e20f9a928c460ce7c8f2d4ad0c64303e2b7a85.jpg)

<details>
<summary>line</summary>

| t[sec] | a_T[ft/sec²] |
| --- | --- |
| 0 | β |
| 1 | -β |
| 2 | -β |
| 3 | β |
| 4 | -β |
| 5 | β |
| 6 | -β |
| 7 | β |
| 8 | -β |
| 9 | β |
| 10 | -β |
| 11 | β |
| 12 | -β |
| 13 | β |
| 14 | -β |
| 15 | β |
| 16 | -β |
| 17 | β |
| 18 | -β |
| 19 | β |
| 20 | -β |
| 21 | β |
| 22 | -β |
| 23 | β |
| 24 | -β |
| 25 | β |
| 26 | -β |
| 27 | β |
| 28 | -β |
| 29 | β |
| 30 | -β |
| 31 | β |
| 32 | -β |
| 33 | β |
| 34 | -β |
| 35 | β |
| 36 | -β |
| 37 | β |
| 38 | -β |
| 39 | β |
| 40 | -β |
| 41 | β |
| 42 | -β |
| 43 | β |
| 44 | -β |
| 45 | β |
| 46 | -β |
| 47 | β |
| 48 | -β |
| 49 | β |
| 50 | -β |
| 51 | β |
| 52 | -β |
| 53 | β |
| 54 | -β |
| 55 | β |
| 56 | -β |
| 57 | β |
| 58 | -β |
| 59 | β |
| 60 | -β |
| 61 | β |
| 62 | -β |
| 63 | β |
| 64 | -β |
| 65 | β |
| 66 | -β |
| 67 | β |
| 68 | -β |
| 69 | β |
| 70 | -β |
| 71 | β |
| 72 | -β |
| 73 | β |
| 74 | -β |
| 75 | β |
| 76 | -β |
| 77 | β |
| 78 | -β |
| 79 | β |
| 80 | -β |
| 81 | β |
| 82 | -β |
| 83 | β |
| 84 | -β |
| 85 | β |
| 86 | -β |
| 87 | β |
| 88 | -β |
| 89 | β |
| 90 | -β |
| 91 | β |
| 92 | -β |
| 93 | β |
| 94 | -β |
| 95 | β |
| 96 | -β |
| 97 | β |
| 98 | -β |
| 99 | β |
| 100 | -β |
</details>

Fig. 4.34. Poisson target acceleration maneuver.
