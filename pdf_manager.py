from PIL import Image, ImageDraw, ImageFont
from fillpdf import fillpdfs

def createDictionary():
    global dictionaryloop, skippedErrors, totalErrors, data_dict, errorList,NamesCorrectAnswers, trialDict, incorrectAnswers, correctAnswers, stimsList, correctAnswerForString, femaleTotalErrors, maleTotalErrors
    global highIntensityErrors, lowIntensityErrors, happyErrors, sadErrors, angryErrors, fearfulErrors
    global happyHighIntensityErrors, happyLowIntensityErrors, sadHighIntensityErrors, sadLowIntensityErrors, angryHighIntensityErrors, angryLowIntensityErrors, fearfulHighIntensityErrors, fearfulLowIntensityErrors
    global femaleHappyErrors, femaleSadErrors, femaleAngryErrors, femaleFearfulErrors
    global maleHappyErrors, maleSadErrors, maleAngryErrors, maleFearfulErrors, misattributedHappySad, misattributedHappyAngry, misattributedHappyFearful, misattributedSadHappy, misattributedSadAngry, misattributedSadFearful, misattributedAngryHappy, misattributedAngrySad, misattributedAngryFearful, misattributedFearfulHappy, misattributedFearfulSad, misattributedFearfulAngry
    data_dict = {}
    stimsList = {}
    incorrectAnswers = {}
    errorList = []
    NamesCorrectAnswers = {}
    genderOfAnswer = ''
    intensityOfAnswer = ''
    totalerrors = totalErrors
    
    for i in trialDict:
        # Let's do the basic things first:
        stimsList['stim' + str(dictionaryloop)] = (trialDict[dictionaryloop]['stimFile'])
        
        if trialDict[dictionaryloop]['response'] == '0':
            skippedErrors = skippedErrors + 1
        
        # Let's concact a string to fill in the correct answer with intensity and gender column, we'll start with emotion
        if trialDict[dictionaryloop]['correctAnswer'] == '1':
            correctAnswerForString = 'Happy '
        elif trialDict[dictionaryloop]['correctAnswer'] == '2':
            correctAnswerForString = 'Sad '
        elif trialDict[dictionaryloop]['correctAnswer'] == '3':
            correctAnswerForString = 'Angry '
        elif trialDict[dictionaryloop]['correctAnswer'] == '4':
            correctAnswerForString = 'Fearful '
            
        # Now let's grab the intensity
        if  trialDict[dictionaryloop]['intensity'] == '1':
            intensityOfAnswer = 'Low '
        elif trialDict[dictionaryloop]['intensity'] == '2':
            intensityOfAnswer = 'High '
        else:
            pass
        
        # Now let's grab the gender:
        if  trialDict[dictionaryloop]['stimuliGender'] == '1':
            genderOfAnswer = 'Female'
        elif trialDict[dictionaryloop]['stimuliGender'] == '2':
            genderOfAnswer = 'Male'
        else:
            pass
        
        # Now let's plug that into the PDF
        correctAnswers['correctAnswer'+ str(dictionaryloop)] = (correctAnswerForString) + (intensityOfAnswer) + (genderOfAnswer)

        if trialDict[dictionaryloop]['response'] != trialDict[dictionaryloop]['correctAnswer']:
            totalErrors = totalErrors + 1
            response = int(trialDict[dictionaryloop]['response'])
            correctAnswerKey = trialDict[dictionaryloop]['correctAnswer']
            
            if trialDict[dictionaryloop]['stimuliGender'] == '2':
                maleTotalErrors = maleTotalErrors + 1
            elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                femaleTotalErrors = femaleTotalErrors + 1
            else:
                pass
            
            if  trialDict[dictionaryloop]['intensity'] == '1':
                lowIntensityErrors = lowIntensityErrors + 1
            elif trialDict[dictionaryloop]['intensity'] == '2':
                highIntensityErrors = highIntensityErrors + 1
            else:
                pass        
            
            if correctAnswerKey == '1':
                happyErrors = happyErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    happyLowIntensityErrors = happyLowIntensityErrors + 1
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    happyHighIntensityErrors = happyHighIntensityErrors + 1
                else:
                    pass        

                if response == 2:
                    misattributedHappySad = misattributedHappySad + 1
                elif response == 3:
                    misattributedHappyAngry = misattributedHappyAngry + 1
                elif response == 4:
                    misattributedHappyFearful = misattributedHappyFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleHappyErrors = maleHappyErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleHappyErrors = femaleHappyErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '2':
                sadErrors = sadErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    sadLowIntensityErrors = sadLowIntensityErrors + 1     
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    sadHighIntensityErrors = sadHighIntensityErrors + 1                
                else:
                    pass

                if response == 1:
                    misattributedSadHappy = misattributedSadHappy + 1
                elif response == 3:
                    misattributedSadAngry = misattributedSadAngry + 1
                elif response == 4:
                    misattributedSadFearful = misattributedSadFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleSadErrors = maleSadErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleSadErrors = femaleSadErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '3':
                angryErrors = angryErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    angryLowIntensityErrors = angryLowIntensityErrors + 1        
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    angryHighIntensityErrors = angryHighIntensityErrors + 1                
                else:
                    pass
                
                if response == 1:
                    misattributedAngryHappy = misattributedAngryHappy + 1
                elif response == 2:
                    misattributedAngrySad = misattributedAngrySad + 1
                elif response == 4:
                    misattributedAngryFearful = misattributedAngryFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleAngryErrors = maleAngryErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleAngryErrors = femaleAngryErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '4':
                fearfulErrors = fearfulErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    fearfulLowIntensityErrors = fearfulLowIntensityErrors + 1
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    fearfulHighIntensityErrors = fearfulHighIntensityErrors + 1
                else:
                    pass
                
                if response == 1:
                    misattributedFearfulHappy = misattributedFearfulHappy + 1
                elif response == 2:
                    misattributedFearfulSad = misattributedFearfulSad + 1
                elif response == 3:
                    misattributedFearfulAngry = misattributedFearfulAngry + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleFearfulErrors = maleFearfulErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleFearfulErrors = femaleFearfulErrors + 1
                else:
                    pass
            else:
                pass

            if response == 1:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Happy'        
            elif response == 2:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Sad'
            elif response == 3:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Angry'
            elif response == 4:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Fearful'
            else:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Skipped'
        dictionaryloop = dictionaryloop + 1

def createPDF():
    global dictionaryloop, dictionaryloop2, correctAnswers, age, participant, errorsByMisjudgement
    totalerrors = totalErrors
    age = ageInput.get_value()
    participant = participantInput.get_value()
    errorsByMisjudgement = totalErrors - skippedErrors
    
    totalErrors1 = totalerrors
    totalErrors2 = totalerrors
    happyErrors2 = happyErrors
    sadErrors2 = sadErrors
    angryErrors2 = angryErrors
    fearfulErrors2 = fearfulErrors

    for i in (dictionarydefinitions):
        data_dict [dictionarydefinitions[dictionaryloop2]] = (eval(dictionarydefinitions[dictionaryloop2]))
        dictionaryloop2 = dictionaryloop2 + 1

    data_dict.update(stimsList)
    data_dict.update(expInfo)
    data_dict.update(incorrectAnswers)
    data_dict.update(correctAnswers)

    happycolor = "#00FF00"
    sadcolor = "#0000FF"
    angrycolor = "#FF0000"
    fearfulcolor = "#FFFF00"
    malecolor = "#FF8300"
    femalecolor = "#7800E1"

    widthmain = 480
    heightmain = 30

    totalerrorsincrement = widthmain/24

    widthmisattributions = 378
    heightmisattributions = 20
    misattributionerrorsincrement = widthmisattributions/6

    widthgendererrors = 378
    errorsincrementgender = widthgendererrors/24

    happystartx = 0
    happyendx = (happyErrors * totalerrorsincrement)
    sadstartx = happyendx
    sadendx = sadstartx + (sadErrors * totalerrorsincrement)
    angrystartx = sadendx
    angryendx = angrystartx + (angryErrors * totalerrorsincrement)
    fearfulstartx = angryendx
    fearfulendx = fearfulstartx + (fearfulErrors * totalerrorsincrement)

    happyrectangle = [(0, 0), (happyendx , heightmain)]
    sadrectangle = [(sadstartx,0),(sadendx,heightmain) ]
    angryrectangle = [(angrystartx,0), (angryendx, heightmain)]
    fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmain)]
    
    # creating new Image object
    totalerrorsgraph = Image.new("RGB", (widthmain, heightmain),color = "#FFFFFF")
    # create rectangle image for happy errors
    happyerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
    saderrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
    angryerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
    fearfulerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)

    happyerrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
    saderrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
    angryerrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
    fearfulerrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

    totalerrorsgraph.save("src/graphPictures/totalerrorsgraph.jpg")


    #create picture for happy misattributions
    happystartx = 0
    happyendx = (0) # only since we're on the happy misattributions graph
    sadstartx = happyendx
    sadendx = sadstartx + (misattributedHappySad * misattributionerrorsincrement)
    angrystartx = sadendx
    angryendx = angrystartx + (misattributedHappyAngry * misattributionerrorsincrement)
    fearfulstartx = angryendx
    fearfulendx = fearfulstartx + (misattributedHappyFearful * misattributionerrorsincrement)

    happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
    sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
    angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
    fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]
    # creating new Image object
    happyMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

    # create rectangle image for happy Errors
    happyErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
    sadErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
    angryErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
    fearfulErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)

    sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
    angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
    fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

    happyMisattributionsGraph.save("src/graphPictures/happyMisattributions.jpg")

    happystartx = 0
    happyendx = (misattributedSadHappy * misattributionerrorsincrement) 
    sadstartx = happyendx
    sadendx = sadstartx # only since we're on the sad misattributions graph
    angrystartx = sadendx
    angryendx = angrystartx + (misattributedSadAngry * misattributionerrorsincrement)
    fearfulstartx = angryendx
    fearfulendx = fearfulstartx + (misattributedSadFearful*misattributionerrorsincrement)

    happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
    angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
    fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]

    # creating new Image object
    sadMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

    # create rectangle image for happy Errors
    happyErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
    angryErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
    fearfulErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)

    happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
    angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
    fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

    sadMisattributionsGraph.save("src/graphPictures/sadMisattributions.jpg")

    happystartx = 0
    happyendx = happystartx + (misattributedAngryHappy * misattributionerrorsincrement) 
    sadstartx = happyendx
    sadendx = sadstartx + (misattributedAngrySad * misattributionerrorsincrement)
    angrystartx = sadendx
    angryendx = angrystartx # only since we're on the Angry misattributions graph
    fearfulstartx = angryendx
    fearfulendx = fearfulstartx + (misattributedAngryFearful * misattributionerrorsincrement)

    happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
    sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
    fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


    # creating new Image object
    angryMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

    # create rectangle image for happy Errors
    happyErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
    sadErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
    fearfulErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)

    happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
    sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
    fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

    angryMisattributionsGraph.save("src/graphPictures/angryMisattributions.jpg")

    happystartx = 0
    happyendx = (misattributedFearfulHappy * misattributionerrorsincrement) 
    sadstartx = happyendx
    sadendx = sadstartx + (misattributedFearfulSad*misattributionerrorsincrement)
    angrystartx = sadendx
    angryendx = angrystartx + (misattributedFearfulAngry*misattributionerrorsincrement)
    fearfulstartx = angryendx
    fearfulendx = fearfulstartx # because we are making the fearful graph

    happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
    sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
    angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
    fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


    # creating new Image object
    fearfulMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")
    happyErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph) # create rectangle image for happy Errors
    sadErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph) 
    angryErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph) 
    happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None) 
    sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None) 
    angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None) 
    fearfulMisattributionsGraph.save("src/graphPictures/fearfulMisattributions.jpg")

    # Gender Errors Graph
    malestartx = 0
    maleendx = malestartx + (maleTotalErrors * errorsincrementgender) 
    femalestartx = maleendx
    femaleendx = femalestartx + (femaleTotalErrors * errorsincrementgender)
    malerectangle = [(0, 0), (maleendx , heightmisattributions)]
    femalerectangle = [(femalestartx,0),(femaleendx,heightmisattributions) ]
    
    # creating new Image object
    genderErrorsGraph = Image.new("RGB", (widthgendererrors, heightmisattributions),color = "#FFFFFF")
    # create rectangle image for happy Errors
    maleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)
    femaleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)
    maleTotalErrorsrectangle.rectangle(malerectangle, fill =malecolor, outline=None)
    femaleTotalErrorsrectangle.rectangle(femalerectangle, fill =femalecolor, outline=None)
    genderErrorsGraph.save("src/graphPictures/errorsbygender.jpg")

    # Now let's insert the images

    fillpdfs.place_image('src/graphPictures/totalerrorsgraph.jpg', 124, 769, 'src/pdfMagic/blankDocumentNumberLine.pdf', 'src/pdfMagic/completed.pdf', 1, width=636, height=165)


    page2GraphStart = 120
    happygraphstarty = 161
    #The following are for the other graphs
    fillpdfs.place_image('src/graphPictures/happyMisattributions.jpg', page2GraphStart, happygraphstarty, 'src/pdfMagic/completed.pdf', 'src/pdfMagic/completed1.pdf', 2, width=widthmisattributions, height=heightmisattributions)
    fillpdfs.place_image('src/graphPictures/sadMisattributions.jpg', page2GraphStart, happygraphstarty-43, 'src/pdfMagic/completed1.pdf', 'src/pdfMagic/completed2.pdf', 2, width=widthmisattributions, height=heightmisattributions)
    fillpdfs.place_image('src/graphPictures/angryMisattributions.jpg', page2GraphStart, happygraphstarty-85, 'src/pdfMagic/completed2.pdf', 'src/pdfMagic/completed3.pdf', 2, width=widthmisattributions, height=heightmisattributions)
    fillpdfs.place_image('src/graphPictures/fearfulMisattributions.jpg', page2GraphStart, happygraphstarty-126, 'src/pdfMagic/completed3.pdf', 'src/pdfMagic/completed4.pdf', 2, width=widthmisattributions, height=heightmisattributions)
    fillpdfs.place_image('src/graphPictures/errorsbygender.jpg',page2GraphStart, happygraphstarty-238, 'src/pdfMagic/completed4.pdf', 'src/pdfMagic/completed.pdf', 2, width=widthmisattributions, height=heightmisattributions)

    fillpdfs.write_fillable_pdf('src/pdfMagic/completed.pdf', ('reports/'+expInfo['date']+participant+danvasubtest+'.pdf'), data_dict, flatten=False) # was fillpdfs.write_fillable_pdf('src/pdfMagic/completed.pdf', 'reports/completed.pdf', data_dict, flatten=False)


    # for some reason I am not having luck directly opening the file, and some coding other than the most obvious seems necesary

    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('reports/'+expInfo['date']+participant+danvasubtest+'.pdf', cur_path)
    os.startfile(new_path)