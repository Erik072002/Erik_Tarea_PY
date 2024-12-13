from Historial import historial

MaxSize = 10
histo = historial(MaxSize)

Paginas = ["TechWave.com","EcoHaven.com", "FoodieVerse.com", "FitTrackers.io","BookBazaar.co","TravelSphere.com","CódigoNest.dev", "PetPalsWorld.com","ArtisanHub.net","Zona de juegos.gg"]


for j in Paginas:
    histo.push(j)
histo.traverse()

histo.atras()

