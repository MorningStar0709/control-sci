# Parameter\_update

We assume that the estimated model has the form

$$y (t) = \varphi^ {T} (t) \theta$$

where the components in the regression vector $\varphi$ are lagged and filtered inputs and outputs. The ordering, the number of lags, and so on depend on the specific model; these details are easily sorted out for the chosen model structure. Rows 6 and 13 of the algorithm contain the bookkeeping of the $\varphi$ vector (i.e., the usual shift of some parts of the vector and supplement of the latest measurements and outputs). This part of the algorithm should also include the data filtering discussed in Sections 11.2, 11.3, and 11.7. For simplicity it is assumed that the estimation and the covariance update are done by using ordinary recursive least squares (Eqs. 11.19). The calculations can be organized as in the listing below, where eps is the residual, th\_estimated is the parameter vector, P is the covariance matrix, phi is the data vector, and lambda is the forgetting factor.

```txt
"Compute residual
eps = y - phi'*th_estimated
"Update estimate
w = P*phi
den = lambda + phi'*w
gain = w/den
th_estimated = th_estimated + gain*eps
"Update covariance
P = (P - w*w'/den)/lambda 
```

The prime is the transpose, and \* is matrix multiplication. This skeleton can easily be transferred to any preferred programming language.
