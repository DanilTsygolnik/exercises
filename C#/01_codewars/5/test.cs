namespace Solution 
{
  using NUnit.Framework;
  using System;

  [TestFixture]
  public class CalculatorTest
  {
    [Test, Description("should calculate the result of valid inputs")]
    public void Test()
    {
      Assert.AreEqual(8, Kata.Calculator(6, 2, '+'));
      Assert.AreEqual(1, Kata.Calculator(4, 3, '-'));
      Assert.AreEqual(25, Kata.Calculator(5, 5, '*'));
      Assert.AreEqual(1.25, Kata.Calculator(5, 4, '/'));
    }
    
    [Test, Description("should throw ArgumentException with invalid inputs")]
    public void ErrorTest()
    {
      Assert.Throws<ArgumentException>(() => Kata.Calculator(6, 2, '&'));
      Assert.Throws<ArgumentException>(() => Kata.Calculator(6, 2, '\\'));
      Assert.Throws<ArgumentException>(() => Kata.Calculator(6, 2, '='));
      Assert.Throws<ArgumentException>(() => Kata.Calculator(6, 2, '\t'));
    }
    
    private static Random rnd = new Random();
    
    private static double solution(double a, double b, char op)
    {
      switch (op)
      {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        default:  throw new ArgumentException("Unrecognized operation.");
      }
    }
    
    private static char[] operations = new char[] {'+', '-', '*', '-'};
    private static char[] invalidOperations = new char[] {'a', 'b', '%', '_', '[', 'm', '7', '9', 'o', '^', '#'};
    
    [Test, Description("should work for random inputs")]
    public void RandomTests()
    {
      const int Tests = 1000;
      
      for (int i = 0; i < Tests; ++i)
      {
        double a = rnd.NextDouble() * 1000, b = rnd.NextDouble() * 1000;
        
        if (rnd.Next(0, 2) == 0)
        {
          char op = operations[rnd.Next(0, operations.Length)];
          
          double expected = solution(a, b, op);
          double actual = Kata.Calculator(a, b, op);
          
          Assert.AreEqual(expected, actual);
        }
        else
        {
          Assert.Throws<ArgumentException>(() => Kata.Calculator(a, b, invalidOperations[rnd.Next(0, invalidOperations.Length)]));
        }
      }
    }
  }
}
