# 7.5.1 GPS/INS Integration

In many applications, GPS/INS integration is necessary. Specifically, this integration has proved to be a very efficient means of navigation, primarily because of the shortterm accuracy achieved by the inertial navigation system (INS) and the long-term accuracy of the GPS fixes. Two versions of the GPS/INS integration are available. These are (1) the tightly coupled GPS/INS, and (2) the loosely couple or modular GPS/INS. Here we will briefly discuss the tightly coupled version, because its ability to perform optimal signal processing allows the various errors and noise sources (e.g., clock delays, atmospheric effects, inertial instrument biases) acting on both the GPS and INS units to be taken into account in a global way. Kalman filtering has been a popular tool for handling estimation problems (see also Section 4.8). However, its optimality depends on linearity. When used in nonlinear filtering (i.e., extended Kalman filter (EKF)), its performance relies on, and is limited by, the linearizations performed on the model in question. Moreover, implementation of nonlinear filters has been plagued so far by the difficulties inherent to their infinite-dimensional nature. Nevertheless, for the reader’s convenience, the discrete form of the conventional Kalman filter will be given here [1], [4], [9].

System Model:

$$
\begin{array}{l} \mathbf {x} _ {k} = \Phi_ {k - 1} \mathbf {x} _ {k - 1} + \mathbf {w} _ {k - 1} \\ \mathbf {w} _ {k} \sim N (0, Q _ {k}). \\ \end{array}
$$

Measurement Model:

$$
\begin{array}{l} \mathbf {z} _ {k} = H _ {k} \mathbf {x} _ {k} + \mathbf {v} _ {k}, \\ \mathbf {v} _ {k} \sim N (0, R _ {k}). \\ \end{array}
$$

Initial Conditions:

$$
\begin{array}{l} E \{\mathbf {x} (0) \} = \hat {\mathbf {x}} _ {o}, \\ E \{(\mathbf {x} (0) - \hat {\mathbf {x}} _ {o}) (\mathbf {x} (0) - \hat {\mathbf {x}} _ {o}) ^ {T} \} = P _ {o}. \\ \end{array}
$$

Other Assumptions:

$$E \{\mathbf {w} _ {k} \mathbf {v} _ {\mathbf {j}} ^ {T} \} = 0 \forall j, k.$$

State Estimate Extrapolation:

$$\hat {\mathbf {x}} _ {k} (-) = \Phi_ {k - 1} \hat {\mathbf {x}} _ {k - 1} (+).$$

(Note: the (−) sign denotes the time immediately before a discrete measurement, and (+) the time immediately after a discrete measurement.)

Error Covariance Extrapolation:

$$P _ {k} (-) = \Phi_ {k - 1} P _ {k - 1} (+) \Phi_ {k - 1} ^ {T} + Q _ {k - 1}.$$

State Estimate Update:
