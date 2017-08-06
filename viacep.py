 # -*- coding:utf-8 -*-

import requests

url_via_cep = "https://viacep.com.br/ws/{cep}/json/"

def address_by_cep(cep):

    resource = url_via_cep.format(cep=cep)
    response = requests.get(resource).json()

    return response

def show_address(address):
    
    if "show" in address:
        print("Dados não encontrados")
    else:
        print("CEP: {}".format(address.get("cep")))
        print("Logradouro: {}".format(address.get("logradouro")))
        print("Complemento: {}".format(address.get("complemento")))
        print("Bairro: {}".format(address.get("bairro")))
        print("Localidade: {}".format(address.get("bairro")))
        print("UF: {}".format(address.get("uf")))
        print("Unidade: {}".format(address.get("unidade")))
        print("IBGE: {}".format(address.get("ibge")))
        print("GIA: {}".format(address.get("gia")))

if __name__ == "__main__":

    cep = "01001000"

    print("Endereço pesquisado:\n")

    show_address(address_by_cep(cep))