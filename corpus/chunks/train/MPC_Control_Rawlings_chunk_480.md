# 4.4 Extended Kalman Filtering

The extended Kalman filter (EKF) generates estimates for nonlinear systems by first linearizing the nonlinear system, and then applying the linear Kalman filter equations to the linearized system. The approach can be summarized in a recursion similar in structure to the Kalman filter (Stengel, 1994, pp.387–388)

$$
\begin{array}{l} \hat {x} ^ {-} (k + 1) = f (\hat {x} (k), 0) \\ P ^ {-} (k + 1) = \overline {{A}} (k) P (k) \overline {{A}} (k) ^ {\prime} + \overline {{G}} (k) Q \overline {{G}} (k) ^ {\prime} \\ \hat {x} ^ {-} (0) = \overline {{{{x}}}} _ {0} \quad P ^ {-} (0) = Q _ {0} \\ \end{array}
$$

The mean and covariance after measurement are given by

$$
\begin{array}{l} \hat {x} (k) = \hat {x} ^ {-} (k) + L (k) (y (k) - h (\hat {x} ^ {-} (k))) \\ L (k) = P ^ {-} (k) \overline {{{C}}} (k) ^ {\prime} (R + \overline {{{C}}} (k) P ^ {-} (k) \overline {{{C}}} (k) ^ {\prime}) ^ {- 1} \\ P (k) = P ^ {-} (k) - L (k) \overline {{{C}}} (k) P ^ {-} (k) \\ \end{array}
$$

in which the following linearizations are made

$$\overline {{A}} (k) = \left. \frac {\partial f (x , w)}{\partial x} \right| _ {(\hat {x} (k), 0)} \quad \overline {{G}} (k) = \left. \frac {\partial f (x , w)}{\partial w} \right| _ {(\hat {x} (k), 0)} \quad \overline {{C}} (k) = \left. \frac {\partial h (x)}{\partial x} \right| _ {\hat {x} ^ {-} (k)}$$

The densities of w, v and $x _ { 0 }$ are assumed to be normal. Many variations on this theme have been proposed, such as the iterated EKF and the second-order EKF (Gelb, 1974, 190–192). Of the nonlinear filtering methods, the EKF method has received the most attention due to its relative simplicity and demonstrated effectiveness in handling some nonlinear systems. Examples of implementations include estimation for the production of silicon/germanium alloy films (Middlebrooks and Rawlings, 2006), polymerization reactions (Prasad, Schley, Russo, and Bequette, 2002), and fermentation processes (Gudi, Shah, and Gray, 1994). The EKF is at best an ad hoc solution to a difficult problem, however, and hence there exist many pitfalls to the practical implementation of EKFs (see, for example, (Wilson, Agarwal, and Rippin, 1998)). These problems include the inability to accurately incorporate physical state constraints and the naive use of linearization of the nonlinear model.
