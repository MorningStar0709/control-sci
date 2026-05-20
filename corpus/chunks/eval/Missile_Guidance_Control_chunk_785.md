As discussed earlier, the objective of the user receiver is to take the pseudorange measurements so that the receiver can perform continuous navigation fixes. To this end, let the coordinate system be the Earth-centered Earth-fixed (ECEF) coordinate. Then, the user’s position can be denoted by $( X _ { u } , Y _ { u } , Z _ { u } )$ and the ith satellite position by $( X _ { s i } , Y _ { s i } , Z _ { s i } )$ . Mathematically, the pseudorange measurement, $\rho _ { i }$ , to the ith satellite can be obtained as follows [5]:

$$\rho_ {i} = R _ {i} + \Delta B = \left[ \left(X _ {s i} - X _ {u}\right) ^ {2} + \left(Y _ {s i} - Y _ {u}\right) ^ {2} + \left(Z _ {s i} - Z _ {u}\right) ^ {2} \right] ^ {1 / 2} + \Delta B,i = 1, 2, 3, 4, \tag {7.20}$$

where 
B is the user’s clock bias with respect to the GPS system time. Since the satellite position can be precomputed from the ephemeris data, the user position and clock bias can be derived by solving the above nonlinear inhomogeneous equations $( \mathrm { i . e . , } \rho _ { i } , i = 1 , 2 , 3 , 4 )$ . In other words, pseudoranges are modeled as the time range between satellite and receiver, corrupted by the user equipment clock bias. A more accurate model must include atmospheric propagation delay. Thus, (7.20) for the pseudorange can be written as

Table 7.2. WGS-84 Ellipsoid

<table><tr><td>Parameter</td><td>Value</td><td>Description</td></tr><tr><td> $a$ </td><td>6,378,137.00 [meters]</td><td>Semimajor axis</td></tr><tr><td> $b$ </td><td>6,356,752.3142 [meters]</td><td>Semiminor axis</td></tr><tr><td> $f$ </td><td>1/298.257223563</td><td>Flattening</td></tr><tr><td> $e$ </td><td> $3.4704208374 \times 10^{-3}$ </td><td>Eccentricity*</td></tr><tr><td> $\Omega_{E}$ </td><td> $7.292115 \times 10^{-5}$  [rad/sec]</td><td>Earth’s angular velocity</td></tr><tr><td> $\mu$ </td><td> $3986005.00 \times 10^{8}$  [ $m^{3}$ /sec $^{2}$ ]</td><td>Earth’s gravitational constant</td></tr></table>

$$
\begin{array}{l} \rho_ {i} = R _ {i} + c (\Delta t _ {u} - \Delta t _ {s i}) + c \Delta t _ {A i} \\ = [ (X _ {s i} - X _ {u}) ^ {2} + (Y _ {s i} - Y _ {u}) ^ {2} + (Z _ {s i} - Z _ {u}) ^ {2} ] ^ {1 / 2} \\ + c (\Delta t _ {u} - \Delta t _ {s i}) + c \Delta t _ {A i}, \tag {7.21} \\ \end{array}
$$

where

ρi = pseudorange to the ith satellite,

$R _ { i }$ = true range,

c = speed of light,

$\Delta t _ { s i }$ = ith satellite clock offset from the GPS system time,

$\Delta t _ { u }$ = user clock offset from the GPS system time,
