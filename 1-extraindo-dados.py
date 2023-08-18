# Databricks notebook source
import requests

def extraindo_dados(date, base="BRL"):

  url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"

  headers = {
  "apikey": "rsFBMyq54zoyvSQtFRAznhEOMFZkcCXV"
 }

  parametros = {"base":base}
 
  response = requests.request("GET", url, headers-headers, params = parametros)

  if response.status_code != 200:
    raise Exception("Não consegui extrair dados!!!")

  return response.json()


# COMMAND ----------

extraindo_dados("2022-09-07", base="BRL")

# COMMAND ----------

print(result)
