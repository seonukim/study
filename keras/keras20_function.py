# 1. 데이터
import numpy as np
x = np.array([range(1, 101), range(311, 411), range(100)])
y = np.array(range(711, 811))

# 1-1. 행과 열을 바꾸기 - 전치행렬 구하기
x = x.transpose()
y = y.transpose()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size = 0.8, shuffle = False)


# 2. 모델 구성 - 함수형 모델
from keras.models import Sequential, Model
from keras.layers import Dense, Input
# model = Sequential()
# model.add(Dense(5, input_dim = 3))
# model.add(Dense(4))
# model.add(Dense(1))

input1 = Input(shape = (3, ))    # 첫번째 인풋 레이어 구성 후 input1 변수에 할당
x = Dense(3, activation = 'relu')(input1)  # 첫번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(4, activation = 'relu')(x)  # 두번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(2, activation = 'relu')(x)  # 세번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(5, activation = 'relu')(x)  # 네번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(6, activation = 'relu')(x)  # 다섯번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(4, activation = 'relu')(x)  # 여섯번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(8, activation = 'relu')(x)  # 일곱번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(4, activation = 'relu')(x)  # 여덟번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(3, activation = 'relu')(x)  # 아홉번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
x = Dense(1, activation = 'relu')(x) # 열번째 히든레이어 구성, 이전 레이어를 뒤에 명시해줌
output1 = Dense(1)(x)      # 아웃풋 레이어

model = Model(inputs = input1, outputs = output1)   # 함수형 모델 구성(인풋, 아웃풋 명시)

model.summary()  # 모델 요약표


# 3. 훈련
model.compile(loss = 'mse', optimizer = 'adam', metrics = ['mse'])
model.fit(x_train, y_train, epochs = 100, batch_size = 1,
          validation_split = 0.25, verbose = 1)


# 4. 평가 및 예측
loss, mse = model.evaluate(x_test, y_test, batch_size = 1)
print("loss : ", loss)
print("mse : ", mse)

y_predict = model.predict(x_test)
print(y_predict)


# 5. RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))


# 6. R2 구하기
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)
