using System;
using MMKCore;
using MMKCore.TokenComponents;
using UnityEngine;

using NUnit.Framework;

public class ManualMatchTesting : MatchTesting
{
    private GameObject first;
    private GameObject second;

    [Test]
    public void TestMatch3()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof (TokenMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Orange,
                MatchType = typeof (TokenMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Green,
            MatchType = typeof (TokenMatchSubstitution),
            Position = new PositionInfo(4, 0)
        });
        SetupNewToken(new TokenInfo {
            Color = TokenColor.Green,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 0) });

        RunTest();
    }

    [Test]
    public void Match3WithIngridient ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof (TokenMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.None,
                Position = new PositionInfo(5, 0)
            });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Green,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(4, 0)
        });
        SetupNewToken(new TokenInfo {
            Color = TokenColor.Green,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 0)
        });

        RunTest();
    }

    [Test]
    public void BonusMatch3 ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.Orange,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof(TokenMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Orange,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(4, 0)
        });
        SetupNewToken(new TokenInfo {
            Color = TokenColor.Orange,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 0)
        });

        RunTest();
    }

    [Test]
    public void ColorBombWithTokenMatch ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                MatchableWithTokens = true,
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof(TokenMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        RunTest();
    }

    [Test]
    public void DoubleBonus ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        RunTest();
    }

    [Test]
    public void ColorBombWithBonus ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                MatchableWithTokens = true,
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        RunTest();
    }

    [Test]
    public void DoubleColorBomb ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                MatchableWithTokens = true,
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                MatchableWithTokens = true,
                Position = new PositionInfo(5, 0)
            });

        RunTest();
    }

    [Test]
    public void BonusWithTokenFail ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.Green,
                MatchType = typeof(TokenMatchSubstitution),
                Position = new PositionInfo(5, 0)
            });

        RunTest(false);
    }

    [Test]
    public void BonusWithIngridientFail ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.None,
                Position = new PositionInfo(5, 0)
            });

        RunTest(false);
    }

    [Test]
    public void ColorBombWithIngridientFail ()
    {
        SetupToken(out first,
            new TokenInfo {
                Color = TokenColor.None,
                MatchType = typeof(BonusMatchSubstitution),
                MatchableWithTokens = true,
                Position = new PositionInfo(5, 1)
            });
        SetupToken(out second,
            new TokenInfo {
                Color = TokenColor.None,
                Position = new PositionInfo(5, 0)
            });

        RunTest(false);
    }

    protected override void RunTest (bool shouldBeTrue = true)
    {
        if (shouldBeTrue) {
            Assert.True(first.Match(second) || second.Match(first));
        } else {
            Assert.False(first.Match(second) || second.Match(first));
        }
    }
}
