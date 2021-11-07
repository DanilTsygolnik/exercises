using NUnit.Framework;
using System;
using System.Text;

[TestFixture]
public class Tests
{
  [Test]
  public static void MyTests()
  {
    Assert.AreEqual("", Kata.RemoveExclamationMarks(""), "Input: Empty string");
    Assert.AreEqual("", Kata.RemoveExclamationMarks("!"), "Input: " + "!");
    Assert.AreEqual("", Kata.RemoveExclamationMarks("!!"), "Input: " + "!!");
    Assert.AreEqual("Hi", Kata.RemoveExclamationMarks("Hi!"), "Input: " + "Hi!");
    Assert.AreEqual("?", Kata.RemoveExclamationMarks("!?!"), "Input: " + "!?!");
  }
}
