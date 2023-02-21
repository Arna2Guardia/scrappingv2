import json
import requests

headers = {
        'Apollographql-Client-Name': 'Iron',
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'Origin': 'https://stockx.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'X-Stockx-Device-Id': 'jsui_1_bot_mdr'
}

id_chaussure = 'nike-dunk-low-grey-fog'
#On charge notre data depuis notre json (les données dans la requête post)
with open("data.json", "r") as file:
    data = json.load(file)

#Notre paramètre pour le modele de chaussure
data['variables']['id'] = id_chaussure

# On fait notre requete post
response = requests.post("https://stockx.com/api/p/e", json=data, headers=headers)

print(response)
#On deffini notre objet json

datajson = response.json()

#On prends uniquement les données de la réponse qui nous intéressent
liste_taille = datajson['data']['product']['variants']
allPrices = []
demandes = []
#On se retrouve donc avec un liste python, facilement traitable
print(liste_taille[1])

for i in range(len(liste_taille)):
    element = liste_taille[i]
    interesting = element['market']['bidAskData']
    prix_bas = interesting['highestBid']
    taille = interesting['highestBidSize']
    # prix_haut = interesting['']
    if interesting['lowestAsk'] == 'None':
        prix_haut = prix_bas
    else:
        prix_haut = interesting['lowestAsk']
    nb_demande = interesting['numberOfAsks']
    allPrices.append([prix_bas,prix_haut])
    demandes.append(nb_demande)

    print('Pour la taille ' + str(taille) + ' US.')
    print('Le prix max est de ' + str(prix_haut) + "$.")
    print('Et le prix le plus bas de ' + str(prix_bas) + "$.")
    print('Il y a actuellement ' + str(nb_demande) + ' demandes pour cette taille et ce modèle.\n')

print(allPrices)
print(demandes)

