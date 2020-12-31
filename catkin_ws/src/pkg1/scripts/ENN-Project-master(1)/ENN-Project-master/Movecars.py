import math
import numpy
import sys
import time
import pdb
from ApplyGA import ApplyGA
from Feedforward import Feedforward
import rospy
from std_srvs.srv import Empty

#  Prerequisites  Chromosomes,  Chromosomes_Fitness
# Outputs  Fitness(standing vector: an element for each car)
# Initializations
def read_lidar(path):
    print("reading lidar")
    try:
        outfile = open(path, 'r')
    except IOError:
        read_lidar(path)
    with outfile:
        s = outfile.readlines()
        outfile.close()
        data = []
        for line in s:
            if (float(line) != float("inf")):
                print("in", line)
                data.append(float(line))
        return data



def write_flag(path, values):
    print("writing value ")
    try:
        outfile = open(path, 'r+')
    except IOError:
        read_lidar(path)
    with outfile:
        outfile.seek(0)
        outfile.truncate(0)
        for value in values:
            outfile.write(str(value)+'\n')
        outfile.close()


def MoveCars(env, nbrOfTimeStepsToTimeout, GA, dt, sensor, car, num, smallXYVariance, Chromosomes_Fitness, Chromosomes,
             Network_Arch, unipolarBipolarSelector, collison_value):
    carLocations = env.start_points  # Car Initial Location[X, Y] in [Meters]
    carHeadings = env.start_headings  # Car Initial Heading Counter Clock Wise[Degrees]
    steerAngles = 0  # env.start_steerAngles  # [Degrees] Counter Clock Wise(Same for all cars)

    # timesteps = 1
    # Old_Locations = []
    # for i in range(int(nbrOfTimeStepsToTimeout) - 1):
    #     l = []
    #     for j in range(2):
    #         l.append(0)
    #     Old_Locations.append(l)

    Generation_ids = 0  # At which generation
    Chromosome_ids = 1  # At which chromosome
    timeStepsDone = 0  # How many time steps passed
    prev_carLines = []
    BestFitnessChromoID = 1
    Car_Finished_Pool = 0
    nbrOfParentsToKeep = math.ceil(GA.PercentBestParentsToKeep * GA.populationSize / 100)  # For replacement

    All_Chromosomes = []  # All chromosome weights
    All_Chromosomes_Fitness = []  # Fitness of each chromosome (in terms of time)

    # To store things from surviving chromosomes in later on
    for i in range(GA.populationSize):
        l = []
        for j in range(GA.chromosomeLength):
            l.append(0)
        All_Chromosomes.append(l)
        All_Chromosomes_Fitness.append(0)

    # Iterating Generations
    while (1):
        # Move Car and Draw Environment - Get Sensor Readings and Collision State
        LifeTimes = 0  # In number of draw steps(multiple of GA.dt)
        sensor_readings = []
        y = 0
        sensor_readings = read_lidar("/home/admin/catkin_ws/src/pkg1/scripts/lidar.txt")
            #sensor_readings = read_lidar("/home/admin/catkin_ws/src/pkg1/scripts/lidar.txt")
        if (sensor_readings != []):
            dist = min(sensor_readings)  # will be used to determines if there is a collision
            id = sensor_readings.index(dist)
        else:
            dist= 10000000
        collison_bools = False
        if dist <= float(collison_value):
            collison_bools = True
            print("collision")
        else:
            collison_bools = False
            print("no collision")
        if (sensor_readings == []):
            collison_bools=False

        timeStepsDone = timeStepsDone + 1

        # Increase lifetimes by 1

        # Update Fitness
        Fitness = LifeTimes  # fitness used as a measure of time steps (steps is an iteration of this while loop)
        LifeTimes = LifeTimes + 1
        Fitness += 1
        # If car is almost in same place after nbrOfTimeStepsToTimeout has passed, set rotating_around_my_self_bool
        rotating_around_my_self_bool = 0
        # if (LifeTimes >= nbrOfTimeStepsToTimeout):
        #     Old_Locations.append(carLocations)
        #     mean_x = statistics.mean(Old_Locations[:][0])
        #     mean_y = statistics.mean(Old_Locations[:][1])
        #     x = Old_Locations[0]
        #     for i in range(len(x)):
        #         try:
        #             x[i] = math.pow((x[i] - mean_x), 2)
        #         except OverflowError:
        #             x[i] = float('inf')
        #         var_x = statistics.mean(x)  # numpy.mean(( - mean_x) ^ 2)
        #         x = Old_Locations[1]
        #         for i in range(len(x)):
        #             try:
        #                 x[i] = math.pow((x[i] - mean_y), 2)
        #             except OverflowError:
        #                 x[i] = float('inf')
        #         var_y = statistics.mean(x)
        #
        #         if var_x <= smallXYVariance and var_y <= smallXYVariance:
        #             rotating_around_my_self_bool = 1
        # else:
        #     Old_Locations[LifeTimes - 1][0] = carLocations[0]
        #     Old_Locations[LifeTimes - 1][1] = carLocations[1]

        if (collison_bools):
            if (Fitness > max(Chromosomes_Fitness)):
                BestFitnessChromoID = Chromosome_ids  # Save Best Fitness
                print("best fitness bec collided, ",BestFitnessChromoID)

            Chromosomes_Fitness[Chromosome_ids] = Fitness
            print("fitness bec collided, ",Chromosomes_Fitness[Chromosome_ids])

            if (Fitness >= GA.goodFitness):  # if fitness is better than good fitness, save it
                Car_Finished_Pool = 1
                BestFitnessChromoID = Chromosome_ids
                print("best fitness")

            # ResetCarAndLifeTime(carLocations, env, 0, carHeadings, steerAngles, LifeTimes, prev_carLines)
            
            LifeTimes=0
            steerAngles=[0]
            carHeadings=0
            carLocations=0
            prev_carLines=0
            reset_simulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
            reset_simulation()
            
            if (Car_Finished_Pool != 1):
                Chromosome_ids = Chromosome_ids + 1

        elif (rotating_around_my_self_bool == 1):
            All_Chromosomes_Fitness[Chromosome_ids] = 0  # TODO Is this good ?
            # ResetCarAndLifeTime(carLocations, env, 0, carHeadings, steerAngles, LifeTimes, prev_carLines)
            LifeTimes = 0
            steerAngles = [0]
            carHeadings = 0
            carLocations = 0
            prev_carLines = 0
            reset_simulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
            reset_simulation()

            if (Car_Finished_Pool != 1):
                Chromosome_ids = Chromosome_ids + 1
            rotating_around_my_self_bool = 0

        # Jump to car next Generation if necessary
        if (Chromosome_ids >= GA.populationSize and (Car_Finished_Pool != 1)):
            print("next generation")
            if (Generation_ids >= GA.nbrOfGenerations_max):
                Car_Finished_Pool = 1
                Chromosome_ids = BestFitnessChromoID
            else:
                # if (GA.replacement_option == 0)
                All_Chromosomes[(i - 1) * GA.populationSize: i * GA.populationSize] = Chromosomes
                x = 0
                for i in range((i - 1) * GA.populationSize, i * GA.populationSize):
                    All_Chromosomes_Fitness[i] = Chromosomes_Fitness[x]
                    x += 1

                y += 1
                tmp = All_Chromosomes_Fitness.copy()
                idx = numpy.argsort(tmp, kind='mergesort', axis=0).tolist()[::-1]
                idx2 = numpy.array(idx).tolist()[0:nbrOfParentsToKeep]
                ParentsToKeep = []
                for i in range(len(idx2)):
                    ParentsToKeep.append(All_Chromosomes[idx2[i]])

                tmp = Chromosomes_Fitness.copy()
                idx = numpy.argsort(tmp, kind='mergesort', axis=0).tolist()[::-1]
                idx2 = numpy.array(idx).tolist()[0:len(idx) - nbrOfParentsToKeep]
                Current_Chromosomes = []
                Current_Fitness = []
                for i in range(len(idx2)):
                    Current_Chromosomes.append(Chromosomes[idx2[i]])
                    Current_Fitness.append(Chromosomes_Fitness[idx2[i]])

                Chromosomes_Childs = []
                Chromosomes_Childs = ApplyGA(GA, Current_Chromosomes, Current_Fitness)
                Chromosomes = []
                for i in range(len(ParentsToKeep)):
                    Chromosomes.append(ParentsToKeep[i])
                for i in range(len(Chromosomes_Childs)):
                    Chromosomes.append(Chromosomes_Childs[i])

                Chromosome_ids = 1
                Generation_ids = Generation_ids + 1
                for i in range(len(Chromosomes_Fitness)):
                    Chromosomes_Fitness[i] = 0
                BestFitnessChromoID = 1
        current_chromosome = Chromosomes[Chromosome_ids]

        # Apply sensor reading to ANN to calculate steerAngle

        print("sample org", sensor_readings)
        outputs = Feedforward(sensor_readings, current_chromosome, Network_Arch, unipolarBipolarSelector)
        steerAngles = numpy.pi / 2 * (outputs[1] - outputs[0])  # From - 90 to 90 degrees
        print("Feedforward output", outputs)

        frontWheel = []
        backWheel = []
        # 2D car steering physics(Calculate carLocation and carHeading)
        frontWheel.append(float(carLocations[0] + car.wheelBase / 2 * math.cos(carHeadings)))
        frontWheel.append(float(carLocations[1] + car.wheelBase / 2 * math.sin(carHeadings)))
        backWheel.append(float(carLocations[0] - car.wheelBase / 2 * math.cos(carHeadings)))
        backWheel.append(float(carLocations[1] - car.wheelBase / 2 * math.sin(carHeadings)))
        backWheel[0] = backWheel[0] + car.speed * dt * math.cos(carHeadings)
        backWheel[1] = backWheel[1] + car.speed * dt * math.sin(carHeadings)
        frontWheel[0] = frontWheel[0] + car.speed * dt * math.cos(carHeadings + steerAngles)
        frontWheel[1] = frontWheel[1] + car.speed * dt * math.sin(carHeadings + steerAngles)
        for i in range(len(carLocations)):
            carLocations[i] = (frontWheel[i] + backWheel[i]) / 2
        carHeadings = math.atan2(frontWheel[1] - backWheel[1], frontWheel[0] - backWheel[0])
        if (collison_bools == False):
            write_flag("/home/admin/catkin_ws/src/pkg1/scripts/move.txt", [0.7,0.7])
        else:
            write_flag("/home/admin/catkin_ws/src/pkg1/scripts/move.txt", outputs)
        # print("Front Wheel: ", frontWheel)
        # print("Back Wheel: ", backWheel)
        print("Steering Angles: ", steerAngles)