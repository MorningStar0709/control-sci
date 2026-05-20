$$J = \int_ {0} ^ {\infty} [ Q _ {3 3} \Delta \omega_ {0} ^ {2} + Q _ {4 4} \Delta_ {1} ^ {2} + Q _ {5 5} \Delta_ {2} ^ {2} + R _ {1 1} u _ {1} ^ {2} + R _ {2 2} u _ {2} ^ {2} ] d t$$

as the performance index.

a. Start with $Q_{33} = 1 / (2)^2$ , $Q_{44} = Q_{55} = 1 / (0.02)^2$ , and $R_{11} = R_{22} = 1 / (180 - u_i^*)^2$ , and calculate the LQ gain. Here, $u_i^*$ , $i = 1, 2$ , are the steady-state values of $u_i$ .   
b. Compute the zero-state response for $\omega_{d}=2.0\ rad/s$ , $u_{1}^{*}=u_{2}^{*}$ . Increase weights where constraints are violated; decrease if some “play” is still possible. Repeat parts (a) and (b) until the constraints are reasonably close to being just satisfied.   
c. Repeat the process with only one input, $u_{1}$ . (You will need to reduce the model.) To get a fair comparison, allow $u_{1}$ to have a magnitude of 360 V (to get the same total torque). Compare the responses $\omega_0$ for the cases of one and two control variables.

M

7.24 Blending tank A linearized model was found in Problem 2.13 (Chapter 2) for the blending tank of Problem 2.7.

a. Using the linearized model, calculate the steady-state values of the control and state variables for $\Delta C_A^* = 0.1$ , $\Delta \ell^* = 0$ , $\Delta F_B^* = 1 \times 10^{-5} \mathrm{~m}^3/\mathrm{s}$ .   
b. We wish to move from the steady state of Problem 2.13 to the new steady state of part (a) without undue liquid flow variations or changes in liquid level. Specifically, we require $|\Delta\ell(t)| \leq 0.02$ m and $|\Delta F_{A}|$ , $|\Delta F_{0}| \leq 0.5 \times 10^{-4}$ m $^{3}$ /s. Use

$$J = \int_ {0} ^ {\infty} [ Q _ {1 1} \Delta \ell^ {2} + R _ {1 1} \Delta F _ {A} ^ {2} + R _ {2 2} \Delta F _ {0} ^ {2} ] d t$$

with $Q_{11}=1/(0.02)^{2}$ and $R_{11}=R_{22}=1/(0.5\times10^{-4})^{2}$ as initial guesses. Compute the optimal gain, and express the control law for $\Delta F_{A}$ and $\Delta F_{0}$ , referred to the original steady state. Note: This control law should have a linear feedforward term in $F_{B}$ , also referred to the original values.

c. Simulate the transient to the new steady state and adjust $R_{11}$ and $R_{22}$ until (i) the specifications are met and (ii) the speed of response of $\Delta C(t)$ is maximized.

M
