# PhotoManager

`PhotoManager` é uma classe que permite conectar-se a uma URL e manipular imagens em memória. A classe oferece funcionalidades para conectar a uma URL, salvar, codificar em base64, decodificar de base64, converter para JPEG e comprimir imagens.

## Métodos

Inicializa a instância da classe com um nome e uma imagem opcional.

- `name`: O nome da imagem.
- `image`: A imagem em bytes ou base64 (opcional).

```python
"""Possibilidades para Instânciar"""

photo_manager.('minha-foto') # Instância Simples

photo_manager.('minha-foto', imagem_base64) # Instância com Foto Base64 em str
```


### Retorna a imagem atual armazenada na instância.
```python
photo_manager.get_image()
```

### Retorna a imagem recortada, se houver.
```python
photo_manager.get_croped_image()
```

### Define uma imagem como base64 em formato de string.
- `image_str`: A representação base64 da imagem em formato de string.
```python
photo_manager.set_image_as_str(image_str)
```

### Conecta-se a uma URL, recupera a imagem e a armazena na instância.
- `url`: A URL da imagem a ser conectada.
```python
photo_manager.connect_to_url(url)
```


### Salva a imagem atual em um arquivo no caminho especificado.
- `file_path`: O caminho onde a imagem recortada será salva.
  *deve finalizar com '/' se for no diretório, porém pode ser por exemplo finalizado em '/original-' para indicar que vai para arquele diretório e recebe no início do nome a palavra 'original-'.
```python
photo_manager.save_image(file_path)
```


### Salva a imagem recortada em um arquivo no caminho especificado.
- `file_path`: O caminho onde a imagem recortada será salva.
  *deve finalizar com '/' se for no diretório, porém pode ser por exemplo finalizado em '/original-' para indicar que vai para arquele diretório e recebe no início do nome a palavra 'cortada-'.
```python
photo_manager.save_croped_image(file_path)
```

### Converte a imagem atual em formato base64 e armazena na instância.
```python
photo_manager.to_base64()
```

### Decodifica a imagem da representação base64 e armazena na instância.
```python
photo_manager.from_base64()
```

### Converte a imagem atual para o formato JPEG e armazena na instância.
```python
photo_manager.to_jpeg()
```

### Comprime a imagem atual no formato JPEG com a qualidade especificada.
- `quality`: A qualidade da compressão (0-100).
```python
photo_manager.compress_image(85) # Comprime para 85 de qualidade
```

### Recorta a imagem com base em coordenadas proporcionais.
- `top`: Porcentagem da borda superior (0-100).
- `right`: Porcentagem da borda direita (0-100).
- `bottom`: Porcentagem da borda inferior (0-100).
- `left`: Porcentagem da borda esquerda (0-100).
```python
photo_manager.relative_crop(top, right, bottom, left)
```

# Exemplo de Uso
```python
# Origem e destino da imagem
origin_image = "https://images.alphacoders.com/601/601059.jpg"
save_path = "/media/jsrwell/1234-5678/"

# Instância e conexão obtendo a imagem
photo_manager = PhotoManager("giant-image")
photo_manager.connect_to_url(origin_image)

# Apenas para exemplo de conversão para base64 e retorno
photo_manager.to_base64()  
photo_manager.from_base64()

# Compreesão em 50%
photo_manager.compress_image(50)   

# Salvando a imagem original
photo_manager.save_image(f"{save_path}original-")

# Localizando as 3 faces com base na imagem original e salvando elas
photo_manager.relative_crop(top=5, right=55, bottom=17, left=50) 
photo_manager.save_croped_image(f"{save_path}face1-")
photo_manager.relative_crop(top=0, right=24, bottom=24, left=8) 
photo_manager.save_croped_image(f"{save_path}face2-")
photo_manager.relative_crop(top=3, right=82, bottom=10, left=77) 
photo_manager.save_croped_image(f"{save_path}face3-")
```
