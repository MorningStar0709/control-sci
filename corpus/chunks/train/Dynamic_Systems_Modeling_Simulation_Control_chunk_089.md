# MATLAB Problems

2.18 An engineer wants to develop mathematical models for two mechanical springs. She loads the springs (in tension and compression), measures their static deflections, and compiles the results in Table P2.18. Use MATLAB’s polyfit command to determine spring-force modeling equations for each spring. Plot both spring-model equations for deflections ranging from −8 to 8 mm and include the data points from Table P2.18 on your plot. Comment on whether the springs exhibit linear or nonlinear relationships.

Table P2.18

<table><tr><td>Load force (N)</td><td>Spring #1 deflection (mm)</td><td>Spring #2 deflection (mm)</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>10</td><td>1.2482</td><td>1.1682</td></tr><tr><td>15</td><td>1.8822</td><td>1.7523</td></tr><tr><td>25</td><td>3.1938</td><td>2.9206</td></tr><tr><td>35</td><td>4.6099</td><td>4.0888</td></tr><tr><td>45</td><td>6.2354</td><td>5.2570</td></tr><tr><td>50</td><td>7.2055</td><td>5.8411</td></tr><tr><td>-10</td><td>-1.2482</td><td>-1.1682</td></tr><tr><td>-15</td><td>-1.8822</td><td>-1.7523</td></tr><tr><td>-25</td><td>-3.1938</td><td>-2.9206</td></tr><tr><td>-35</td><td>-4.6099</td><td>-4.0888</td></tr><tr><td>-45</td><td>-6.2354</td><td>-5.2570</td></tr><tr><td>-50</td><td>-7.2055</td><td>-5.8411</td></tr></table>

2.19 Accurately modeling friction in mechanical systems is often challenging because of the “stick-slip” characteristic at very low relative velocities. A nonlinear friction model that accommodates the stick-slip phenomena is

$$F _ {f} = [ F _ {C} + (F _ {\mathrm{st}} - F _ {C}) \exp (- | \dot {x} | / c) ] \mathrm{sgn} (\dot {x}) + b \dot {x}$$
