# 5.15 Earth Curvature

As mentioned in Sections 5.8 and 5.12, sometimes it becomes necessary to release ordnance from a greater distance than usual and assume a flat Earth in the computation of a target’s distance. In such cases, the weapon delivery system and/or the fire control computer must consider the Earth’s curvature. Figure 5.33 illustrates the derivation of the Earth curvature equation.

The Earth’s curvature to the specified point is computed as follows:

$$
\begin{array}{l} C _ {Z} = (R _ {E} + h _ {S}) - [ (R _ {E} + h _ {S}) ^ {2} - R _ {L} ^ {2} ] ^ {1 / 2} \\ = (R _ {E} + h _ {S}) [ 1 - (1 - R _ {L} ^ {2} / (R _ {E} + h _ {S}) ^ {2}) ^ {1 / 2} ] \\ = (R _ {E} + h _ {S}) [ 1 - (1 - R _ {L} ^ {2} / 2 (R _ {E} + h _ {S}) ^ {2}) ] \\ = R _ {L} ^ {2} / 2 (R _ {E} + h _ {S}) \\ \cong R _ {L} ^ {2} / 2 R _ {E}, \tag {5.72} \\ \end{array}
$$

where

hS = mean sea-level elevation of the specified point,

$R _ { L }$ = horizontal component of range to the specified point,

$R _ { E }$ = radius of the Earth.

Figure 5.34 illustrates the definition of the Earth curvature limit window.

The depression angle to the Earth’s curvature, that is, the limit window, can be calculated from the following expression:

$$\tan^ {2} \theta_ {D L I M} = (| h _ {T} | + C _ {L I M}) / R _ {E C L I M} ^ {2}, \tag {5.73}$$

![](image/ce26c6c372fb23527c3fa9f29aa75b1004bceb73cf623fa6ff46934ddbfc403e.jpg)

<details>
<summary>text_image</summary>

h_T
θ_DLIM
Lower limit of earth
curvature window
C_LIM
R_ECLIM
</details>

Fig. 5.34. Definition of the Earth curvature limit window.

where

$$h _ {T} = \text { height above the terrain },C _ {L I M} = \text { limit on Earth's curvature (6076.12 ft) },R _ {E C L I M} = \text { horizontal range to Earth curvature limit (504,275.8 ft) },\theta_ {D L I M} = \text { depression angle to each curvature limit. }$$
