# 9.6.9 Multiple measurement models

Some systems have different measurements available at different times due to varying sample rates or environmental factors (e.g., obscured localization targets). To incorporate them all into the state estimate, perform an update step at each time with a measurement model containing only the available measurements.

For example, consider the following system

$$
\underbrace {\left[ \begin{array}{c} x _ {k + 1} \\ y _ {k + 1} \\ \theta_ {k + 1} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {k} \\ y _ {k} \\ \theta_ {k} \end{array} \right] + \left[ \begin{array}{c c c} \Delta T & 0 & 0 \\ 0 & \Delta T & 0 \\ 0 & 0 & \Delta T \end{array} \right] \left[ \begin{array}{c} v _ {x , k} \\ v _ {y , k} \\ \omega_ {k} \end{array} \right]} _ {\text {dynamical model}}

\underbrace {\left[ \begin{array}{c} x _ {k} \\ y _ {k} \\ \theta_ {k} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {k} \\ y _ {k} \\ \theta_ {k} \end{array} \right] + \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} v _ {x , k} \\ v _ {y , k} \\ \omega_ {k} \end{array} \right]} _ {\text {measurement model}}
\underbrace {\mathbf {R} = \mathrm{diag} (\sigma_ {x} ^ {2} , \sigma_ {y} ^ {2} , \sigma_ {\theta} ^ {2})} _ {\text { measurement covariance matrix }}
$$

If the θ measurement is unavailable, we can remove it from the measurement model and R matrix for that update step.

$$
\left[ \begin{array}{c} x _ {k} \\ y _ {k} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {k} \\ y _ {k} \\ \theta_ {k} \end{array} \right] + \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} v _ {x, k} \\ v _ {y, k} \\ \omega_ {k} \end{array} \right]
\mathbf {R} = \mathrm{diag} (\sigma_ {x} ^ {2}, \sigma_ {y} ^ {2})
$$
