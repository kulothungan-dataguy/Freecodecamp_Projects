import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.education.value_counts().Bachelors/df.shape[0])*100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    temp = pd.DataFrame(df, columns= ['education','salary'])
    options_high = ['Bachelors' , 'Masters' , 'Doctorate' ]
    salary_option = ['>50K']
    min_option = [1]
    country = ['India']

    higher_education = temp.loc[(temp['education'].isin(options_high)) & (temp['salary'].isin(salary_option)) ]
    higher_education1 = temp.loc[(temp['education'].isin(options_high))]
    lower_education = temp.loc[(-temp['education'].isin(options_high)) & (temp['salary'].isin(salary_option)) ]
    lower_education1 = temp.loc[(-temp['education'].isin(options_high))]

    # percentage with salary >50K
    higher_education_rich = round((higher_education.shape[0]/higher_education1.shape[0])*100 , 1)
    lower_education_rich = round((lower_education.shape[0]/lower_education1.shape[0])*100 , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    temp = df['hours-per-week']
    min_work_hours = temp.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    temp = pd.DataFrame(df, columns= ['hours-per-week','salary'])
    numberhours = temp.loc[(temp['hours-per-week'].isin(min_option)) & (temp['salary'].isin(salary_option)) ]
    numberhours1 = temp.loc[(temp['hours-per-week'].isin(min_option))]
    rich_percentage = round((numberhours.shape[0]/numberhours1.shape[0])*100 , 1)

    # What country has the highest percentage of people that earn >50K?
    temp = pd.DataFrame(df, columns= ['native-country','salary'])
    temp1 = temp.dropna()


    z = temp1['native-country' ].value_counts()

    z1 = z.to_dict() #converts to dictionary

    temp1['allcount'] = temp1['native-country'].map(z1)
    #del temp1['salary']
    temp1 = temp1.drop_duplicates()
    temp1 = temp1.loc[(temp1['salary'].isin(salary_option))]
    del temp1['salary']
    #new_header = ['native-country','salary' , 'allcount']
    #temp1 = temp1.reindex(new_header, axis="columns")
    highest_earning_country = temp.loc[(temp['salary'].isin(salary_option))]
    highest_earning_country = highest_earning_country.dropna()
    z = highest_earning_country['native-country'].value_counts()

    z1 = z.to_dict() #converts to dictionary

    highest_earning_country['richcount'] = highest_earning_country['native-country'].map(z1)
    del highest_earning_country['salary']
    highest_earning_country = highest_earning_country.drop_duplicates()
    temp1['richcount'] = highest_earning_country['richcount']
    temp1['percentage'] = temp1['richcount']/temp1['allcount']
    temp1 = temp1.sort_values(by="percentage",ascending=False)
    highest_earning_country = temp1.iloc[0,0]
    highest_earning_country_percentage = round(temp1.iloc[0,3]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    temp = pd.DataFrame(df, columns= ['native-country' , 'occupation','salary'])
    temp = temp.loc[(temp['native-country'].isin(country)) & (temp['salary'].isin(salary_option)) ]
    del temp['salary']
    del temp['native-country']
    z = temp['occupation'].value_counts()

    z1 = z.to_dict() #converts to dictionary

    temp['count'] = temp['occupation'].map(z1)
    temp = temp.drop_duplicates()
    top_IN_occupation = temp.iloc[0,0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
