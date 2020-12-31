# ENN Project 

The model. 

## Inputs

the minimum distance where we consider a collison occured  
19 Sensor Readings of distances 

## Outputs

Steering Angles gives the steering angle of the whole car  
Front Wheel and Back Wheel -> positions of the wheels (won't use most probably)  

## Parameters (could be modified )
All of these objects exist in the main. 

### Settings object

```
unipolarBipolarSelector # 0 (Unipolar) or 1 (Bipolar) - changes the activation function 
dt #[Seconds] Time Step
timeout 
nbrOfInputNodes # number of sensor inputs 

```
### GenticAlgorithmSettings object

```
nbrOfGenerations_max # after which the model ends 
goodFitness # time 
populationSize #for each generation
corssoverProb_mean_percent
corssoverProb_stdDev_percent
mutationProb
selection_option  # 0(Tournament) or  1 (Truncation)
tournament_size 
truncation_percentage
replacement_option # 0: All children replace parents unless best ceil(PercentBestParentsToKeep), 1: Use good parents based on tournaments and add other children, 2: Use good parents
PercentBestParentsToKeep 
keptParentsAreGolobal_option
weightsRange #Intially wights are random following a uniform distrubution from -weightsRange to weightsRange. Mutation adds random weights follwoing the same distribution.
```
### CarSettings object

```
wheelBase #The distance between the two axles.
width
length
wheelLength
wheelWidth
speed
```
### SensorSettings object

```
angles # for each sensor reading.
# Note that they need to match the original ones 
```
### EnvSettings object

```
angles # for each sensor reading.
# Note that they need to match the original ones 
```
## License

This project is licensed under the MIT License MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
