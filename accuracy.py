#id= int(input('Enter your id:'))
id=0
while(True):
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    l=len(pred)
    test=[]
    i=0
    for i in range(l):
        test.append(id)
        i+=1
    len(test)
    cm=confusion_matrix(test,pred)
    if(metrics.accuracy_score(test,pred)>.5):
        print("accuracy",metrics.accuracy_score(test,pred))
        print("Person ID: ",id)
        break
    else:
        id+=1
#print("confusion_matrix- ",cm)-