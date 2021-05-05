spin = input()
charge = input()
key = f'{spin}' + f'{charge}'
particles = {'1/2-1/3': 'Strange Quark', '1/22/3': 'Charm Quark', '1/2-1': 'Electron Lepton',
             '1/20': 'Neutrino Lepton', '10': 'Photon Boson'}
print(particles[key])
