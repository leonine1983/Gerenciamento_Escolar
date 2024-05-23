from django import template

register = template.Library()

@register.filter(name='criar_sigla')
def criar_sigla(value):
    # Dividir o valor em palavras
    palavras = value.split()

    # Pegar a primeira letra de cada palavra e juntá-las
    sigla = ''.join(word[0].upper() for word in palavras)

    return sigla