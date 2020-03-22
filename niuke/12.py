o1 = [1,1,0,0]
o2 = [-1,1,0,0]
o3 = [-1,1,0,0]
o4 = [-1,1,0,0]

def rotate(o,step):
	cx = o[2]
	cy = o[3]
	x = o[0] - cx
	y = o[1] - cy

	rx = x
	ry = y
	for i in range(step):
		rx = - y
		ry = x
		x = rx
		y = ry
	o_ = [i for i in o]
	o_[0] = rx + cx
	o_[1] = ry + cy
	return o_

def rectangled(o1,o2,o3,o4):
	cx = float(o1[0] + o2[0] + o3[0] + o4[0])/4
	cy = float(o1[1] + o2[1] + o3[1] + o4[1])/4
	# print(cx,cy)
	x1 = o1[0] - cx
	y1 = o1[1] - cy
	x2 = o2[0] - cx
	y2 = o2[1] - cy
	x3 = o3[0] - cx
	y3 = o3[1] - cy
	x4 = o4[0] - cx
	y4 = o4[1] - cy

	if x1 == x2 and y1 == y2:
		return False
	points_list = [[x2,y2],[x3,y3],[x4,y4]]
	if not rotate([x1,y1,0.,0.],1)[:2] in points_list:
		return False
	if not rotate([x1,y1,0.,0.],2)[:2] in points_list:
		return False
	if not rotate([x1,y1,0.,0.],3)[:2] in points_list:
		return False
	return True

total_step = 1000
for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				o1_ = rotate(o1,i)
				o2_ = rotate(o2,j)
				o3_ = rotate(o3,k)
				o4_ = rotate(o4,l)

				if rectangled(o1_,o2_,o3_,o4_):
					if i+j+k+l < total_step:
						total_step = i+j+k+l
if total_step == 1000:
	total_step = -1
print(total_step)




