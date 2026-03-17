## RF Coil

| Parameter                 | Value                                           |
|---------------------------|-------------------------------------------------|
| Number of Turns           | 27                                              |
| Pitch between turns       | 117/27= 4.333333                                |
| Wire thickness            | 1.65mm                                          |
| Inductance                | uH (Measured )                                  |
| Inner diameter            | 58mm( After printing) and 60mm before printing  |
| Outer Diameter            | 63mm                                            |
| Length of turns           | 117mm                                           |
| Length of Coil            | 143mm                                           |
| Tuning Capacitance        | 330pF+ 24pF+ 25pF( variable )                   |
| Matching Capacitance      | 47pF + 18pF                                     |
| Center Frequency          | 2.035MHz                                        |
| Reflected Power           | -30.7dB                                         |
| Resistance on Smith Chat  | -52 ohms                                        |

STEPS 
1. Place the RF coil in the MRI scanner and add gradients and a shield. 
2. Then connect the RF coil to the VNA to see the peak. 
3. Add capacitors on the tuning side ( S21). To attain a frequency of 2.1MHz for a 50 mT scanner system. 
4. After attaining the Tuning Capacitance, measure the quality factor of the coil, loaded and unloaded. 
5. The value of the Quality Factor should be greater than 1. In that case, add capacitors for the matching channel until the reflected power is closer to –50dB. 

