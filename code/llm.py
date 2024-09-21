class LLM:
    #TODO: interpolate the text into the prompt
    def prompt(self, text: str):
        to_send = """
        You are an expert in analyzing a poetic structure called "chiasmus." A chiasmus is a poem that acts as a mirror, where the first half of the poem is reflected in the second half (semantically). 
        You have been asked to analyze a poem to determine if it is a chiasmus.
        The poem is as follows:
        ‘There's no question Grape-Nuts is right for you. The question is, are you right for Grape-Nuts?’
        Your response should ONLY contain the following:
        How certain are you that the provided text is a chiasmus? (1-10)
        """

        test_return_value = "10"
        response = self.__extract_response(test_return_value)
        return response

    def __extract_response(self, response: str) -> int:
        certainty = int(response)
        return certainty