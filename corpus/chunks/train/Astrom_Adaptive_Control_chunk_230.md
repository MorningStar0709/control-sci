# 4.4 UNIFICATION OF DIRECT SELF-TUNING REGULATORS

The moving-average self-tuner is attractive because of its simplicity. It is easy to explain intuitively how the algorithm works, and the algorithm is easy to implement. This has led to great interest in the algorithm. The algorithm can be explained as follows: Determine the structure of a predictor that can be used to predict the output d steps ahead. The parameters of the predictor are estimated in real time. On the basis of the estimated parameters the control signal is determined such that the predicted output of the process is equal to the reference value. The algorithm has been analyzed extensively. The closed-loop bandwidth depends critically on the sampling period h and the prediction horizon d, so both must be chosen with care. The algorithm may result in a controller in which process zeros are canceled; the cancellations depend on the choice of prediction horizon. Many variants of the algorithm have been suggested. A number of these can be described in a unified framework, as we will demonstrate.

Consider the model of Eq. (4.1), and introduce the filtered output

$$y _ {f} (t) = \frac {Q ^ {*} (q ^ {- 1})}{P ^ {*} (q ^ {- 1})} y (t)$$

where $Q^{*}$ and $P^{*}$ are stable polynomials. The filtered output satisfies the equation

$$A ^ {*} (q ^ {- 1}) P ^ {*} (q ^ {- 1}) y _ {f} (t) = B ^ {*} (q ^ {- 1}) Q ^ {*} (q ^ {- 1}) u (t - d _ {0}) + C ^ {*} (q ^ {- 1}) Q ^ {*} (q ^ {- 1}) e (t)$$

Introduce the identity

$$C ^ {*} (q ^ {- 1}) Q ^ {*} (q ^ {- 1}) = A ^ {*} (q ^ {- 1}) P ^ {*} (q ^ {- 1}) R _ {1} ^ {*} (q ^ {- 1}) + q ^ {- d _ {0}} S ^ {*} (q ^ {- 1})$$

Then

$$y _ {f} (t + d _ {0}) = \frac {1}{C ^ {*} Q ^ {*}} \left(S ^ {*} y _ {f} (t) + B ^ {*} Q ^ {*} R _ {1} ^ {*} u (t)\right) + R _ {1} ^ {*} e (t + d _ {0})$$

Introducing

$$y _ {f} ^ {\prime} (t) = \frac {1}{Q ^ {*} (q ^ {- 1})} y _ {f} (t) = \frac {1}{P ^ {*} (q ^ {- 1})} y (t)$$

gives the model

$$y _ {f} (t + d _ {0}) = \frac {1}{C ^ {*}} \left(S ^ {*} y _ {f} ^ {\prime} (t) + B ^ {*} R _ {1} ^ {*} u (t)\right) + R _ {1} ^ {*} e (t + d _ {0}) \tag {4.31}$$

By analogy with Eq. (4.21) this model structure could be used with Algorithm 4.1 to derive a self-tuning regulator for minimization of the variance of $y_{f}$ . This reparameterized model now suggests the following generalized self-tuning algorithm.
