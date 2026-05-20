# 1.3 Optimal Control

low a state variable (or trajectory) and at the same time extremize a performance index which may take several forms as described below.

1. Performance Index for Time-Optimal Control System: We try to transfer a system from an arbitrary initial state $\mathbf{x}(t_0)$ to a specified final state $\mathbf{x}(t_f)$ in minimum time. The corresponding performance index (PI) is

$$J = \int_ {t _ {0}} ^ {t _ {f}} d t = t _ {f} - t _ {0} = t ^ {*}. \tag {1.3.1}$$

2. Performance Index for Fuel-Optimal Control System: Consider a spacecraft problem. Let $u(t)$ be the thrust of a rocket engine and assume that the magnitude $|u(t)|$ of the thrust is proportional to the rate of fuel consumption. In order to minimize the total expenditure of fuel, we may formulate the performance index as

$$J = \int_ {t _ {0}} ^ {t _ {f}} | u (t) | d t. \tag {1.3.2}$$

For several controls, we may write it as

$$J = \int_ {t _ {0}} ^ {t _ {f}} \sum_ {i = 1} ^ {m} R _ {i} | u _ {i} (t) | d t \tag {1.3.3}$$

where $R$ is a weighting factor.

3. Performance Index for Minimum-Energy Control System: Consider $u_{i}(t)$ as the current in the ith loop of an electric network. Then $\sum_{i=1}^{m} u_{i}^{2}(t) r_{i}$ (where, $r_{i}$ is the resistance of the ith loop) is the total power or the total rate of energy expenditure of the network. Then, for minimization of the total expended energy, we have a performance criterion as

$$J = \int_ {t _ {0}} ^ {t _ {f}} \sum_ {i = 1} ^ {m} u _ {i} ^ {2} (t) r _ {i} d t \tag {1.3.4}$$

or in general,

$$J = \int_ {t _ {0}} ^ {t _ {f}} \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) d t \tag {1.3.5}$$

where, $\mathbf{R}$ is a positive definite matrix and prime (') denotes transpose here and throughout this book (see Appendix A for more details on definite matrices).

Similarly, we can think of minimization of the integral of the squared error of a tracking system. We then have,

$$J = \int_ {t _ {0}} ^ {t _ {f}} \mathbf {x} ^ {\prime} (t) \mathbf {Q} \mathbf {x} (t) d t \tag {1.3.6}$$

where, $\mathbf{x}_d(t)$ is the desired value, $\mathbf{x}_a(t)$ is the actual value, and $\mathbf{x}(t) = \mathbf{x}_a(t) - \mathbf{x}_d(t)$ , is the error. Here, $\mathbf{Q}$ is a weighting matrix, which can be positive semi-definite.
