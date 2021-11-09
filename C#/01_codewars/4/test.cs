using System;
using System.Text.RegularExpressions;
using NUnit.Framework;

public class Tests
{
  [Test]
  [TestCase("123", ExpectedResult=true)]
  [TestCase("248", ExpectedResult=true)]
  [TestCase("8", ExpectedResult=false)]
  [TestCase("321", ExpectedResult=true)]
  [TestCase("9453", ExpectedResult=false)]
  public static bool FixedTest(string code)
  {
    return Kata.ValidateCode(code);
  }
  
  [Test]
  public static void RandomTest([Random(0,20,100)]int length)
  {
    string str = RandomString(length, "1234567890abcdefghijklmnopqrstuvwxyzABC_ ");
    Assert.AreEqual(Solution(str), Kata.ValidateCode(str), string.Format("Should work for {0}", str));
  }
  
  private static bool Solution(string code) 
  {
      return Regex.IsMatch(code, "^[1-3]");
  }
  
  private static string RandomString(int randStrLength, string allowedChars)
  {
    string randStr = string.Empty;
    Random r = new Random();
    for(int i = 0; i < randStrLength; i++)
    {
      randStr += allowedChars[r.Next(allowedChars.Length)];
    }
    return randStr;
  }
}
