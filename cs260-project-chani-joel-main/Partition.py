"""
Manages dataset information, feature selection, uses information gain and classification accuracy to find the best feature
Author: Chandini Ragobar & Joel Torres
Date: 12/01/2023
"""

################################################################################
# CLASSES
################################################################################
import math

class Example:

    def __init__(self, features, label):
        """Helper class (like a struct) that stores info about each example."""
        # dictionary. key=feature name: value=feature value for this example
        self.features = features
        self.label = label

class Partition:

    def __init__(self, data, F):
        """Store information about a dataset"""
        # list of Examples
        self.data = data
        self.n = len(self.data)

        # dictionary. key=feature name: value=list of possible values
        self.F = F
    
    def best_feature(self):
        "Finds the best feature overall using information gain"
        entropy_y = self.calculate_entropy(self.data)
        best_info_gain = -float('inf')
        best_feature = None
        feature_with_info_gain = {}

        for feature_name in self.F:
            info_gain = self.info_gain(entropy_y, feature_name)
            #if feature_name != 'Episodes' and feature_name != 'Licensors' and feature_name != 'Source' and feature_name !='Rating':
            feature_with_info_gain[feature_name] = info_gain
                #print("Feature Name with Info Gain:", feature_name,info_gain)

            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature_name
        
        print("Best Info Gain:", best_info_gain)
        print("Best Feature: ",best_feature)
        return best_feature, feature_with_info_gain

    def calculate_entropy(self, set):
        "Calculates the entropy of a given dataset "
        label_counts = {}
        total_count = len(set)
    
        if total_count == 0:
            return 0 
        
        #adds the label of each example to the dictionary of labels
        for example in set:
            label = example.label
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1
        
        entropy = 0
        #goes through each label and calculates the probability of it occuring
        
        for label in label_counts:
            prob = label_counts[label] / total_count
            entropy -= prob * math.log2(prob) #the entropy contribution of the unique label
        return entropy

    def info_gain(self, entropy, feature_name):
        "Calculates the information gain using entropy and conditonal entropy"
        feature_values = self.F[feature_name] #gets the possible values for a give feature
        total = len(self.data)
        cond_entropy = 0
            
        #goes through each feature value
        for value in feature_values:
            true = []
            for example in self.data:
                if example.features[feature_name] == value: #sees if the current feature value matches the example feature value
                    true.append(example)
            prob_true = len(true) / total  #probabilty of current feature value occuring
            
            entropy_true = self.calculate_entropy(true) #entropy of subset of examples with current feature value
            cond_entropy += prob_true * entropy_true  

        information_gain = entropy - cond_entropy
        return information_gain
    
    def best_feature_by_accuracy(self):
        "Find the best feature by classifcation accuracy"
        best_acc = 0
        best_feature = None
    
        #goes through each feature to calculate its accuracy
        for feature_name in self.F:
            acc = self.feature_accuracy(feature_name)

            if acc > best_acc:
                best_acc = acc
                best_feature = feature_name
        print("Best Feature by Accuracy: ", best_feature)
        return best_feature

    def feature_accuracy(self, feature_name):
        "Finds the accuracy of a feature"
        feature_values = self.F[feature_name]
        total = len(self.data)
        correct = 0

        "Goes through each value and retrieves the majority label"
        for value in feature_values:
            m_label = self.majority_label(feature_name, value)

            for example in self.data:
                #checks if the example's feature value matches the current value and if the prediction is right
                if example.features[feature_name] == value and example.label == m_label:
                    correct += 1

        return correct / total

    def majority_label(self, feature_name, value):
        "Determines the majority label for each feature"
        pos = 0 #positive label counter
        neg = 0 #negative label counter

        for example in self.data:
            #check if the example's feature value matches the current value and updates label counter accordingly
            if example.features[feature_name] == value:
                if example.label == 1:
                    pos += 1
                else:
                    neg += 1
                    
        #determines majority label based on counters
        if pos >= neg:
            return 1 
        else: 
            return 0
    
                
            

        
    
    
        

        
    

       