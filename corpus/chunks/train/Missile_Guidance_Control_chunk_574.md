$$\partial r / \partial b = [ (\partial f _ {1} / \partial b) (\partial f _ {2} / \partial \theta) - (\partial f _ {1} / \partial \theta) (\partial f _ {2} / \partial b) ] / (\partial f _ {2} / \partial \theta), \tag {6.143a}\partial \theta / \partial b = (\partial f _ {2} / \partial b) / (\partial f _ {2} / \partial \theta), \tag {6.143b}\partial V _ {r} / \partial b = [ (\partial f _ {2} / \partial \theta) (\partial f _ {3} / \partial b) - (\partial f _ {2} / \partial b) (\partial f _ {3} / \partial \theta) ] / (\partial f _ {2} / \partial \theta), \tag {6.144a}\partial V _ {\theta} / \partial b = [ (\partial f _ {2} / \partial \theta) (\partial f _ {4} / \partial b) - (\partial f _ {2} / \partial b) (\partial f _ {4} / \partial \theta) ] / (\partial f _ {2} / \partial \theta). \tag {6.144b}$$

We will now compute the in-plane error equations by implicitly differentiating the spherical Earth hit equation (6.75) with respect to the central angle $\phi$ and each of the burnout variables. This gives, after some trigonometric substitutions [16],

$$\delta \phi [ ((\sin \phi) / \lambda \sin^ {2} \gamma)) - (\cos (\gamma - \phi) / \sin \gamma) ] = (2 \delta V _ {r} / V _ {r}) [ (1 - \cos \phi) / (\lambda \sin^ {2} \gamma) ]+ \left(\delta h / r _ {t}\right) \left\{1 + \left(r _ {t} / r _ {i}\right) \left[ \left(1 - \cos \phi\right) / \left(\lambda \sin^ {2} \gamma\right) \right] \right\}+ (\delta \gamma) [ 2 (r _ {t} / r _ {i}) \cot \gamma - (\sin (2 \gamma - \phi) / \sin^ {2} \gamma) ]. \tag {6.145}$$

From Figure 6.11, the range error is given by

$$\delta R = r _ {t} \delta \phi , \tag {6.146}$$

where R is the range, thus related to each of the burnout errors through (6.145).

The analysis of the burnout errors will be performed assuming independent variations of each, even though they are actually interdependent. That is, to study the range error due to a specific burnout error, it will be assumed that all other burnout variables are controlled perfectly. In a similar manner, we can write the required (or correlated) velocity perturbed equation as follows:

$$\delta V _ {R} = (\partial \mathbf {V} _ {R} / \partial \mathbf {r} _ {t}) \delta \mathbf {r} _ {t} + (\partial \mathbf {V} _ {R} / \partial t _ {f f}) \delta t _ {f f}. \tag {6.147}$$

A variation in the burnout speed will modify the trajectory profile and impact point, since either more or less energy has been imparted to the vehicle at burnout. The error equation is obtained from (6.145) and (6.146) as [16]
