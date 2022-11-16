from threading import Thread #usar threads para acelerar o programa(nao implementado)
import requests,json,timeit

#faz a requisicao dos dados via api
def Requisicao(url):
  response = requests.get(url)
  objeto=response.json()
  intermediario = json.dumps(objeto)
  final = json.loads(intermediario)  
  return final


start = timeit.default_timer()

for num in range(1,20):
  x= Requisicao("https://zoo-animal-api.herokuapp.com/animals/rand")
  print(x["name"])

stop = timeit.default_timer()

print('Time: ', stop - start) 

