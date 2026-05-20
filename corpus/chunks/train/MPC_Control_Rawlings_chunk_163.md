# Exercise 1.41: Signal processing in the good old days — recursive least squares

Imagine we are sent back in time to 1960 and the only computers available have extremely small memories. Say we have a large amount of data coming from a process and we want to compute the least squares estimate of model parameters from these data. Our immediate challenge is that we cannot load all of these data into memory to make the standard least squares calculation.

Alternatively, go 150 years further back in time and consider the situation from Gauss’s perspective,

It occasionally happens that after we have completed all parts of an extended calculation on a sequence of observations, we learn of a new observation that we would like to include. In many cases we will not want to have to redo the entire elimination but instead to find the modifications due to the new observation in the most reliable values of the unknowns and in their weights.

C.F. Gauss, 1823

G.W. Stewart Translation, 1995, p. 191.

Given the linear model

$$y _ {i} = X _ {i} ^ {\prime} \theta$$

in which scalar $y _ { i }$ is the measurement at sample $i , X _ { i } ^ { \prime }$ is the independent model variable (row vector, $1 \times p )$ at sample i, and θ is the parameter vector $( p \times 1 )$ to be estimated from these data. Given the weighted least squares objective and n measurements, we wish to compute the usual estimate

$$\hat {\theta} = (X ^ {\prime} X) ^ {- 1} X ^ {\prime} y \tag {1.63}$$

in which

$$
y = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right] \qquad X = \left[ \begin{array}{c} X _ {1} ^ {\prime} \\ \vdots \\ X _ {n} ^ {\prime} \end{array} \right]
$$

We do not wish to store the large matrices $X ( n \times p )$ and $y ( n \times 1 )$ required for this calculation. Because we are planning to process the data one at a time, we first modify our usual least squares problem to deal with small n. For example, we wish to estimate the parameters when $n < p$ and the inverse in (1.63) does not exist. In such cases, we may choose to regularize the problem by modifying the objective function as follows

$$\Phi (\theta) = (\theta - \overline {{\theta}}) ^ {\prime} P _ {0} ^ {- 1} (\theta - \overline {{\theta}}) + \sum_ {i = 1} ^ {n} (y _ {i} - X _ {i} ^ {\prime} \theta) ^ {2}$$
