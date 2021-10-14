
import pandas as pd,statistics as st,plotly.figure_factory as pff

#taking input for the student performance score
score=input("which student score's performance would you like to know? ")
#reading data of score inputted
data=pd.read_csv('Student_Performance.csv')
newData=data[score].tolist()

#finding and printing mean,median,mode and std. dev. of data
mean=st.mean(newData)
median=st.median(newData)
mode=st.mode(newData)
stdev=st.stdev(newData)
print('the {} of the data is: {}'.format('mean',mean))
print('the {} of the data is: {}'.format('median',median))
print('the {} of the data is: {}'.format('mode',mode))
print('the {} of the data is: {}'.format('standard deviation',stdev))

#finding start and end of all 3 std. dev.
stdStart1=mean-stdev
stdEnd1=mean+stdev
stdStart2=mean-(stdev*2)
stdEnd2=mean+(stdev*2)
stdStart3=mean-(stdev*3)
stdEnd3=mean+(stdev*3)

#finding data in list form b/w the start and end of the std dev for all 3 seperately
data_in_stdDev1=[result for result in newData if result >stdStart1 and result < stdEnd1]
data_in_stdDev2=[result for result in newData if result >stdStart2 and result < stdEnd2]
data_in_stdDev3=[result for result in newData if result >stdStart3 and result < stdEnd3]

#converting the data found to percentage
stddev1=len(data_in_stdDev1)*100/len(newData)
stddev2=len(data_in_stdDev2)*100/len(newData)
stddev3=len(data_in_stdDev3)*100/len(newData)

#printing the 3 std. dev. in percentage form
print('{}% lies in the {}'.format(stddev1,'standard deviation 1'))
print('{}% lies in the {}'.format(stddev2,'standard deviation 2'))
print('{}% lies in the {}'.format(stddev3,'standard deviation 3'))

#creating graph for score based on what the user inputted
fig=pff.create_distplot([newData],[score])
fig.show()