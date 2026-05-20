# Now set up conversion (2 examples)
fs = 20 # 2x highest pole/zero sampling
Ts = 1/fs # Sample time
sysDT01 = ctl.sample_system(sysCT, Ts, method='tustin')
fs = 40 # 4x highest pole/zero sampling
Ts = 1/fs # Sample time
sysDT02 = ctl.sample_system(sysCT, Ts, method='tustin')
print('\n ECE 447 Example: Conversion to Discrete Time: \n')
print('Continuous Time System: ',sysCT)
print('\nDiscrete Time System (20Hz): ', sysDT01)
print('\nDiscrete Time System (40Hz): ', sysDT02) 
```  
Listing 11.1. Conversion to discrete time system using two dierent sampling times (Ts).
