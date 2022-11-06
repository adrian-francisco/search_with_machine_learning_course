import fasttext

model = fasttext.load_model("/workspace/datasets/fasttext/title_model.bin")
top_words_file = open("/workspace/datasets/fasttext/top_words.txt", 'r')
synonyms = open("/workspace/datasets/fasttext/synonyms.csv", 'w')
threshold = 0.75

for word in top_words_file.readlines():
    neighbors = model.get_nearest_neighbors(word)
    for neighbor in neighbors:
        fixed_word = word.strip()
        if neighbor[0] >= threshold:
            synonyms.write(neighbor[1] + ",")
    synonyms.write("\n")
