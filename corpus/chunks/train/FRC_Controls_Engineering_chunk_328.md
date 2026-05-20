# 9.9.2 Square-root UKF

The UKF uses a matrix square root (Cholesky decomposition) to compute the scaling for the sigma points. This operation can introduce numerical instability. The squareroot UKF[12] avoids this by propagating the square-root of the error covariance directly instead of the error covariance; the Cholesky decomposition is replaced with a QR decomposition and a Cholesky rank-1 update.
