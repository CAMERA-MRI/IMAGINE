# Optimisation 

## Overview

This section includes the optimisation process used for the ERNIE 1 & 2 magnets. The optimisation was performed using a [genetic algorithm](https://github.com/tmachtelinckx/halbacharray-GA)developed by one of the IMAGINE 2025 Summer School participants.

For details on the optimisation approach and the genetic algorithm implementation, please refer to the [Github repository](https://github.com/tmachtelinckx/halbacharray-GA).

## ⚙️ Genetic algorithm 
  
  <p align="center"><img width="334" height="236" alt="ga" src="https://github.com/user-attachments/assets/26ded014-a9b5-4914-a640-07622776ac3d" />
 </p>
 
## 📊 Results obtained after optimisation
<h3>Optimisation for ERNIE 1</h3>

<table>
<tr style="background-color:#38761d; color:white;">
<th>Generation</th>
<th>Best_Individual</th>
<th>Fitness_Value</th>
<th>Mean_Field_Strength</th>
<th>Homogeneity_PPM</th>
<th>Algorithm_Time_Seconds</th>
<th>Total_Execution_Time_Seconds</th>
<th>Ring_Positions</th>
</tr>

<tr style="background-color:#d9ead3;">
<td>150</td>
<td>321, 288, 251, 42</td>
<td>162.63</td>
<td>0.05</td>
<td>143.48</td>
<td>1476.98</td>
<td>1768.29</td>
<td>-0.07, -0.05, -0.02, 0.00, 0.02, 0.05, 0.07</td>
</tr>
</table>


<h3>Best Rings</h3>

<table>
<tr style="background-color:#38761d; color:white;">
<th>Configuration_Number</th>
<th>Band_Number</th>
<th>Band_Radii_Gap_mm</th>
<th>Magnet_Space_mm</th>
<th>Band_Separation_mm</th>
<th>Band_1_Radius_mm</th>
<th>Band_1_Magnet_Count</th>
</tr>

<tr style="background-color:#d9ead3;">
<td>321</td>
<td>1</td>
<td>0</td>
<td>8.82</td>
<td>16.95</td>
<td>65.43</td>
<td>16</td>
</tr>

<tr style="background-color:#d9ead3;">
<td>288</td>
<td>1</td>
<td>0</td>
<td>11.76</td>
<td>15.29</td>
<td>63.77</td>
<td>14</td>
</tr>

<tr style="background-color:#d9ead3;">
<td>251</td>
<td>1</td>
<td>0</td>
<td>8.82</td>
<td>13.63</td>
<td>62.11</td>
<td>15</td>
</tr>

<tr style="background-color:#d9ead3;">
<td>42</td>
<td>1</td>
<td>0</td>
<td>10.29</td>
<td>3.66</td>
<td>52.15</td>
<td>12</td>
</tr>

<tr style="background-color:#d9ead3;">
<td><b>Total</b></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><b>98</b></td>
</tr>

</table>
## 🧩 Optimisation parameters and CAD pictures of the rings

<p align="center"> <img width="662" height="290" alt="optimisation parameters, cad assembly" src="https://github.com/user-attachments/assets/40593b50-5eca-4f26-8852-69496aa51889" />  </p>
 </p>
