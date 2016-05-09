#!/usr/bin/python
# this in objector oriented implementation of a Lotka-Volterra model. The code was at one time inherited from my good friend Damian Sowinski, not sure if he wrote it himself, repurposed it from elsewhere etc, so the history is a little shady. I've updated and commented it a bunch as of May 2016

import matplotlib.pylab as plt

#define a class that keeps track of the number of a population
class pop:   
   #initialize the class to contain the population as well as a vector of the populations over time, and the time
   def __init__(self, init_population):
      self.pop  = init_population
      self.pop_history = [[init_population],[0]]
   
   #evolve the populations
   def evolve(self, pop_inflow, pop_outflow, dt = 1.):
      pop_change = (pop_inflow - pop_outflow)*dt #eulers method integration
      self.pop += pop_change
      if self.pop < 0: #make sure populations do not become negative
         self.pop = 0
      
      #append to population vector
      self.pop_history[0].append(self.pop)
      #append to time series vectors (use[-1] to be end of list)
      self.pop_history[1].append(self.pop_history[1][-1] + dt) 

# the parameters for the model, birth of rabbits aR, catch rate of rabits beta, growth rate of wolves given catches gam, death rate of wolves dW 
aR, beta, gam, dW = 1, .05, .1, 10 

dt = .001 #time step

#initialize populations
rabits = pop(100); wolves = pop(10)

#loop for days and evolve the populations accordingly
numsteps=10000
for t in range (numsteps):
   rabits.evolve(aR*rabits.pop, beta*rabits.pop*wolves.pop, dt)
   wolves.evolve(gam*wolves.pop*rabits.pop, dW*wolves.pop, dt)

#make a figure
fig1=plt.figure(figsize=(12,6))

#plot the time series data
plt.subplot(121)
plt.semilogy(rabits.pop_history[1],rabits.pop_history[0],color = 'blue')
plt.semilogy(wolves.pop_history[1],wolves.pop_history[0],color = 'red')
plt.title('Time series')
plt.ylabel('Population')
plt.xlabel('Time')
plt.legend(['Rabbits','Wolves'])

#plot the phase portrait
plt.subplot(122)
plt.plot(rabits.pop_history[0],wolves.pop_history[0],'-')
plt.title('Phase plot')
plt.xlabel('Rabbit population')
plt.ylabel('Wolf population')
#plt.xlim([0,max(rabits.pop_history[0]+wolves.pop_history[0])]) #make axes equal
#plt.ylim([0,max(rabits.pop_history[0]+wolves.pop_history[0])])
plt.axis('equal')
plt.show()
      
