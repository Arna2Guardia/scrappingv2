import requests
import bs4
import time
import csv
import json
import random


baseUrl = 'https://stockx.com'
uri = '/fr-fr/sneakers?page='

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Accept": "application/json",
#     "Referer": "https://stockx.com/",
#     "Origin": "https://stockx.com",
#     "Connection": "keep-alive",
#     "sec-fetch-site": "none",
#     "sec-fetch-mode": "navigate",
#     "Cache-Control": "no-cache",
#     "Pragma": "no-cache",  
#     "Sec-Fetch-Dest": "document"
#     }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stockx.com/',
    'Origin': 'https://stockx.com'
}


http_proxies = {
    "HTTPS": "https://104.223.135.178:10000"
}

response = requests.get(baseUrl + uri, headers=headers,proxies=http_proxies)

def endpointsCollector():
  webpoints = []

  for i in range(1,25):
    webpoints.append(baseUrl + uri + str(i))
  endpoints = []
  idChaussures = []
  nameChaussures = []
  for webpoint in webpoints:
    response = requests.get(webpoint, headers=headers)
    if response.ok:
      swoup = bs4.BeautifulSoup(response.text,'html.parser')
      id = swoup.find('div', {"id": "browse-grid"})
      divs = swoup.findAll('div', {"class": "css-1ibvugw-GridProductTileContainer"})
      for div in divs:
          a = div.find('a')
          name = div.find('p', {"class": "css-3lpefb"})
          name = name.contents[0]
          #print(name)
          endpoints.append(baseUrl + a['href'])
          id = a['href']
          id = id.replace('/fr-fr/','')
          idChaussures.append(id)
          nameChaussures.append(name)
  return endpoints, idChaussures, nameChaussures


print(response) 


#             try:
#               price = price.contents[0]
#               intPrice = int(price.replace('\xa0€',''))
#               print("Link:", baseUrl + a['href'])
#               print("Price:", price)
#               endpoints.append([baseUrl + a['href'], price.replace(u'\xa0', ' ')])
#               new = requests.get(baseUrl + a['href'], headers=headers)

#               if new.ok:
#                 swoup2 = bs4.BeautifulSoup(new.text,'html.parser')
#                 lastSellAll = swoup2.find('p', {'class': 'css-xfmxd4'})
#                 lastSellAll = lastSellAll.contents[0]
#                 intLastSellAll = int(lastSellAll.replace('\xa0€',''))                
#                 res = intPrice - intLastSellAll

#                 try:
#                   difference = swoup2.findAll('p', {'class': 'css-eqh2n0'})
#                   print('Last sell:', lastSellAll, '\n')
#                   cpt = 0
#                   for dif in difference:
#                     if cpt == 0:
#                       print('Difference between 2 last sales:', dif.contents[0], '\n')
#                     else:
#                       print(dif.contents[0], '\n')
#                     cpt +=1
#                 except:
#                   print("Class css-eqh2n0 not found")
#                   pass

#                 try:
#                   difference = swoup2.findAll('p', {'class': 'css-as46lx'})
#                   #print('Last sell:', lastSellAll, '\n')
#                   cpt = 0
#                   for dif in difference:
#                     if cpt == 0:
#                       print('Difference between 2 last sales:', dif.contents[0], '\n')
#                     else:
#                       print(dif.contents[0], '\n')
#                     cpt +=1
#                 except:
#                   print('Class css-as46lx not found')
#                   pass
              
#                 try:
#                   difference = swoup2.findAll('p', {'class': 'css-1qumzfe'})
#                   #print('Last sell:', lastSellAll, '\n')
#                   cpt = 0
#                   for dif in difference:
#                     if cpt == 0:
#                       print('Difference between 2 last sales:', dif.contents[0], '\n')
#                     else:
#                       print('+',dif.contents[0], '\n')
#                     cpt +=1
#                 except:
#                   print('Class css-1qumzfe not found')
#                   pass
              



#             except:
#               pass

#             time.sleep(1)
#     #print('\nL id est:', id)
    

headers3 = {
    'Apollographql-Client-Name': 'Iron',
    'App-Version': '2023.01.29.00',
    'App-Platform': 'Iron',
    'Accept-Language': 'fr-FR',
    'User-Agent': 'myUserAgent2/0',
    'X-Stockx-Device-Id': 'jsui_1_bot_mdr'
}



headers4 = {
    'Apollographql-Client-Name': 'Venus',
    'App-Version': '2023.02.01.01',
    'App-Platform': 'iOS',
    'Accept-Language': 'de-DE',
    'User-Agent': 'myUserAgent4/0',
    'X-Stockx-Device-Id': 'jsui_1_bot_fef'
}

headers5 = {
    'Apollographql-Client-Name': 'Mars',
    'App-Version': '2023.02.02.00',
    'App-Platform': 'Windows',
    'Accept-Language': 'es-ES',
    'User-Agent': 'myUserAgent5/0',
    'X-Stockx-Device-Id': 'jsui_1_bot_lol'
}

headers6 = {
    'Apollographql-Client-Name': 'Mercury',
    'App-Version': '2023.02.01.00',
    'App-Platform': 'Android',
    'Accept-Language': 'en-US',
    'User-Agent': 'myUserAgent3/0',
    'X-Stockx-Device-Id': 'jsui_1_bot_jdh'
}

proxies = [
    {"SOCKS5":"socks5://157.245.223.201:59166"},
    {"SOCKS5":"socks5://159.89.49.172:59166"},
    {"SOCKS5": "socks5://142.44.241.192:59166"}
]

headers_list = [headers3, headers4, headers5, headers6]
random_headers = random.choice(headers_list)
random_proxy = random.choice(proxies)

_, idChaussures, _ = endpointsCollector()
#print(idChaussures)

with open("data.json", "r") as file:
  data = json.load(file)


allInfo = []
cpt = 0

# boucle sur chaque chaussure
for idChaussure in idChaussures:
  print("On en est à la paire n°",cpt)
  data['variables']['id'] = idChaussure

  response2 = requests.post("https://stockx.com/api/p/e", json=data, headers=random_headers, proxies=random_proxy)
  if response2.status_code != 200:
    print('Request failed with status code:', response2.status_code)
    break
  else:
    datajson = response2.json()
    #print(datajson)
    try:
      listeTaille = datajson['data']['product']['variants']
    except TypeError:
      print(f"Error processing idChaussure: {idChaussure}")
      pass

    # boucle sur chaque pointure
    obj = {}
    for i in range(len(listeTaille)):

      element = listeTaille[i]
      interesting = element['market']['bidAskData']
      prixBas = interesting['highestBid']
      taille = interesting['highestBidSize']
      if str(taille)[-1] == 'Y':
        taille = str(taille)[0:len(taille) - 1]
      if str(taille)[-1] == 'W':
        taille = str(taille)[0:len(taille) - 1]
      if interesting['lowestAsk'] == 'None':
          prixHaut = prixBas
      else:
          prixHaut = interesting['lowestAsk']
      nbDemande = interesting['numberOfAsks']
      obj[str(taille)] = [prixBas, prixHaut, nbDemande]

      # print('Pour la taille ' + str(taille) + ' US.')
      # print('Le prix max est de ' + str(prixHaut) + "$.")
      # print('Et le prix le plus bas de ' + str(prixBas) + "$.")
      # print('Il y a actuellement ' + str(nbDemande) + ' demandes pour cette taille et ce modèle.\n')
      time.sleep(2)
      print("Tout va bien")
    allInfo.append(obj)
    cpt+=1
    print("On en est à la paire n°",cpt)
    if cpt == 0%3:
      print("petite pause")
      time.sleep(60)
    if cpt == 100:
       break
    

  
  
rows = []
end, _, name = endpointsCollector()
for i in range(cpt):
  rowsBuilder = {}
  rowsBuilder["id"] = i
  rowsBuilder["name"] = name[i]
  rowsBuilder["link"] = end[i]
  for key, value in allInfo[i].items():
    rowsBuilder[key] = value

  rows.append(rowsBuilder)

headers2 = ["id","name","link","3.5","4","4.5","5","5.5","6",
            "6.5","7","7.5","8","8.5","9","9.5","10","10.5",
            "11","11.5","12","12.5","13","13.5","14","14.5",
            "15","15.5","16","16.5","17","17.5","18"]


with open("all_data.csv", 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers2)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print('Done')