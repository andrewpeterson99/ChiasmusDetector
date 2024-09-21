

class ResponseVerdict:
    Yes = "Yes"
    No = "No"

class LLM:
    def prompt(text):
        to_send = """
        You are an expert in analyzing a poetic structure called "chiasmus." A chiasmus is a poem that acts as a mirror, where the first half of the poem is reflected in the second half (semantically). 
        You have been asked to analyze a poem to determine if it is a chiasmus.
        The poem is as follows:
        ‘There's no question Grape-Nuts is right for you. The question is, are you right for Grape-Nuts?’
        Your response should ONLY contain the following:
        Is this a chiasmus? (yes/no)
        How certain are you in your answer? (1-10)
        """

        test_return_value = "Yes\n10"
        return test_return_value

    #function to extract the "Yes" and "10" from the response as a tuple
    def extract_response(response):
        response_tuple = response.split("\n")
        verdict = ResponseVerdict.Yes if response_tuple[0].lower() == "yes" else ResponseVerdict.No
        certainty = int(response_tuple[1])
        return (verdict, certainty)


instance = LLM()
instance.prompt("There's no question Grape-Nuts is right for you. The question is, are you right for Grape-Nuts?")