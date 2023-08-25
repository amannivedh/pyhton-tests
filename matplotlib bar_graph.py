import matplotlib.pyplot as plt

fig=plt.figure()
langs=['C','C++','Java','Python','PhP']
students=[23,17,35,79,12]
x=['orange','red','pink','green','black']
plt.bar(langs,students,color=x)
plt.xlabel("Languages")
plt.ylabel("No.of Students")
plt.title("Programming Chart")
plt.show()