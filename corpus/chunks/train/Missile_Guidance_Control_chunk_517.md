$$[ \ddot {r} - r \dot {\theta} ^ {2} + (\mu / r ^ {2}) ] \cos \theta - (2 \dot {r} \dot {\theta} + r \ddot {\theta}) \sin \theta = 0, \tag {6.8a}[ \ddot {r} - r \dot {\theta} ^ {2} + (\mu / r ^ {2}) ] \sin \theta + (2 \dot {r} \dot {\theta} - r \ddot {\theta}) \cos \theta = 0. \tag {6.8b}$$

Since (6.8) must hold for all values of θ , then a planet’s motion is governed by the following equations of force:

$$m (\ddot {r} - r \dot {\theta} ^ {2}) = - m (\mu / r ^ {2}),m (2 \dot {r} \dot {\theta} + r \ddot {\theta}) = 0,$$

or

Radial force:

$$\frac {d ^ {2} r}{d t ^ {2}} - r \left(\frac {d \theta}{d t}\right) ^ {2} = - (\mu / r ^ {2}); \tag {6.9a}$$

Transverse force:

$$r \ddot {\theta} + 2 \dot {r} \dot {\theta} = (1 / r) \left(\frac {d}{d t}\right) (r ^ {2} \dot {\theta}) = 0. \tag {6.9b}$$

The second equation, (6.9b), leads to the statement of conservation of moment of momentum per unit mass $r ^ { 2 } ( d \theta / d t ) = h$ . These are the polar equations of motion. Since

$$\left(\frac {d}{d t}\right) (r ^ {2} \dot {\theta}) = (2 \dot {r} \dot {\theta} + r \ddot {\theta}) r,$$

the function

$$r ^ {2} \left(\frac {d \theta}{d t}\right) = h \tag {6.10}$$

satisfies (6.9b), where h is the constant of integration (h is also called the angular momentum). Equation (6.10) is simply the mathematical expression of Kepler’s second law. Now let us introduce the variable

$$u = 1 / r. \tag {6.11}$$

From (6.10) we have

$$\frac {d \theta}{d t} = h / r ^ {2} = h u ^ {. 2}. \tag {6.12}$$

Taking the derivative of (6.11) yields

$$\frac {d r}{d t} = - u ^ {- 2} \left(\frac {d u}{d t}\right) = - (1 / u ^ {2}) \left(\frac {d u}{d \theta}\right) \left(\frac {d \theta}{d t}\right), \tag {6.13}$$

and from (6.10) and (6.11),

$$\frac {d \theta}{d t} = h u ^ {2}. \tag {6.14}$$

Hence, (6.13) may be written as follows:

$$\frac {d r}{d t} = - u ^ {- 2} (d u / d \theta) h u ^ {2} = - h (d u / d \theta). \tag {6.15}$$

Taking the second derivative of (6.15), we have

$$\frac {d ^ {2} r}{d t ^ {2}} = - h \left(\frac {d}{d t}\right) (d u / d \theta) = - h \left(\frac {d ^ {2} u}{d t ^ {2}}\right) \left(\frac {d \theta}{d t}\right). \tag {6.16}$$

Again from (6.10) we have

$$\frac {d ^ {2} r}{d t ^ {2}} = - h ^ {2} (d ^ {2} u / d \theta^ {2}) u ^ {2}. \tag {6.17}$$

Substituting (6.10) into (6.9a), results in

$$- (1 / h ^ {2} u ^ {2}) [ - h ^ {2} (d ^ {2} u / d \theta^ {2}) u ^ {2} - (1 / u) h ^ {2} u ^ {4} = - \mu u ^ {2} ],$$

or

$$\frac {d ^ {2} u}{d \theta^ {2}} + u = \frac {\mu}{h ^ {2}}. \tag {6.18}$$
