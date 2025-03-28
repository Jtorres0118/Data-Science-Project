""" 
Chani and Joel
12/1/23
Creates plots of the data in multiple forms (helper file)
 """
import pandas as pd
import matplotlib.pyplot as plt
from best_feature import read_arff, Partition


def create_bar_graph(ax, arff_file, threshold, color):
    train_partition = read_arff(arff_file)
    best_feature, feature_with_info_gain = train_partition.best_feature()

    features = list(feature_with_info_gain.keys())
    info_gains = list(feature_with_info_gain.values())

    ax.bar(features, info_gains, color=color, alpha=0.6, label=f'Threshold {threshold}')
    ax.set_xlabel('Features')
    ax.set_ylabel('Information Gain')
    ax.set_title(f'Information Gain for Each Feature')
    ax.tick_params(axis='x', rotation=45)  

# Load your CSV file into a DataFrame
df = pd.read_csv('data/anime-dataset-2023_original.csv')

# Create a dot plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Episodes_Count'], df['Score'], s=100, c='blue', alpha=0.5)
plt.title('Episode Count vs. Anime Score')
plt.xlabel('Episode Count')
plt.ylabel('Anime Score')
plt.grid(True)
plt.savefig("figures/score_by_episode_count.pdf")
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

create_bar_graph(ax, 'data/anime-data-6.arff', 6, 'darkviolet')
create_bar_graph(ax, 'data/anime-data-7.5.arff', 7.5, 'lightskyblue')
create_bar_graph(ax, 'data/anime-data-8.arff', 8, 'yellowgreen')

ax.legend()
plt.tight_layout()
plt.savefig("figures/info_gain_combined.pdf")
plt.show()