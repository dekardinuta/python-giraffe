
es_hombre = False
es_alto = False

#if es_hombre or es_alto:
#    print("Eres hombre o alto, o ambos")
#else:
#    print("No eres hombre, ni alto")

#if es_hombre and es_alto:
#    print("es un hombre alto")
#else:
#    print("ni es hombre ni es alto")

if es_hombre and es_alto:
    print("es un hombre alto")
elif es_hombre and not(es_alto):
    print("eres un hombre bajo")
elif not(es_hombre) and es_alto:
    print("no eres hombre pero eres alto")
else:
    print("ni eres hombre ni eres alto")
