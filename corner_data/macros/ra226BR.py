
from printVal import printVal

ra226br =  1 # top of chain for this source
at218br =  0.02/100

pb214br = []
pb214br.append( 99.980/100 )
pb214br.append( at218br )
pb214br[-1] *=  0.10/100
pb214br = sum( pb214br )
pb214bre = 0.002/100 # unused
print( 'Pb-214 to Ra-226 BR:', printVal(pb214br, pb214bre) )

bi214br = []
bi214br.append( at218br )
bi214br[-1] *= 99.90/100
bi214br.append( pb214br )
bi214br[-1] *= 99.979/100 # beta decay of Bi-214 BR
bi214br = sum( bi214br )
print( 'Bi-214 to Ra-226 BR:',bi214br)

pb210br  = 1
pb210bre = 7e-3/100
