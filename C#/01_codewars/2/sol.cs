// Make a function that will return a greeting statement that uses an input;
// your program should return, "Hello, <name> how are you doing today?".

// https://www.codewars.com/kata/55a70521798b14d4750000a4/

using System;

public static class Kata
{
  public static string Greet(string name)
  {
    string greeting = String.Format("Hello, {0} how are you doing today?", name);
    return greeting;
  }
}
