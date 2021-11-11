using System;

public static class Kata
{
  public static string Greet(string name)
  {
    string greeting = String.Format("Hello, {0} how are you doing today?", name);
    return greeting;
  }
}
