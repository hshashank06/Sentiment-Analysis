project = open('project_twitter_data.csv','r')
result = open('resulting_data.csv','w')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(str1):
    for i in punctuation_chars:
        str1 = str(str1).replace('%s' % i, '')
    
    return str1

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
positive_words.append('#incredible')
#print(positive_words)
def get_pos(str1):
    #print(str1)
    
    count = 0
    stri = str1.lower()
    lst = stri.split()
    for item in lst:
        #print(item)
        if item in positive_words:
            
            count = count + 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
negative_words.append('abrupt.')
#print(negative_words)
def get_neg(str2):
    print(str2)
    str2 = str2.lower()
    #print(str2)
    counts = 0
    new_ls = str2.split()
    #print(new_ls)
    for item in new_ls:
        if item in negative_words:
            counts = counts + 1
    return counts


def results(result):

    result.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    result.write('\n')    
    file = project.readlines()
    headnot = file.pop(0)
    for line in file:
        lin = line.strip().split(',')
        lins = strip_punctuation(lin[0])
        result.write('{}, {}, {}, {}, {}'.format(lin[1],lin[2],get_pos(lins),get_neg(lins),(get_pos(lins)-get_neg(lins))))
        result.write('\n')

  
results(result)
project.close()
result.close()
    
