NEW nth1 nth2 nth3 nth4

NEW nf1 nf2 nf3 nf4

NEW n11 n12 n13 n14 n22 n23 n24 n33 n34 n44

TIME t

TSAMP ts

INITIAL

"Compute sampled Am and Ao

a=exp(-z\*w\*h)

am1=-2\*a\*cos(w\*h\*sqrt(1-z\*z))

```txt
am2=a*a
aop=IF w*To>100 THEN 0 ELSE -exp(-h/To)
ao=IF cancel>0.5 THEN 0 ELSE -aop 
```

SORT   
```txt
"1.0 Parameter Estimation
"1.1 Computation of P*f and estimator gain k
pf1=p11*f1+p12*f2+p13*f3+p14*f4
pf2=p12*f1+p22*f2+p23*f3+p24*f4
pf3=p13*f1+p23*f2+p33*f3+p34*f4
pf4=p14*f1+p24*f2+p34*f3+p44*f4
denom=lambda+f1*pf1+f2*pf2+f3*pf3+f4*pf4
k1=pf1/denom
k2=pf2/denom
k3=pf3/denom
k4=pf4/denom 
```

```txt
"1.2 Update estimates and covariances
eps=y-f1*th1-f2*th2-f3*th3-f4*th4
nth1=th1+k1*eps
nth2=th2+k2*eps
nth3=th3+k3*eps
nth4=th4+k4*eps
n11=(p11-pf1*k1)/lambda
n12=(p12-pf1*k2)/lambda
n13=(p13-pf1*k3)/lambda
n14=(p14-pf1*k4)/lambda
n22=(p22-pf2*k2)/lambda
n23=(p23-pf2*k3)/lambda
n24=(p24-pf2*k4)/lambda
n33=(p33-pf3*k3)/lambda
n34=(p34-pf3*k4)/lambda
n44=(p44-pf4*k4)/lambda 
```

```txt
"1.3 Update and filter regression vector
nf1=-y
nf2=f1
nf3=u
nf4=f3 
```

```txt
"2.0 Control design
"2.1 Rename parameters
a1=nth1
a2=nth2 
```

```txt
b0=nth3
b1=nth4 
```

```txt
"2.2 Solve the polynomial identity AR+BS=AoAm
n=b1*b1-ai*b0*b1+a2*b0*b0
r10=(ao*am2*b0^2+(a2-am2-ao*am1)*b0*b1+(ao+am1-a1)*b1^2)/n
w1=(a2*am1+a2*ao-a1*a2-am2*ao)*b0
s00=(w1+(-a1*am1-a1*ao-a2+a1^2+am2+am1*ao)*b1)/n
w2=(-a1*am2*ao+a2*am2+a2*am1*ao-a2^2)*b0
s10=(w2+(-a2*am1-a2*ao+a1*a2+am2*ao)*b1)/n 
```

```txt
"2.3 Compute polynomial T=Ao*Am(1)/B(1)
bs=b0+b1
as=1+am1+am2
bm0=as/bs 
```

```txt
"2.4 Choose control algorithm
r1=IF cancel>0.5 THEN b1/b0 ELSE r10
s0=IF cancel>0.5 THEN (am1-a1)/b0 ELSE s00
s1=IF cancel>0.5 THEN (am2-a2)/b0 ELSE s10
t0=IF cancel>0.5 THEN as/b0 ELSE bm0
t1=IF cancel>0.5 THEN 0 ELSE bm0*ao 
```

```txt
"3.0 Control law with anti-windup
v=-ao*v1+t0*ysp+t1*ysp1-s0*y-s1*y1+(ao-r1)*u1
u=IF v<-ulim THEN -ulim ELSE IF v<ulim THEN v ELSE ulim 
```

```txt
"3.1 Update controller state
ny1=y
nu1=u
nvl=v
nysp1=ysp 
```

```txt
"4.0 Update sampling time ts=t+h 
```

```lisp
"Parameters
lambda:1 "forgetting factor
To:200 "observer time constant
z:0.7 "desired closed loop damping
w:1 "desired closed loop natural frequency
h:1 "sampling period
ulim:1 "limit of control signal
cancel:1 "switch for cancellation
th1:-2 "initial estimates 
```

th2:1

th3:0.01

th4:0.01

p11:100 "initial covariances

p22:100

p33:100

p44:100
