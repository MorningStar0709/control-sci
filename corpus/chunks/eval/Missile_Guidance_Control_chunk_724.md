The functions that must be performed within the various NAM modules are as follows: (1) within the NAM data format validation, (a) evaluate buffer table data for range limits, (b) evaluate buffer record sequences, (c) evaluate waypoint locations before and after map areas, and (d) output error messages and waypoint recomputation flags as necessary; (2) within navigation matrix initialization, (a) read and load proper start navigation matrices and data, (b) build navigation matrices. Also, the following functions must be performed: (1) set matrices to alignment initialization, (2) propagate backward from launch point to alignment initialization (power on), to establish alignment initialization position and direction cosine matrix, (3) propagate error covariance matrix forward from alignment initialization to launch point, and (4) combine carrier error covariance matrix with the alignment error covariance matrix to obtain initial free-flight error covariance matrix.

I. Within inertial computations, the following must be performed:

1. Compare Earth relative angular velocity and propagate the direction cosine matrix (DCM) C.   
2. Calculate the state transition matrix .   
3. Calculate the process noise matrix Q.   
4. Propagate the error covariance matrix P according to [9]:

$$P _ {i} = \Phi_ {i} P _ {i - 1} \Phi_ {i} ^ {T} + Q _ {i}. \tag {7.1}$$

II. Within primary T C computations, perform the following:

(1) At the first map in a voting group save the error covariance matrix.   
(2) Calculate the accumulated state transition matrix $\Phi ^ { \prime }$ between map centers according to

$$\Phi_ {i} ^ {\prime} = \Phi_ {i - 1} ^ {\prime} + \Phi_ {i}, \tag {7.2}$$

where $\Phi _ { i } ^ { \prime }$ is reset to the identity matrix at step centers.

(3) Calculate the accumulated process noise matrix $Q ^ { \prime }$ between map centers according to

$$Q _ {i} ^ {\prime} = Q _ {i - 1} ^ {\prime} + Q _ {i}, \tag {7.3}$$

where $Q _ { i } ^ { \prime }$ is reset to zero at map centers.

(4) Save the accumulated matrices at map centers before resetting values.

(5) Calculate and save one-sigma downtrack and crosstrack errors at map centers.

III. Within secondary TC computations, perform the following:
