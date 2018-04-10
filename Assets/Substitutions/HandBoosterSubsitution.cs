using UnityEngine;
using System.Collections;

public class HandBoosterSubsitution : HandBooster
{
    public GameObject FirstHit
    {
        set { firstHit = value; }
    }

    public bool Match (GameObject target)
    {
        return CheckForMatch(target);
    }
}
