import os
import requests
from bs4 import BeautifulSoup

def conexionQ() -> bool:
    try:
        URL = "https://www.ine.gob.gt/ine/institucion/organizacion/"
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        requests.get(url=URL, headers=headers)
        return True
    except:
        return False

def junta_directiva(ruta: str):
    URL = "https://www.ine.gob.gt/ine/institucion/organizacion/"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    r = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    recuadros = soup.find_all("div", attrs={"class":"vc_tta-panel-body"})

    junta_directiva = {}
    for i in range(2):
        apartados = [texto.text for texto in recuadros[i].find_all("h3", attrs={"class":"vc_custom_heading"})]
        sub_apartados = [texto.text.replace(u'\xa0', u' ').replace("\nT", "T") for texto in recuadros[i].find_all("p", attrs={"style":"text-align: center;"})]
        if i == 0:
            sub_apartados = [titular_suplente.replace("Titular: ", "").split("\nSuplente: ") for titular_suplente in sub_apartados]
            sub_apartados_dict = [dict(zip(("TITULAR", "SUPLENTE"), titular_suplente)) for titular_suplente in sub_apartados]
            junta_directiva["JUNTA DIRECTIVA"] = dict(zip(apartados, sub_apartados_dict))
        else:
            sub_apartados_replace = [i.replace("Subgerencia Técnica\n", "").replace("Subgerencia Administrativa Financiera\n", "") for i in sub_apartados]
            junta_directiva["GERENCIA"] = dict(zip(("GERENTE", "SUBGERENTE TECNICO", "SUBGERENTE ADMINISTRATIVO FINANCIERO"), sub_apartados_replace))

    with open(os.path.join(ruta, "organizacion.tex"), mode='w', encoding='utf-8') as file:
        file.write("{\\Bold \\LARGE AUTORIDADES}\\\\[1cm]\n")
        file.write("{\\Bold \\large \\color{color1!89!black} JUNTA  DIRECTIVA} \\\\[0.4cm]\n")
        for ministerio, titular_suplente in junta_directiva["JUNTA DIRECTIVA"].items():
            file.write("{\\Bold " + ministerio + "}\\\\ \n")
            file.write("Titular: {}\\\\ \n".format(titular_suplente["TITULAR"]))
            file.write("Suplente: {}\\\\[0.4cm]\n\n".format(titular_suplente["SUPLENTE"]))
        file.write("{\\Bold \\large \\color{color1!89!black} GERENCIA}\\\\[0.2cm]\n")
        for puesto, nombre in junta_directiva["GERENCIA"].items():
            file.write("{}: {}\\\\ \n".format(puesto.title().replace("Tecnico", "Técnico"), nombre))
