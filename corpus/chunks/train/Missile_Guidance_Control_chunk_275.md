# Method

Compute the LOS turn rate by the following expression:

$$\frac {d \sigma}{d t} = (\mathbf {R} _ {x y} \times \mathbf {v} _ {x y}) / R _ {x y} ^ {2} = (v _ {2 x y} \sin \theta - v _ {1 x y} \sin \chi) / R _ {x y}, \tag {L.1}$$

and the closure rate

$$\frac {d R}{d t} = \left(\mathbf {R} _ {x y} \cdot \mathbf {v} _ {1 x y} + \mathbf {R} _ {x y} \cdot \mathbf {v} _ {2 x y}\right) / R _ {x y} = v _ {2 x y} \cos \theta + v _ {1 x y} \cos \chi . \tag {L.2}$$

The desired heading angle turn rate for the LOS interception is given by

$$\frac {d \Psi_ {1}}{d t} = - K _ {L} \left[ \left(\frac {d \sigma}{d t}\right) \left(\frac {d R}{d t}\right) + 0. 5 \left(\frac {d \Psi_ {2}}{d t}\right) \right]. \tag {L.3}$$

On the other hand, if the missile keeps flying with a flight path angle determined by the horizontal plane and the LOS vector, the missile will reach the same altitude with the target at the interception point. Moreover, if the altitude of the vehicle is initially higher than that of the target, the missile will approach the target from above, and vice versa. The LOS flight path angle can be computed as follows:

$$\varpi = \sin^ {- 1} [ (h _ {2} - h _ {1}) / R ]. \tag {L.4}$$

The angle change rate for the LOS interception is then taken as

$$\frac {d \gamma_ {1}}{d t} = K _ {\gamma} (\varpi - \gamma) - \left(\frac {d \gamma_ {2}}{d t}\right). \tag {L.5}$$
