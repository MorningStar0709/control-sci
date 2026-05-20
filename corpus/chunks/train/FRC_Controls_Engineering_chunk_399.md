# 14.1 Ordinary least squares

The parameter estimation in this chapter will be performed using ordinary least squares (OLS). Let there be a linear equation of the form $y = \beta _ { 1 } x _ { 1 } + . . . + \beta _ { p } x _ { p }$ . We want to find the constants $\beta _ { 1 } , \ldots , \beta _ { p }$ that best fit a set of observations represented by $x _ { 1 , \ldots , n } – y$ tuples. Consider the overdetermined system of n linear equations $\mathbf { y } = \mathbf { X } { \boldsymbol { \beta } } $ where

$$
\mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right] \quad \mathbf {X} = \left[ \begin{array}{c c c} x _ {1 1} & \dots & x _ {1 p} \\ \vdots & \ddots & \vdots \\ x _ {n 1} & \dots & x _ {n p} \end{array} \right] \quad \boldsymbol {\beta} = \left[ \begin{array}{c} \beta_ {1} \\ \vdots \\ \beta_ {p} \end{array} \right]
$$

each row corresponds to a datapoint, and $n \ > \ p$ (more datapoints than unknowns). OLS is a type of linear least squares method that estimates the unknown parameters $\beta$ in a linear regression model $\mathbf { y } = \mathbf { X } \beta + \epsilon$ where ϵ is the error in the observations y. $\beta$ is chosen by the method of least squares: minimizing the sum of the squares of the difference between $\mathbf { y }$ (observations of the dependent variable) and $\mathbf { X } \beta$ (predictions of y using a linear function of the independent variable $\beta )$ .

Geometrically, this is the sum of the squared distances, parallel to the y-axis, between each value in y and the corresponding value in $\mathbf { X } { \boldsymbol { \beta } } .$ . Smaller differences mean a better model fit.

To find the $\beta$ that fits best, we can solve the following quadratic minimization problem

$$\hat {\boldsymbol {\beta}} = \underset {\boldsymbol {\beta}} {\arg \min} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta}) ^ {\mathsf {T}} (\mathbf {y} - \mathbf {X} \boldsymbol {\beta})$$

arg min $^ { 1 } \beta$ means “find the value of $\beta$ that minimizes the following function of $\beta ^ { \prime }$ . Given corollary 5.12.3, take the partial derivative of the cost function with respect to $\beta$ and set it equal to zero, then solve for $\hat { \beta }$ .

$$\mathbf {0} = - 2 \mathbf {X} ^ {\mathsf {T}} (\mathbf {y} - \mathbf {X} \hat {\boldsymbol {\beta}})\mathbf {0} = \mathbf {X} ^ {\top} (\mathbf {y} - \mathbf {X} \hat {\boldsymbol {\beta}})\mathbf {0} = \mathbf {X} ^ {\top} \mathbf {y} - \mathbf {X} ^ {\top} \mathbf {X} \hat {\boldsymbol {\beta}}\mathbf {X} ^ {\mathsf {T}} \mathbf {X} \hat {\boldsymbol {\beta}} = \mathbf {X} ^ {\mathsf {T}} \mathbf {y}\hat {\boldsymbol {\beta}} = (\mathbf {X} ^ {\mathsf {T}} \mathbf {X}) ^ {- 1} \mathbf {X} ^ {\mathsf {T}} \mathbf {y} \tag {14.1}$$
