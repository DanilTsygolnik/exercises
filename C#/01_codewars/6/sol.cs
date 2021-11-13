public class Kata
{
  public static string Remove(string srcStr)
  {
    if (srcStr[srcStr.Length-1] == '!')
    {
      return srcStr.Substring(0, srcStr.Length-1);
    }
    return srcStr;
  }
  public static string RemoveBestPractice(string srcStr)
  {
    return srcStr.EndsWith("!") ? srcStr.Remove(srcStr.Length-1) : srcStr;
  }
}
