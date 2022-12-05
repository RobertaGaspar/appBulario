import requests
from django.shortcuts import render


def search(request, template_name="search.html"):
    return render(request, template_name)


def listing(request, template_name="listing.html"):
    nomeMedicamento = "DIPIRONA"
    endpoint = 'https://bula.vercel.app/pesquisar?nome=' + nomeMedicamento
    response = requests.get(endpoint)
    lista = response.json()['content']

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "medicamentos": dicionario
    }

    return render(request, template_name, contexto)


def listing(request, template_name="listing.html"):
    endpoint = 'https://bula.vercel.app/filtrar?nomeProduto=acetilcisteínanumeroRegistro=1097402230041expediente=4291960221razaoSocial=UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/Acnpj=60665981000118data=2022-06-14T08:44:18.000-0300'
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "expediente": "4774506222"
    }

    response = requests.post(endpoint, json=payload, headers=headers)
    lista = response.json()['content']

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "medicamentos": dicionario
    }

    return render(request, template_name, contexto)
