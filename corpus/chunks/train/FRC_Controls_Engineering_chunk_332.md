# 10.1 Forward Euler integration

The simplest way to perform pose estimation via dead reckoning (that is, no direct measurements of the pose are used) is to integrate the velocity in each orthogonal direction over time. In two dimensions, one could use

$$
\begin{array}{l} x _ {k + 1} = x _ {k} + v _ {k} \cos \theta_ {k} T \\ y _ {k + 1} = y _ {k} + v _ {k} \sin \theta_ {k} T \\ \theta_ {k + 1} = \theta_ {g y r o, k + 1} \\ \end{array}
$$

where T is the sample period. This odometry approach assumes that the robot follows a straight path between samples (that is, ω = 0 at all but the sample times).
