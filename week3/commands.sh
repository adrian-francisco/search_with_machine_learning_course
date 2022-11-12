shuf /workspace/datasets/fasttext/labeled_queries.txt > /workspace/datasets/fasttext/shuffled_labeled_queries.txt

head -50000 /workspace/datasets/fasttext/shuffled_labeled_queries.txt > /workspace/datasets/fasttext/training_queries.txt
tail -10000 /workspace/datasets/fasttext/shuffled_labeled_queries.txt > /workspace/datasets/fasttext/test_queries.txt

cd /workspace/datasets/fasttext

~/fastText-0.9.2/fasttext supervised -input training_queries.txt -output queries_model
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt
    R@1     0.488
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt 3
    R@3     0.653
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt 5
    R@5     0.714

~/fastText-0.9.2/fasttext supervised -input training_queries.txt -output queries_model -lr 0.5 -epoch 25 -wordNgrams 2
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt
    R@1     0.528
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt 3
    R@3     0.71
~/fastText-0.9.2/fasttext test queries_model.bin test_queries.txt 5
    R@5     0.777