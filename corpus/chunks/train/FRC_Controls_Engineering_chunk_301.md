# Finding the optimal Kalman gain

The error in the a posteriori state estimation is xk+1 − xˆ+k+1. We want to minimize $\mathbf x _ { k + 1 } - \hat { \mathbf x } _ { k + 1 } ^ { + }$ the expected value of the square of the magnitude of this vector, which can be written as $E [ ( \mathbf { x } _ { k + 1 } - \hat { \mathbf { x } } _ { k + 1 } ^ { + } ) ( \mathbf { x } _ { k + 1 } - \hat { \mathbf { x } } _ { k + 1 } ^ { + } ) ^ { \mathsf { T } } ]$ . By definition, this expected value is the a posteriori error covariance $\mathbf { P } _ { k + 1 } ^ { + }$ . Remember that the eigenvectors of a matrix are the fundamental transformation directions of that matrix, and the eigenvalues are the magnitudes of those transformations. By minimizing the eigenvalues, we minimize the error variance (the uncertainty in the state estimate) for each state.

$\mathbf { P } _ { k + 1 } ^ { + }$ is positive definite, so we know all the eigenvalues are positive. Therefore, a reasonable quantity to minimize with our choice of Kalman gain is the sum of the eigenvalues. We don’t have direct access to the eigenvalues, but we can use the fact that the sum of the eigenvalues is equal to the trace of $\mathbf { P } _ { k + 1 } ^ { + }$ P+ and minimize that instead.[4]

We’ll start with the equation for $\mathbf { P } _ { k + 1 } ^ { + }$ .

$$\mathbf {P} _ {k + 1} ^ {+} = (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) \mathbf {P} _ {k + 1} ^ {-} (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}$$

We’re going to expand the equation for $\mathbf { P } _ { k + 1 } ^ { + }$ and collect terms. First, multiply in P−k+1 . $\mathbf { P } _ { k + 1 } ^ { - }$

$$\mathbf {P} _ {k + 1} ^ {+} = (\mathbf {P} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}) (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}$$

Tranpose each term in $\mathbf { I } - \mathbf { K } _ { k + 1 } \mathbf { C } _ { k + 1 }$ . I is symmetric, so its transpose is dropped.

$$\mathbf {P} _ {k + 1} ^ {+} = (\mathbf {P} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}) (\mathbf {I} - \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}) + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}$$

Multiply in $\mathbf { I } - \mathbf { C } _ { k + 1 } ^ { \top } \mathbf { K } _ { k + 1 } ^ { \top }$
