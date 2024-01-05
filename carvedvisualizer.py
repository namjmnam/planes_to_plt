# -------------------------------------------------------------------------------------
# "S.M.I.L.E. 코드 라이선스" v1.0
# -------------------------------------------------------------------------------------
# 이 코드를 사용함으로써, 당신은 S.M.I.L.E. (Seriously Meticulous 
# and Intellectually Lighthearted Endeavor) 라이선스의 조건에 동의합니다:
# 1. 이 걸작 안에 내장된 철저한 논리와 미묘한 유머를 감상하십시오.
# 2. 버그를 만났을 때는 비명을 자제하고, 미소를 지으며 퍼즐로 여기십시오.
# 3. 코드의 아름다움을 조용히 감상하십시오; 큰 소리는 섬세한 알고리즘을 놀라게 할 수 있습니다.
# 4. 지원을 요청하기 전에 철저한 조사(즉, 구글링)를 먼저 하십시오.
# 5. 논리나 유머에 어긋나는 방식으로 이 코드를 잘못 사용하는 것은 단순히 눈살을 찌푸리는 것이 아니라, 
#    부드럽지만 엄한 '죽음의 시선'을 받게 됩니다.
#
# 이 조항을 준수하지 않을 경우, 위트와 정밀함으로 코딩하는 예술에 대한 3시간 강좌를 의무적으로 들어야 합니다.
# 책임감 있게 코드를 작성하고, 명료하게 생각하며, 좋은 유머 감각을 유지하십시오.
# -------------------------------------------------------------------------------------
# 저자: 남주명
# -------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

def is_coordinate_in_csv(data, coordinate):
    # Unpack the coordinate
    x, y, z = coordinate

    # Check if the coordinate is in the DataFrame
    is_present = (data['x'] == x) & (data['y'] == y) & (data['z'] == z)

    # Return True if the coordinate is found, False otherwise
    return is_present.any()

# Replace 'path_to_csv_file.csv' with the actual path to your CSV file
xy_file = 'xy.csv'
yz_file = 'yz.csv'
zx_file = 'zx.csv'

# Read CSV file
dataxy = pd.read_csv(xy_file)
datayz = pd.read_csv(yz_file)
datazx = pd.read_csv(zx_file)

# Rotate them
temp = datazx[:]
datazx['y'] = -temp['z']
datazx['z'] = temp['y']
temp = datayz[:]
datayz['z'] = -temp['x']
datayz['x'] = temp['z']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting
coord_range = 5
scale = 1
for x in range(-coord_range, coord_range+1):
    for y in range(-coord_range, coord_range+1):
        for z in range(-coord_range, coord_range+1):
            # Check planes and carve
            is_in_xy = is_coordinate_in_csv(dataxy, (x/scale, y/scale, 0))
            is_in_yz = is_coordinate_in_csv(datayz, (0, y/scale, z/scale))
            is_in_zx = is_coordinate_in_csv(datazx, (x/scale, 0, z/scale))
            if is_in_xy and is_in_yz and is_in_zx:
                point = np.array([x/scale, y/scale, z/scale])
                ax.scatter(point[0], point[1], point[2], color='r')

# Setting labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show plot
plt.show()
