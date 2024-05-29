from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor


def train_model_with_strategy(dataframe, y_col_name, strategy_id=1):
    if strategy_id == 1:  # Linear Regression
        return train_LR(dataframe, y_col_name)
    elif strategy_id == 2:  # Decision Tree
        return train_DT(dataframe, y_col_name)
    elif strategy_id == 3:  # Random Forest
        return train_RF(dataframe, y_col_name)
    elif strategy_id == 4:  # Gradient Boost
        return train_GB(dataframe, y_col_name)
    elif strategy_id == 5:  # MLP
        return train_MLP(dataframe, y_col_name)
    elif strategy_id == 6:  # Support Vector Regression
        return train_SVR(dataframe, y_col_name)
    elif strategy_id == 7:  # KNN
        return train_KNN(dataframe, y_col_name)
    else:
        raise ValueError("Strategy not recognized. Use min 1 max 7.")


def train_LR(dataframe, y_col_name, fit_intercept=True):  # id 1
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = LinearRegression(fit_intercept=fit_intercept)
    model.fit(X, y)

    return model


def train_DT(dataframe, y_col_name, max_depth=None, min_samples_split=None):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split)
    model.fit(X, y)

    return model


def train_SVR(dataframe, y_col_name, kernel='linear'):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = SVR(kernel=kernel)
    model.fit(X, y)

    return model


def train_KNN(dataframe, y_col_name, k=3):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X, y)

    return model


def train_RF(dataframe, y_col_name, max_features=None, estimators=None):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    if estimators == None:
        model = RandomForestRegressor(max_features=max_features)
    else:
        model = RandomForestRegressor(max_features=max_features, n_estimators=estimators)

    model.fit(X, y)

    return model


def train_GB(dataframe, y_col_name, estimators=None, learning_rate=None):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = GradientBoostingRegressor(n_estimators=estimators, learning_rate=learning_rate)
    model.fit(X, y)

    return model


def train_MLP(dataframe, y_col_name):
    y = dataframe.pop(y_col_name).to_numpy()
    X = dataframe.to_numpy()

    model = MLPRegressor()
    model.fit(X, y)

    return model

