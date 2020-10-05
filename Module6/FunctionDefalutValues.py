def score_input(test_name, test_score = 0, invalid_message = 'Invalid test score, try again!'):
    if test_score == 0:
        print("Enter the test score : ")
        test_score = input()
        test_score = int(test_score)
    else:
        while 0 > test_score > 100:
            print(invalid_message)
        print("Re-Enter the test score, 0-100")
        test_score = int(test_score)
    test_score = str(test_score)
    print(test_name + " : " + test_score)
def test_score_name():
    score_input("Bob Bill")
def test_score_valid():
    score_input("Bill Billington", 70)
def test_score_below():
    score_input("Sue Suzan", -4)
def test_score_above():
    score_input("Jill Crim", 112)
def test_score_all_parameters():
    score_input("Earl Crim", 99, "Wrong!!")

if __name__ == '__main__' :
    '''demonstrating that score_input can take in one value'''
    test_score_name()
    '''demonstrating testing of manditory name and test score'''
    test_score_valid()
    '''test of a score below required range'''
    test_score_below()
    '''test of score above required range'''
    test_score_above()
    test_score_all_parameters()

