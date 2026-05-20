Kepler’s first law states that the path, or orbit, of a planet around the Sun is an ellipse, the position of the Sun being at one focus of the ellipse. Kepler’s first law is illustrated in Figure 6.3. Furthermore, Kepler’s second law states that the radius vector SP sweeps out equal areas in equal times. Now, from Figure 6.3 we let (x, y) be the coordinates of the planet referenced from these axes. Therefore, using (6.4), the equations of motion in the orbital plane of the planet are [10]

$$\frac {d ^ {2} x}{d t ^ {2}} + \mu \left(\frac {x}{r ^ {3}}\right) = 0, \tag {6.5a}$$

![](image/a473b882f7a8184f39b585d9da792cd52a52e3a15a5b6f6bd420d6a9d2f260d1.jpg)

<details>
<summary>text_image</summary>

D
Q
P
y
r
θ - ω
θ
ω
B
F
C
S
A
Y, x
</details>

Definitions

$$P = \text { Position of planet }C A = \text { Semi - major axis } = aC S / C A = \text { Eccentricity } = e\text { Point } A = \text { Perihelion }\text { Point } B = \text { Aphelion }S A = \text { Perihelion distance } = a (1 - e)S B = \text { Aphelion distance } = a (1 + e)b ^ {2} = a ^ {2} (1 - e ^ {2})$$

Fig. 6.3. The elliptical orbit.

$$\frac {d ^ {2} y}{d t ^ {2}} + \mu \left(\frac {y}{r ^ {3}}\right) = 0, \tag {6.5b}$$

where $r = ( x ^ { 2 } + y ^ { 2 } ) ^ { 1 / 2 }$ . We wish now to transform these equations given in rectangular coordinates $( x , y )$ into polar coordinates $( r , \theta )$ . Let

$$x = r \cos \theta \quad \text { and } \quad y = r \sin \theta .$$

Taking the first and second derivatives of these equations, we have

$$\frac {d x}{d t} = \dot {r} \cos \theta - r \dot {\theta} \sin \theta , \tag {6.6a}\frac {d ^ {2} x}{d t ^ {2}} = \ddot {r} \cos \theta - \dot {r} \dot {\theta} \sin \theta - \dot {r} \dot {\theta} \sin \theta - r \dot {\theta} ^ {2} \cos \theta - r \ddot {\theta} \sin \theta= \ddot {r} \cos \theta - 2 \dot {r} \dot {\theta} \sin \theta - r \dot {\theta} ^ {2} \cos \theta - r \ddot {\theta} \sin \theta . \tag {6.6b}$$

Similarly,

$$\frac {d y}{d t} = \dot {r} \sin \theta + r \dot {\theta} \cos \theta , \tag {6.7a}\frac {d ^ {2} y}{d t ^ {2}} = \ddot {r} \sin \theta + \dot {r} \dot {\theta} \cos \theta + \dot {r} \dot {\theta} \cos \theta - r \dot {\theta} ^ {2} \sin \theta + r \ddot {\theta} \cos \theta= \ddot {r} \sin \theta + 2 \dot {r} \dot {\theta} \cos \theta - r \dot {\theta} ^ {2} \sin \theta - r \ddot {\theta} \cos \theta . \tag {6.7b}$$

Substituting (6.6) and (6.7) into (6.5) results in
