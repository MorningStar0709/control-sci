$$p _ {1 1} = \sigma_ {D R} ^ {2},p _ {2 2} = \sigma_ {D R} ^ {2},p _ {1 2} = p _ {2 1} = \rho_ {C R, D R} \sigma_ {C R} \sigma_ {D R},$$

or

$$
P = \left[ \begin{array}{c c} \sigma_ {D R} ^ {2} & \rho_ {C R, D R} \sigma_ {C R} \sigma_ {D R} \\ \rho_ {C R, D R} \sigma_ {C R} \sigma_ {D R} & \sigma_ {C R} ^ {2} \end{array} \right], \tag {5.96}
$$

where the statistical correlation coefficient $\rho _ { C R , D R }$ is given in terms of the cross-range and down-range position errors by

$$E \{x _ {C R} y _ {D R} \} / \sigma_ {C R} \sigma_ {D R} = E \{x _ {C R} y _ {D R} \} / \sigma_ {x _ {C R}} \sigma_ {y _ {D R}}. \tag {5.97}$$

The position error covariance matrix is a tensor that defines an ellipse of constant probability indicating the variances and covariances of the down-range and crossrange position errors as shown in Figure 5.38.

Define now

$$h \triangleq [ (\sigma_ {y _ {D R}} ^ {2} - \sigma_ {x _ {C R}} ^ {2}) ^ {2} + 4 A ^ {2} ] ^ {1 / 2}, \tag {5.98a}$$

where $A = \rho \sigma _ { x } \sigma _ { y } = \rho \sigma _ { x _ { C R } } \sigma _ { y _ { D R } }$ . After some algebra we obtain the covariances in the form

$$\sigma_ {x _ {C R}} ^ {2} = \frac {1}{2} (\sigma_ {x _ {C R}} ^ {2} + \sigma_ {y _ {D R}} ^ {2} + h), \tag {5.98b}\sigma_ {x _ {C R}} ^ {2} = \frac {1}{2} (\sigma_ {x _ {C R}} ^ {2} + \sigma_ {y _ {D R}} ^ {2} - h), \tag {5.98c}$$

and

$$\theta = \frac {1}{2} \tan^ {- 1} [ 2 \rho_ {C R, D R} \sigma_ {x _ {C R}} \sigma_ {y _ {D R}} / (\sigma_ {D R} ^ {2} - \sigma_ {C R} ^ {2}) ]. \tag {5.98d}$$

The radius of the circle of 50% equivalent probability is obtained as follows:

For $\sigma _ { y } ^ { 2 } / \sigma _ { x } ^ { 2 } \ge 0 . 9$

$$R _ {C E P} = 0. 5 6 2 \sigma_ {x} + 0. 6 1 5 \sigma_ {y}. \tag {5.99a}$$

For $\sigma _ { y } ^ { 2 } / \sigma _ { x } ^ { 2 } \le 0 . 9 ,$

$$R _ {C E P} = \sigma_ {y} [ 0. 6 7 5 + 0. 8 3 5 (\sigma_ {y} ^ {2} / \sigma_ {x} ^ {2}) ]. \tag {5.99b}$$

Another way to compute the CEP is as follows. Assume that, by the central limit theorem, the probability density function describing target miss distance will be normal. Then,

$$f (x, y) = (1 / 2 \pi \sigma_ {x} \sigma_ {y}) \exp \{- 1 / 2 [ (x / \sigma_ {x}) ^ {2} + (y / \sigma_ {y}) ^ {2} ] \}. \tag {5.100}$$

When this function is integrated over the ellipse (see Figure 5.38) whose major axis is $C E P \bullet \sigma _ { x }$ and set equal to $\frac { 1 } { 2 }$ , the major axis becomes $1 . 1 7 7 4 \sigma _ { x }$ , and the minor axis becomes $1 . 1 7 7 4 \sigma _ { y }$ . When these are averaged, the familiar formula results:

$$C E P = 0. 5 8 8 7 (\sigma_ {x} + \sigma_ {y}). \tag {5.101}$$
