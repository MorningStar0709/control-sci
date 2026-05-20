# EXAMPLE 11.8 Conditional updating

Consider the system in Example 11.7, but modify the estimator to provide conditional updating. In this particular case the estimate is updated if the test quantity

$$\varphi (t) ^ {T} P (t) \varphi (t) > 2 (1 - \lambda)$$

Figure 11.14 shows a simulation that is comparable to Fig. 11.12. Notice that the exponential growth is now avoided. The elements of the P-matrix remain bounded, and the estimator gains are well behaved. □

The selection of the condition for updating is critical. If the criterion is too stringent, the estimates will be poor because updating is done too infrequently. If the criterion is too liberal, we get covariance windup.
