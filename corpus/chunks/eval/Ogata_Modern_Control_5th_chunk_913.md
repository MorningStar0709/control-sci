# MATLAB commands  (Cont. )

K = acker(A',C',L)', 773

K = acker(Abb,Aab,L)', 773

K e = place(A',C',L)', 773

K e = place(Abb',Aab',L)', 773

[K,P,E] = lqr(A,B,Q,R), 798

[K,r] = rlocfind(num,den), 303

logspace(d1,d2), 422

logspace(d1,d2,n), 422–23

lqr(A,B,Q,R), 797

lsim(A,B,C,D,u,t), 201

lsim(num,den,r,t), 201

magdB = 20\*log10(mag), 422

[mag,phase,w] = bode(A,B,C,D), 422

[mag,phase,w] = bode(A,B,C,D,iu,w), 422

[mag,phase,w] = bode(A,B,C,D,w), 422

[mag,phase,w] = bode(num,den), 422

[mag,phase,w] = bode(num,den,w), 422, 476

[mag,phase,w] = bode(sys), 422

[mag,phase,w] = bode(sys,w), 476

mesh, 192

mesh(y), 192, 249

mesh(y'), 192, 249

[Mp,k] = max(mag), 476

NaN, 799

[num,den] = feedback(num1,den1, num2,den2), 20–21

[num,den] = parallel(num1,den1, num2,den2), 20–21

[num,den] = series(num1,den1, num2,den2), 20–21

[num,den] = ss2tf(A,B,C,D), 41, 657

[num,den] = ss2tf(A,B,C,D,iu), 41–42, 58, 657

[NUM,den] = ss2tf(A,B,C,D,iu), 59, 659

nyquist(A,B,C,D), 436, 441–42

nyquist(A,B,C,D,iu), 441

nyquist(A,B,C,D,iu,w), 436, 441

nyquist(A,B,C,D,w), 436

nyquist(num,den), 436

nyquist(num, den,w), 436

nyquist(sys), 436

polar(theta,r), 545

printsys(num,den), 20–21, 189

printsys(num,den,'s'), 189

r = abs(z), 544

[r,p,k] = residue(num,den), 239, 871–72

[re,im,w] = nyquist(A,B,C,D), 436

[re,im,w] = nyquist(A,B,C,D,iu,w), 436

[re,im,w] = nyquist(A,B,C,D,w), 436

[re,im,w] = nyquist(num,den), 436

[re,im,w] = nyquist(num,den,w), 436

[re,im,w] = nyquist(sys), 436

residue, 867

resonant\_frequency = w(k), 476

resonant\_peak = 20\*log10(Mp), 476

rlocfind, 303

rlocus(A,B,C,D), 295

rlocus(A,B,C,D,K), 290, 295

rlocus(num,den), 290–91

rlocus(num,den,K), 290

sgrid, 297

sortsolution, 584

step(A,B,C,D), 184, 186

step(A,B,C,D,iu), 184

step(num,den), 184

step(num,den,t), 184

step(sys), 184

sys = ss(A,B,C,D), 184

sys = tf(num,den), 184

text, 188

theta = angle(z), 544

w = logspace(d2,d3,100), 425

y = lsim(A,B,C,D,u,t), 201

y = lsim(num,den,r,t), 201

[y, x, t] = impulse(A,B,C,D), 195

[y, x, t] = impulse(A,B,C,D,iu), 195

[y, x, t] = impulse(A,B,C,D,iu,t), 195

[y, x, t] = impulse(num,den), 195

[y, x, t] = impulse(num,den,t), 195

[y, x, t] = step(A,B,C,D,iu), 184

[y, x, t] = step(A,B,C,D,iu,t), 184

[y, x, t] = step(num,den,t), 184, 190

z = re+j\*im, 544
