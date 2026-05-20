9. Propagate Covariance Matrix: The error covariance matrix propagation consists of the propagation of a covariance matrix P of navigation errors at a fixed propagation interval of 60 seconds unless terrain correlation is in progress (i.e., between map centers) when it is 12 seconds. The navigation error state consists of fifteen elements. These are x, y position error; x, y velocity error; x, y platform tilt; platform azimuth error; x, y, z gyroscope bias drift rates; computer azimuth error; x, y gyrotorquer scale factor error; and x, y accelerometer scale factor error. The covariance matrix is updated at terrain correlation position fixes where special logic is used to accommodate the time delay in the updates due to the voting logic and characteristics of the terrain correlation process. This submodule also stores and saves elements of Q for output calculations, saves accumulated state transition and process noise matrices, and resets the temporary accumulation matrix variables.

10. Primary TC Computations: This module calculates the intermap accumulated state transition matrix $\Phi ^ { \prime }$ and the accumulated process noise matrix $Q ^ { \prime }$ , as in (7.2) and (7.3):

$$\Phi_ {i} ^ {\prime} = \Phi_ {i} + \Phi_ {i - 1} ^ {\prime}, \tag {7.2}Q _ {i} ^ {\prime} = Q _ {i} + Q _ {i - 1} ^ {\prime}, \tag {7.3}$$

where the initial values of $\Phi ^ { \prime }$ and $Q ^ { \prime }$ starting at a map center are

$$\Phi^ {\prime} = I (\text { the identity matrix }),Q ^ {\prime} = 0 (\text {zero matrix}).$$

These propagations actually take place after calculation of  and $Q$ within the “inertial computations module” but before the propagation of the covariance matrix P .

11. Secondary TC Computations:

11.1 Perform Kalman Filter Updates: This submodule uses crosstrack and downtrack one-sigma $( 1 - \sigma )$ error values to establish a $2 \times 2$ matrix R. Moreover, R, P , and the previously defined measurement matrix H are used to develop the Kalman gain matrix K according to

$$K = P H ^ {T} (H P H ^ {T} + R) ^ {- 1}, \tag {7.4}$$

where K, P , and R are values established at a map center. The covariance matrix is updated at the map center according to

$$P ^ {+} = (I - K H) P, \tag {7.5}$$

where I is the unity matrix and $P ^ { + }$ is the updated covariance matrix. This matrix $P ^ { + }$ is used with the stored accumulation matrices $\Phi ^ { \prime }$ and $Q ^ { \prime }$ to propagate P to the next map center according to
