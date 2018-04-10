using System;
using MMKCore;
using MMKCore.TokenComponents;
using UnityEngine;
using NUnit.Framework;

public abstract class MatchTesting
{
    protected ITokensCollection tokens;

    protected struct TokenInfo
    {
        public PositionInfo Position { get; set; }
        public TokenColor Color { get; set; }
        public Type MatchType { get; set; }
        public bool MatchableWithTokens { get; set; }
    }

    [SetUp]
    public virtual void Setup ()
    {
        tokens = new TokensArray(6, 6);
        LevelConfig.columns = 6;
        LevelConfig.rows = 6;
    }

    protected void SetupToken (out GameObject token, TokenInfo info)
    {
        token = new GameObject("Token");
        var color = token.AddComponent<MMKCore.TokenComponents.Color>();
        color.Value = info.Color;

        if (info.MatchType != null) {
            var match = token.AddComponent(info.MatchType);
            var substitution = match as BonusMatchSubstitution;
            if (substitution != null) {
                substitution.matchableWithTokens = info.MatchableWithTokens;
            }
        }

        var movement = token.AddComponent<Movement>();
        movement.Assign(info.Position);

        tokens[info.Position] = token;
    }

    protected void SetupNewToken (TokenInfo info)
    {
        GameObject gameObject;
        SetupToken(out gameObject, info);
    }

    protected abstract void RunTest(bool shouldBeTrue = true);
}
