Guidance systems can use any one of several methods or laws to navigate a missile along a trajectory or flight-path to intercept a target (e.g., an aircraft). The specific target flight path information required by the guidance package depends on which law is used. In this section we will discuss the three types of pursuit courses, namely, pure pursuit, deviated pursuit, and pure collision, and develop the respective differential equations. The homing trajectory that a missile flies depends in the type of guidance law employed. The guidance law depends on the mathematical requirements or constraints of the engagement. Figure 4.7 will be used as the basis to derive these equations. In particular, the kinematics of an attack course, as illustrated in Figure 4.7, are based on the relationships between the interceptor (or missile) velocity $V _ { I }$ , the target velocity $V _ { T }$ , the interceptor lead angle λ, the target aspect angle α, and the interceptor to target range R.

The basic differential equations can be derived from considerations of the geometry. Referring to Figure 4.7, the range rate can be written in the form

$$\frac {d R}{d t} = V _ {I} \cos \lambda + V _ {T} \cos (1 8 0 - \alpha) = V _ {I} \cos \lambda - V _ {T} \cos \alpha , \tag {4.11}$$

where the angle reference is the interceptor-to-target range vector. The velocity components orthogonal to R consist of two parts: (1) the translational component, and (2) the tangential (or turning) component. Selecting the interceptor as the reference point for the tangential component, and taking $d \lambda / d t$ positive in the same sense as λ (i.e., increasing λ implies increasing $d \lambda / d t )$ , the equations can be written as follows:

$$R \left(\frac {d \lambda}{d t}\right) = V _ {I} \sin \lambda - V _ {T} \sin (1 8 0 - \alpha) = V _ {I} \sin \lambda - V _ {T} \sin \alpha . \tag {4.12}$$

The conditions for the various types of trajectories result from holding constant one of the parameters in the equations.
