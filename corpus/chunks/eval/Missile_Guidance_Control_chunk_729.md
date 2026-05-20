2. Navigation Matrix Initialization: If this is a restart program, then the NAM will obtain route leg and map record information from the IOBT. The error covariance matrix will be initialized with data stored in the IOBT. The direction cosine matrix (DCM) will be initialized using stored values of position, ground speed, and heading. Propagation will proceed from the carrier vehicle action point specified.

3. Build Navigation Matrices: For nonrestart programs, this module initializes the data and matrices for the missile alignment trajectory. The generation of the trajectory is done in two phases. The first stage initializes the DCM with the launch position and propagates backward using data on carrier maneuvers until missile power-on time is reached (which is the assumed beginning of fine alignment). The second stage generates the direction cosines and velocity changes using a normal forward integration at 60-second intervals for use in the computation of the state transition and process noise matrices. These are used for propagation of the error covariance matrix, as in (7.1):

$$P _ {i} = \Phi_ {i} P _ {i - 1} \Phi_ {i} ^ {T} + Q _ {i}, \tag {7.1}$$

where $P _ { i }$ is initially set to $P _ { o } ,$ , the expected navigation error state at the completion of coarse alignment; $\Phi _ { i }$ is the state transition matrix; and $Q _ { i }$ is the process noise. A captive alignment measurement noise matrix R and a measurement matrix H are used for calculating the Kalman gain matrix K, according to

$$K _ {i} = P _ {i} H ^ {T} (H P _ {i} H ^ {T} + R) ^ {- 1}, \tag {7.4}$$

and the error covariance matrix is updated at each iteration or integration step as

$$P _ {i} ^ {+} = \left(I - K _ {i} H\right) P _ {i}, \tag {7.5}$$

where I is the identity matrix. At the completion of captive fine alignment the error covariance matrix corresponds to the error state relative to the carrier aircraft. Therefore, it is necessary to combine the captive alignment error covariance matrix with the carrier covariance matrix $P _ { c }$ at launch to obtain an error covariance matrix of navigation errors relative to an Earth reference frame.

4. Inertial Computations: This module performs the integration steps for propagation of the error covariance matrix. It is processed by three minor submodules that set iteration values, and it is composed of four submodules to perform the propagation.
