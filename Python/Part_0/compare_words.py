key_graph = {"q" : ["w", "a"],
             "w" : ["q", "a", "s", "e"],
             "e" : ["w", "s", "d", "r"],
             "r" : ["e", "d", "f", "t"],
             "t" : ["r", "f", "g", "y"],
             "y" : ["t", "g", "h", "u"],
             "u" : ["y", "h", "j", "i"],
             "i" : ["u", "j", "k", "o"],
             "o" : ["i", "k", "l", "p"],
             "p" : ["o", "l"],
             "a" : ["q", "w", "s", "z"],
             "s" : ["a", "w", "e", "d", "x", "z"],
             "d" : ["s", "e", "r", "f", "c", "x"],
             "f" : ["d", "r", "t", "g", "v", "c"],
             "g" : ["f", "t", "y", "h", "b", "v"],
             "h" : ["g", "y", "u", "j", "n", "b"],
             "j" : ["h", "u", "i", "k", "m", "n"],
             "k" : ["j", "i", "o", "l", "m"],
             "l" : ["k", "o", "p"],
             "z" : ["a", "s", "x"],
             "x" : ["z", "s", "d", "c"],
             "c" : ["x", "d", "f", "v"],
             "v" : ["c", "f", "g", "b"],
             "b" : ["v", "g", "h", "n"],
             "n" : ["b", "h", "j", "m"],
             "m" : ["n", "j", "k"]}

def breadth_first(graph,start, end):
    """
    Breadth First Search Algorithm.
    Returns shortest path.
    -------------------------------------
    Inputs:
        graph : Dictionary of connecting nodes
        start : Starting point on the graph
        end   : Ending point on the graph
    Outputs:
        path  : List of shortest path
    """
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def find_difference(seg1, seg2):
    """
    Utilizes graph distance to find the differences between similar length segments of words.
    """
    letter_score = []
    for c1,c2 in zip(seg1, seg2):
        letter_score.append(float(len(breadth_first(key_graph, c1, c2)) - 1))
    return sum(letter_score)/len(letter_score)


def compare_words(word1, word2):
    """
    Main function to check keystroke differences between words.
    """
    word1 = word1.lower()
    word2 = word2.lower()
    seg_scores = []
    if len(word1) >= len(word2):
        for i in range(0, len(word1) - len(word2) + 1):
            seg_scores.append(find_difference(word1[i:i+len(word2)], word2))
    else:
        for i in range(0, len(word2) - len(word1) + 1):
            seg_scores.append(find_difference(word2[i:i+len(word1)], word1))
    return round(min(seg_scores) + abs(len(word1) - len(word2))/float(len(max([word1, word2]))),2)




if __name__ == "__main__":
    word1 = input("What is the first word?  ")
    word2 = input("What is the second word?  ")
    comp = compare_words(word1, word2)
    print("The similarity between '{}'' and '{}' is: {}".format(word1,
                                                                word2,
                                                                comp))
