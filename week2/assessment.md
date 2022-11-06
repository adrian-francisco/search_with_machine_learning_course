# Assessment

1. For classifying product names to categories:

    - What precision (P@1) were you able to achieve?

        $ ~/fastText-0.9.2/fasttext test product_classifier.bin test_data.txt 
        N       9669
        P@1     0.652
        R@1     0.652

    - What fastText parameters did you use?

        $ ~/fastText-0.9.2/fasttext supervised -input training_data.txt -output product_classifier -lr 1.0 -epoch 25 -wordNgrams 2

    - How did you transform the product names?

        cat /workspace/datasets/fasttext/shuffled_labeled_products.txt |sed -e "s/\([.\!?,'/()]\)/ \1 /g" | tr "[:upper:]" "[:lower:]" | sed "s/[^[:alnum:]_]/ /g" | tr -s ' ' > /workspace/datasets/fasttext/normalized_labeled_products.txt

    - How did you prune infrequent category labels, and how did that affect your precision?

        (search_with_ml) gitpod /workspace/search_with_machine_learning_course/week2 (main) $ python pruneLabeledProducts.py 
        Read 0M words
        Number of words:  6719
        Number of labels: 32
        (9967, 0.9699006722183204, 0.9699006722183204)

    - How did you prune the category tree, and how did that affect your precision?

        N/A

2. For deriving synonyms from content:

    - What were the results for your best model in the tokens used for evaluation?

        (search_with_ml) gitpod /workspace/datasets/fasttext $ ~/fastText-0.9.2/fasttext nn title_model.bin 

        Query word? headphones
        headphone 0.93314
        earbud 0.900922
        ear 0.86424
        earphones 0.830453
        earbuds 0.744133
        bud 0.742874
        2xl 0.724573
        behind 0.715003
        ears 0.711591
        microphones 0.710679

        Query word? laptop
        laptops 0.724873
        laps 0.702514
        156b 0.698645
        174 0.675639
        172 0.674083
        177 0.674072
        17r 0.671922
        l305d 0.670067
        lapdesk 0.669725
        lapgear 0.667516

        Query word? freezer
        freezers 0.917305
        refrigerator 0.822141
        frost 0.799795
        refrigerators 0.799712
        cu 0.744186
        customstyle 0.743709
        cleansteel 0.741717
        satina 0.726023
        mug 0.72581
        ft 0.724251

        Query word? nintendo
        nintendogs 0.975516
        ds 0.916309
        wii 0.871617
        3ds 0.845404
        gamecube 0.776787
        rabbids 0.773047
        psp 0.728653
        luigi 0.728271
        ninjas 0.725994
        katmai 0.721348

        Query word? whirlpool
        whirl 0.870835
        maytag 0.854945
        biscuit 0.843085
        frigidaire 0.824981
        bisque 0.813661
        cleansteel 0.773059
        hotpoint 0.760662
        bahama 0.747576
        gallery 0.743749
        ge 0.739077

        Query word? kodak
        easyshare 0.876168
        m763 0.788951
        m863 0.784232
        m893 0.774387
        m341 0.757219
        c813 0.750543
        m1063 0.746262
        m381 0.742557
        m340 0.73907
        m590 0.719541

        Query word? ps2
        ps3 0.884508
        2k5 0.817576
        gba 0.813262
        2k3 0.803736
        xbox 0.803344
        gamecube 0.799325
        2k6 0.793146
        nhl 0.793036
        2k8 0.790634
        psp 0.78485

        Query word? razr
        krzr 0.898193
        a855 0.888881
        i90c 0.878735
        e71 0.87604
        i55sr 0.86558
        i60c 0.865493
        r225 0.862825
        sgh 0.861384
        i50sx 0.860903
        7v 0.850002

        Query word? stratocaster
        telecaster 0.928238
        starcaster 0.886682
        strat 0.827563
        forecaster 0.817743
        squier 0.817059
        hss 0.810459
        synyster 0.807102
        fender 0.771956
        sunburst 0.760373
        tremolo 0.755661

        Query word? holiday
        holidays 0.976752
        kwanzaa 0.843171
        congrats 0.837444
        día 0.837285
        vibes 0.831365
        cumpleaños 0.826011
        hanukkah 0.822809
        dreidel 0.818025
        slaphappy 0.815651
        birthday 0.813089

        Query word? plasma
        600hz 0.848825
        58 0.808571
        hdtvs 0.808529
        480hz 0.808278
        73 0.806592
        hdtv 0.801524
        63 0.798324
        480p 0.79422
        xbr 0.792713
        regza 0.787754

        Query word? leather
        leatherskin 0.905709
        recliner 0.712574
        hipcase 0.667525
        sofa 0.663437
        magnolia 0.662782
        berkline 0.6598
        weather 0.651577
        curved 0.648482
        theaterseatstore 0.646529
        featherlite 0.640426

    - What fastText parameters did you use?

        $ ~/fastText-0.9.2/fasttext skipgram -input normalized_titles.txt -output -output title_model

    - How did you transform the product names?

        cat /workspace/datasets/fasttext/titles.txt | sed -e "s/\([.\!?,'/()]\)/ \1 /g" | tr "[:upper:]" "[:lower:]" | sed "s/[^[:alnum:]]/ /g" | tr -s ' ' > /workspace/datasets/fasttext/normalized_titles.txt

3. For integrating synonyms with search:

    - How did you transform the product names (if different than previously)?

        used the same

    - What threshold score did you use?

        0.75

    - Were you able to find the additional results by matching synonyms?

        yes, updated query.py with synonyms flag and retrieved more results with synonyms than without

4. For classifying reviews:

    - What precision (P@1) were you able to achieve?

        N/A

    - What fastText parameters did you use?

        N/A

    - How did you transform the review content?

        N/A

    - What else did you try and learn?

        N/A