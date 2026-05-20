Several drastic modifications are made to simplify the calculations. A constant value of the gain is used. The multiplication is avoided by just using the signs of the signals. Leakage is also added to make sure that the estimator is stable. The updating of the parameters $b_{i}$ is then given by the sign-sign algorithm

$$\hat {b} _ {i} (t) = \left(1 - 2 ^ {- 8}\right) \hat {b} _ {i} (t) + 2 ^ {- 7} \operatorname{sign} (e (t - i)) \operatorname{sign} (e (t)) \tag {13.1}$$

Similar approximations are made in the other equations. The computations in Eq. (13.1) are very simple. They can be done by shifts and the addition of a few bits, which can be accomplished with a small VLSI circuit. The CCITT ADCPM standard was achieved after significant experimentation. It is a good example of how drastic simplifications can be made with good engineering.
