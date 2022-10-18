from wordexpansion import ChineseSoPmi

sopmier = ChineseSoPmi(inputtext_file='test/test_corpus.txt',
                       seedword_txtfile='test/test_seed_words.txt',
                       pos_candi_txt_file='test/pos_candi.txt',
                       neg_candi_txtfile='test/neg_candi.txt')
sopmier.sopmi()