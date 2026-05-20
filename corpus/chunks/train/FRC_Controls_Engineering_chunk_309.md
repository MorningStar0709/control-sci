# Equations to model

The following example system will be used to describe how to define and initialize the matrices for a Kalman filter.

A robot is between two parallel walls. It starts driving from one wall to the other at a velocity of 0.8 cm/s and uses ultrasonic sensors to provide noisy measurements of the distances to the walls in front of and behind it. To estimate the distance between the walls, we will define three states: robot position, robot velocity, and distance between the walls.

$$x _ {k + 1} = x _ {k} + v _ {k} \Delta T \tag {9.25}v _ {k + 1} = v _ {k} \tag {9.26}x _ {k + 1} ^ {w} = x _ {k} ^ {w} \tag {9.27}$$

This can be converted to the following state-space model.

$$
\mathbf {x} _ {k} = \left[ \begin{array}{l} x _ {k} \\ v _ {k} \\ x _ {k} ^ {w} \end{array} \right] \tag {9.28}

\mathbf {x} _ {k + 1} = \left[ \begin{array}{l l l} 1 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right] \mathbf {x} _ {k} + \left[ \begin{array}{l} 0 \\ 0. 8 \\ 0 \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0. 1 \\ 0 \end{array} \right] w _ {k} \tag {9.29}
$$

where the Gaussian random variable $w _ { k }$ has a mean of 0 and a variance of 1. The observation model is

$$
\mathbf {y} _ {k} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right] \mathbf {x} _ {k} + \theta_ {k} \tag {9.30}
$$

where the covariance matrix of Gaussian measurement noise θ is a $2 \times 2$ matrix with both diagonals 10 cm2.

The state vector is usually initialized using the first measurement or two. The covariance matrix entries are assigned by calculating the covariance of the expressions used when assigning the state vector. Let k = 2.

$$
\mathbf {Q} = [ 1 ] \tag {9.31}
\mathbf {R} = \left[ \begin{array}{c c} 1 0 & 0 \\ 0 & 1 0 \end{array} \right] \tag {9.32}

\hat {\mathbf {x}} = \left[ \begin{array}{c} \mathbf {y} _ {k, 1} \\ (\mathbf {y} _ {k, 1} - \mathbf {y} _ {k - 1, 1}) / d t \\ \mathbf {y} _ {k, 1} + \mathbf {y} _ {k, 2} \end{array} \right] \tag {9.33}

\mathbf {P} = \left[ \begin{array}{c c c} 1 0 & 1 0 / d t & 1 0 \\ 1 0 / d t & 2 0 / d t ^ {2} & 1 0 / d t \\ 1 0 & 1 0 / d t & 2 0 \end{array} \right] \tag {9.34}
$$
