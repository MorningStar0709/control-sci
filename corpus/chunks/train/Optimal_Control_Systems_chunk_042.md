4. Performance Index for Terminal Control System: In a terminal target problem, we are interested in minimizing the error between the desired target position $\mathbf{x}_{d}(t_{f})$ and the actual target position $\mathbf{x}_{a}(t_{f})$ at the end of the maneuver or at the final time $t_{f}$ . The terminal (final) error is $\mathbf{x}(t_{f}) = \mathbf{x}_{a}(t_{f}) - \mathbf{x}_{d}(t_{f})$ . Taking care of positive and negative values of error and weighting factors, we structure the cost function as

$$J = \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} \mathbf {x} (t _ {f}) \tag {1.3.7}$$

which is also called the terminal cost function. Here, $\mathbf{F}$ is a positive semi-definite matrix.

5. Performance Index for General Optimal Control System: Combining the above formulations, we have a performance index in general form as

$$J = \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F x} (t _ {f}) + \int_ {t _ {0}} ^ {t _ {f}} [ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) ] d t \tag {1.3.8}$$

or,

$$J = S \left(\mathbf {x} \left(t _ {f}\right), t _ {f}\right) + \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t \tag {1.3.9}$$

where, R is a positive definite matrix, and Q and F are positive semidefinite matrices, respectively. Note that the matrices Q and R may be time varying. The particular form of performance index (1.3.8) is called quadratic (in terms of the states and controls) form.
