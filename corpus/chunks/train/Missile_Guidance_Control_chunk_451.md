where $\chi _ { \alpha } ( \alpha = 1 , \ldots , 6 )$ has been defined as $x , y , z , ~ ( d x / d t ) , ( d y / d t ) , ( d z / d t )$ , respectively, $\sigma _ { k , l }$ is the k, l element of the input covariance matrix $P ( t _ { 0 } )$ , and $S _ { \alpha , k }$ are known from integration of (5.47) to impact. Equation (5.48) considers only the initial system errors. Ballistic and/or wind table parameter errors would require extension of the k, l summation limits in (5.48) to include the associated ballistic and/or wind sensitivities, and appropriate augmentation of $\sigma _ { k , l }$ . Finally, (5.48) applies for “small” errors, and the reference trajectory is assumed to impact the target, giving a zero mean dispersion.

Statistical air-to-ground weapon delivery error analysis employing an ensemble of events indicates that the horizontal velocity errors from the INS are the dominant error sources among those present, including sensor, computer, pilot, and weapon related error sources. Simulation program outputs indicate system performance in terms of horizontal position accuracy, CEP, where the CEP can be approximated by (see also Section 5.7.2, (5.12))

$$C E P \cong 0. 5 8 9 (\sigma_ {x} + \sigma_ {y}), \tag {5.49}$$

and horizontal velocity accuracy $\sigma _ { v }$ , where

$$\sigma_ {v} = (\sigma_ {v x} ^ {2} + \sigma_ {v y} ^ {2}) ^ {1 / 2}. \tag {5.50}$$

The one-sigma ensemble statistics of the velocity error applied to weapon delivery analysis are given by the expression

$$\sigma_ {v s} = \sqrt {(1 / T) \int_ {0} ^ {t} \sigma_ {v} ^ {2} (t) d t}, \tag {5.51}$$

which is equivalent to the root-mean-square (rms) value of the time-dependent, one-sigma statistics from the Kalman covariance analysis for a given expected penetration time span T .
