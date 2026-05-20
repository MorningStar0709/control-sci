$$J = \int_ {0} ^ {\infty} [ Q (\Delta C _ {A} (t) - \Delta C _ {A d} (t) ] ^ {2} + R \Delta F _ {0} ^ {2} + R \Delta F _ {A} ^ {2} ] d t$$

and give the control law. Start with $Q = 1 / (.8)^2$ and $R = 1 / (10^{-4})^2$ . Adjust $R$ so that, for $\Delta \ell(0) = \Delta V_A(0) = 0$ and $\Delta C_{Ad}^* = 0.1$ , the error $\Delta C_A(t) - \Delta C_{Ad}$ is minimized, while $|\Delta F_A(t)|$ and $|\Delta F_0(t)|$ are held below $0.5 \times 10^{-4} \mathrm{~m}^3/\mathrm{s}$ .

![](image/57e907daef9ef1e9b5631a0fe40b9ffabb58a9c04aaea9b9557fcf45daab4e08.jpg)

7.36 Heat exchanger A heat exchanger is often a good candidate for the use of feedforward control. A pole-placement design was carried out in Problem 7.12, based on the linearized model of Problem 2.14 (Chapter 2). The major disturbance input is $\Delta T_{C0}$ , the cold liquid inlet temperature.

a. Use the linearized model of Problem 2.14 with the control law of Problem 7.12. For the system initially in the nominal dc steady state, compute $\Delta T_{C3}(t)$ for a step increase of $2^{\circ}\mathrm{C}$ in $T_{C0}$ .   
b. We now add feedforward. Use the linearized model to calculate the steady-state incremental input $\Delta F_H^*$ that corresponds to the same steady-state outlet temperature as before ( $\Delta T_{C3}^* = 0$ ), but with $\Delta T_{C0}^* \neq 0$ . Use the linear expression for $\Delta F_H^*$ as a function of $\Delta T_{C0}^*$ as a feedforward term in the control law, and repeat the simulation of part (a).

7.37 For the system of Problem 7.1, design a second-order observer such that the poles of the error system are at $-3 \pm j\sqrt{3}$ . Calculate the state $\mathbf{x}(t)$ and the estimate $\widehat{\mathbf{x}}(t)$ , given that $u(t)$ is a unit step, $\mathbf{x}(0) = [{}]$ , and $\widehat{\mathbf{x}}(0)$ is the zero state.

7.38 Repeat Problem 7.37 for the system of Problem 7.2.

![](image/73cd97db7a7d9b77f543785156158e89d0d32abff6b0f5166bee864f1e3a4bf2.jpg)

7.39 Heat exchanger The heat exchanger model of Problem 2.8 (Chapter 2) was linearized about a particular dc steady state in Problem 2.14. The outlet temperature $\Delta T_{C3}$ is measured, and we wish to design an observer to estimate the other state variables.

a. With $\Delta T_{C0} = \Delta T_{H0} = 0$ and with $\Delta F_H$ and $\Delta F_C$ available for measurement, design an observer with error system poles at $-1 \pm j$ , $-.8 \pm j.8$ , $-1$ , and $-1.1$ .
