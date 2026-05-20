# Extensions of the Least-Squares Method

The least-squares method gives unbiased results of the parameters in (13.1) only if $C(q) = q^{n}$ . However, the maximum likelihood method can be used for the general case. It can be shown that maximizing the likelihood function is equivalent to minimizing the loss function of (13.3), where the residuals, $\varepsilon$ , are related to the inputs and outputs by

$$C (q) \varepsilon (k) = A (q) y (k) - B (q) u (k)$$

The residuals can be interpreted as the one-step-ahead prediction error. However, the loss function is not linear in the parameters and it has to be minimized numerically. This can be done using a Newton-Raphson gradient routine, which involves computation of the gradient of J with respect to the parameters, as well as the matrix of second partial derivatives. The maximum-likelihood method is thus an off-line method. It is possible to make approximations of the maximum-likelihood method that allow on-line computations of the parameters of the model in (13.1). Some common methods are Extended Least Squares (ELS), Generalized Least Squares (GLS), and Recursive Maximum Likelihood (RML).
