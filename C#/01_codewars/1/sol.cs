// Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
// https://www.codewars.com/kata/57a0885cbb9944e24c00008e

public class Kata
{
  public static string RemoveExclamationMarks(string str_inp)
  {
    string ans = "";
    foreach(char c in str_inp)
    {
      if (c != '!')
      {
        ans = string.Concat(ans, c);
      }
    }
    return ans;
  }
}
