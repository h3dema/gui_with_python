"""
    crawler que busca os resultados de busca de cep
    do site https://cepbrasil.org/

    - nao utilizar para uso comercial
    - pode parar de funcionar a qualquer momento

    http://github.com/h3dema/gui_with_python
"""

import re
import json
import requests


class ConteudoNaoLocalizado(Exception):
    pass


def busca_endereco_cep(cep: str):
    """
        Busca o endereco com base no CEP.
        Utiliza um webcrawler para buscar a informação de um site.

        Args:
            cep (str):

    """
    # checagem simples. Pode melhorar, e.g., converte em int e checa, mas ai tem que verificar casos como cep de Sao Paulo que começa com zero, etc...
    assert len(cep.strip()) == 8, f"CEP deve ter 8 caracteres. CEP fornecido: {cep}"

    url = f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=pt-PT&source=gcsc&gss=.com&cselibv=f275a300093f201a&cx=015319603693638169556:qrxl9xutvg0&q={cep.strip()}&safe=off&cse_tok=AB1-RNU0JMLWrlc_6kQ5YJDMKgXe:1665165673235&sort=&exp=csqr,cc&oq=31275050&gs_l=partner-generic.3...162744.164519.3.165318.8.8.0.0.0.0.68.485.8.8.0.csems,nrl=10...0....1.34.partner-generic..14.17.1210.V3BMkqKHKkk&callback=google.search.cse.api3916'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)

    # print("Status:", response.status_code)
    # print("Tipo da resposta", type(response.text))
    # print("Conteudo:\n", response.text)

    if "google.search.cse.api3916" in response.text:
        try:
            result = json.loads(re.findall(r"google.search.cse.api3916\((.*)\);", response.text.replace("\n", " "))[0])
        except IndexError:
            raise ConteudoNaoLocalizado("Conteudo nao localizado")
        except json.JSONDecodeError:
            raise ConteudoNaoLocalizado("Erro na conversao do json retornado pelo site.")

        results = result.get("results", None)
        if isinstance(results, list):
            # achou alguma coisa
            values = results[0].get("richSnippet", {}).get("postaladdress")
            # print(values)
            return {"Logradouro": values.get("streetaddress"),
                    "CEP": values.get("postalcode"),
                    "Cidade": values.get("addresslocality"),
                    "Estado": values.get("addressregion"),
                    }

    # se chegou aqui, eh porque nao achou
    return None


if __name__ == "__main__":
    #
    cep = busca_endereco_cep(cep="01002020")
    print(cep)
