def codefightsTeamNames(firstName):
    names = {'Tigran': "Sloyan",
             "Aida": "Taturyan",
             'Albert': "Sahakyan",
             "Albina": "Ezus",
             "Anastasia": "Iovleva",
             "Anastasiya": "Zhyrkevich",
             "Aram": "Shatakhtsyan",
             "Damien":"Martin",
             "Danila":"Malyutin", #
             
             "Dmitry":"Filippov",###
             "Eduard":"Piliposyan",
             "Mariam":"Sargsyan",
             "Michael":"Newman", ###
             "Narek":"Haytyan", ###
             "Ruben":"Ashughyan", ###
             "Sofya":"Kochkova", ###
             "Vahan":"Hovhannisyan", ###
            }
    try:
        return names[firstName]
    except KeyError:
        return ""
