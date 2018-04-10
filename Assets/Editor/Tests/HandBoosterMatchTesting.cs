using UnityEngine;
using UnityEditor;
using NUnit.Framework;

public class HandBoosterMatchTesting : MatchTesting
{
    private HandBoosterSubsitution handBooster;
    private GameObject firstHit;
    private GameObject target;

    private GameObject baseObject;

    public HandBoosterMatchTesting()
    {
        baseObject = new GameObject("Base");
        handBooster = baseObject.AddComponent<HandBoosterSubsitution>();
    }

    [Test]
    public void TokensSwapTest ()
    {
        SetupNewToken(new TokenInfo {
            Color = TokenColor.Blue,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 0)
        });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Blue,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 1)
        });

        SetupToken(out firstHit, new TokenInfo {
            Color = TokenColor.Red,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 2)
        });

        SetupToken(out target, new TokenInfo {
            Color = TokenColor.Blue,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 3)
        });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Red,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 4)
        });

        SetupNewToken(new TokenInfo {
            Color = TokenColor.Red,
            MatchType = typeof(TokenMatchSubstitution),
            Position = new PositionInfo(3, 5)
        });

        RunTest();
    }

    protected override void RunTest(bool shouldBeTrue = true)
    {
        handBooster.FirstHit = firstHit;

        tokens.Swap(firstHit, target);

        if (shouldBeTrue) {
            Assert.IsTrue(handBooster.Match(target));
        } else {
            Assert.IsFalse(handBooster.Match(target));
        }
    }
}
