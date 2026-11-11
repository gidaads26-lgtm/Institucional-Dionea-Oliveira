# Site institucional | Dionea Oliveira

Site de uma página da Dionea Oliveira, hipnoterapeuta clínica, terapeuta de PNL e de reprogramação mental, especialista em ansiedade e autoestima. Atendimento presencial em Novo Hamburgo e Estância Velha (RS) e online.

## O que tem aqui

| Arquivo | Para que serve |
|-|-|
| `index.html` | O site pronto, com CSS e JavaScript embutidos. |
| `assets/` | Fotos do site e ícone do celular. |
| `og-image.jpg` | Imagem que aparece quando alguém compartilha o link (1200×630). Precisa ficar na raiz do domínio. |
| `fonte/src.html` | O código-fonte para editar, com marcadores no lugar das fotos. |
| `fonte/build.py` | Gera o `index.html` final a partir da fonte. |

## Como publicar

O site está na Vercel, ligado a este repositório: cada envio para a `main` publica sozinho. Em outra hospedagem, envie `index.html`, `og-image.jpg` e a pasta `assets/` para a pasta pública.

## Onde trocar os dados

- **WhatsApp e Instagram:** no fim do `index.html` (ou do `fonte/src.html`), nas constantes `WHATSAPP` e `INSTAGRAM`. Os botões usam esses valores.
- **Endereço do site:** hoje é `https://institucionaldioneaoliveira.vercel.app`. Ele aparece no topo do arquivo (canonical, Open Graph, Twitter Card e JSON-LD). Se o site passar para um domínio próprio, troque todas as ocorrências.
- **Prévia no WhatsApp e redes:** a imagem é `og-image.jpg` (1200×630). Se trocar a imagem, aumente o número em `og-image.jpg?v=3` para as redes buscarem a versão nova.

## Como editar

1. Altere `fonte/src.html` (ou troque uma foto em `assets/` mantendo o mesmo nome).
2. Rode `python3 fonte/build.py` na raiz do repositório.
3. Publique o `index.html` gerado.

## Pendências

- Endereços completos (rua, número, bairro e CEP) de Novo Hamburgo e Estância Velha.
- Formação da Dionea: cursos, instituições e há quanto tempo atende.
- WhatsApp configurado: +55 51 8402-0168 (wa.me/555184020168).
- Confirmar com as participantes do Desafio Código da Calma o uso dos depoimentos no site.
