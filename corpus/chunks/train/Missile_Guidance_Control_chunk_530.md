$$V _ {1} ^ {2} - V _ {2} ^ {2} = 2 \mu [ (1 / r _ {1}) - (1 / r _ {2}) ]. \tag {6.60}$$

Thus, (6.59) is the energy equation for an elliptic orbit. That (6.59) represents a true integral of the equations of motion may be demonstrated starting with Newton’s second law in the form of (6.4):

$$\frac {d ^ {2} \mathbf {r}}{d t ^ {2}} = - (\mu / r ^ {2}) \mathbf {e} _ {r}, \tag {6.61}$$

where $\mathbf { e } _ { r }$ is a unit vector in the radial direction, and r is the radius vector to the point in question. (Note that throughout the book, we will use boldface notation to denote vectors.) Performing the dot product on both sides of this equation results in

$$\dot {\mathbf {r}} \cdot \ddot {\mathbf {r}} = \frac {1}{2} \left(\frac {d}{d t}\right) (\mathbf {r} \cdot \mathbf {r}) = - (\mu / r ^ {2}) (\mathbf {r} \cdot \mathbf {e} _ {r}) = - (\mu / r ^ {2}) \left(\frac {d r}{d t}\right),$$

and integrating yields

$$\left(\frac {d \mathbf {r}}{d t}\right) \cdot \left(\frac {d \mathbf {r}}{d t}\right) = V ^ {2} = (2 \mu / r) + \text { constant }, \tag {6.62}$$

which applies to all motion in an inverse-square force field. The vis viva equation is given in textbooks on celestial mechanics in a slightly different form. We will make use of one such reference [4]. Using (6.56) and (6.10), we can write the equations of motion in the orbital plane as [5]

$$\frac {d ^ {2} x}{d t ^ {2}} = - \mu (x / r ^ {3}), \quad \frac {d ^ {2} y}{d t ^ {2}} = - \mu (y / r ^ {3}) \tag {6.63}$$

with

$$r ^ {2} = x ^ {2} + y ^ {2}.$$

Now introduce polar coordinates by

$$x = r \cos \theta , y = r \sin \theta .$$

Then

$$\left(\frac {d x}{d t}\right) ^ {2} + \left(\frac {d y}{d t}\right) ^ {2} = \left(\frac {d r}{d t}\right) ^ {2} + r ^ {2} \left(\frac {d \theta}{d t}\right) ^ {2}.$$

Consequently, the integral of area and the vis viva integral may be written as

$$r ^ {2} \left(\frac {d \theta}{d t}\right) = h, \tag {6.64a}\left(\frac {d r}{d t}\right) ^ {2} + r ^ {2} \left(\frac {d \theta}{d t}\right) ^ {2} = 2 [ (\mu / r) + C ]. \tag {6.64b}$$

These equations are a system of the second order, but the presence of two constants of integration renders them fully equivalent to the system (6.63), which is of the fourth order.
