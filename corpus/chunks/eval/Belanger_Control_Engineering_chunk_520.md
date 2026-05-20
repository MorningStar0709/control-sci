8.16 Heat exchanger A linearized model for the heat exchanges of Problem 2.8 (Chapter 2) is given in Problem 2.14. The two control inputs $\Delta F_{c}$ and $\Delta F_{H}$ are to be used to control the temperature outputs $\Delta T_{c3}$ and $\Delta T_{H3}$ . The interaction is to be minimized; i.e., the response of $\Delta T_{H3}$ to a set-point change $\Delta T_{c3d}$ should be small, as should the response of $\Delta T_{c3}$ to a set-point change $\Delta T_{H3d}$ . Also, the model is known to hold only to about 2 rad/min. The following specifications are given:

a. Let $T_{\mathrm{d3}}$ be defined by the relation $[\Delta T_{c3}] = T_{d3}[\Delta T_{c3d}]$ , and let $W_{1}(s) = 20 / (s + 1)$ . Then

$$\left\| W _ {1} \frac {\Delta T _ {c 3 d} - \Delta T _ {c 3}}{\Delta T _ {c 3 d}} \right\| _ {\infty} \leq 1\left\| W _ {1} \frac {\Delta T _ {H 3 d} - \Delta T _ {H 3}}{\Delta T _ {H 3 d}} \right\| _ {\infty} \leq 1\left\| W _ {1} \frac {\Delta T _ {c 3}}{\Delta T _ {H 3 d}} \right\| _ {\infty} \leq 1\left\| W _ {1} \frac {\Delta T _ {H 3}}{\Delta T _ {c 3 d}} \right\| _ {\infty} \leq 1.$$

b. Let $W_{2}(s) = 0.1(0.5s + 1)$ . Then

$$\| W _ {2} T _ {d 3} \| _ {\infty} \leq 1.$$

c. To keep the two flows down to reasonable values,

$$\left\| \alpha T _ {d F} \right\| \leq 1$$

where $T_{dF}$ is the transmission from $\left[\begin{array}{c}T_{c3d}\\ T_{H3d}\end{array}\right]$ to $\left[\begin{array}{c}\Delta F_c\\ \Delta F_H\end{array}\right]$ .

Design an $H^{\infty}$ control with as large a value of $\alpha$ as possible. Display (i) the weighted frequency responses corresponding to the specifications and (ii) the four transmissions, from the two set points to the two temperature outputs. (It may be necessary to add fictitious measurement noise to the measured outputs.)

M

8.17 Two-pendula problem The two-pendula problem of Problem 2.19 (Chapter 2) is really a regulator problem, but we shall nevertheless do a design for a step change in the set point $x_{d}$ . The model derived in Problem 2.19 is the linearized model; use $\ell_1 = 1\mathrm{m}$ , $\ell_2 = 0.75\mathrm{m}$ .

We need to keep $x$ bounded in order to have a finite "track" for the cart. At the same time, excursions from the vertical must also be kept down, to avoid nonlinear behavior. We let $T_{de} = (x_d - x) / x_d$ , $T_{d\theta_1} = \theta_1 / x_d$ , $T_{d\theta_2} = \theta_2 / x_d$ , and $T_{dF} = F / x_d$ . The specifications are as follows:
