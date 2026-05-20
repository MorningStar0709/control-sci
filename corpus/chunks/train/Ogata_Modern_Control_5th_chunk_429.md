bode returns the frequency response of the system in matrices mag, phase, and w. No plot is drawn on the screen.The matrices mag and phase contain magnitudes and phase angles of the frequency response of the system, evaluated at user-specified frequency points.The phase angle is returned in degrees.The magnitude can be converted to decibels with the statement

$$\mathrm{magdB} = 2 0 ^ {*} \log 1 0 (\mathrm{mag})$$

Other Bode commands with left-hand arguments are

```matlab
[mag,phase,w] = bode(num,den)
[mag,phase,w] = bode(num,den,w)
[mag,phase,w] = bode(A,B,C,D)
[mag,phase,w] = bode(A,B.C,D,w)
[mag,phase,w] = bode(A,B,C,D,iu,w)
[mag,phase,w] = bode(sys) 
```

To specify the frequency range, use the command logspace(d1,d2) or logspace (d1,d2,n). logspace(d1,d2) generates a vector of 50 points logarithmically equally spaced between decades $1 0 ^ { \mathrm { d } 1 }$ and ${ \bf \bar { \boldsymbol { 1 0 } } } ^ { \mathrm { d } 2 }$ . (50 points include both endpoints. There are 48 points between the endpoints.) To generate 50 points between 0.1 radsec and 100 radsec, enter the command

$$w = \text { logspace } (- 1, 2)$$

logspace(dl,d2,n) generates n points logarithmically equally spaced between decades $1 0 ^ { \mathrm { d 1 } }$ and $1 0 ^ { \mathrm { d } 2 } .$ . (n points include both endpoints.) For example, to generate 100 points including both endpoints between 1 radsec and 1000 radsec,enter the following command:

$$w = \text { logspace } (0, 3, 1 0 0)$$

To incorporate the user-specified frequency points when plotting Bode diagrams, the bode command must include the frequency vector w, such as bode(num,den,w) and $[ \mathsf { m a g } , \mathsf { p h a s e } , \mathsf { w } ] = \mathsf { b o d e } ( \mathsf { A } , \mathsf { B } , \mathsf { C } , \mathsf { D } , \mathsf { w } )$ .
