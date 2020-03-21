# The part of speech
POS_dic = {'CC': ['but', 'nor', 'or', 'and'],
        'WRB': ['how', 'why', 'when'],
        'RP': ['up'],
        'PRP$': ['my', 'his', 'its', 'your', 'her', 'their'],
        'PRP': ['me', 'us', 'him', 'she', 'themselves', 'he', 'herself', 'you', 'them', 'they', 'it'],
        'IN': ['over', 'than', 'like', 'in', 'before', 'about', 'with', 'of', 'that', 'as', 'if', 'at', 'though', 'into', 'by', 'for', 'on'],
        'VBG': ['surrounding', 'settling', 'thinking', 'entering', 'visiting', 'marrying', 'giving'],
        'VBP': ['think', 'have', 'say', 'do', 'are', 'want', 'am', 'dare'],
        'FW': ['i'],
        'WDT': ['which'],
        'VB': ['give', 'recommend', 'pretend', 'go', 'tell', 'see', 'let', 'affect', 'engage', 'consider', 'assure', 'understand', 'develop', 'mean', 'get', 'take', 'throw', 'be', 'make', 'know', 'send'],
        'JJR': ['better', 'more', 'less'],
        'VBN': ['known', 'fixed', 'made', 'heard', 'returned', 'grown', 'determined', 'considered', 'taken', 'been'],
        'NN': ['such', 'sir', 'possession', 'of', 'quickness', 'information', 'beauty', 'the', 'lucas', 'mistake', 'nonsense', 'caprice', 'invitation', 'none', 'man', 'delight', 'hearing', 'party', 'compassion', 'humoured', 'thing', 'humour', 'property', 'business', 'neighbourhood', 'day', 'as', 'respect', 'character', 'netherfield', 'chaise', 'truth', 'talk', 'abuse', 'morris', 'estab', 'them', 'house', 'do', 'temper', 'three', 'design', 'by', 'occasion', 'something', 'news', 'visit', 'england', 'word', 'good', 'monday', 'whichever', 'may', 'end', 'likely', 'bingley', 'must', 'discontented', 'solace', 'objection', 'he', 'wife', 'name', 'bennet', 'love', 'always', 'sarcastic', 'lizzy', 'desire', 'week', 'it', 'rightful', 'fall', 'mind', 'park', 'mr', 'ignorant', 'preference', 'way', 'lishment', 'woman', 'general', 'half', 'when', 'place', 'understanding', 'you', 'jane', 'chapter', 'michaelmas', 'was', 'mrs', 'fortune', 'bit', 'vexing', 'consideration', 'so', 'impatiently', 'flatter', 'our', 'to', 'anything', 'ought', 'reserve', 'with', 'think', 'mixture', 'account', 'william', 'fancied', 'nerves', 'lady', 'year', 'experience', 'lydia', 'still', 'answer', 'cried', 'fine', 'than', 'consent'],
        'TO': ['to'],
        'DT': ['an', 'a', 'the', 'all', 'any', 'this', 'no', 'these', 'some'],
        'VBD': ['came', 'told', 'had', 'was', 'acknowledged', 'said', 'replied', 'agreed'],
        'JJ': ['large', 'such', 'last', 'insufficient', 'young', 'old', 'little', 'first', 'impossible', 'high', 'hearty', 'sure', 'quick', 'long', 'odd', 'poor', 'single', 'married', 'tiresome', 'nervous', 'much', 'handsome', 'silly', 'own', 'extraordinary', 'good', 'glad', 'scrupulous', 'other', 'next', 'uncertain', 'few'],
        'NNS': ['views', 'newcomers', 'parts', 'servants', 'daughters', 'girls', 'others', 'children', 'minds', 'feelings', 'nerves', 'friends', 'sisters', 'cases', 'families', 'years'],
        'VBZ': ['chooses', 'says', 'has', 'comes', 'is'],
        'RB': ['just', 'only', 'however', 'very', 'so', 'north', 'often', 'well', 'down', 'indeed', 'merely', 'certainly', 'enough', 'dear', 'universally', 'soon', 'immediately', 'therefore', 'not', 'here', 'now', 'perhaps', 'surely'],
        'WP': ['who', 'what'],
        'MD': ['may', 'will', 'must', 'would', 'can'],
        'JJS': ['least', 'best'],
        'CD': ['five', 'one', 'four', 'thousand', 'twenty'],
        'UH': ['oh']
        }


# Here your code
while True:
    file_name = input("Which file? ")
    if file_name=="-1":
        break
    while True:
        pos_list={}
        pos_name = input("Which POS? ")
        if pos_name == "-1":
            break
        if pos_name not in POS_dic:
            print("There isn't",pos_name,"in POS")
            continue
        file = open(file_name,"r")
        for line in file:
            line1=str(line).replace("."," ")
            line2=line1.replace("'"," ")
            line3=line2.replace(","," ")
            line4=line3.replace("?"," ")
            line5=line4.replace("-"," ")
            line6=line5.replace(";"," ")
            line7=line6.replace("!"," ")
            line8=line7.lower()
            line9=line8.split()
            line = line9
            for word in line:
                if word in POS_dic[pos_name]:
                    if word in pos_list:
                        pos_list[word] +=1
                    else:
                        pos_list[word] = 1
        print(pos_list)
        print()
        file.close()
