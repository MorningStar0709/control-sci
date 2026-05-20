# EXAMPLE 1.6 Short-period aircraft dynamics

A schematic diagram of an airplane is given in Fig. 1.12. To illustrate the effect of parameter variations, we consider the pitching motion of the aircraft. Introduce the pitch angle $\theta$ . Choose normal acceleration $N_{z}$ , pitch rate $q = \dot{\theta}$ , and elevon angle $\delta_{e}$ as state variables and the input to the elevon servo as the input signal u. The following model is obtained if we assume that the aircraft is a rigid body:

![](image/e928361a506d093dc53710668e18bb299874fc2e78eef780eece2988af4ff4f9.jpg)

<details>
<summary>text_image</summary>

q = \u0394θ
θ
α
V
Nz
δe
</details>

Figure 1.12 Schematic diagram of the aircraft in Example 1.6.

$$
\frac {d x}{d t} = \left( \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ 0 & 0 & - a \end{array} \right) x + \left( \begin{array}{c} b _ {1} \\ 0 \\ a \end{array} \right) u \tag {1.6}
$$

where $x^{T} = \left( N_{z} \quad \dot{\theta} \quad \delta_{e} \right)$ . This model is called short-period dynamics. The parameters of the model given depend on the operating conditions, which can be described in terms of Mach number and altitude; see Fig. 1.13, which shows the flight envelope.

Table 1.1 shows the parameters for the four flight conditions (FC) indicated in Fig. 1.13. The data applies to the supersonic aircraft F4-E. The system has three eigenvalues. One eigenvalue, -a = -14, which is due to the elevon servo, is constant. The other eigenvalues, $\lambda_{1}$ and $\lambda_{2}$ , depend on the flight conditions. Table 1.1 shows that the system is unstable for subsonic speeds (FC 1, 2, and 3) and stable but poorly damped for the supersonic condition FC 4. Because of these variations it is not possible to use a controller with the same parameters for all flight conditions. The operating condition is determined from air data sensors that measure altitude and Mach number. The controller parameters are then changed as a function of these parameters. How this is done is discussed in Chapter 9.

Much more complicated models will have to be considered in practice because the airframe is elastic and will bend. Notch prefilters on the command signal from the pilot are also used so that the control actions will not excite the bending modes of the airplane.

![](image/cc8f1bffea84cd29c67e769ca540d951cc32ec0cb3554e31449adf552da277d0.jpg)

<details>
<summary>line</summary>
