namespace Solution {
  using NUnit.Framework;
  using System;
  using System.Linq;
  using System.Text;
  using System.Text.RegularExpressions;

  [TestFixture]
  public class SolutionTest
  {
    private static Random rng = new Random();
  
    [Test, Description("It should work for basic tests")]
    public void SampleTest()
    {
      Action[] tests = new Action[]
      {
        () => Assert.AreEqual("Hi", Kata.Remove("Hi!")),
        () => Assert.AreEqual("Hi!!", Kata.Remove("Hi!!!")),
        () => Assert.AreEqual("!Hi", Kata.Remove("!Hi")),
        () => Assert.AreEqual("!Hi", Kata.Remove("!Hi!")),
        () => Assert.AreEqual("Hi! Hi", Kata.Remove("Hi! Hi")),
        () => Assert.AreEqual("Hi", Kata.Remove("Hi")),
      };
      tests.OrderBy(x => rng.Next()).ToList().ForEach(a => a.Invoke());
    }
    
    private static string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
    
    [Test, Description("It should work for random tests too")]
    public void RandomTest()
    {
      for (int i = 0; i < 100; ++i)
      {
        int length = rng.Next(4, 101);
        StringBuilder sb = new StringBuilder(length);
        for (int j = 0; j < sb.Capacity; ++j)
        {
          sb.Append(chars[rng.Next(0, chars.Length)]);
        }
        string test = sb.ToString();
        string expected = new Regex(@"\!$").Replace(test, "");
        string actual = Kata.Remove(test);
        Assert.AreEqual(expected, actual);
      }
    }
    
    [Test, Description("<font color='#00aa00' size=2><b>I'm waiting for your <font color='#dddd00'>feedback, rank and vote.<font color='#00aa00'>many thanks! ;-)</b></font>")]
    public void Advertisement() 
    {
      
    }
  }
}
