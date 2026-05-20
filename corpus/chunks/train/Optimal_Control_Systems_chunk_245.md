# Example 4.5

Consider a simple example where we can verify the analytical solutions by another known method. Find the optimal feedback coefficients for the system

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t) \tag {4.5.22}$$

and the performance measure

$$J = \frac {1}{2} \int_ {0} ^ {\infty} \left[ x _ {1} ^ {2} (t) + x _ {2} ^ {2} (t) + u ^ {2} (t) \right] d t. \tag {4.5.23}$$

Solution: First it is easy to identify the various matrices as

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right]; \quad \mathbf {B} = \mathbf {b} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]; \quad \mathbf {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]; \quad \mathbf {R} = r = 1. \tag {4.5.24}
$$

Also, note since $\mathbf{Q} = \mathbf{R} = \mathbf{I}$ , we have $\mathbf{C} = \mathbf{D} = \mathbf{I}$ and $\mathbf{B} = \mathbf{I}$ . Thus, the Kalman equation (4.5.18) with $j\omega = s$ becomes

$$\left| \left| \mathbf {I} + \bar {\mathbf {K}} ^ {\prime} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right| \right| ^ {2} = \mathbf {I} + \left| \left| \mathbf {C} ^ {\prime} [ s \mathbf {I} - \mathbf {A} ] ^ {- 1} \mathbf {B} \right| \right| ^ {2}. \tag {4.5.25}$$

Further, we have

$$
[ s \mathbf {I} - \mathbf {A} ] ^ {- 1} = \left[ \begin{array}{l l} \frac {1}{s} & 0 \\ \frac {1}{s ^ {2}} & \frac {1}{s} \end{array} \right]; \quad \bar {\mathbf {K}} = \bar {\mathbf {k}} = [ k _ {1 1} k _ {1 2} ]. \tag {4.5.26}
$$

Then, the Kalman equation (4.5.25) becomes

$$
\begin{array}{l} \left[ 1 + \left[ k _ {1 1} k _ {1 2} \right] \left[ \begin{array}{c c} \frac {1}{- s} & \frac {1}{(- s) ^ {2}} \\ 0 & \frac {1}{- s} \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \right] \left[ 1 + \left[ k _ {1 1} k _ {1 2} \right] \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s ^ {2}} \\ 0 & \frac {1}{s} \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \right] = \\ 1 + \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} \frac {1}{- s} & \frac {1}{(- s) ^ {2}} \\ 0 & \frac {1}{- s} \end{array} \right] \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c c} \frac {1}{s} & \frac {1}{s ^ {2}} \\ 0 & \frac {1}{s} \end{array} \right] \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]. \tag {4.5.27} \\ \end{array}
$$
