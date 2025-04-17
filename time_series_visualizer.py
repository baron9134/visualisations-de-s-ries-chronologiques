import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importer les données
def load_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    return df

# 2. Nettoyer les données
def clean_data(df):
    # Calculer les 2,5 % des valeurs les plus faibles et les plus élevées
    lower_limit = df['page_views'].quantile(0.025)
    upper_limit = df['page_views'].quantile(0.975)
    
    # Filtrer les jours où les vues sont dans les 2,5% les plus bas ou les plus élevés
    df_clean = df[(df['page_views'] >= lower_limit) & (df['page_views'] <= upper_limit)]
    return df_clean

# 3. Créer un diagramme linéaire pour afficher l'évolution des pages vues par jour
def draw_line_plot(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['page_views'], color='b', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    return plt

# 4. Créer un diagramme à barres pour les pages vues moyennes par mois et par année
def draw_bar_plot(df):
    df_monthly = df.resample('M').mean()
    df_monthly['year'] = df_monthly.index.year
    df_monthly['month'] = df_monthly.index.month
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_monthly, x='year', y='page_views', hue='month', palette="Set2")
    plt.title('Monthly Average Page Views')
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    plt.tight_layout()
    return plt

# 5. Créer un diagramme en boîte pour montrer la tendance par année et par mois
def draw_box_plot(df):
    df['year'] = df.index.year
    df['month'] = df.index.month
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df, x='year', y='page_views')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='month', y='page_views')
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    return plt
