def watertTrappedd(buildings):
    left=[0]*len(buildings)
    right=[0]*len(buildings)
    left[0]=buildings[0]
    right[-1]=buildings[-1]
    for i in range(1,len(buildings)):
        left[i]=max(left[i-1],buildings[i])
    for i in range(len(buildings)-2,-1,-1):
        right[i]=max(buildings[i],right[i+1])
    water=0
    for i in range(len(buildings)):
        water+=min(left[i],right[i])-buildings[i]
    return water
buildings=[2,5,2,3,6,7,1,0,5,7]
# buildings=[4,3,4,5,6,1,0,6,7]
print(watertTrappedd(buildings))