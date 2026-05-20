# Method

Suppose that the target flies straight and level. A collision course will lead the missile to collide with the target, provided that the missile also flies straight and level along the course. The collision course (CC) interception strategy is to turn the missile’s heading to coincide with the predicted collision course by commanding a turn rate proportional to the angle between the collision and the current heading of the interceptor missile. If the missile is on the collision course, then from the triangular law we have

$$v _ {2 x y} \tau / \sin \xi = v _ {1 x y} \tau / \sin (1 8 0 ^ {\circ} - \theta), \tag {C.1}$$

where τ is the interception time. Consequently, the collision antenna train angle $( C A T A ) \xi$ can be determined from the relation

$$\xi = \sin^ {- 1} (v _ {2 x y} \sin \theta / v _ {1 x y}). \tag {C.2}$$

The degree to turn for the collision course interception in the xy-plane is $( \chi - \xi )$ . The desired heading-angle turn rate for the collision course interception is taken as

$$\frac {d \Psi}{d t} = K _ {c} (\chi - \xi), \tag {C.3}$$

where $\mathrm { K } _ { c }$ is a design factor given by

$$K _ {c} = 6 v _ {1} / R. \tag {C.4}$$

Moreover, from the triangular law, we have the following expression:

$$
\tau = \left\{ \begin{array}{l l} - R _ {x y} / 2 v _ {2 x y} \cos \theta & \text { if } \quad v _ {1 x y} = v _ {2 x y}, \\ v _ {2 x y} \cos \theta \pm [ (2 v _ {2 x y} \cos \theta) ^ {2} \\ + (v _ {1 x y} ^ {2} - v _ {2 x y} ^ {2}) ] ^ {1 / 2} / R _ {x y} (v _ {1 x y} ^ {2} - v _ {2 x y} ^ {2}) & \text { if } \quad v _ {1 x y} \neq v _ {2 x y}. \end{array} \right. \tag {C.6}
$$

If $\tau < 0$ , the interception is then impossible. To reach altitude $h _ { 2 }$ after time t, The missile needs a flight path angle  . Thus,

$$\varpi = \sin^ {- 1} [ (h _ {2} - h _ {1}) / v \tau ]. \tag {C.7}$$

Consequently, the desired flight path angle change rate for the LOS interception is taken as

$$\frac {d \gamma}{d t} = K _ {\gamma} (\varpi - \gamma), \tag {C.8}$$

where $K _ { \gamma }$ is determined by the missile’s aero-characteristics.
