palavras começadas com letras maiusculas

```
([A-Z])\w+
```

telefone começado com 9 ou 8
```
([89][0-9]{8})
```

palavras começadas com letras maiusculas
```
([A-Z][a-z]*)
```

palavras começadas com letras maiusculas e caracteres especiais
```
([A-Z][a-z\u00C0-\u00FF]*)
```

validar email
```
([a-zA-Z0-9_\-\.\+]+[@][a-z]+[.][a-z]{3})
```

hash md5
```
([0-9a-f]){32}
```

hash sha1
```
([0-9a-f]){40}
```

pegar texto ignorando limiters dentro do texto
```
([^promotor][A-Za-z].*[^\(a-z\)])
```

caracteres especiais
```
([!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?\]*$])
```

pegar somente texto em um lista 
( Nico Steppat|14/05/1977|Rua Buarque de Macedo|50|22222-222|Rio de Janeiro )
```
[^\|]([A-Za-z\s]+)[^\|]
```