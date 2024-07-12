# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

# Brief analysis: 

Some notes: 
Values of 0 = always good
          1 = always bad
Cardio represents the presence or absence of cardiovascular disease
ap_lo/ap_hi os diastolic/systolic blood pressure

Below are the plots I generated: 
![medical_data_viz_count](https://github.com/user-attachments/assets/6ca06490-a584-43dc-b5ab-c4b0593651a0)
It can be noted that in those who have cardiovascular diasese, there is a large difference in count between those who are overweight and those who are not as compared to those without cardiovascular dieases. Cholosterol levels also appear to be increased in comparison to those without cardiovascular dieases. Alcohol seems to be relatively indifferent between the groups. 


![medical_data_heatmap](https://github.com/user-attachments/assets/17484212-3e8b-4e11-8d6f-e6cdee178706)
According to the heatmap, there is a strong correlation between bmi and weight, and if the person was overight (0 or 1) and their weight. And as follows, a strong correlation between bmi and if the person was overweight. In terms of negative correlation, there seems to be a negative correlation between bmi and height. Further explanations to these correlated variables can be explored further with causal analysis. However, in terms of further regression analysis, the correlated variables can be taken into account and can be noted if we see that they have similar regression patterns upon and the dependent variable of interest.  
