# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:35:03 2020

@author: John
"""

import random
import math
import matplotlib.pyplot as plt

# Create a new centroid with random (x,y) and a number
def initializeCentroid(i):
    centroid = {}
    centroid['x'] = random.uniform(-10, 10)
    centroid['y'] = random.uniform(-10, 10)
    centroid['number'] = i
    return centroid

# Create a new point with random (x,y), and assign it to the
# closest centroid
def initializePoint(centroids):
    point = {}
    point['x'] = random.uniform(-10, 10)
    point['y'] = random.uniform(-10, 10)
    point['cluster'] = updateMembership(point, centroids)
    return point

# Given a point, find the closest centroid and return it as the 
# new assignment
def updateMembership(point, centroids):
    minIdx = -1
    minDist = 9999999
    current = 0
    
    for centroid in centroids:
        if distance(point, centroid) < minDist:
            minDist = distance(point, centroid)
            minIdx = current
        current += 1
        
    return minIdx

# Given a centroid, find all points assigned to it and average their
# positions, returning that average as the new position
def updateCentroid(centroid, points):
    sumX = 0
    sumY = 0
    count = 0
    for point in points:
        if point['cluster'] == centroid['number']:
            sumX += point['x']
            sumY += point['y']
            count += 1
            
    # If no points were assigned to a centroid, then reinitialize
    # the centroid with a new random position
    if count == 0:
        sumX = random.uniform(-10, 10)
        sumY = random.uniform(-10, 10)
    else:        
        sumX /= count
        sumY /= count
    return (sumX, sumY)

# Standard Euclidean distance
def distance(p1, p2):
    return math.sqrt( (p1['x']-p2['x'])**2 + (p1['y']-p2['y'])**2 )

# Visualize the output
def plotMe(points, centroids, k):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    
    # plot points
    for i in range(k):
        x = []
        y = []
        for point in points:
            if point['cluster'] == i:
                x.append(point['x'])
                y.append(point['y'])
        plt.scatter(x, y, c=colors[i], marker=".")
    
    # plot centroids
    x = []
    y = []
    for centroid in centroids:
        x.append(centroid['x'])
        y.append(centroid['y'])
    plt.scatter(x, y, marker="o")

    plt.show()    


def main():
    points = []
    centroids = []
    k = 7
    
    # initialize the centroids
    for i in range(k):
        centroids.append(initializeCentroid(i))
    
    # initialize the points
    for i in range(1000):
        points.append(initializePoint(centroids))
    
    # start looping until convergence
    for i in range(500):
        # update centroid position
        for centroid in centroids:
            (centroid['x'], centroid['y']) = updateCentroid(centroid, points)
        
        # update point memberships
        for point in points:
            point['cluster'] = updateMembership(point, centroids)
    
    # output
    plotMe(points, centroids, k)

main()












