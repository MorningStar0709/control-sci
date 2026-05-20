# 6.4.3.1 In-Plane Error Coefficients

In the guidance problem of ballistic missiles, it is important to know how, for example, the range and velocity are dependent upon the other variables affecting the problem. The purpose of this section is to derive the partial derivatives of range and velocity with respect to the other variables. The total set of error coefficients consists of two independent subsets: (1) the coefficients that generate position and velocity changes in the plane of the free-fall trajectory, and (2) those that generate changes normal to the plane of the free-fall trajectory. The derivation of the in-plane coefficients involves time explicitly. The normal-to-plane coefficients, on the other hand, are derived solely on the basis of trajectory geometry and do not involve time explicitly. The coordinate system and geometry upon which the in-plane coefficients are based are shown in Figure 6.18.

We will formulate the problem in polar coordinates, using a rotating radial– transverse coordinate system with unit vectors rˆ and $\widehat { \pmb { \theta } } .$ In this coordinate system, the position and velocity vectors are given by

$$\mathbf {r} = r \hat {\mathbf {r}} \tag {6.118}$$

and

$$\mathbf {V} = \frac {d \mathbf {r}}{d t} = \left(\frac {d r}{d t}\right) \hat {\mathbf {r}} + r \left(\frac {d \theta}{d t}\right) \hat {\boldsymbol {\theta}} = V _ {r} \hat {\mathbf {r}} + V _ {\theta} \hat {\boldsymbol {\theta}}, \tag {6.119}$$

![](image/24edeb4237375981f6d7688f7835250e2bdc3001ad3e56c8b341e1efc4600014.jpg)  
DR = R cos B   
CR = –Rδ L sin B   
DR = R cos L sin B   
CR = –R cos L cos B   
R = radius of the earth   
B = Bearing angle   
L = Latitude   
= Longitude   
Longitude position effect   
DR = 0   
CR = –Reδ sin L sin   
Longitude bearing effect

Fig. 6.17. Relation of latitude and longitude to position errors.

where

$$V _ {r} \cong \frac {d r}{d t}, \tag {6.120a}$$

and

$$V _ {\theta} \cong r \left(\frac {d \theta}{d t}\right). \tag {6.120b}$$

Again, referring to Figure 6.18, the four initial conditions at burnout that determine the subsequent free-fall trajectory are V, γ , h, and $\theta _ { o }$ . Perturbations in any one of these burnout variables cause position and velocity changes at the endpoint of the trajectory. (Note that here we will drop the subscript(s) from the required velocity vector V in order not to confuse it with the components of $V _ { r }$ and $V _ { \theta } . )$
