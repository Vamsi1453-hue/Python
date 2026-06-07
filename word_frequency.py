# an ai resume screening tool counts keywords frequencies in a resume text. given a string of resume text build a dictionary where keys are unique words 
def keyword_frequency(resume_text): 
    words = resume_text.lower().split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

resume = "Python SQL Python Data Analysis SQL Excel Python"
print(keyword_frequency(resume))
