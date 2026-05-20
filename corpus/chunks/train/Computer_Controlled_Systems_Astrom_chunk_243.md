# Reconstruction Using a Dynamic System

Let n be the order of the system. The direct calculation we have just performed gives the state after at most n measurements of input-output pairs. The disadvantage of the method is that it may be sensitive to disturbances; the operations done on the data are typically to form differences, as illustrated in Example 4.7. It is therefore useful to have other alternatives that are less sensitive to noise.

Consider the system (4.23). Assume that the state x is to be approximated by the state $\hat{x}$ of the model

$$\hat {x} (k + 1) = \Phi \hat {x} (k) + \Gamma u (k) \tag {4.27}$$

which has the same input as the system of (4.23). If the model is perfect in the sense that the elements of the matrices $\Phi$ and $\Gamma$ are identical to those of the system (4.23) and if the initial conditions are the same, then the state $\hat{x}$ of the model of (4.27) will be identical to the state $x$ of the true system in (4.23). If the initial conditions are different, then $\hat{x}$ will converge to $x$ only if the system (4.27) is asymptotically stable.

Reconstruction by Eq. (4.27) gives the state as a function of past input. The reconstruction can be improved by also using the measured outputs. This can be done by introducing a feedback from the difference between the measured and estimated outputs, $y - C\hat{x}$ . Hence

$$\hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k - 1) + \Gamma u (k) + K \left(y (k) - C \hat {x} (k \mid k - 1)\right) \tag {4.28}$$

where K is a gain matrix. The notation $\hat{x}(k+1 \mid k)$ is used to indicate that it is an estimate of $x(k+1)$ based on measurements available at time k, that is, a one-step prediction. Notice that the feedback term $K[y(k)-C\hat{x}(k \mid k-1)]$ gives no contribution if the output predicted by the model agrees exactly with the measurements. To determine the matrix K we introduce the reconstruction error

$$\tilde {x} = x - \hat {x} \tag {4.29}$$

Subtraction of (4.28) from (4.23) gives

$$\tilde {x} (k + 1 \mid k) = \Phi \tilde {x} (k \mid k - 1) - K (y (k) - C \hat {x} (k \mid k - 1)) = (\Phi - K C) \tilde {x} (k \mid k - 1) \tag {4.30}$$
