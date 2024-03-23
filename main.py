import pandas
from matplotlib import pyplot
from sklearn import linear_model, metrics, model_selection
from sklearn.metrics import mean_squared_error

dataframe = pandas.read_csv("Data")

mylog_model = linear_model.LogisticRegression()
y = dataframe.values[:, 1]
X = dataframe.values[:, 2:9]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=.3)

mylog_model.fit(X_train, y_train)
y_prediction = mylog_model.predict(X_test)

accuracy_score = metrics.accuracy_score(y_test, y_prediction)


def first_graph():
    graphlist = []
    for i in range(len(dataframe)):
        score1 = dataframe.values[i][2]
        score1 += dataframe.values[i][3]
        score1 += dataframe.values[i][4]
        score1 += dataframe.values[i][5]
        score1 += dataframe.values[i][6]
        score1 += dataframe.values[i][7]
        score1 += dataframe.values[i][8]
        score1 = score1 / 7
        career = dataframe.values[i][1]

        graphlist.append((score1, career))
    x, y = zip(*graphlist)
    pyplot.scatter(x, y)
    pyplot.xlabel("Grades")
    pyplot.ylabel("Career")
    pyplot.show()
    print("Thank you for using career predictor!")


def second_graph():
    x = ["STEM", "Non-STEM"]
    y = {"STEM": 0, "Non-STEM": 0}
    for i in range(len(dataframe)):
        if dataframe.values[i][1] == "STEM":
            y["STEM"] += 1
        else:
            y["Non-STEM"] += 1
    y_graph = list(y.values())
    pyplot.bar(x, y_graph)
    pyplot.xlabel("Career")
    pyplot.ylabel("Number of Students")
    pyplot.show()
    print("Thank you for using career predictor!")

def third_graph():



try:
    first_input = input(
        "Welcome to the career predictor!\nUsing your grades from school, this program will predict whether you are "
        "better suited for a STEM career or a Non-STEM career.\nEnter '1'to Begin, or enter '2' for graphs and data!\n")

    if first_input == '1':

        math_score = int(input("Please enter your math grade. (0-100)\n"))
        history_score = int(input("Please enter your history grade. (0-100)\n"))
        phys_score = int(input("Please enter your physics grade. (0-100)\n"))
        chem_score = int(input("Please enter your chemistry grade. (0-100)\n"))
        biology_score = int(input("Please enter your biology grade. (0-100)\n"))
        english_score = int(input("Please enter your English grade. (0-100)\n"))
        geo_score = int(input("Please enter your geography grade. (0-100)\n"))
        all_scores = [math_score, history_score, phys_score, chem_score, biology_score, english_score, geo_score]

        for score in all_scores:
            if not 0 <= score <= 100:
                print("All grades were not between 0-100")
                exit()
        student_prediction = mylog_model.predict([all_scores])
        print(
            "Congratulations! Based on your grades, we believe you would do well in a " + student_prediction + " career!")
        exit()

    elif first_input == '2':
        second_input = input("Enter '1' for scatterplot of grade averages. Enter '2' for bar graph of training data. Enter '3' for Graph.\n")
        if second_input == '1':
            first_graph()
            exit()
        elif second_input == '2':
            second_graph()
            exit()
        elif second_input == '3':
            third_graph()
            exit()
        else:
            print("Invalid Input\nExiting Program")
            exit()



    else:
        print("Invalid Input\nExiting Program")
        exit()


except ValueError:
    print("Invalid Input\nExiting Program")
    exit()
