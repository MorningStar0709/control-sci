where $y _ { d }$ is the miss distance and $x r M$ is the missile-to-target range measured along the original LOS. For modeling purposes, accurate computation of λ is not required during the period it becomes large, thus allowing small-angle approximation, eliminating the nonlinear $\tan ^ { - 1 }$ operation. Therefore,

$$\lambda \cong y _ {d} / x _ {T M} [ \text { radians } ]. \tag {4.149}$$

Next, we will consider the target model. It will be assumed that the target may have random changes in its acceleration normal to its velocity vector. The assumed acceleration time history model is a randomly reversing Poisson square wave, as shown in Figure 4.34, with an average of v zero-crossings per second and an rms level (or amplitude) of $\dot { \mathbf { \eta } } \pm \beta \mathbf { f t } / \mathrm { s e c } ^ { 2 }$ (that is, the square wave switches between $\pm \beta )$ .

The autocorrelation function for the observation times $t _ { 1 }$ and $t _ { 2 }$ is given by [25]

$$\phi (t _ {1} - t _ {2}) = \beta^ {2} \exp (- 2 v | t _ {1} - t _ {2} |). \tag {4.150}$$

If $v  0 ,$ , the target acceleration ${ \bf a } _ { T }$ approaches a constant level. That is, the meansquared value of $\mathbf { a } _ { T }$ is $\beta ^ { 2 }$ . The power spectral density of this Poisson wave, associated with $\mathbf { a } _ { T }$ , is

$$\Phi (\omega) = \left(\beta^ {2} / 2 \pi v\right) \left[ 1 / \left(1 + \left(\omega / 2 v\right) ^ {2} \right]. \right. \tag {4.151}$$

Note that since the Kalman filter is based on minimizing the mean-squared error of the state estimate, it is justifiable to replace the Poisson wave model of target maneuver with one that has the same mean and autocorrelation function, so as to obtain the same quality of estimate with a mathematically more convenient model.

The control input to be determined is the commanded missile lateral (or normal) acceleration. Continuous control will be assumed in developing the guidance laws. To this end, it is desired to minimize the expected square of the miss distance $y _ { d }$ subject to a penalty function on the total control energy. Consequently, the performance index to be minimized is given by (4.152) [3], [17], [19],

$$J = y _ {d} ^ {2} (T) + \gamma \int_ {0} ^ {T} u _ {c} ^ {2} d t, \tag {4.152}$$

where, as before, $y _ { d } ( T )$ and $\gamma$ are respectively the terminal miss distance at the intercept time $T$ and the weighting on the control effort $u _ { c }$ , subject to
