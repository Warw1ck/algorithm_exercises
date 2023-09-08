words = ["flower", "flourish", "flight"]


def longest_common_substring(words):
    sord_list = sorted(words, key=lambda x:len(x))
    longest_word = sord_list.pop()
    prefix = []
    for i in range(len(longest_word)):
        for n in range(i, len(longest_word)):
            prefix.append([ch for ch in longest_word[i:n]])
    prefix = list(filter(lambda x: len(x)>=2, prefix))
    common_prefix = []
    for pre in prefix:
        if len(list(filter(lambda x: ''.join(pre) in x, sord_list))) == len(sord_list):
            common_prefix.append(pre)
    if common_prefix:
        print(''.join(sorted(common_prefix)[-1]))
    else:
        print('No common prefix')



longest_common_substring(words)