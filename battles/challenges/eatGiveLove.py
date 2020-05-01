def eatGiveLove(m):
    verbs = {'吃': 'eat',
             '给': 'give',
             '爱': 'love'}

    subj = {'我': 'i',
            '你': 'you',
            '他': 'he',
            '她': 'she',
            'M': 'mother',
            'B': 'father',
            '饭': 'rice',
            'T': 'tofu',
            'N': 'beef',
            '鱼': 'fish',
            '钱': 'money',
    }
    
    rec = {'我': 'me',
           '你': 'you',
           '他': 'him',
           '她': 'her',
           'M': 'mother',
           'B': 'father',
           '饭': 'rice',
           'T': 'tofu',
           'N': 'beef',
           '鱼': 'fish',
           '钱': 'money',
    }


    m = m.replace('妈妈', 'M')
    m = m.replace('爸爸', 'B')
    m = m.replace('豆腐', 'T')
    m = m.replace('牛肉', 'N')

    w = list(m)

    def conjug(s, v):
        if s in "我你":
            return verbs[v]
        else:
            return verbs[v] + "s"
        
    # imperative
    if w[0] in verbs:
        if len(w) == 2:
            return "{} {}".format(verbs[w[0]], rec[w[1]])
        else:
            return "{} {} {}".format(verbs[w[0]], rec[w[1]], rec[w[2]])

    elif len(w) == 3:
        return "{} {} {}".format(subj[w[0]], conjug(w[0], w[1]), rec[w[2]])

    else:
        return "{} {} {} {}".format(subj[w[0]], conjug(w[0], w[1]), rec[w[2]], rec[w[3]])


pairtest(eatGiveLove("吃牛肉"), "eat beef",
         eatGiveLove("妈妈爱我"), "mother loves me",
         eatGiveLove("给我钱"), "give me money",
         eatGiveLove("爸爸给她饭"), "father gives her rice",
         eatGiveLove("我爱你"), "i love you",
         eatGiveLove("他给你钱"), "he gives you money",
         eatGiveLove("妈妈爱豆腐"), "mother loves tofu",
         eatGiveLove("爸爸爱她"), "father loves her",
         eatGiveLove("她给我豆腐"), "she gives me tofu",
         eatGiveLove("给妈妈饭"), "give mother rice",
         eatGiveLove("你吃饭"), "you eat rice",
         eatGiveLove("爸爸爱钱"), "father loves money",
         eatGiveLove("我吃牛肉"), "i eat beef",
         eatGiveLove("吃鱼"), "eat fish",
         eatGiveLove("妈妈给他鱼"), "mother gives him fish",
         eatGiveLove("他给爸爸牛肉"), "he gives father beef",
         )
