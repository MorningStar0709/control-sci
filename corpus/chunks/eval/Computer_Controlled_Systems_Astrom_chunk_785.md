# Criteria

When formulating an identification problem, a criterion is postulated to give a measure of how well a model fits the experimental data. By making statistical assumptions, it is also possible to derive criteria from probabilistic arguments. The criteria for discrete-time systems are often expressed as

$$J (\theta) = \sum_ {k = 1} ^ {N} g (\varepsilon (k))$$

where $\varepsilon$ is the input error, the output error, or a generalized error. The prediction error is a typical example of a generalized error. The function g is frequently chosen to be quadratic, but it is possible for it to be of many other forms.

The first formulation, solution, and application of an identification problem were given by Gauss in his famous determination of the orbit of the asteroid Ceres. Gauss formulated the identification problem as an optimization problem and introduced the principle of least squares, a method based on the minimization of the sum of the squares of the error. Since then, the least-squares criterion has been used extensively.

The least-squares method is very simple and easy to understand. Under some circumstances it gives estimates with the wrong mean values (bias). However, this can be overcome by using various extensions. The least-squares method is restricted to model structures that are linear in the unknown parameters.

When the disturbances of a process are described as stochastic processes, the identification problem can be formulated as a statistical parameter-estimation problem. It is then possible to use the maximum-likelihood method, for example; this method has many attractive statistical properties. It can be interpreted as a least-squares criterion if the quantity to be minimized is taken as the sum of squares of the prediction error. The maximum-likelihood method is a very general technique that can be applied to a wide variety of model structures.
