import requests

class API:
    def __init__(self):
        self.__url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

        self.__headers = {
            "x-rapidapi-key": "a917dfceb7msh6f09733b35af7b3p10f65ejsn1285bb4c78b8",
            "x-rapidapi-host": "twinword-sentiment-analysis.p.rapidapi.com"
        }

        self.emo_headers = {
            "x-rapidapi-key": "a917dfceb7msh6f09733b35af7b3p10f65ejsn1285bb4c78b8",
            "x-rapidapi-host": "twinword-emotion-analysis-v1.p.rapidapi.com",
            "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
        }
        self.emo_url = "https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/"

    def sentiment_analysis(self, text):
        querystring = {"text": text}
        response = requests.get(self.__url, headers=self.__headers, params=querystring)
        sentiment = response.json()['type']
        return sentiment

    # print("Sentiment: ", sentiment,"\n")
    # print(response.json())
    def emotion_analysis(self, emotext):
        emo_payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n" + emotext + "\r\n-----011000010111000001101001--\r\n\r\n"
        emo_response = requests.post(self.emo_url, data=emo_payload, headers=self.emo_headers).json()
        return emo_response['emotions_detected']
        print(emo_response)


if __name__ == '__main__':
    apicall = API()
    apicall.emotion_analysis(emotext="i have been rejected from my interview,feeling sad")
print(__name__)


# i am excited to announce that i have been placed as a data scientist, looking forward to the job!!
