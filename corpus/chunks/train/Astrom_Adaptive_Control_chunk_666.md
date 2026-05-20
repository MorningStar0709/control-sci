# EXAMPLE 11.6 Covariance resetting

Consider the same system as in Example 11.5, but assume now that the parameter is piecewise constant. In Fig. 11.10 we show the results obtained with exponential forgetting with $\lambda = 0.95$ . The figure shows clearly that the estimate of the process gain responds quite slowly when the gain changes. Notice also the strong asymmetry in the response of the estimate when the gain changes. It takes much longer for the estimate of the gain to increase than to decrease. The reason for this is the large difference in excitation. Also notice the stepwise nature of the estimates. Good excitation is obtained only when the command signal changes. In Fig. 11.11 we show the same system as in Fig. 11.10 with $\lambda = 1$ and covariance resetting. The covariance matrix is reset by reducing $\lambda$ to 0.0001 when the parameter changes. Notice the drastic difference in the tracking rate.

![](image/6278e0ebd8a0629b27b6526eb3e3664c7575ce20415a697ffad7f9659ff7f455.jpg)  
Figure 11.10 Tracking piecewise constant parameters using exponential forgetting when $\lambda = 0.95$ .

The example clearly illustrates the advantage of using covariance resetting when the parameters change abruptly. To use this effectively, it is necessary to detect the changes in the parameters. There are many ways to do this by analyzing residuals or parameter changes. It is also possible to reset the covariance periodically.
