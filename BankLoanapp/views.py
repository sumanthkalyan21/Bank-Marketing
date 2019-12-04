from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
@csrf_exempt
def index(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        job = request.POST.get('job')
        education = request.POST.get('education')
        balance = request.POST.get('balance')
        loan = request.POST.get('loan')
        day = request.POST.get('day')
        month = request.POST.get('month')
        duration = request.POST.get('duration')
        campaign = request.POST.get('campaign')
        pdays = request.POST.get('pdays')
        previous = request.POST.get('previous')
        poutcome = request.POST.get('poutcome')
        df = pd.read_csv('bank.csv')
        X = df[['age','job','education','balance','loan','day','month','duration','campaign','pdays','previous','poutcome']].values
        y = df['prediction'].values
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        labelencoder_X_1 = LabelEncoder()
        X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
        labelencoder_X_2 = LabelEncoder()
        X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
        labelencoder_X_4 = LabelEncoder()
        X[:, 4] = labelencoder_X_4.fit_transform(X[:, 4])
        labelencoder_X_6 = LabelEncoder()
        X[:, 6] = labelencoder_X_6.fit_transform(X[:, 6])
        labelencoder_X_11 = LabelEncoder()
        X[:, 11] = labelencoder_X_11.fit_transform(X[:, 11])
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=11)
        from sklearn.ensemble import RandomForestClassifier
        rf = RandomForestClassifier(max_depth=10, n_estimators=10)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        print(y_test)
        print(y_pred)
        new = {'age': [11],
               'job': [1],
               'education': [2],
               'balance': [3],
               'loan': [4],
               'day': [22],
               'month': [5],
               'duration': [333],
               'campaign': [44],
               'pdays': [444],
               'previous': [6],
               'poutcome': [7]
               }
        new['age'][0] = int(age)
        new['job'][0] = int(job)
        new['education'][0] = int(education)
        new['balance'][0] = int(balance)
        new['loan'][0] = int(loan)
        new['day'][0] = int(day)
        new['month'][0] = int(month)
        new['duration'][0] = int(duration)
        new['campaign'][0] = int(campaign)
        new['pdays'][0] = int(pdays)
        new['previous'][0] = int(previous)
        new['poutcome'][0] = int(poutcome)
        df2 = pd.DataFrame(new, columns=['age','job','education','balance','loan','day','month','duration','campaign','pdays','previous','poutcome'])
        y_pred = rf.predict(df2)
        name=str(y_pred[0])
        context = {
            'name' : name,
        }
        template = loader.get_template('showdata.html')
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
