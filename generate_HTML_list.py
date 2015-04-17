list_of_concepts = [['Python','Pyhton is a programming language'],
                    ['For Loops','For loops allow you to itterate over lists'],
                    ['Lists','Lists are sequences of data']]


for i in list_of_concepts:
    title = i[0]
    concept = i[1]
    print '''<div class="topic">'''+ title + '''</div>
  <div class="text">''' + concept + '''</div>
    '''
    
