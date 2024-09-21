

class LLM:
    def prompt(text):
        return 
        """
        You are an expert in analyzing a poetic structure called "chiasmus." A chiasmus is a poem that acts as a mirror, where the first half of the poem is reflected in the second half (semantically). 
        You have been asked to analyze a poem to determine if it is a chiasmus.
        The poem is as follows:
        ‘There's no question Grape-Nuts is right for you. The question is, are you right for Grape-Nuts?’
        Your response should ONLY contain the following:
        Is this a chiasmus? (yes/no)
        How certain are you in your answer? (1-10)
        """


instance = LLM()
instance.prompt("There's no question Grape-Nuts is right for you. The question is, are you right for Grape-Nuts?")