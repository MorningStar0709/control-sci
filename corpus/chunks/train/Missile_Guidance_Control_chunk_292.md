# Command Guidance

In Section 4.2.2 the concept of command guidance was discussed. Here we will present some of the mathematical aspects of command guidance. A command guidance scheme, shown in Figure 4.16, consists of missile guidance commands calculated at the launch (or ground) site and transmitted to the missile.

The Patriot MIM-104 surface-to-air missile (SAM) is an example of a radarcommand-guided system using a multifunction phased array (i.e., electronically scanning) radar. The Patriot’s accuracy is due to its TVM terminal guidance method. Targets are selected by the system and illuminated by its ground or ECS (engagement control station) phased-array radars. A lateral error command guidance scheme is used for many of the SAM systems. In a command guidance system, the ground site tracks the target and missile and transmits acceleration commands to the missile, which are proportional to the lateral displacement error from the desired course. Several variations of this scheme that have been implemented in various SAM programs are described below. Figure 4.17 illustrates the lateral error components in the elevation plane for command guidance.

Assuming small-angle approximations, the lateral displacement from the missile to the desired course, $\lambda _ { \varepsilon }$ , and the displacement from the site to the target, $D _ { \varepsilon }$ , can be expressed as

$$D _ {\varepsilon} = R _ {m} (\theta_ {D} - \theta_ {t}), \tag {4.53a}\lambda_ {\varepsilon} + D _ {\varepsilon} = R _ {m} (\theta_ {m} - \theta_ {t}). \tag {4.53b}$$

Subtracting these equations gives the missile’s lateral error from the desired course:

$$\lambda_ {\varepsilon} = R _ {m} (\theta_ {m} - \theta_ {t}) - R _ {m} (\theta_ {D} - \theta_ {t}). \tag {4.54}$$

![](image/4ac33452bd683aa2e98802b882691ef9573a3493cca29bcb43a847cedbec6289.jpg)

<details>
<summary>text_image</summary>

z
λε
θmt
Rt
Dε
Rm
θm θD θt
Launch site
x
</details>

Fig. 4.17. Command guidance geometry.

In order to achieve an intercept, the missile and target range must be the same when the time-to-go $t _ { g o }$ is zero. This condition can exist only if

$$\theta_ {D} = \theta_ {t} + \left(\frac {d \theta_ {t}}{d t}\right) t _ {g o}, \tag {4.55}$$

where

$$t _ {g o} = (R _ {t} - R _ {m}) / (\dot {R} _ {m} - \dot {R} _ {t}). \tag {4.56}$$

Substituting these values in (4.54) gives the basic equation for the lateral elevation error:
