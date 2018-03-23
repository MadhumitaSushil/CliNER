

if __name__ == '__main__':
    import doctest
    
    import os, sys

    CLINER_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    home = os.path.join(CLINER_DIR , 'cliner' )
    if home not in sys.path: sys.path.append(home)

    #from features_dir import *
    
    from code.feature_extraction import features
    doctest.testmod(features)

    from code.feature_extraction import read_config
    doctest.testmod(read_config)

    from code.feature_extraction import sentence_features
    doctest.testmod(sentence_features)

    from code.feature_extraction import utils
    doctest.testmod(utils)

    from code.feature_extraction import word_features
    doctest.testmod(word_features)
