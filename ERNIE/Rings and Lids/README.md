<p align="justify">
The genetic algorithm (GA) optimizes a multi-ring Halbach array design using: 
1) A predefined dataset of individual ring designs
2) A magnetic field simulator.
3) Fitness evaluation.
To initialize the optimisation process, a user defines specific parameters inner bore diameter, outer bore diameter, number of bands, magnet size and spacing, array length, band gap, and number of rings. This information was then used to generate a dataset of individual rings.
The Halbach arrays were then created from ring combinations using rings from a predefined dataset. Each of these arrays forms an individual in the GA population, which is then evaluated and evolved to minimize the field inhomogeneity and target field error.
The simulated magnetic field strength on the spherical volume F is approximated by the superposition of each magnet, individual contributions on each ring, using the single dipole model.
Each of these arrays forms an individual in the GA population, which is then evaluated and evolved to minimize the field inhomogeneity and target field error. The simulated magnetic field strength on the spherical volume $F$ is approximated by the superposition of each magnet, with individual contributions on each ring using the single dipole model.

Finally, the fitness function is implemented as:

$$
f(x) = 0.8\,E_H(x) + 0.2\,E_T(x)
$$

where

$$
E_H(x) = \frac{\max(\mu_F) - \min(\mu_F)}{\mu_F}
$$

$$
E_T(x) = \left|\mu_F - \mu_T\right|
$$

are the homogeneity and mean magnetic field strength error functions, respectively. Note that $\mu_F$ is the mean value of $F$, $\mu_T$ is the target mean field strength, and $x$ is the configuration vector that describes which rings from the dataset are being used. The GA is executed using the island model.
 
To optimize ERNIE 1, we set specific parameters to develop a mouse-brain-like inner bore diameter Halbach array scanner. These parameters were selected based on the size of a mouse brain being about 30mm. Henceforth, the Diameter to Spherical Volume was set as 40mm. 

Table 1 below shows the parameters set during the optimization of the ERNIE 1 magnet.

| Parameter                     | Value        |
|-----------------------------|-------------|
| Inner Bore                  | 80 mm       |
| Outer Bore                  | 160 mm      |
| Magnet Size                 | 12 × 12 × 12 mm |
| Target Field Strength       | 50 mT       |
| Array Length                | 156 mm      |
| Number of Rings             | 7           |
| Diameter to Spherical Volume | 40 mm       |

After optimisation, a combination of the best rings is attained. For this case, the best rings were **#321**, **#252**, **#288** and **#42**. These were designed using Autodesk inventor/, AutoCAD/ Solid Works.
![CAD Designs](Rings_and_Lids/CAD_Designs_of_rings.png)
Corresponding lids to cover the rings were also designed using Autodesk Inventor. An assembly was made using Fusion 360 to check if all the rings fit together alongside the Brass rods, screws, nuts, and other parts that will be discussed in the next section.
To evaluate the genetic Algorithm approach, a 50 mT scanner is designed and constructed.
</p>

