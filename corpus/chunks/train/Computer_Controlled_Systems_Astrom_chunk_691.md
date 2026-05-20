# Model Complexity

One criticism of LQ-control is that an accurate full-order model of the process must be available. Most physical processes are of high order. However, for control purposes it is often sufficient to use a low-order approximation. Ways to obtain mathematical models are discussed in Chapter 13.

One way to decrease the sensitivity to modeling errors is to decrease the desired bandwidth of the closed-loop system by changing the weightings in the loss function. Compare this with the robustness results in Sec. 3.3. Another way to decrease the sensitivity to modeling errors is to introduce artificial noise, which means that the noise covariances used in the design of the Kalman filter are larger than the true values.
