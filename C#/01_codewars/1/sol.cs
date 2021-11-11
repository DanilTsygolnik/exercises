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
