# EXAMPLE 1.11 Adjustment of a friction compensator

Friction is common in all mechanical systems. Consider a simple servo drive. Friction can to some extent be compensated for by adding the signal $u_{fc}$ to a controller, where

$$
u _ {f c} = \left\{ \begin{array}{c l} u _ {+} & \text { if } v > 0 \\ - u _ {-} & \text { if } v <   0 \end{array} \right.
$$

where v is the velocity. The signal attempts to compensate for Coulomb friction by adding a positive control signal $u_{+}$ when the velocity is positive and subtracting $u_{-}$ when the velocity is negative. The reason for having two parameters is that the friction forces are typically not symmetrical. Since there are so many factors that influence friction, it is natural to try to find a mechanism that can adjust the parameters $u_{+}$ and u. automatically.
