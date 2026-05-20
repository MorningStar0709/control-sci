# Models

Extremum control systems are, by necessity, nonlinear. How the processes are modeled is therefore all-important. Many investigations of extremum control systems assume that the systems are static. This assumption can be justified if the time between the changes in the reference value is sufficiently long. For static systems it is possible to use many of the methods from numerical optimization. A typical description of the process is

$$y (t) = f (u (t), \theta , t) \tag {13.2}$$

where $f$ is a nonlinear function and $\theta$ is a vector of unknown parameters that may change with time.

If there are dynamics in the process, the performance may not have settled at a new steady-state value before the next measurement is taken. This will give an interaction in the control system that can be difficult to handle. The dynamic influence will increase the complexity considerably.

In many applications it is not easy to find the appropriate models and to determine the exact nature of the nonlinearities involved. It can therefore be appropriate to combine adaptivity and extremum control. One way to simplify the identification of an unknown nonlinear model is to assume that the process can be divided into one nonlinear static part and one linear dynamic part. Models with different properties are obtained if the nonlinearity precedes or follows the linear part. The complexity of the problem will also depend on which of the variables in the process can be measured. One special type of model that has been used in extremum control systems is the Hammerstein model. A typical discrete-time model of this type is

$$A (q) y (t) = B (q) f (u (t)) \tag {13.3}$$

where $f$ is a nonlinear function, typically a polynomial.

The main effect of an input nonlinearity is that it restricts the possible input values for the linear part. The nonlinear control problem can then be treated as a linear control problem with input constraints. The case with the output nonlinearity perhaps leads to more realistic problems but is also more difficult to solve.
