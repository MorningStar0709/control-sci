# Pure Pursuit

In the pure pursuit trajectory, the interceptor missile flies directly toward the target at all times. Thus, the heading of the missile is maintained essentially along the line of sight between the missile and the target by the guidance system. Missiles flying a pure pursuit course usually end up in a tail-chase situation, similar to a dog chasing a rabbit. Furthermore, in pure pursuit the nose of the interceptor missile (note that the term interceptor is used to denote missiles as well as fighter aircraft) is pointed at the target aircraft. The interceptor missile directing its velocity vector toward the target flies a pure pursuit attack course. In such a case the interceptor’s lead angle is zero. Consider now Figure 4.8.

![](image/68b6e078911173790990449d29ad1009cc9e695b39133350897ad2676105ea06.jpg)  
Fig. 4.7. Derivation of the guidance equations.

The decomposition of the velocity vector components along and perpendicular to R yields the following equations:

$$\frac {d R}{d t} = V _ {M} - V _ {T} \sin \theta , \tag {4.13a}R \left(\frac {d \theta}{d t}\right) = - V _ {T} \cos \theta , \tag {4.13b}$$

![](image/6db81c7657b0706952788b638a9810dbb26a039386946c40f1ad9b7622207983.jpg)

<details>
<summary>text_image</summary>

V_T
θ
R
V_M
</details>

Fig. 4.8. Pure pursuit guidance geometry.

where R is the range magnitude, θ is the orientation of the line of sight to the target, $V _ { M }$ is the interceptor missile velocity component, and $V _ { T }$ is the target’s velocity. For the special but nontrivial cases of a stationary target or head/tail chase $( \theta = \pm { 9 0 ^ { \circ } } )$ , we have

$$\left(\frac {d R}{d t}\right) / R = \{(1 / \cos \theta) (V _ {M} / V _ {T}) + \tan \theta \} \left(\frac {d \theta}{d t}\right) = \{(\kappa / \cos \theta) + \tan \theta \} \left(\frac {d \theta}{d t}\right), \tag {4.14}$$

where $\kappa = V _ { M } / V _ { T }$ . For a constant speed ratio κ, the following expression results:

$$\int (d R / R) = \int \tan \theta d \theta + \kappa \int (d \theta / \cos \theta). \tag {4.15}$$

Letting C be the constant of integration, the general solution of (4.15) assumes the form

$$l n (R / C) = - l n \cos \theta + (\kappa / 2) l n [ (1 + \sin \theta) / (1 - \sin \theta) ].$$

Therefore,

$$R / C = (1 / \cos \theta) [ (1 + \sin \theta) / (1 - \sin \theta) ] ^ {\kappa / 2}.$$

From the identity

$$1 / \cos \theta = 1 / (1 + \sin \theta) ^ {1 / 2} (1 - \sin \theta) ^ {1 / 2}$$

we have
