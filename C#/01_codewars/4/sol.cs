using System;
using System.Text.RegularExpressions;

public class Kata
{
  public static bool ValidateCode(string code) 
  {
    string pattern = @"\b[1-3]\S*\b";
    Regex rg = new Regex(pattern);
    MatchCollection matches = rg.Matches(code);
    bool ans = matches.Count > 0;
    return ans;
  }

  public static bool ValCodeBestPractice(string code) 
  {
      return Regex.IsMatch(code, "^[1-3]");
  }
}
