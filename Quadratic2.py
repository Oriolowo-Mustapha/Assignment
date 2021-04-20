from Quadratic import QuadraticEquation

equation = QuadraticEquation(8,-7,-5)
result = equation.getDiscriminant()
if result < 0:
    print("There is no root")
elif result > 0:
    root = equation.getRoot1()
    root2 = equation.getRoot2()
    print(root)
    print(root2)
elif result ==0:
    root = equation.getRoot1()
    print(root)
