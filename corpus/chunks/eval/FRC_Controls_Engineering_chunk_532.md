# E.3.2 Fourier transform

The Fourier transform decomposes a function of time into its component frequencies. Each of these frequencies is part of what’s called a basis. These basis waveforms can be multiplied by their respective contribution amount and summed to produce the original signal (this weighted sum is called a linear combination). In other words, the Fourier transform provides a way for us to determine, given some signal, what frequencies can we add together and in what amounts to produce the original signal.

Think of an Fmajor4 chord which has the notes $F _ { 4 }$ (349.23 Hz), $A _ { 4 }$ (440 Hz), and $C _ { 4 }$ (261.63 Hz). The waveform over time looks like figure E.10.

Notice how this complex waveform can be represented just by three frequencies. They show up as Dirac delta functions[4] in the frequency domain with the area underneath them equal to their contribution (see figure E.11).
