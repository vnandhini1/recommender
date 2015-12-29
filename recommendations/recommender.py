from recommendations import critics
from math import sqrt

import recommendations


# Find similarity between two users Euclidian distance
print(recommendations.sim_distance(recommendations.critics,'Lisa Rose','Gene Seymour'))

# Find similarity between two users Pearson distance
print(recommendations.sim_pearson(recommendations.critics,'Lisa Rose','Gene Seymour'))

#Find similar users
print(recommendations.topMatches(recommendations.critics,'Toby',n=3))

#Get recommendations of movies default=Pearson
print(recommendations.getRecommendations(recommendations.critics,'Toby'))

#Get recommendations of movies using Euclidian
print(recommendations.getRecommendations(recommendations.critics,'Toby',similarity=recommendations.sim_distance))


# Transpose the matrix to movies vs user
movies=recommendations.transformPrefs(recommendations.critics)

#Print similar movies
print(recommendations.topMatches(movies,'Superman Returns'))

#Similarity matirx of items
itemsim=recommendations.calculateSimilarItems(recommendations.critics)
print(itemsim)

#Get recommendations based on similarity matrix
print(recommendations.getRecommendedItems(recommendations.critics,itemsim,'Toby'))

# print(recommendations.sim_pearson(critics,'Lisa Rose','Gene Seymour'))

# print(recommendations.getRecommendations(recommendations.critics,'Toby'))

# delusers=deliciousrec.initializeUserDict('programming')




# itemsim=recommendations.calculateSimilarItems(recommendations.critics)
#
# print(itemsim)