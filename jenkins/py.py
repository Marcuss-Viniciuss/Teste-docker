def process_line(line):
    inside_quotes = False
    processed_line = ""

    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes
        if char == ',' and inside_quotes:
            char = ' '

        processed_line += char

    return processed_line

caminho_do_arquivo = 'actors.csv'
contagem_filmes = {}

with open(caminho_do_arquivo, 'r') as file:
    lines = file.readlines()

for line_number, line in enumerate(lines[1:], start=2):
    processed_line = process_line(line)
    fields = processed_line.split(",")

    if len(fields) >= 6:
        movie_name = fields[4].strip()
        contagem_filmes[movie_name] = contagem_filmes.get(movie_name, 0) + 1
    else:
        print(f"ignorando linha {line_number}: número insuficiente de campos")

if contagem_filmes:
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]), reverse=True)

    with open('resultados_contagem_filmes.txt', 'w') as output_file:
        for sequencia, (filme, quantidade) in enumerate(filmes_ordenados, start=1):
            output_file.write(f"{sequencia} - O filme {filme} aparece {quantidade} vez(es) no dataset\n")

    print("resultados estão salvos no arquivo 'resultados_contagem_filmes.txt'")
else:
    print("não há dados válidos para a contagem de filmes.")