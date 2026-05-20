# Extremum Control of Dynamic Systems

If there are dynamics in the process, it is necessary to take this into consideration in doing the optimization. The correlation and interaction between different measurements of the performance will otherwise confuse the optimization routine. One possibility, discussed previously, is to wait until the transients have vanished before the next change is made. Of course, this will increase the convergence time, especially if the process has long time constants. One way around the problem is to base the optimization on nonlinear dynamic models. An example is the Hammerstein model. A model of this type with an input nonlinearity of second order is

$$A (q) y (t) = b _ {0} + B _ {1} (q) u (t) + B _ {2} (q) u ^ {2} (t) + C (q) e (t) \tag {13.4}$$

The main reason for the popularity of the Hammerstein model is not that it is a good picture of the reality, but rather that it is linear in the parameters. The parameters can be estimated, for example, by using recursive least squares. The static response between the input and the output is given by

$$A (1) y _ {0} = b _ {0} + B _ {1} (\mathbf {1}) u _ {0} + B _ {2} (\mathbf {1}) u _ {0} ^ {2}$$

The methods for static optimization discussed previously can now be used. Also note that the gradients and the Hessian are easily computed, a feature that will speed up the convergence.
