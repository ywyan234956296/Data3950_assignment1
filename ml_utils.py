class EDA:
    """
    A class used to perform common EDA tasks

    ...

    Attributes
    ----------
    data : dataframe
        a dataframe on which the EDA will be performed
    target : str
        the name of the target column
    cat : list
        a list of the names of the categorical columns
    num : list
        a list of the names of the numerical columns

    Methods
    -------
    display_head(self, n=5):
        displays the first n rows of the dataset using the head method.
    
    summary_statistics(self):
        print the summary statistics(mean,std,max,and min etc)
    
    missing_values(self):
        prints the sum of missing values for each column    
    
    data_types(self):
        prints the data types of each column 
    
    def info(self):
        find some basic information of the data
    
    setCat(catList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        catlist : list
            The list of column names that are categorical

    setNum(numList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        numlist : list
            The list of column names that are numerical
    numeric_alalysis(self,column):
        plots a histogram of a numeric column using the hist method
    
    categorical_distribution(self, column, filter_threshold=None):
        plots a count plot for a categorical column.
    
    bivariate_analysis_numeric(self, column1, column2):
        plots a scatter plot between two numeric columns.

    box_plot_outliers(self, column):
        plots a box plot to visualize the distribution and identify potential outliers in a numeric column.
    correlation_matrix(self):
        plots a heatmap of the correlation matrix for all numeric columns
    fullEDA()
        Displays the full EDA process. 

    """
    def __init__(self,data,target):
        self.data = data
        self.target = target
        self.cat = []
        self.num = []
    def display_head(self, n=10):
        print(self.data.head(n))
        #display the first 10 row of the data set
    def summary_stats(self):
        print(self.data.describe())
        #find the summary statistics 
    def missing(self):
        print(self.data.isnull().sum())
        #find the missing value in data
    def data_types(self):
        print(self.data.dtypes)
    
    def info(self):
        return self.data.info()

    def giveTarget(self):
        return self.target
        
    def setCat(self, catList):
        self.cat = catList
    
    def setNum(self, numList):
        self.num = numList
    def numeric_alalysis(self,column):
        plt.hist(self.data[column], bins=20, color='blue', aloha=0.7)
        plt.title(f'Distribution of {column}')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()
        #Plots a histogram of a numeric column
    
    def categorical_distribution(self, column, filter_threshold=None):
        if filter_threshold is not None:
            value_counts = self.data[column].value_counts()
            filtered_value_counts = value_counts[value_counts > filter_threshold]
            sns.barplot(x=filtered_value_counts.index, y=filtered_value_counts.values, palette="viridis")
            plt.title(f'Filtered Value Counts (Count > {filter_threshold}) of {column}')
        else:
            sns.countplot(self.data[column])
            plt.title(f'Distribution of {column}')
        plt.show()
        #Plots a count plot for a categorical column
    def bivariate_analysis_numeric(self, column1, column2):
        plt.scatter(self.data[column1], self.data[column2])
        plt.title(f'Scatter Plot between {column1} and {column2}')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show()
        #Plots a scatter plot between two numeric columns.
    def box_plot_outliers(self, column):
        sns.boxplot(self.data[column])
        plt.title(f'Box Plot of {column}')
        plt.show()
        #Plots a box plot to visualize the distribution and identify potential outliers in a numeric column
    
    def correlation_matrix(self):
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()
        #Plots a heatmap of the correlation matrix for all numeric columns 
    

