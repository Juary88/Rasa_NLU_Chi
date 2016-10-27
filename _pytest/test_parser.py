from parsa.backends.simple_interpreter import HelloGoodbyeInterpreter

interpreter = HelloGoodbyeInterpreter()



def test_samples():
    samples = [
      ("Hey there",{'text':"Hey there",'intent':'hello', 'entities' : []}),
      ("good bye for now",{'text':"good bye for now",'intent':'goodbye', 'entities' : []})
    ]   

    for text, result in samples:
        assert interpreter.parse(text) == result, "text : {0} \nresult : {1}, expected {2}".format(text,interpreter.parse(text),result)



