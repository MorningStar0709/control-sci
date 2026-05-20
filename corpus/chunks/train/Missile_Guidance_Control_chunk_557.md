(3) Spherical Earth Case: Earth Fixed target For an Earth fixed target, we note from (1) and (2) that the target position becomes a function of the free-flight time $t _ { f f } = t - t _ { o }$ . The free-flight time, however, is a function of the required velocity, and the required velocity is in turn a function of the target position. Thus, to effect a solution, it is necessary to perform an iterative computation procedure, such as the following:

(a) Estimate future position of the target.   
(b) Compute the required velocity from (12).   
(c) Compute the time of free flight.   
(e) The procedure is repeated until it converges.

(d) Compute the new target position from the time of free flight.

The time of free flight $t _ { f f } = t - t _ { o }$ can be shown to be (see (6.92))

$$t _ {f f} = (\sqrt {a ^ {3} / \mu}) [ (E _ {t} - E _ {v}) - e (\sin E _ {t} - E _ {v}) ], \tag {13}$$

where

$$
\begin{array}{l} E _ {t} = \text { eccentric   anomaly   of   the   target   position }, \\ E _ {v} = \text { eccentric   anomaly   of   the   missile   position }, \\ e = \text { trajectory   eccentricity }. \\ \end{array}
$$

An examination of the equations presented in this section shows that we are forcing a solution to the problem of impacting the target for a given flight path angle $\gamma$ . Thus, for a given vehicle position and flight path angle $\gamma _ { : }$ , there is a unique solution to the problem. If the flight path angle were to have a different value, the time of flight to impact the target would be different, and the required azimuth heading would be different, by the control (8).

(4) Required Velocity: Fixed Time-of-Flight Schemes A sufficient constraint in (7) to reduce the dependent variables to (3) and therefore to effect a unique solution is to constrain the total time of flight of the missile from launch to impact. For this scheme, the target becomes an inertially fixed target, the position of which is given as

$$\mathbf {r} _ {t} = \mathbf {r} _ {t} (t _ {L}) + \int_ {t _ {L}} ^ {T} \left(\frac {d \mathbf {r} _ {t}}{d t}\right) d t \tag {14}$$

where

$$
\begin{array}{l} t _ {L} = \text { launch   time }, \\ \begin{array}{l} T = \text { constrained   time   of   missile   arrival } \\ \text { at   the   target }, \end{array} \\ \frac {d \mathbf {r} _ {t}}{d t} = \text { velocity   of   the   target   given   by } (2). \\ \end{array}
$$

As before, the discussion of this guidance scheme will begin with a spherical Earth gravitational model.

(4.1) Velocity Required: Spherical Earth Case For the spherical Earth case, the required velocity can be formulated in many different ways. The following represents three possibilities.
