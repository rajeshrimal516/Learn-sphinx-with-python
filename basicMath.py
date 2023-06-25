from Source.Addition import Addition
from Source.Subtraction import Subtraction
from Source.Multiplication import Multiplication
from Source.Division import Division

if __name__ == "__main__":

    number_1 = 10
    number_2 = 5

    sum = Addition(number_1=number_1, number_2=number_2)
    print("Sum of " + str(number_1) + " and "+ str(number_2) +" : " + str(sum))

    difference = Subtraction(number_1=number_1, number_2=number_2)
    print("Difference of " + str(number_1) + " and "+ str(number_2) + " : " + str(difference))

    product = Multiplication(number_1=number_1, number_2=number_2)
    print("Product of " + str(number_1) + " and "+ str(number_2) +" : " + str(product))

    quotient = Division(number_1=number_1, number_2=number_2)
    print("Quotient of " + str(number_1) + " divided by "+ str(number_2) +" : " + str(quotient))
