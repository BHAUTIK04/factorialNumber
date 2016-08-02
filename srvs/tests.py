from django.test import Client, TestCase
import json
# Create your tests here.
class callHubTest(TestCase):
    
    def negativeNumberTestCaseSuccess(self):
        c = Client()
        actual_response = c.post('/srvs/calculation', '{"number":-1}',\
                                                        'Application/json', secure=False)
        act_rep = json.loads(actual_response.content)
        print act_rep
        output=act_rep["output"]
        print output
        self.assertEqual(output, "NUMBER IS NEGATIVE")
        
    def negativeNumberTestCaseFail(self):
        c = Client()
        actual_response = c.post('/srvs/calculation', '{"number":-1}',\
                                                        'Application/json', secure=False)
        act_rep = json.loads(actual_response.content)
        print act_rep
        output=act_rep["output"]
        print output
        self.assertEqual(output, "NEGATIVE IS NUMBER")
    
    def zeroNumberTestCaseSuccess(self):
        c = Client()
        actual_response = c.post('/srvs/calculation', '{"number":0}',\
                                                        'Application/json', secure=False)
        act_rep = json.loads(actual_response.content)
        print act_rep
        output=act_rep["output"]
        print output
        self.assertEqual(output, "0")
    def positiveNumberTestCaseSuccess(self):
        c = Client()
        actual_response = c.post('/srvs/calculation', '{"number":100}',\
                                                        'Application/json', secure=False)
        act_rep = json.loads(actual_response.content)
        print act_rep
        output=act_rep["output"]
        print output
        self.assertEqual(output, "354224848179261915075")