import random
import fasttext

input = "/workspace/datasets/fasttext/labeled_products.txt"
output = "/workspace/datasets/fasttext/pruned_labeled_products.txt"
shuffled = "/workspace/datasets/fasttext/shuffled_pruned_labeled_products.txt"
training = "/workspace/datasets/fasttext/shuffled_pruned_training_data.txt"
test = "/workspace/datasets/fasttext/shuffled_pruned_test_data.txt"
minimumLabels = 500

inputFile = open(input, 'r')
outputFile = open(output, 'w+')
shuffledFile = open(shuffled, 'w+')
trainingFile = open(training, 'w+')
testFile = open(test, 'w+')

categoryToProducts = {}

for line in inputFile.readlines():
    category = line[0:line.find(' ')]
    name = line[line.find(' '):len(line)]

    if categoryToProducts.get(category) is None:
        categoryToProducts[category] = []
    
    categoryToProducts[category].append(name)

for category in categoryToProducts:
    if len(categoryToProducts[category]) >= minimumLabels:
        for product in categoryToProducts[category]:
            outputFile.write(category + " " + product)

outputFile.seek(0)
lines = outputFile.readlines()
random.shuffle(lines)
shuffledFile.writelines(lines)

shuffledFile.seek(0)
for line in (shuffledFile.readlines()[:10000]):
    trainingFile.write(line)

shuffledFile.seek(0)
for line in shuffledFile.readlines()[-10000:]:
    testFile.write(line)

model = fasttext.train_supervised(input=training, lr=1.0, epoch=25, wordNgrams=2)
print(model.test(test))