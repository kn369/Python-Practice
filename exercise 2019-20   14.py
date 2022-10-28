# PROGRAMMING EXERCISES 14

mass=int(input("Enter the mass of object :"))
velocity=int(input("Enter the velocity of object :"))

def kinetic_energy(M,V):
    KE=0.5*mass*velocity**2
    print("Kinetic energy of the object is ",KE,"joules")

kinetic_energy(mass,velocity)
