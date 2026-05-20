% mechanical system parameters
m1 = 20;    % seat mass, kg
m2 = 50;    % driver mass, kg
k1 = 7410;    % suspension stiffness, N/m
k2 = 8230;    % seat cushion stiffness, N/m
b1 = 1430;    % suspension friction, N-s/m
b2 = 153;    % seat cushion friction, N-s/m

% State-space representation:
% x = [ z1 ; z1dot-b1*z0/m1 ; z2 ; z2dot ]'
% u = z0(t) (floor displacement)
Arow1 = [ 0 1 0 0 ];
Arow2 = [(-k1-k2)/m1 (-b1-b2)/m1 k2/m1 b2/m1 ];
Arow3 = [ 0 0 0 1 ];
Arow4 = [ k2/m2 b2/m2 -k2/m2 -b2/m2 ];
A = [ Arow1 ; Arow2 ; Arow3 ; Arow4 ];
B = [ b1/m1 ; (-b1*b1 - b1*b2 + k1*m1)/m1^2 ; 0 ; b1*b2/(m1*m2 ) ];
% output y = z2 = x3 (driver displacement)
C = [ 0 0 1 0 ];
D = 0;

% build SSR system
sys = ss(A,B,C,D);

% Loop for computing TR for range of input frequency
Npts = 500;
w_Hz = linspace(0.1,5,Npts);    % range of frequency: 0.1 --> 5 Hz

for i=1:Npts
    w_in = w_Hz(i)*2*pi;    % input frequency in rad/s
    [mag,phase] = bode(sys,w_in);
    TR(i) = mag;    % transmissibility = |z2|/|z0|
end

% Plot TR vs input frequency
plot(w_Hz,TR)
grid
xlabel('Input frequency, Hz')
ylabel('Transmissibility') 
```

![](image/16c33d604d9ebe174a545282c7c954b912aaf95cbe04006e4a59f36676fd9c63.jpg)  
Figure 11.10 Transmissibility $| z _ { 2 } | / | z _ { 0 } |$ for variations in seat-cushion stiffness $k _ { 2 }$

$k _ { 2 }$ appears to provide good performance, as transmissibility at 2.5 Hz is about unity when $k _ { 2 } = 8 2 3 0 \mathrm { N } / \mathrm { m }$ . If reducing the transmitted vibrations at 2.5 Hz is more important than attenuating the peak transmissibility, then decreasing the seat-cushion stiffness is likely a good option because Fig. 11.10 shows that transmissibility at 2.5 Hz is highly sensitive to $k _ { 2 }$ .
