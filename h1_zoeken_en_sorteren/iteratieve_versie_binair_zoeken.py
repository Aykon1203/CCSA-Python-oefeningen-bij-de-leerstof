def zoek_binair(rij,getal):
  links=0
  rechts=len(rij)-1
  while links!=rechts:
    midden = (links+rechts)//2 #doet zelfde als floor(), maar zonder import
    if rij[midden]<getal: #getal = te zoeken item in de array
      links = midden+1 #zoeken in rechterhelft
    else: 
      rechts=midden #zoeken linkerhelft inclusief midden
  if rij[links]==getal: #links gelijk aan rechts -> getal is gevonden want 1 element over
    return links
  else:
    return -1;

mijn_rij = [0,10,20,30,40,50,60,70,80,90]
print(zoek_binair(mijn_rij,70))