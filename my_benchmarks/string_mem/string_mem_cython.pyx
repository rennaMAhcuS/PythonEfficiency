def word_count(str text):
    cdef dict counts = {}
    cdef str word
    cdef int i
    words = text.split()
    for i in range(len(words)):
        word = words[i]
        counts[word] = counts.get(word, 0) + 1
    return counts
