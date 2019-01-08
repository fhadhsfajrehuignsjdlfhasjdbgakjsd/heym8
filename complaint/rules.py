#this file contains thigs which users aren't allowed to do 
#and what should happen in case they do it
#it's more like docs than code


FORBIDDEN_STUFF = (
    'Explicit extremism/drugs propaganda',#complaint on this theme can be sent towards
    #photo, video, thought and news. Number of signifacant complaints is based on number of mates+receivedRequests(thoughts) or number of members(News)
    #Before community has 1000 members sig.number=300, after sig.number=30% of members
    #Before user has 200 m+rq sig.number=65, after sig.number=25% of m+rq
    #banning comes after 2 news have obtained sig.number of complaints
    #1-time breaking: 2month ban. Second time - 4month ban. Third time - 1year ban.

    'Suicide call',#complaint on this theme can be sent towards
    #photo, video, thought and news. Number of signifacant complaints is based on number of mates+receivedRequests(thoughts) or number of members(News)
    #Before community has 1000 members sig.number=300, after sig.number=30% of members
    #Before user has 200 m+rq sig.number=65, after sig.number=25% of m+rq
    #banning comes after 2 news have obtained sig.number of complaints
    #For 1-time breaking: 4month ban. Second time - 1year ban. Third time - 3year ban

    'Sending spam',#complaint can be sent only towards message
    #user "collects" this complaints and one time in 2 months this number becomes 0
    #sending this complaint automatically blocks user
    #breaking=collecting 50 complaints
    #ban time = month*number of breaking
    'Discredit users because of their nationality, gender and religion',#complaint on this theme can be sent towards
    #photo, video thought and news. Number of signifacant complaints is based on number of mates+receivedRequests(thoughts) or number of members(News)
    #Before community has 1000 members sig.number=300, after sig.number=30% of members
    #Before user has 200 m+rq sig.number=65, after sig.number=25% of m+rq
    #banning comes after 2 news have obtained sig.number of complaints
    #ban time = month*number of breaking
    'Spreading adult content',#complaint on this theme can be sent towards
    #photo, video thought and news. Number of signifacant complaints is based on number of mates+receivedRequests(thoughts) or number of members(News)
    #Before community has 1000 members sig.number=300, after sig.number=30% of members
    #Before user has 200 m+rq sig.number=65, after sig.number=25% of m+rq
    #banning comes after 2 news have obtained sig.number of complaints
    #ban time = month*number of breaking
)


