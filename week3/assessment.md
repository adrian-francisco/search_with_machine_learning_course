# Week 3 Project Assessment

1. For query classification:

	- How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?

		```
		$ python create_labeled_queries.py --min_queries 1000
		number of unique categories: 375

		$ python create_labeled_queries.py --min_queries 10000
		number of unique categories: 58
		```

	- What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.

		```
		~/fastText-0.9.2/fasttext supervised -input training_queries.txt -output queries_model
			R@1     0.488
			R@3     0.653
			R@5     0.714

		~/fastText-0.9.2/fasttext supervised -input training_queries.txt -output queries_model -lr 0.5 -epoch 25 -wordNgrams 2
			R@1     0.528
			R@3     0.71
			R@5     0.777
		```

2. For integrating query classification with search:

	- Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.

		```
		query: laptop
		results without filtering: 7255
		results with filtering: 1492
		classifier output:
			labeled as: __label__pcmcat247400050000 with probability: 0.6350484490394592

		query: ipod
		results without filtering: 8433
		results with filtering: 129
		classifier output:
			labeled as: __label__abcat0201011 with probability: 0.6997542977333069

		query: xbox
		results without filtering: 2676
		results with filtering: 69
		classifier output:
			labeled as: __label__abcat0701001 with probability: 0.6083675026893616
		```

	- Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

		```
		query: iphone
		result: top hit was an HDTV when sorting by price, categories were wrong
		classifier output:
			labeled as: __label__cat02015 with probability: 0.2484178990125656
			labeled as: __label__cat09000 with probability: 0.09025927633047104
			labeled as: __label__pcmcat247400050000 with probability: 0.05321386083960533
			labeled as: __label__cat02009 with probability: 0.05176478251814842
			labeled as: __label__abcat0101001 with probability: 0.031204992905259132
			labeled as: __label__abcat0301014 with probability: 0.02280971221625805
			labeled as: __label__pcmcat209400050001 with probability: 0.020235443487763405

		query: beats
		result: top hit was an HP laptop when sorting by price, categories were wrong
		classifier output:
			labeled as: __label__cat02015 with probability: 0.2460121065378189
			labeled as: __label__cat09000 with probability: 0.09020650386810303
			labeled as: __label__pcmcat247400050000 with probability: 0.052727110683918
			labeled as: __label__cat02009 with probability: 0.051959455013275146
			labeled as: __label__abcat0101001 with probability: 0.03150687366724014
			labeled as: __label__abcat0301014 with probability: 0.02346012555062771
			labeled as: __label__pcmcat209400050001 with probability: 0.02006489224731922
		```