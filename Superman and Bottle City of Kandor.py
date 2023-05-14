def findPlanet(solarSystems, range):
    # loop through each solar system
    for i, system in enumerate(solarSystems):
        totalEnergy = 0
        # loop through each star in the system
        for star in system:
            # calculate the energy received from the star
            energy = star[0] / star[1]
            totalEnergy += energy
        # check if the total energy falls within the range
        if range[0] <= totalEnergy <= range[1]:
            return i+1
    # if no suitable planet found, return -1
    return -1

# example usage
solarSystems = [
    [
        [0.433, 200]
    ],
    [
        [0.89, 400],
        [0.6, 300]
    ]
]
range = [0.003, 0.005]
suitablePlanet = findPlanet(solarSystems, range)
if suitablePlanet == -1:
    print("No suitable planet found")
else:
    print("Suitable planet is in solar system", suitablePlanet)
