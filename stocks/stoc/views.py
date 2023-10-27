from django.shortcuts import render, HttpResponse
import joblib
import pandas as pd

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def handleRegister(request):
    fname = request.POST.get('fname', 'default')
    lname = request.POST.get('lname', 'default')
    mail = request.POST.get('mail', 'default')
    passs = request.POST.get('passs', 'default')
    print(fname)
    print(lname)
    print(mail)
    print(passs)
    return render(request, "index.html")

def secScr(request):
    return render(request, "secScr.html")

def preprocess(data):
    # Implement your data preprocessing steps here
    # For example, if you need to encode categorical data:
    # data['categorical_column'] = encoder.transform(data['categorical_column'])
    # If you need to scale numerical data:
    # data['numeric_column'] = scaler.transform(data['numeric_column'])
    return data

def handlesecScr(request):
    stock = request.POST.get('stock', 'default')
    print(stock)
    cls = joblib.load("D:/PROJECTS/techspark/stocks/stoc/gradient_boosting_model.pkl")
    
    new_data = [{'High': 4412.8, 'Low': 4371.8, 'Close': 4404.7, 'Adj Close': 4390.6, 'Volume': 11100, 'Company': 7.0, 'Direction': 0, 'Comp': 0.8, 'Negative': 0.2, 'Neutral': 0.3, 'Positive': 0.7}]
    new_data = pd.DataFrame.from_dict(new_data)
    
    # Apply preprocessing to the user data
    preprocessed_data = preprocess(new_data)

    # Make predictions
    ans = cls.predict(preprocessed_data)[0]
    ans_formatted = '{:.2f}'.format(ans)

    return render(request, "result.html", {'ans': ans_formatted, 'stock': stock})

def handleLogin(request):
    mail = request.POST.get('mail', 'default')
    passs = request.POST.get('passs', 'default')
    print(mail)
    print(passs)
    return render(request, "secScr.html")
