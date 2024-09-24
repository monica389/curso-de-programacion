texto = "Los miles de millones de seres humanos que viven (conectados)"
"palabras_clave = ["conectados"]
palabra_destacada = next(palabra for palabra in palabras_clave if palabra in texto )
print(f"Palabra_detectada:{palabra_detectada}")