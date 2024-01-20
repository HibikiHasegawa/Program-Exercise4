import matplotlib.pyplot as plt
import numpy as np

# データの準備
data = """
# t=1.0s
0.0, 300.0
0.01, 277.51053834914245
0.02, 273.85816740016156
0.03, 273.2650089797389
0.04, 273.1686778795711
0.05, 273.15303335602005
0.06, 273.1504926278964
0.07, 273.15008000314566
0.08, 273.15001298400387
0.09, 273.1500020544634
0.1, 273.1500020544634

# t=10.0s
0.0, 300.0
0.01, 290.00205060776744
0.02, 282.30595618885184
0.03, 277.5320936114737
0.04, 275.0333999080251
0.05, 273.889458873463
0.06, 273.41901138295054
0.07, 273.24178066928727
0.08, 273.1798493502742
0.09, 273.1601143945591
0.1, 273.1601143945591

# t=20.0s
0.0, 300.0
0.01, 292.93155854374845
0.02, 286.66031201587526
0.03, 281.70056267293705
0.04, 278.17628273481745
0.05, 275.90530476462686
0.06, 274.5661009833671
0.07, 273.83841820235403
0.08, 273.4753906117412
0.09, 273.3191344019087
0.1, 273.3191344019087

# t=30.0s
0.0, 300.0
0.01, 294.23464776876204
0.02, 288.89728440657865
0.03, 284.317577621288
0.04, 280.66768397278946
0.05, 277.95892280393576
0.06, 276.0834163276149
0.07, 274.8746564422502
0.08, 274.16298024152724
0.09, 273.81379745242486
0.1, 273.81379745242486

# t=40.0s
0.0, 300.0
0.01, 295.01126274733343
0.02, 290.29904684224203
0.03, 286.09343881452395
0.04, 282.5454395256557
0.05, 279.7162205817719
0.06, 277.58820917471996
0.07, 276.0912439402586
0.08, 275.1343794841479
0.09, 274.63515099411296
0.1, 274.63515099411296

# t=50.0s
0.0, 300.0
0.01, 295.54349508411394
0.02, 291.28564024139774
0.03, 287.39948141169464
0.04, 284.01309170814443
0.05, 281.2006767471522
0.06, 278.9852375478638
0.07, 277.3507836229313
0.08, 276.2600572280155
0.09, 275.67312874106483
0.1, 275.67312874106483

# t=60.0s
0.0, 300.0
0.01, 295.94165379505534
0.02, 292.03689671909444
0.03, 288.423894562989
0.04, 285.21322112223646
0.05, 282.4813192942278
0.06, 280.270500978293
0.07, 278.5948024644098
0.08, 277.4497360222015
0.09, 276.8232952908062
0.1, 276.8232952908062
"""

# 改行でデータを分割
sections = data.strip().split('\n\n')

# 各セクションごとにデータを取得してプロット
for section in sections:
    lines = section.strip().split('\n')
    title = lines[0][2:]  # セクションのタイトル（'# t='の部分を取り除く）
    time, values = [], []
    for line in lines[1:]:
        t, v = map(float, line.split(','))
        time.append(t)
        values.append(v)
    
    # グラフをプロット
    plt.plot(time, values, label=title)

# ラベルと凡例の設定
plt.xlabel('x [m]')
plt.ylabel('T [k]')
plt.legend()
plt.grid(True)

# グラフを表示
plt.show()