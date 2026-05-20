# Generalized Predictive Control (GPC)

The predictive controllers discussed so far have considered the output at only one future instant of time. Different generalizations of predictive control have been suggested, in which different loss functions are minimized. One possibility is to use

$$J \left(N _ {1}, N _ {2}, N _ {u}\right) = E \left\{\sum_ {k = N _ {1}} ^ {N _ {2}} \left(y (t + k) - y _ {m} (t + k)\right) ^ {2} + \sum_ {k = 1} ^ {N _ {u}} \rho \Delta u (t + k - 1) ^ {2} \right\} \tag {4.61}$$

where

$$\Delta = 1 - q ^ {- 1}$$

is the difference operator. Different choices of $N_{1}$ , $N_{2}$ , and $N_{u}$ give rise to the different schemes suggested in the literature.

The methodology of generalized predictive control is illustrated by using the loss function of Eq. (4.61) and the process model

$$A ^ {*} (q ^ {- 1}) y (t) = B ^ {*} (q ^ {- 1}) u (t - d _ {0}) + \frac {e (t)}{\Delta} \tag {4.62}$$

This model is sometimes called the CARIMA (controlled auto-regressive integrating moving-average) model. It has the advantage that the controller will automatically contain an integrator. (Compare Section 3.6.) As with Eq. (4.50), the following identity is introduced:

$$1 = A ^ {*} (q ^ {- 1}) F _ {d} ^ {*} (q ^ {- 1}) (1 - q ^ {- 1}) + q ^ {d} G _ {d} ^ {*} (q ^ {- 1}) \tag {4.63}$$

This can be used to determine the output d steps ahead:

$$y (t + d) = F _ {d} ^ {*} B ^ {*} \Delta u (t + d - d _ {0}) + G _ {d} ^ {*} y (t) + F _ {d} ^ {*} e (t + d)$$

$F_{d}^{*}$ is of degree d-1. The optimal mean squared error predictor, given measured output up to time t and any given input sequence, is

$$\hat {y} (t + d) = F _ {d} ^ {*} B ^ {*} \Delta u (t + d - d _ {0}) + G _ {d} ^ {*} y (t) \tag {4.64}$$

Suppose that the future desired outputs, $y_{m}(t+k)$ , $k=1,2,\ldots$ are available. The loss function of Eq. (4.61) can now be minimized, giving a sequence of future control signals. Notice that the expectation in Eq. (4.61) is made with respect to data obtained up to time t, assuming that no future measurements are available. That is, it is assumed that the computed control sequence is applied to the system. However, only the first element of the control sequence is used. The calculations are repeated when a new measurement is obtained. The resulting controller belongs to the confusingly named class called open-loop-optimal-feedback control. As the name suggests, it is assumed that feedback is used, but it is computed only on the basis of the information available at the present time.
