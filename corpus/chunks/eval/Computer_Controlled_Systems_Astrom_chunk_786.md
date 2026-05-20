# Parameter Estimation

Solving the parameter-estimation problem requires the following:

- Input-output data from the process   
• A class of models   
• A criterion

Parameter-estimation problem can then be formulated as an optimization problem, where the best model is the one that best fite the data according to the given criterion.

The result of the estimation problem depends, of course, on how the problem is formulated. For instance, the obtained model depends on the amplitude and frequency content of the input signal. There are many possibilities for combining experimental conditions, model classes, and criteria. There are also many different ways to organize the computations. Consequently, there is a large number of different identification methods available. One broad distinction is between on-line methods and off-line methods. The on-line methods give estimates recursively as the measurement are obtained and are the only alternative if the identification is going to be used in an adaptive controller or if the process is time-varying. In many cases the off-line methods give estimates with higher precision and are more reliable, for instance, in terms of convergence.

The large number of methods is confusing for an industrial engineer who is primarily interested in having a tool to obtain a model. Several attempts to compare different identification methods have been made. The comparisons are largely inconclusive in the sense that there is no method that is universally best. Fortunately, it appears that the choice of method is not crucial. Therefore, it can be recommended that a prospective user learn the classic methods (frequency- and transient-response analysis and correlation and spectral analysis), the least-squares method with extensions, and the maximum-likelihood method.
