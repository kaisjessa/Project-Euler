import math
def get_anagrams():
    with open("files/pe098_words.txt", 'r') as f:
        l = f.read().replace('"', '').split(",")
        word_dict = {}
        for w in l:
            word_dict[''.join(sorted(w))] = []
        for w in l:
            word_dict[''.join(sorted(w))].append(w)

        anagrams = []
        for k in word_dict:
            if(len(word_dict[k]) > 1):
                anagrams.append(word_dict[k])
    
    for a in anagrams:
        if(len(a) > 2):
            anagrams.remove(a)
            anagrams.append([a[0], a[1]])
            anagrams.append([a[1], a[2]])
            anagrams.append([a[0], a[2]])
    anagrams.sort(key=lambda x: len(x[0]), reverse=True)
    return anagrams

def largest_square(pair):
    m = -1
    a,b = pair
    l = len(a)
    i = 1
    p = str(i**2)
    while(len(p) <= l):
        if(len(p) == l and len(list(set(list(p)))) == len(p)):
            temp = b[:]
            for j in range(l):
                temp = temp.replace(a[j], p[j])
            if math.sqrt(int(temp)) % 1 == 0 and temp[0] != '0':
                m = max(m, max(int(p), int(temp)))
        i += 1
        p = str(i**2)
    return(m)

if __name__ == "__main__":
    anagrams = get_anagrams()
    m = -1
    for a in anagrams:
        m = max(m, largest_square(a))
    print(m)
