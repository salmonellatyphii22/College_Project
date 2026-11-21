def classify(prompt):

    prompt = prompt.lower()

    if any(word in prompt for word in
           ["python","java","c++","code","bug","program"]):
        return "Coding Help"

    elif any(word in prompt for word in
             ["grammar","correct","rewrite"]):
        return "Grammar Check"

    elif any(word in prompt for word in
             ["summary","summarize","shorten"]):
        return "Summarization"

    elif any(word in prompt for word in
             ["translate"]):
        return "Translation"

    elif any(word in prompt for word in
             ["email","letter"]):
        return "Email Writing"

    elif any(word in prompt for word in
             ["story","poem"]):
        return "Creative Writing"

    elif any(word in prompt for word in
             ["calculate","+","-","*","/","math"]):
        return "Mathematics"

    elif any(word in prompt for word in
             ["what is","define","explain"]):
        return "Explanation"

    else:
        return "General"